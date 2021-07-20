from src.ec2 import ec2_client
from src.ec2.utils import (
    get_ec2_describe_instances,
    filter_state_name_from_ec2_intances,
)

RUNNING = "running"
STOPPED = "stopped"


def start_ec2():
    ec2_describe_instances = get_ec2_describe_instances()
    stopped_ec2_intance_ids = filter_state_name_from_ec2_intances(
        ec2_describe_instances=ec2_describe_instances, state_name=STOPPED
    )
    ec2_client.start_instances(InstanceIds=stopped_ec2_intance_ids)


def stop_ec2():
    ec2_describe_instances = get_ec2_describe_instances()
    running_ec2_intance_ids = filter_state_name_from_ec2_intances(
        ec2_describe_instances=ec2_describe_instances, state_name=RUNNING
    )
    ec2_client.stop_instances(InstanceIds=running_ec2_intance_ids)
