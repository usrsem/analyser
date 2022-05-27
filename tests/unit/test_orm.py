from sqlalchemy.ext.asyncio.session import AsyncSession
from analyser.domain.dtos import CitizenDto


async def test_citizen_mapper_can_save_row(
    citizen: CitizenDto,
    session: AsyncSession
) -> None:

    async with session.begin():
        session.add(citizen)

    after = await session.get(
                        CitizenDto, (citizen.import_id, citizen.citizen_id))

    async with session.begin():
        await session.delete(citizen)

    msg: str = f"{after = }, {citizen = }"

    assert after == citizen, msg

