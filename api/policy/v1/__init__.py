from fastapi import APIRouter

from .policy import policy_router

sub_router = APIRouter()
sub_router.include_router(policy_router, prefix="/api/v1/policies", tags=["Policy"])


__all__ = ["sub_router"]
