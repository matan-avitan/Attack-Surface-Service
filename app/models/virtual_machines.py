from app.models import db


class VirtualMachines(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    vm_id = db.Column(db.String, nullable=False)
    tag = db.Column(db.String, nullable=True)

    def __init__(self, vm_id, name, tag):
        self.vm_id = vm_id
        self.name = name
        self.tag = tag
