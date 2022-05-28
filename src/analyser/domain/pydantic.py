import uuid

from pydantic.class_validators import validator
from pydantic.error_wrappers import ValidationError

from analyser.domain.dtos import Gender
from datetime import date, datetime
from pydantic.main import BaseModel

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

    @validator('relatives')
    def validate_relatives_unique(cls, v: list):
        if len(v) != len(set(v)):
            raise ValidationError('relatives must be unique', CitizenModel)


class ImportModel(BaseModel):
    citizens: list[CitizenModel]

    # @validator("citizens")
    # def validate_unique_citizen_id(cls, v):
    #     citizen_ids = set()
    #     for citizen in v:
    #         if citizen.citizen_id in citizen_ids:
    #             raise ValidationError(
    #                 f"Citizen id {citizen.citizen_id} is not unique",
    #                 CitizenModel
    #             )

    #         citizen_ids.add(citizen.citizen_id)

    #     return v

    # @validator("citizens")
    # def validate_relatives(cls, v):
    #     relatives = {
    #         citizen.citizen_id: set(citizen.relatives)
    #         for citizen in v
    #     }

    #     for citizen_id, relative_ids in relatives.items():
    #         for relative_id in relative_ids:
    #             if citizen_id not in relatives.get(relative_id, set()):
    #                 raise ValidationError(
    #                     f"citizen {relative_id} does not have "
    #                     f"relation with {citizen_id}",
    #                     ImportModel
    #                 )

