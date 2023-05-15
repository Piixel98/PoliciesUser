from uuid import UUID

from app.policy.service import PolicyQueryService
from app.user.repository import UserRepository
from app.user.schema import UserSchema, Role


class UserQueryService:
    def __init__(self, user_repo: UserRepository = UserRepository()):
        self.user_repo = user_repo

    async def get_users(self, name: str = None) -> list[UserSchema]:
        if name:
            return await self.user_repo.get_users(name=name)

        return await self.user_repo.get_users()

    async def get_user_by_id(self, user_id: UUID) -> UserSchema:
        list_users = await self.user_repo.get_users(id=user_id)
        return list_users[0]

    async def get_users_by_policy_id(self, policy_id: UUID) -> UserSchema:
        policyFound = await PolicyQueryService().get_policy_by_id(policy_id=policy_id)
        return await self.get_user_by_id(user_id=policyFound.clientId)

    async def is_admin(self, user_id: UUID) -> bool:
        user = await self.get_user_by_id(user_id=user_id)
        if not user:
            return False

        if user.role != Role.admin:
            return False

        return True

    async def is_user(self, user_id: UUID) -> bool:
        user = await self.get_user_by_id(user_id=user_id)
        if not user:
            return False

        if user.role != Role.user:
            return False

        return True
