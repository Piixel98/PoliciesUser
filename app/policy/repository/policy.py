from abc import abstractmethod, ABCMeta
from http import HTTPStatus
from typing import Optional

import httpx
from uuid import UUID

from app.policy.exception import PolicyNotFoundException
from app.policy.schema.policy import PolicySchema
from core.config import config
from core.exceptions.base import InternalServerErrorException


class PolicyRepository:
    __metaclass__ = ABCMeta

    @abstractmethod
    async def get_by_id(self, user_id: UUID) -> Optional[PolicySchema]:
        pass

    @abstractmethod
    async def get_by_user_id(self, user_id: UUID) -> Optional[list[PolicySchema]]:
        pass


class PolicyMockRepository(PolicyRepository):
    def __init__(self):
        self._timeout = httpx.Timeout(30.0, read=None)
        self._client = httpx.Client(timeout=self._timeout)
        self.headers = {
            'Charset': 'UTF-8',
            'Accept': 'application/json'
        }

    async def get_by_id(self, policy_id: UUID) -> PolicySchema:
        try:
            response = self._client.get(f"{config.POLICY_MOCK_URL}", headers=self.headers)
            if response.status_code == HTTPStatus.OK:
                policies_found = [x for x in response.json()['policies'] if x['id'] == str(policy_id)]
                if len(policies_found) == 0:
                    raise PolicyNotFoundException
                if len(policies_found) == 1:
                    return PolicySchema.parse_obj(policies_found[0])
            raise InternalServerErrorException
        except PolicyNotFoundException:
            raise PolicyNotFoundException
        except Exception:
            raise InternalServerErrorException

    async def get_by_user_id(self, user_id: UUID) -> list[PolicySchema]:
        try:
            response = self._client.get(f"{config.POLICY_MOCK_URL}", headers=self.headers)
            if response.status_code == HTTPStatus.OK:
                policies_found = [x for x in response.json()['policies'] if x['clientId'] == str(user_id)]
                if len(policies_found) == 0:
                    raise PolicyNotFoundException
                if len(policies_found) > 0:
                    return [PolicySchema.parse_obj(policy) for policy in policies_found]
            raise InternalServerErrorException
        except PolicyNotFoundException:
            raise PolicyNotFoundException
        except Exception:
            raise InternalServerErrorException

