from asyncio import current_task
from contextlib import asynccontextmanager
from typing import AsyncGenerator
from sqlalchemy.ext.asyncio.engine import create_async_engine
from sqlalchemy.orm import sessionmaker, Mapper, Query
from sqlalchemy.ext.asyncio import AsyncSession, async_scoped_session
from analyser.config import ASYNC_DEFAULT_PG_URL
from db.mappers import start_mappers


@asynccontextmanager
async def new_session(**kwargs) -> AsyncGenerator:
    new_session = _async_session_factory(**kwargs)

    try:
        yield new_session
        await new_session.commit()
    except:
        await new_session.rollback()
        raise
    finally:
        await new_session.close()


def _get_query_cls(mapper, session):
    if mapper:
        m = mapper
        if isinstance(m, tuple):
            m = mapper[0]
        if isinstance(m, Mapper):
            m = m.entity

        try:
            return m.__query_cls__(mapper, session)
        except AttributeError:
            pass

    return Query(mapper, session)


_engine = create_async_engine(ASYNC_DEFAULT_PG_URL, echo=True)

_async_session_factory: sessionmaker = sessionmaker(
    _engine,
    query_cls=_get_query_cls,
    expire_on_commit=False,
    class_=AsyncSession)

session: async_scoped_session = async_scoped_session(
    _async_session_factory, scopefunc=current_task)


start_mappers()

