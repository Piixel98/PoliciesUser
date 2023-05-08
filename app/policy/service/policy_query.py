from uuid import UUID

from app.policy.repository import PolicyRepository
from app.policy.schema import PolicySchema


class PolicyQueryService:
    def __init__(self, policy_repo: PolicyRepository = PolicyRepository()):
        self.policy_repo = policy_repo

    async def get_policy_by_id(self, policy_id: UUID) -> PolicySchema:
        return await self.policy_repo.get_by_id(policy_id=policy_id)

    async def get_policies_by_user_id(self, user_id: UUID) -> list[PolicySchema]:
        return await self.policy_repo.get_by_user_id(user_id=user_id)
