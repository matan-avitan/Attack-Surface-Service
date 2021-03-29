from flask_restful import Resource, reqparse

parser = reqparse.RequestParser()
parser.add_argument("vm_id")


class Attack(Resource):

    def get(self):
        arg = parser.parse_args()
        return {"vm": arg.get("vm_id")}
