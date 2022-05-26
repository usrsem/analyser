from contextlib import asynccontextmanager
from typing import AsyncGenerator
from sqlalchemy.orm import sessionmaker, Mapper, Query
from sqlalchemy.orm.scoping import scoped_session
from sqlalchemy.ext.asyncio import AsyncSession
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


start_mappers()

_async_session_factory: sessionmaker = sessionmaker(
        query_cls=_get_query_cls, class_=AsyncSession)

async_session: scoped_session = scoped_session(_async_session_factory)

