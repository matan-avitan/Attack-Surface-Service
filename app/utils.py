from app.models import db
from app.models.virtual_machines import VirtualMachines
from app.models.firewall_rules import FirewallRules


# VM utils - insert new Virtual Machine
def add_new_vm(vm_id, name, tag=None):
    new_vm = VirtualMachines(vm_id=vm_id, name=name, tag=tag)
    db.session.add(new_vm)
    db.session.commit()


def extract_vm_fields(vm):
    vm_id = vm['vm_id']
    name = vm['name']
    tags = vm['tags']
    if not tags:
        add_new_vm(vm_id, name)
    for tag in tags:
        add_new_vm(vm_id, name, tag)


# Firewall Rule utils - insert new firewall rule

def add_new_fw_rule(fw_id, source_tag, dest_tag):
    new_fw_rule = FirewallRules(fw_id=fw_id, source_tag=source_tag, dest_tag=dest_tag)
    db.session.add(new_fw_rule)
    db.session.commit()


def extract_fw_rule_fields(fw_rule):
    fw_id = fw_rule['fw_id']
    source_tag = fw_rule['source_tag']
    dest_tag = fw_rule['dest_tag']
    add_new_fw_rule(fw_id, source_tag, dest_tag)


# Setup data to db
def setup_data_to_db(inputs):
    vms = inputs['vms']
    for vm in vms:
        extract_vm_fields(vm)

    fw_rules = inputs['fw_rules']
    for fw_rule in fw_rules:
        extract_fw_rule_fields(fw_rule)
