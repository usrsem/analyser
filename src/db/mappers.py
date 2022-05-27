from analyser.domain.dtos import Citizen, Import
from sqlalchemy.orm import mapper
from db.shemas import citizen_table, import_table

def start_mappers():
    mapper(Citizen, citizen_table, confirm_deleted_rows=False)
    mapper(Import, import_table, confirm_deleted_rows=False)

