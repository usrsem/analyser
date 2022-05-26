from analyser.domain.dtos import Citizen, ImportDto
from sqlalchemy.orm import mapper
from db.shemas import citizen_table, import_table

def start_mappers():
    mapper(Citizen, citizen_table)
    mapper(ImportDto, import_table)

