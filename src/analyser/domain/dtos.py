from dataclasses import dataclass
from datetime import date
from enum import unique, Enum
from typing import Optional


@unique
class Gender(Enum):
    FEMALE = "female"
    MALE = "male"
    NOT_MENTIONED = "not_mentioned"


@dataclass(unsafe_hash=True, eq=True)
class Citizen:
    citizen_id: int
    town: str
    street: str
    building: str
    apartment: int
    name: str
    birth_date: date
    gender: Gender
    import_id: Optional[int] = None
    relatives: tuple[int] = tuple()


@dataclass(unsafe_hash=True, eq=True)
class ImportDto:
    import_id: int


