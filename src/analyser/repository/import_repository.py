from sqlalchemy.ext.asyncio.session import AsyncSession
from analyser.domain.dtos import Import
from typing import Protocol

from analyser.domain.logger import Logger


class AsyncImportRepository(Protocol):
    async def save(self, import_dto: Import) -> None:
        ...


class AsyncSessionImportRepository:
    def __init__(
        self,
        session: AsyncSession,
        logger: Logger
    ) -> None:
        self._session: AsyncSession = session
        self.log: Logger = logger

    async def save(self, import_dto: Import) -> None:
        self._session.add(import_dto)

