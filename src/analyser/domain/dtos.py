import uuid
from dataclasses import dataclass
from datetime import date
from enum import Enum

from dataclasses import dataclass


class Gender(Enum):
    FEMALE = "female"
    MALE = "male"
    NOT_MENTIONED = "not_mentioned"


@dataclass
class CitizenDto:
    town: str
    street: str
    building: str
    apartment: int
    name: str
    birth_date: date
    gender: Gender
    import_id: uuid.UUID
    citizen_id: uuid.UUID
    relatives: tuple[uuid.UUID, ...] = ()


@dataclass
class ImportIdDto:
    import_id: uuid.UUID = uuid.uuid4()


@dataclass
class ImportDto:
    citizens: list[CitizenDto]
    import_id: ImportIdDto

