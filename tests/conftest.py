import boto3
import pytest
from moto import mock_ec2
from moto.emr.models import EXAMPLE_AMI_ID


@pytest.fixture
def ec2():
    with mock_ec2():
        yield


@pytest.fixture
def ec2_resource(ec2):
    yield boto3.resource("ec2")


@pytest.fixture
def create_ec2_instance(ec2_resource):
    return ec2_resource.create_instances(
        ImageId=EXAMPLE_AMI_ID,
        MinCount=1,
        MaxCount=1,
        BlockDeviceMappings=[
            {
                "DeviceName": "/dev/sda1",
                "Ebs": {"VolumeSize": 50, "DeleteOnTermination": True},
            }
        ],
    )
