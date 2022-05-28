from typing import Protocol

from analyser.domain.dtos import ImportDto, ImportIdDto
from analyser.repository.repository_uow import RepositoryUnitOfWork


class ImportService(Protocol):
    async def add_import(self, import_dto: ImportDto) -> ImportIdDto:
        ...


class V1ImportService:
    def __init__(self, repository_uow: RepositoryUnitOfWork) -> None:
        self.uow: RepositoryUnitOfWork = repository_uow

    async def add_import(self, import_dto: ImportDto) -> ImportIdDto:
        async with self.uow:
            await self.uow.imports.save(import_dto.import_id)
            await self.uow.commit()
            await self.uow.citizens.save_all(import_dto.citizens)
            await self.uow.commit()

        return import_dto.import_id

