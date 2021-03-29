from flask_restful import Resource, reqparse
from app.models.firewall_rules import FirewallRules
from app.models.virtual_machines import VirtualMachines

parser = reqparse.RequestParser()
parser.add_argument("vm_id")


class Attack(Resource):

    def get(self):
        arg = parser.parse_args()

        return {"vm": arg.get("vm_id")}
