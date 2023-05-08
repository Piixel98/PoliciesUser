from uuid import UUID

from pydantic import BaseModel, Field, EmailStr

from core.enums import BaseEnum


class Role(str, BaseEnum):
    user = 'user'
    admin = 'admin'


class UserSchema(BaseModel):
    id: UUID = Field(description="User ID")
    name: str = Field(description="Name")
    email: EmailStr = Field(description="E-Mail")
    role: Role = Field(description="Role")
