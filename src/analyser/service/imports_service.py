from typing import Protocol

from analyser.domain.dtos import ImportDto, ImportIdDto
from analyser.domain.pydantic import ImportModel
from analyser.repository.repository_uow import RepositoryUnitOfWork
from analyser.loader import log


class ImportsService(Protocol):
    async def add_import(self, import_dto: ImportDto) -> ImportIdDto:
        ...

    async def get_import(self, import_id_dto: ImportIdDto) ->ImportDto:
        ...


class V1ImportsService:
    def __init__(self, repository_uow: RepositoryUnitOfWork) -> None:
        self.uow: RepositoryUnitOfWork = repository_uow

    async def add_import(self, import_dto: ImportDto) -> ImportIdDto:
        for citizen in import_dto.citizens:
            citizen.import_id = import_dto.import_id.import_id

        async with self.uow:
            await self.uow.imports.save(import_dto.import_id)
            await self.uow.commit()
            await self.uow.citizens.save_all(import_dto.citizens)
            await self.uow.commit()

        return import_dto.import_id

    async def get_import(self, import_id_dto: ImportIdDto) -> ImportDto:
        async with self.uow:
            res = await self.uow.imports.get(import_id_dto)

            # TODO: WHAT ??
            await self.uow.commit()

            return res
