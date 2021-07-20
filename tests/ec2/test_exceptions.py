from src.ec2.exceptions import Boto3EC2NetworkError


def test_ok_boto3_ec2_network_error():
    status_code = 500
    request_id = "test_id"
    assert (
        Boto3EC2NetworkError(status_code, request_id).__str__()
        == f"Status code: {status_code}\nRequest id: {request_id}"
    )
