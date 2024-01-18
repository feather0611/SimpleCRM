from flask_restful_swagger_3 import Schema


class MemberResponseModel(Schema):
    properties = {
        "pk": {
            "type": "integer",
            "format": "int64",
        },
        "username": {"type": "string"},
        "create_time": {"type": "datetime"},
    }
    required = ["name"]