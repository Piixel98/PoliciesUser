from abc import ABCMeta, abstractmethod
from http import HTTPStatus

from uuid import UUID
import httpx

from app.user.exception import UserNotFoundException
from app.user.schema import UserSchema
from core.config import config
from core.exceptions.base import InternalServerErrorException


class UserRepository:
    __metaclass__ = ABCMeta

    @abstractmethod
    async def get_by_id(self, user_id: UUID) -> UserSchema:
        pass

    @abstractmethod
    async def get_by_name(self, name: str) -> UserSchema:
        pass

    @abstractmethod
    async def get_by_policy_id(self, policy_id: UUID) -> UserSchema:
        pass


class UserMockRepository(UserRepository):
    def __init__(self):
        self._timeout = httpx.Timeout(30.0, read=None)
        self._client = httpx.Client(timeout=self._timeout)
        self.headers = {
            'Charset': 'UTF-8',
            'Accept': 'application/json'
        }

    async def get_by_id(self, user_id: UUID) -> UserSchema:
        try:
            response = self._client.get(f"{config.CLIENT_MOCK_URL}", headers=self.headers)
            if response.status_code == HTTPStatus.OK:
                users_found = [x for x in response.json()['clients'] if x['id'] == str(user_id)]
                if len(users_found) == 0:
                    raise UserNotFoundException
                if len(users_found) == 1:
                    return UserSchema.parse_obj(users_found[0])
            raise InternalServerErrorException
        except UserNotFoundException:
            raise UserNotFoundException
        except Exception:
            raise InternalServerErrorException

    async def get_by_name(self, name: str) -> UserSchema:
        try:
            response = self._client.get(f"{config.CLIENT_MOCK_URL}", headers=self.headers)
            if response.status_code == HTTPStatus.OK:
                users_found = [x for x in response.json()['clients'] if x['name'] == str(name)]
                if len(users_found) == 0:
                    raise UserNotFoundException
                if len(users_found) == 1:
                    return UserSchema.parse_obj(users_found[0])
            raise InternalServerErrorException
        except UserNotFoundException:
            raise UserNotFoundException
        except Exception:
            raise InternalServerErrorException

    async def get_by_policy_id(self, policy_id: UUID) -> UserSchema:
        try:
            response = self._client.get(f"{config.POLICY_MOCK_URL}", headers=self.headers)
            if response.status_code == HTTPStatus.OK:
                policies_found = [x for x in response.json()['policies'] if x['id'] == str(policy_id)]
                if len(policies_found) == 0:
                    raise UserNotFoundException
                if len(policies_found) == 1:
                    return await self.get_by_id(user_id=policies_found[0]['clientId'])
            raise InternalServerErrorException
        except UserNotFoundException:
            raise UserNotFoundException
        except Exception:
            raise InternalServerErrorException
