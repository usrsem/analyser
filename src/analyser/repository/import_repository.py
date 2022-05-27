from sqlalchemy.ext.asyncio.session import AsyncSession
from analyser.domain.dtos import ImportIdDto
from typing import Protocol

from analyser.domain.logger import Logger


class AsyncImportRepository(Protocol):
    async def save(self, import_dto: ImportIdDto) -> None:
        ...


class AsyncSessionImportRepository:
    def __init__(self,session: AsyncSession) -> None:
        self._session: AsyncSession = session

    async def save(self, import_dto: ImportIdDto) -> None:
        self._session.add(import_dto)

