from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class VirtualMachines(db.Model):
    vm_id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    tag = db.Column(db.String, nullable=False)

    def __init__(self, vm_id, name, tag):
        self.vm_id = vm_id
        self.name = name
        self.tag = tag
