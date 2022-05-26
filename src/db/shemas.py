from analyser.domain.dtos import Gender
from analyser.config import DEFAULT_PG_URL

from sqlalchemy.engine.create import create_engine
from sqlalchemy.sql.schema import MetaData
from sqlalchemy import (
    Table, Column, Integer, String, ForeignKey,
    Date, Enum, ForeignKeyConstraint
)


engine = create_engine(DEFAULT_PG_URL)
metadata = MetaData(bind=engine)


import_table = Table(
    'import',
    metadata,
    Column('import_id', Integer, primary_key=True)
)

citizen_table = Table(
    'citizen',
    metadata,
    Column('import_id', Integer, ForeignKey('imports.import_id'),
           primary_key=True),
    Column('citizen_id', Integer, primary_key=True),
    Column('town', String, nullable=False, index=True),
    Column('street', String, nullable=False),
    Column('building', String, nullable=False),
    Column('apartment', Integer, nullable=False),
    Column('name', String, nullable=False),
    Column('birth_date', Date, nullable=False),
    Column('gender', Enum(Gender, name='gender'), nullable=False),
)

relation_table = Table(
    'relation',
    metadata,
    Column('import_id', Integer, primary_key=True),
    Column('citizen_id', Integer, primary_key=True),
    Column('relative_id', Integer, primary_key=True),
    ForeignKeyConstraint(
        ('import_id', 'citizen_id'),
        ('citizens.import_id', 'citizens.citizen_id')
    ),
    ForeignKeyConstraint(
        ('import_id', 'relative_id'),
        ('citizens.import_id', 'citizens.citizen_id')
    ),
)


