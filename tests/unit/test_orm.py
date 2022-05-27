from sqlalchemy.ext.asyncio.session import AsyncSession
from analyser.domain.dtos import Citizen, ImportDto


async def test_citizen_mapper_can_save_row(
    citizen: Citizen,
    session: AsyncSession
) -> None:

    async with session.begin():
        session.add(citizen)

    after = await session.get(
                        Citizen, (citizen.import_id, citizen.citizen_id))

    async with session.begin():
        await session.delete(citizen)

    msg: str = f"{after = }, {citizen = }"

    assert after == citizen, msg

