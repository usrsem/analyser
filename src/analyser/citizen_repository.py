from analyser.domain.dtos import Citizen
from typing import Optional, Protocol


class CitizenRepository(Protocol):
    def save(self, citizen: Citizen) -> None:
        ...

    def find_by_citizen_id(self, citizen_id: int) -> Optional[Citizen]:
        ...

    def delete_by_citizen_id(self, citizen_id: int) -> None:
        ...

