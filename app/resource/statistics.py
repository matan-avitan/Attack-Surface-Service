from flask_restful import Resource


class Statistic(Resource):

    def get(self):
        return {"vm_count": 2, "request_count": 1120232, "average_request_time": 0.003032268166772597}
