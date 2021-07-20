class Boto3EC2NetworkError(BaseException):
    status_code: str
    request_id: str

    def __init__(self, status_code: int, message: str):
        self.status_code = str(status_code)
        self.request_id = message

    def __str__(self):
        return (
            f"Status code: {self.status_code}\nRequest id: {self.request_id}"
        )
