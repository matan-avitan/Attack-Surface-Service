from app.models import db


class FirewallRules(db.Model):
    fw_id = db.Column(db.String, primary_key=True)
    source_tag = db.Column(db.String(100), nullable=False)
    dest_tag = db.Column(db.String, nullable=False)

    def __init__(self, fw_id, source_tag, dest_tag):
        self.fw_id = fw_id
        self.source_tag = source_tag
        self.dest_tag = dest_tag
