from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlalchemy.future import select
from analyser.domain.dtos import CitizenDto, ImportDto, ImportIdDto
from typing import Protocol

from analyser.domain.pydantic import ImportModel
from analyser.loader import log


class AsyncImportRepository(Protocol):
    async def save(self, import_dto: ImportIdDto) -> None:
        ...

    async def get(self, import_id_dto: ImportIdDto) -> ImportDto:
        ...


class AsyncSessionImportRepository:
    def __init__(self,session: AsyncSession) -> None:
        self._session: AsyncSession = session

    async def save(self, import_dto: ImportIdDto) -> None:
        self._session.add(import_dto)

    async def get(self, import_id_dto: ImportIdDto) -> ImportDto:
        q = (select(CitizenDto)
            .where(CitizenDto.import_id == import_id_dto.import_id))

        result = await self._session.execute(q)

        return ImportDto(result.scalars().all(), import_id_dto)


class FakeImportRepository:

    def __init__(self, cache: list[ImportIdDto]) -> None:
        self.cache: list[ImportIdDto] = cache

    async def save(self, import_dto: ImportIdDto) -> None:
        self.cache.append(import_dto)

    async def get(self, import_id_dto: ImportIdDto) -> ImportDto:
        return None

