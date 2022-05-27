from analyser.domain.dtos import CitizenDto
from analyser.domain.pydantic import CitizenModel
from dataclasses import asdict


def citizen_model_to_dto(m: CitizenModel) -> CitizenDto:
    return CitizenDto(**dict(m))


def citizen_dto_to_model(d: CitizenDto) -> CitizenModel:
    return CitizenModel(**asdict(d))

