from datetime import datetime as dt, timedelta
from flask_restful import Resource, reqparse
from flask_restful_swagger_3 import swagger, Resource
from sqlalchemy import and_, func

from app import db
from app.models.BorrowFeeModel import BorrowFee
from app.models.BorrowFeeResponseModel import BorrowFeeResponseModel
from app.models.MemberModel import *
from app.models.MemberResponseModel import MemberResponseModel


class GetMembers(Resource):
    @swagger.tags(["Get"])
    @swagger.reorder_with(
        MemberResponseModel, description="Returns all members", summary="Get Members"
    )
    def get(self):
        members = (
            Member.query.outerjoin(
                BorrowFee,
                (Member.pk == BorrowFee.member_fk) &
                (BorrowFee.create_time >= dt.now() - timedelta(days=365)),
            )
            .add_columns(
                Member.pk,
                Member.username,
                func.sum(BorrowFee.borrow_fee),
                Member.create_time,
            )
            .group_by(Member.pk)
        )
        print(members[0])
        return [
            {
                "pk": member.pk,
                "username": member.username,
                "totalBorrowFeeLastYear": member[3] if member[3] is not None else 0,
                "create_time": str(member.create_time),
            }
            for member in members
        ], 200


class GetMember(Resource):
    @swagger.tags(["Get"])
    @swagger.reorder_with(
        MemberResponseModel, description="Returns a member", summary="Get Member"
    )
    def get(self, user_id):
        member = Member.query.get(user_id)
        if member:
            return {
                "pk": member.pk,
                "username": member.username,
                "create_time": str(member.create_time),
            }
        else:
            return {"message": "User not found"}, 404


class CreateMember(Resource):
    req_parser = reqparse.RequestParser(bundle_errors=True)
    req_parser.add_argument(
        "username", type=str, required=True, help="username is required parameter!"
    )
    req_parser.add_argument(
        "create_time",
        type=str,
        required=False,
        help="%Y-%m-%d %H:%M:%S",
        default=dt.now().strftime("%Y-%m-%d %H:%M:%S"),
    )

    @swagger.tags(["Create"])
    @swagger.reqparser(name="CreateMember", parser=req_parser)
    @swagger.reorder_with(
        MemberResponseModel,
        description="Create a member with username",
        summary="Create Member",
    )
    def post(self):
        args = self.req_parser.parse_args()
        user = Member(
            username=args["username"],
            create_time=dt.strptime(args["create_time"], "%Y-%m-%d %H:%M:%S"),
        )
        db.session.add(user)
        db.session.commit()
        return {
            "pk": user.pk,
            "username": user.username,
            "create_time": str(user.create_time),
        }, 201


class UpdateMember(Resource):
    req_parser = reqparse.RequestParser(bundle_errors=True)
    req_parser.add_argument(
        "pk", type=int, required=True, help="pk is required parameter!"
    )
    req_parser.add_argument(
        "username", type=str, required=True, help="username is required parameter!"
    )

    @swagger.tags(["Update"])
    @swagger.reqparser(name="UpdateMember", parser=req_parser)
    @swagger.reorder_with(
        MemberResponseModel,
        description="Update a member with pk",
        summary="Update Member",
    )
    def put(self):
        args = self.req_parser.parse_args()
        user = Member.query.get(args["pk"])
        if user:
            user.username = args["username"]
            db.session.commit()
            return {
                "pk": user.pk,
                "username": user.username,
                "create_time": str(user.create_time),
            }, 200
        else:
            return {"message": "User not found"}, 404


class getMemberPeriodBorrowTotal(Resource):
    req_parser = reqparse.RequestParser(bundle_errors=True)
    req_parser.add_argument(
        "member_fk", type=int, required=True, help="member_fk is required parameter!"
    )
    req_parser.add_argument(
        "start_time",
        type=str,
        required=True,
        help="%Y-%m-%d %H:%M:%S",
    )
    req_parser.add_argument(
        "end_time",
        type=str,
        required=True,
        help="%Y-%m-%d %H:%M:%S",
    )

    @swagger.tags(["Get"])
    @swagger.reqparser(name="getMemberLastYearBorrowHistory", parser=req_parser)
    @swagger.reorder_with(
        BorrowFeeResponseModel,
        description="Returns a member's borrow histories",
        summary="Get Borrow History of a member",
    )
    def post(self):
        member_fk_criteria = (
            BorrowFee.member_fk == self.req_parser.parse_args()["member_fk"]
        )
        period_criteria = and_(
            BorrowFee.create_time >= self.req_parser.parse_args()["start_time"],
            BorrowFee.create_time <= self.req_parser.parse_args()["end_time"],
        )
        criteria = and_(member_fk_criteria, period_criteria)
        borrow_fees = BorrowFee.query.filter(criteria).all()

        return {
            "member_fk": self.req_parser.parse_args()["member_fk"],
            "borrow_fees": [borrow_fee.serialize() for borrow_fee in borrow_fees],
        }, 200
