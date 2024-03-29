from app import app, api
from config import Config
from routes import GetMember, CreateMember, GetMembers, UpdateMember, getMemberPeriodBorrowTotal

api.add_resource(GetMembers, "/api/members")
api.add_resource(GetMember, "/api/member/<int:user_id>")
api.add_resource(CreateMember, "/api/createMember")
api.add_resource(UpdateMember, "/api/updateMember")
api.add_resource(getMemberPeriodBorrowTotal, "/api/getMemberPeriodBorrowTotal")

if __name__ == "__main__":
    app.run(host=Config.APP_HOST, port=Config.APP_PORT, debug=False)
