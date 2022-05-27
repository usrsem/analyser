import abc
from typing import Protocol

from loguru import logger
from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlalchemy.orm.session import sessionmaker
from analyser.repository.citizen_repository import AsyncCitizenRepository, AsyncSessionCitizenRepository
from analyser.repository.import_repository import AsyncImportRepository, AsyncSessionImportRepository
from db.context import DEFAULT_SESSION_FACTORY


class RepositoryUnitOfWork(Protocol):
    imports: AsyncImportRepository
    citizens: AsyncCitizenRepository

    async def commit(self):
        ...

    async def rollback(self):
        ...

    async def __aenter__(self):
        ...

    async def __aexit__(self, *args):
        ...


class SqlAlchemyUnitOfWork:

    def __init__(self, asession_factory=DEFAULT_SESSION_FACTORY) -> None:
        self._asession_factory: sessionmaker = asession_factory

    async def __aenter__(self):
        self._asession: AsyncSession = self._asession_factory()
        self.imports = AsyncSessionImportRepository(self._asession)
        self.citizens = AsyncSessionCitizenRepository(self._asession)

    async def __aexit__(self, *args):
        await self.rollback()

    async def commit(self):
        await self._asession.commit()

    async def rollback(self):
        await self._asession.rollback()

