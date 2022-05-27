from uuid import UUID
from analyser.domain.logger import Logger
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from analyser.domain.dtos import CitizenDto
from typing import Iterable, Optional, Protocol


class AsyncCitizenRepository(Protocol):
    async def save_all(self, citizens: Iterable[CitizenDto]) -> None:
        ...

    async def find_by_citizen_id(self, citizen_id: UUID) -> Optional[CitizenDto]:
        ...

    async def delete_by_citizen_id(self, citizen_id: UUID) -> None:
        ...


class AsyncSessionCitizenRepository:
    def __init__(self,session: AsyncSession) -> None:
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

