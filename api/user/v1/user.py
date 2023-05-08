from uuid import UUID
from api.user.v1.response import GetUserResponse
from app.user.service import UserQueryService

from fastapi import APIRouter, Query, Path, Depends
from starlette.status import HTTP_200_OK

from core.fastapi.dependencies import PermissionDependency, IsAdmin, IsUser
from core.fastapi.schemas.response import ExceptionResponseSchema

user_router = APIRouter()


def newService():
    return UserQueryService()


@user_router.get("",
                 description="Get users by criteria",
                 response_model=GetUserResponse,
                 responses=ExceptionResponseSchema,
                 dependencies=[Depends(PermissionDependency([IsUser]))],
                 status_code=HTTP_200_OK)
async def get_user_by_name(name: str = Query(),
                           userService: UserQueryService = Depends(newService)):
    return await userService.get_user_by_name(name=name)


@user_router.get("/{user_id}",
                 description="Get users by id",
                 response_model=GetUserResponse,
                 responses=ExceptionResponseSchema,
                 dependencies=[Depends(PermissionDependency([IsUser]))],
                 status_code=HTTP_200_OK)
async def get_user_by_id(user_id: UUID = Path(),
                         userService: UserQueryService = Depends(newService)):
    return await userService.get_user_by_id(user_id=user_id)


@user_router.get("/policy/{policy_id}",
                 description="Get user by policy id",
                 response_model=GetUserResponse,
                 responses=ExceptionResponseSchema,
                 dependencies=[Depends(PermissionDependency([IsAdmin]))],
                 status_code=HTTP_200_OK)
async def get_user_by_policy_id(policy_id: UUID = Path(),
                                userService: UserQueryService = Depends(newService)):
    return await userService.get_users_by_policy_id(policy_id=policy_id)
