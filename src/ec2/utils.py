from typing import Optional

from src.ec2 import ec2_client
from src.ec2.exceptions import Boto3EC2NetworkError


def get_ec2_describe_instances() -> list[Optional[dict]]:
    response = ec2_client.describe_instances()
    status_code = response["ResponseMetadata"]["HTTPStatusCode"]
    if status_code == 200:
        return response["Reservations"]
    raise Boto3EC2NetworkError(
        status_code, response["ResponseMetadata"]["RequestId"]
    )


def filter_state_name_from_ec2_intances(
    ec2_describe_instances: list[Optional[dict]],
    state_name: str,
) -> list[Optional[dict]]:
    instances = [
        instance
        for instances in ec2_describe_instances
        for instance in instances["Instances"]
    ]
    return [
        instance
        for instance in instances
        if instance["State"]["Name"] == state_name
    ]


def get_instance_ids_from_ec2_intances(
    instances: list[Optional[dict]],
) -> list[Optional[dict]]:
    return [instance["InstanceId"] for instance in instances]
