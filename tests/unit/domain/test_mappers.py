from datetime import date, datetime
from uuid import UUID, uuid4
from analyser.domain.dtos import CitizenDto, Gender
from analyser.domain.pydantic import CitizenModel
from analyser.domain.mappers import citizen_model_to_dto, citizen_dto_to_model
from copy import deepcopy
from typing import Any


import_id: UUID = uuid4()
citizen_id: UUID = uuid4()

data: dict[str, Any] = {
    "town": "some_town",
    "street": "some_street",
    "building": "some_building",
    "apartment": 1,
    "name": "some_name",
    "relatives": tuple(),
    "import_id": import_id,
    "citizen_id": citizen_id
}

model_data = deepcopy(data)
model_data["birth_date"] = "01.01.1970"
model_data["gender"] = "male"

dto_data = deepcopy(data)
dto_data["birth_date"] = datetime.strptime("01.01.1970", "%d.%m.%Y").date()
dto_data["gender"] = Gender.MALE

citizen_model = CitizenModel(**model_data)
citizen_dto = CitizenDto(**dto_data)


def test_mapping_citizen_model_to_dto():
    before = citizen_model
    after = citizen_model_to_dto(before)
    mustbe = citizen_dto

    msg = f"{before=}, {after=}, {mustbe=}"

    assert after == mustbe


def test_mapping_citizen_dto_to_model():
    before = citizen_dto
    after = citizen_dto_to_model(before)
    mustbe = citizen_model

    msg = f"{before=}, {after=}, {mustbe=}"

    assert after == mustbe

