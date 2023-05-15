from abc import abstractmethod, ABCMeta
from http import HTTPStatus

import httpx

from app.policy.exception import PolicyNotFoundException
from app.policy.schema.policy import PolicySchema
from core.config import config


class PolicyRepository:
    __metaclass__ = ABCMeta

    @abstractmethod
    async def get_policies(self, **kwargs) -> list[PolicySchema]:
        pass


class PolicyMockRepository(PolicyRepository):
    def __init__(self):
        self._timeout = httpx.Timeout(30.0, read=None)
        self._client = httpx.Client(timeout=self._timeout)
        self.headers = {
            'Charset': 'UTF-8',
            'Accept': 'application/json'
        }

    async def get_policies(self, **kwargs) -> list[PolicySchema]:
        response = self._client.get(f"{config.POLICY_MOCK_URL}", headers=self.headers)
        if response.status_code == HTTPStatus.OK:
            policies_found = [x for x in response.json()['policies'] if all(x[k] == str(v) for k, v in kwargs.items())]
            if len(policies_found) == 0:
                raise PolicyNotFoundException
            else:
                return [PolicySchema.parse_obj(policy) for policy in policies_found]
