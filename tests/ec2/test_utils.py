from moto.emr.models import EXAMPLE_AMI_ID

from src.ec2.utils import get_ec2_describe_instances


def test_ok_get_ec2_describe_instances(create_ec2_instance):
    describe_instances = get_ec2_describe_instances()
    instance_image_id = describe_instances[0]["Instances"][0]["ImageId"]
    assert len(describe_instances) == 1
    assert instance_image_id == EXAMPLE_AMI_ID


def test_filter_state_name_from_ec2_intances():
    pass


def test_get_instance_ids_from_ec2_intances():
    pass
