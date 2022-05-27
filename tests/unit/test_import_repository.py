import pytest
from analyser.domain.dtos import ImportId
from analyser.repository.import_repository import AsyncImportRepository, AsyncSessionImportRepository
from sqlalchemy.ext.asyncio.session import AsyncSession
from loguru import logger


@pytest.fixture
def repository(session):
    return AsyncSessionImportRepository(session, logger) # type: ignore


async def test_saves_import(
    repository: AsyncImportRepository,
    session: AsyncSession
) -> None:
    import_dto = ImportId()

    await repository.save(import_dto)
    await session.commit()

    new_import = await session.get(ImportId, import_dto.import_id)

    await session.delete(import_dto)
    await session.commit()

    assert new_import == import_dto

