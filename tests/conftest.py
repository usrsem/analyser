from uuid import uuid4
import pytest
from datetime import date
from analyser.config import ASYNC_DEFAULT_PG_URL
from analyser.domain.dtos import CitizenDto, Gender, ImportIdDto
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker


@pytest.fixture(scope="function")
async def session():
    engine = create_async_engine(ASYNC_DEFAULT_PG_URL, echo=True)
    async_session = sessionmaker(
            engine, expire_on_commit=False, class_=AsyncSession)

    async with async_session() as session:
        yield session

    await engine.dispose()


def _random_citizen():
    return CitizenDto(
        town="town1",
        street="street1",
        building="building1",
        apartment=1,
        name="name1",
        birth_date=date.today(),
        gender=Gender.MALE,
        import_id=uuid4(),
        citizen_id=uuid4(),
        relatives=tuple())


@pytest.fixture
def random_citizen():
    return _random_citizen()


@pytest.fixture
def random_citizens_list():
    import_id = uuid4()
    citizens = [_random_citizen() for _ in range(10)]
    for citizen in citizens:
        citizen.import_id = import_id

    return citizens


@pytest.fixture(scope="function")
async def citizen(session):
    import_dto = ImportIdDto()
    session.add(import_dto)
    await session.commit()

    yield CitizenDto(
        town="town1",
        street="street1",
        building="building1",
        apartment=1,
        name="name1",
        birth_date=date.today(),
        gender=Gender.MALE,
        import_id=import_dto.import_id,
        citizen_id=uuid4(),
        relatives=tuple())

    await session.delete(import_dto)
    await session.commit()


# start_mappers()

