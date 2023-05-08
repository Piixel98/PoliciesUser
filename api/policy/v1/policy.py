from uuid import UUID

from fastapi import APIRouter, Path, Depends

from starlette.status import HTTP_200_OK

from api.policy.v1.response import GetPolicyResponse
from app.policy.service import PolicyQueryService
from core.fastapi.schemas import ExceptionResponseSchema

policy_router = APIRouter()


def newService():
    return PolicyQueryService()


@policy_router.get("/{policy_id}",
                   description="Get policies by policy id",
                   response_model=GetPolicyResponse,
                   responses=ExceptionResponseSchema,
                   status_code=HTTP_200_OK)
async def get_policy_by_id(policy_id: UUID = Path(),
                           policyService: PolicyQueryService = Depends(newService)):
    return await policyService.get_policy_by_id(policy_id=policy_id)


@policy_router.get("/user/{user_id}",
                   description="Get policies by user id",
                   response_model=list[GetPolicyResponse],
                   responses=ExceptionResponseSchema,
                   status_code=HTTP_200_OK)
async def get_policies_by_user_id(user_id: UUID = Path(),
                                  policyService: PolicyQueryService = Depends(newService)):
    return await policyService.get_policies_by_user_id(user_id=user_id)
