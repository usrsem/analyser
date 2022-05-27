import uuid
from dataclasses import dataclass
from datetime import date
from enum import unique, Enum

from pydantic.main import BaseModel


@unique
class Gender(Enum):
    FEMALE = "female"
    MALE = "male"
    NOT_MENTIONED = "not_mentioned"


class Citizen(BaseModel):
    town: str
    street: str
    building: str
    apartment: int
    name: str
    birth_date: date
    gender: Gender
    relatives: tuple[uuid.UUID] = tuple()
    import_id: uuid.UUID = uuid.uuid4()
    citizen_id: uuid.UUID = uuid.uuid4()


class ImportDto(BaseModel):
    import_id: uuid.UUID = uuid.uuid4()


