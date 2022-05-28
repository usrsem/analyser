from uuid import uuid4
from analyser.domain.dtos import CitizenDto, ImportDto, ImportIdDto
from analyser.domain.pydantic import CitizenModel, ImportModel
from dataclasses import asdict
from analyser.loader import log


def citizen_model_to_dto(m: CitizenModel) -> CitizenDto:
    m_as_dict = dict(m)
    m_as_dict["import_id"] = uuid4()
    return CitizenDto(**dict(m))


def citizen_dto_to_model(d: CitizenDto) -> CitizenModel:
    return CitizenModel(**asdict(d))


def import_model_to_dto(m: ImportModel) -> ImportDto:
    dto = ImportDto(
        citizens=[citizen_model_to_dto(citizen) for citizen in m.citizens],
        import_id=ImportIdDto())
    log.info(f"{dto=}")
    return dto


def import_dto_to_model(d: ImportDto) -> ImportModel:
    return ImportModel(
        citizens=[citizen_dto_to_model(citizen) for citizen in d.citizens])

