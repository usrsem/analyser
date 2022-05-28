from uuid import uuid4
from analyser.domain.dtos import CitizenDto
from analyser.domain.pydantic import CitizenModel
from dataclasses import asdict


def citizen_model_to_dto(m: CitizenModel) -> CitizenDto:
    m_as_dict = dict(m)
    m_as_dict["import_id"] = uuid4()
    return CitizenDto(**dict(m))


def citizen_dto_to_model(d: CitizenDto) -> CitizenModel:
    return CitizenModel(**asdict(d))

