from uuid import UUID
from sqlalchemy.ext.asyncio.scoping import async_scoped_session
from analyser.domain.logger import Logger
from sqlalchemy.future import select
from sqlalchemy.orm.scoping import scoped_session
from sqlalchemy.ext.asyncio import AsyncSession
from analyser.domain.dtos import Citizen, ImportDto
from typing import Iterable, Optional, Protocol


class AsyncCitizenRepository(Protocol):
    async def save_citizens(self, citizens: Iterable[Citizen]) -> None:
        ...

    async def find_by_citizen_id(self, citizen_id: UUID) -> Optional[Citizen]:
        ...

    async def delete_by_citizen_id(self, citizen_id: UUID) -> None:
        ...


class AsyncSessionCitizenRepository:
    def __init__(
        self,
        session: AsyncSession,
        logger: Logger
    ) -> None:
        self._session: AsyncSession = session
        self.log: Logger = logger

    async def save_citizens(self, citizens: Iterable[Citizen]) -> None:
        self._session.add_all(citizens)

    async def find_by_citizen_id(self, citizen_id: UUID) -> Optional[Citizen]:
        result = await self._session.execute(
            select(Citizen)
            .where(Citizen.citizen_id == citizen_id))

        return result.scalar()

    async def delete_by_citizen_id(self, citizen_id: UUID) -> None:
        citizen: Optional[Citizen] = await self.find_by_citizen_id(citizen_id)

        if citizen is not None:
            await self._session.delete(citizen)

