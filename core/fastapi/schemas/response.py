import http
from typing import Union

from pydantic import BaseModel
from starlette.status import HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND, \
    HTTP_422_UNPROCESSABLE_ENTITY, HTTP_500_INTERNAL_SERVER_ERROR, HTTP_503_SERVICE_UNAVAILABLE


class ResponseModel(BaseModel):
    code: http.HTTPStatus
    error_code: int
    message: Union[str, list[str]]


class HTTPResponseModel(ResponseModel):
    detail: ResponseModel

    class Config:
        schema_extra = {
            "example": {
                "detail": {
                    "code": "{http.HTTPStatus}",
                    "error_code": "1000",
                    "message": "{Union[str,list[str]]}"
                }
            }
        }


ExceptionResponseSchema = {
    HTTP_400_BAD_REQUEST: {"model": HTTPResponseModel},
    HTTP_401_UNAUTHORIZED: {"model": HTTPResponseModel},
    HTTP_404_NOT_FOUND: {"model": HTTPResponseModel},
    HTTP_422_UNPROCESSABLE_ENTITY: {"model": HTTPResponseModel},
    HTTP_500_INTERNAL_SERVER_ERROR: {"model": HTTPResponseModel},
    HTTP_503_SERVICE_UNAVAILABLE: {"model": HTTPResponseModel}
}


class StatusResponseSchema(BaseModel):
    pass
