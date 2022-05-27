import uuid
from dataclasses import dataclass
from datetime import date
from enum import unique, Enum

from dataclasses import dataclass


class Gender(Enum):
    FEMALE = "female"
    MALE = "male"
    NOT_MENTIONED = "not_mentioned"


@dataclass
class Citizen:
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


@dataclass
class ImportId:
    import_id: uuid.UUID = uuid.uuid4()


@dataclass
class Import:
    citizens: list[Citizen]
    import_id: ImportId = ImportId()

