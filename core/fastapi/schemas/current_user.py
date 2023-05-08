from uuid import UUID

from pydantic import BaseModel


class CurrentUser(BaseModel):
    id: UUID = None

    class Config:
        validate_assignment = True
