from flask_restful_swagger_3 import Schema


class BorrowFeeResponseModel(Schema):
    properties = {
        "pk": {
            "type": "integer",
            "format": "int64",
        },
        "member_fk": {
            "type": "integer",
            "format": "int64",
        },
        "type" : {"type": "integer"},
        "borrow_fee" : {"type": "integer"},
        "borrow_time": {"type": "integer"},
        "create_time": {"type": "datetime"},
    }
    required = ["member_fk", "borrow_fee", "borrow_time"]