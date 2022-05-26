from analyser.domain.dtos import Citizen
from sqlalchemy.orm import mapper
from db.shemas import citizen_table

def start_mappers():
    mapper(Citizen, citizen_table)

