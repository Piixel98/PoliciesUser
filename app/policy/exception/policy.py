from core.exceptions import CustomException


class PolicyException(CustomException):
    pass


class PolicyNotFoundException(PolicyException):
    code = 404
    error_code = 1000
    message = "Policy NOT FOUND"
