import pytest
from analyser.domain.dtos import Citizen, ImportDto, Gender
from datetime import date
from sqlalchemy.orm import Session
from sqlalchemy.future import select
from db.context import async_session, new_session


@pytest.fixture
def citizen():
    return Citizen(
        "town1",
        "street1",
        "building1",
        1,
        "name1",
        date.today(),
        Gender.MALE)


async def test_citizen_mapper_can_save_row(citizen):
    import_dto: ImportDto = ImportDto(citizen.import_id)

    async_session.add(import_dto)
    await async_session.commit()
    
    async_session.add(citizen)
    await async_session.commit()

    after = await async_session.get(
                            Citizen, (citizen.import_id, citizen.citizen_id))

    await async_session.delete(citizen)
    await async_session.delete(import_dto)
    await async_session.commit()

    msg: str = f"{after = }, {citizen = }"

    assert after == citizen, msg


