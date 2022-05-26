from enum import unique, Enum
from dataclasses import dataclass
from datetime import date


@unique
class Gender(Enum):
    FEMALE = "female"
    MALE = "male"
    NOT_MENTIONED = "not_mentioned"


@dataclass(unsafe_hash=True, eq=True)
class Citizen:
    citizen_id: int
    town: str
    building: str
    apartment: int
    name: str
    birth_date: date
    gender: Gender


@dataclass(slots=True)
class ImportDto:
    import_id: int


