import datetime
from uuid import UUID

from pydantic import BaseModel, EmailStr, confloat


class PolicySchema(BaseModel):
    id: UUID
    amountInsured: confloat(gt=0)
    email: EmailStr
    inceptionDate: datetime.datetime
    installmentPayment: bool
    clientId: UUID

    class Config:
        json_encoders = {
            UUID: lambda val: str(val)
        }
