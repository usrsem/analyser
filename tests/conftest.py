import pytest
from datetime import date
from analyser.config import ASYNC_DEFAULT_PG_URL
from analyser.domain.dtos import Citizen, Gender, ImportDto
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


@pytest.fixture(scope="function")
async def citizen(session):
    import_dto = ImportDto()
    session.add(import_dto)
    await session.commit()

    yield Citizen(
        "town1",
        "street1",
        "building1",
        1,
        "name1",
        date.today(),
        Gender.MALE,
        import_id=import_dto.import_id)

    await session.delete(import_dto)
    await session.commit()

