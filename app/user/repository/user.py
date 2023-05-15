from abc import ABCMeta, abstractmethod
from http import HTTPStatus

import httpx

from app.user.exception import UserNotFoundException
from app.user.schema import UserSchema
from core.config import config


class UserRepository:
    __metaclass__ = ABCMeta

    @abstractmethod
    async def get_users(self, **kwargs) -> list[UserSchema]:
        pass


class UserMockRepository(UserRepository):
    def __init__(self):
        self._timeout = httpx.Timeout(30.0, read=None)
        self._client = httpx.Client(timeout=self._timeout)
        self.headers = {
            'Charset': 'UTF-8',
            'Accept': 'application/json'
        }

    async def get_users(self, **kwargs) -> list[UserSchema]:
        response = self._client.get(f"{config.CLIENT_MOCK_URL}", headers=self.headers)
        if response.status_code == HTTPStatus.OK:
            users_found = [x for x in response.json()['clients'] if all(x[k] == str(v) for k, v in kwargs.items())]
            if len(users_found) == 0:
                raise UserNotFoundException
            else:
                return [UserSchema.parse_obj(user) for user in users_found]
