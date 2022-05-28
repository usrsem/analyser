from loguru import logger
from analyser.domain.dtos import CitizenDto, ImportIdDto
from sqlalchemy.orm import mapper
from db.shemas import citizen_table, import_table

def start_mappers():
    mapper(CitizenDto, citizen_table, confirm_deleted_rows=False)
    mapper(ImportIdDto, import_table, confirm_deleted_rows=False)
    logger.info("Mappers started")

