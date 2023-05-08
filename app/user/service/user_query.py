from uuid import UUID

from app.user.repository import UserRepository
from app.user.schema import UserSchema, Role


class UserQueryService:
    def __init__(self, user_repo: UserRepository = UserRepository()):
        self.user_repo = user_repo

    async def get_user_by_id(self, user_id: UUID) -> UserSchema:
        return await self.user_repo.get_by_id(user_id=user_id)

    async def get_user_by_name(self, name: str) -> UserSchema:
        return await self.user_repo.get_by_name(name=name)

    async def get_users_by_policy_id(self, policy_id: UUID) -> UserSchema:
        return await self.user_repo.get_by_policy_id(policy_id=policy_id)

    async def is_admin(self, user_id: UUID) -> bool:
        user = await self.user_repo.get_by_id(user_id=user_id)
        if not user:
            return False

        if user.role != Role.admin:
            return False

        return True

    async def is_user(self, user_id: UUID) -> bool:
        user = await self.user_repo.get_by_id(user_id=user_id)
        if not user:
            return False

        if user.role != Role.user:
            return False

        return True
