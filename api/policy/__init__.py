from fastapi import APIRouter

from api.policy.v1.policy import policy_router

sub_router = APIRouter()
sub_router.include_router(policy_router, prefix="/policies", tags=["User"])


__all__ = ["sub_router"]
