from abc import abstractmethod, ABCMeta

from typing import Optional

from uuid import UUID

from app.policy.schema.policy import PolicySchema


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
        pass

    async def get_by_id(self, policy_id: UUID) -> PolicySchema:
        raise NotImplementedError

    async def get_by_user_id(self, user_id: UUID) -> list[PolicySchema]:
        raise NotImplementedError
