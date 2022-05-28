from datetime import datetime
from uuid import UUID, uuid4
from analyser.domain.dtos import CitizenDto, Gender
from analyser.domain.pydantic import CitizenModel
from analyser.domain.mappers import citizen_model_to_dto, citizen_dto_to_model
from typing import Any


import_id: UUID = uuid4()
citizen_id: UUID = uuid4()

model_data: dict[str, Any] = {
    "town": "some_town",
    "street": "some_street",
    "building": "some_building",
    "apartment": 1,
    "name": "some_name",
    "birth_date": "01.01.1970",
    "gender": "male",
    "relatives": tuple(),
    # "import_id": import_id,
    "citizen_id": citizen_id,
}

dto_data: dict[str, Any] = {
    "town": "some_town",
    "street": "some_street",
    "building": "some_building",
    "apartment": 1,
    "name": "some_name",
    "birth_date": datetime.strptime("01.01.1970", "%d.%m.%Y").date(),
    "gender": Gender.MALE,
    "relatives": tuple(),
    "import_id": import_id,
    "citizen_id": citizen_id,
}

citizen_dto = CitizenDto(**dto_data)
citizen_model = CitizenModel(**model_data)


def test_mapping_citizen_model_to_dto():
    before = citizen_model
    after = citizen_model_to_dto(before)
    after.import_id = import_id
    mustbe = citizen_dto

    msg = f"{before=}, {after=}, {mustbe=}"

    assert after == mustbe, msg


def test_mapping_citizen_dto_to_model():
    before = citizen_dto
    after = citizen_dto_to_model(before)
    mustbe = citizen_model
    mustbe.import_id = import_id

    msg = f"{before=}, {after=}, {mustbe=}"

    assert after == mustbe, msg

