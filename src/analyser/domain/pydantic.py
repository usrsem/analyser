import pydantic
import uuid

from pydantic.class_validators import validator
from pydantic.error_wrappers import ValidationError

from analyser.domain.dtos import Gender
from datetime import date, datetime
from pydantic.main import BaseModel

from analyser.domain.dtos import CitizenDto
from typing import Optional


class CitizenModel(BaseModel):
    town: str
    street: str
    building: str
    apartment: int
    name: str
    birth_date: date
    gender: Gender
    relatives: tuple[uuid.UUID, ...]
    import_id: Optional[uuid.UUID]
    citizen_id: uuid.UUID

    @validator("birth_date", pre=True)
    def parse_birthdate(cls, value):
        if isinstance(value, date):
            return value

        return datetime.strptime(
            value,
            "%d.%m.%Y"
        ).date()

    @validator("birth_date")
    def birth_date_must_be_older_then_now(cls, v):
        if v > date.today():
            raise ValidationError(
                "Birth date must be older then today", CitizenModel)

        return v
    

class ImportModel(BaseModel):
    citizens: list[CitizenModel]

