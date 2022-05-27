import pytest
from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlalchemy.future import select
from analyser.domain.dtos import ImportDto, ImportIdDto

from analyser.repository.repository_uow import SqlAlchemyUnitOfWork
from db.context import DEFAULT_SESSION_FACTORY


@pytest.fixture
def uow():
    return SqlAlchemyUnitOfWork()


@pytest.fixture
def session_factory():
    return DEFAULT_SESSION_FACTORY


async def test_rolls_back_uncommitted_work_by_default(session_factory, uow):
    async with uow:
        uow._asession.add(ImportIdDto())

    new_session: AsyncSession = session_factory()
    rows = await new_session.execute(select(ImportIdDto))
    assert rows.scalars().all() == []


async def test_rolls_back_on_error(session_factory, uow):
    class MyException(Exception):
        pass

    with pytest.raises(MyException):
        async with uow:
            uow._asession.add(ImportIdDto())
            raise MyException()

    new_session = session_factory()
    rows = await new_session.execute(select(ImportIdDto))
    assert rows.scalars().all() == []

