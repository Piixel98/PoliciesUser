from uuid import UUID

from app.policy.repository import PolicyRepository
from app.policy.schema import PolicySchema


class PolicyQueryService:
    def __init__(self, policy_repo: PolicyRepository = PolicyRepository()):
        self.policy_repo = policy_repo

    async def get_policies(self, user_id: UUID = None) -> list[PolicySchema]:
        if user_id:
            return await self.policy_repo.get_policies(clientId=user_id)
        return await self.policy_repo.get_policies()

    async def get_policy_by_id(self, policy_id: UUID) -> PolicySchema:
        list_policies = await self.policy_repo.get_policies(id=policy_id)
        return list_policies[0]
