from uuid import UUID
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from analyser.domain.dtos import CitizenDto, ImportIdDto
from typing import Iterable, Optional, Protocol

from analyser.repository.import_repository import FakeImportRepository


class AsyncCitizenRepository(Protocol):
    async def save_all(self, citizens: Iterable[CitizenDto]) -> None:
        ...

    async def find_by_citizen_id(self, citizen_id: UUID) -> Optional[CitizenDto]:
        ...

    async def delete_by_citizen_id(self, citizen_id: UUID) -> None:
        ...


class AsyncSessionCitizenRepository:
    def __init__(self, session: AsyncSession) -> None:
        self._session: AsyncSession = session

    async def save_all(self, citizens: Iterable[CitizenDto]) -> None:
        self._session.add_all(citizens)

    async def find_by_citizen_id(self, citizen_id: UUID) -> Optional[CitizenDto]:
        result = await self._session.execute(
            select(CitizenDto)
            .where(CitizenDto.citizen_id == citizen_id))

        return result.scalar()

    async def delete_by_citizen_id(self, citizen_id: UUID) -> None:
        citizen: Optional[CitizenDto] = await self.find_by_citizen_id(citizen_id)

        if citizen is not None:
            await self._session.delete(citizen)


class FakeCitizenRepository:
    def __init__(
        self,
        cache: list[CitizenDto],
        imports: FakeImportRepository
    ) -> None:
        self.cache: list[CitizenDto] = cache
        self.imports: FakeImportRepository = imports

    async def save_all(self, citizens: Iterable[CitizenDto]) -> None:
        for citizen in citizens:
            if ImportIdDto(citizen.import_id) not in self.imports.cache:
                raise Exception("No such import_id in imports cache")

        self.cache.extend(citizens)

    async def find_by_citizen_id(self, citizen_id: UUID) -> Optional[CitizenDto]:
        for citizen in self.cache:
            if citizen.citizen_id == citizen_id:
                return citizen

    async def delete_by_citizen_id(self, citizen_id: UUID) -> None:
        citizen = await self.find_by_citizen_id(citizen_id)

        if citizen is not None:
            self.cache.remove(citizen)

