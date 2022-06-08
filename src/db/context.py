from asyncio import current_task
from loguru import logger
from sqlalchemy.ext.asyncio.engine import create_async_engine
from sqlalchemy.orm import sessionmaker, Mapper, Query
from sqlalchemy.ext.asyncio import AsyncSession, async_scoped_session
from analyser.config import settings


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

_pg_url = (f"postgresql+asyncpg://{settings.pg_user}:{settings.pg_password}"
           f"@{settings.pg_host}/{settings.pg_db_name}")

DEFAULT_SESSION_FACTORY = sessionmaker(
    create_async_engine(_pg_url, echo=True),
    query_cls=_get_query_cls,
    expire_on_commit=False,
    class_=AsyncSession)


logger.info("Default session factory inited")

