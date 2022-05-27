from loguru import logger
from analyser.repository.citizen_repository import AsyncCitizenRepository, AsyncSessionCitizenRepository
from analyser.repository.import_repository import AsyncImportRepository, AsyncSessionImportRepository
from db.context import session


def get_citizen_repository() -> AsyncCitizenRepository:
    return AsyncSessionCitizenRepository(session(), logger)


def get_imports_repository() -> AsyncImportRepository:
    return AsyncSessionImportRepository(session(), logger)

