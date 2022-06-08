from analyser.repository.citizen_repository import AsyncCitizenRepository, AsyncSessionCitizenRepository
from analyser.repository.import_repository import AsyncImportRepository, AsyncSessionImportRepository
from analyser.repository.repository_uow import SqlAlchemyUnitOfWork
from analyser.service.imports_service import ImportsService, V1ImportsService
from db.context import DEFAULT_SESSION_FACTORY


def get_citizen_repository() -> AsyncCitizenRepository:
    return AsyncSessionCitizenRepository(DEFAULT_SESSION_FACTORY())


def get_imports_repository() -> AsyncImportRepository:
    return AsyncSessionImportRepository(DEFAULT_SESSION_FACTORY())


def get_imports_service() -> ImportsService:
    return V1ImportsService(SqlAlchemyUnitOfWork())

