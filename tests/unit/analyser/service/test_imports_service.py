import pytest
from analyser.domain.dtos import ImportDto
from analyser.repository.repository_uow import FakeUnitOfWork, RepositoryUnitOfWork

from analyser.service.imports_service import ImportsService, V1ImportsService


@pytest.fixture
def service():
    return V1ImportsService(FakeUnitOfWork())


@pytest.fixture
def import_dto(random_citizens_list):
    dto = ImportDto(random_citizens_list)

    for citizen in dto.citizens:
        citizen.import_id = dto.import_id.import_id

    return dto


async def test_add_import(service, import_dto):
    await service.add_import(import_dto)
    assert service.uow.commited, f"{service.uow.commited}"

