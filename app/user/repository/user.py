from abc import ABCMeta, abstractmethod
from uuid import UUID
from app.user.schema import UserSchema


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
        pass

    async def get_by_id(self, user_id: UUID) -> UserSchema:
        raise NotImplementedError

    async def get_by_name(self, name: str) -> UserSchema:
        raise NotImplementedError

    async def get_by_policy_id(self, policy_id: UUID) -> UserSchema:
        raise NotImplementedError
