from core.exceptions import CustomException


class UserException(CustomException):
    pass


class UserNotFoundException(UserException):
    code = 404
    error_code = 2000
    message = "User NOT FOUND"
