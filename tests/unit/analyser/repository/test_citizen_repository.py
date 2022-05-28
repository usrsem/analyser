import pytest
from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlalchemy.exc import SQLAlchemyError
from analyser.repository.citizen_repository import AsyncCitizenRepository, AsyncSessionCitizenRepository
from analyser.domain.dtos import CitizenDto
from typing import Optional


@pytest.fixture
async def repository(session):
    yield AsyncSessionCitizenRepository(session)


async def test_save_citizens(
    repository: AsyncCitizenRepository,
    session: AsyncSession,
    citizen: CitizenDto,
) -> None:
    await repository.save_all([citizen]) 
    await session.commit()

    mustbe = await session.get(
        CitizenDto, (citizen.import_id, citizen.citizen_id))


    await session.delete(citizen)
    await session.commit()

    assert citizen == mustbe


async def test_find_by_citizen_id(
    repository: AsyncCitizenRepository,
    session: AsyncSession,
    citizen: CitizenDto
) -> None:
    await repository.save_all([citizen])
    await session.commit()


    new_citizen: Optional[CitizenDto] = await repository.find_by_citizen_id(
        citizen.citizen_id)

    await session.delete(citizen)
    await session.commit()

    assert citizen == new_citizen


async def test_delete_by_citizen_id(
    repository: AsyncCitizenRepository,
    session: AsyncSession,
    citizen: CitizenDto
) -> None:
    await repository.save_all([citizen])
    await session.commit()

    await repository.delete_by_citizen_id(citizen.citizen_id)
    await session.commit()

    after: Optional[CitizenDto] = await repository.find_by_citizen_id(
        citizen.citizen_id) 

    await session.delete(citizen)
    await session.commit()

    assert after == None


async def test_delete_by_citizen_empty_row(
    repository: AsyncCitizenRepository,
    citizen: CitizenDto
) -> None:
    try:
        await repository.delete_by_citizen_id(citizen.citizen_id)
    except SQLAlchemyError:
        raise AssertionError()

