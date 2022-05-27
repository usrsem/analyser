import uuid
from marshmallow.exceptions import ValidationError
import pytest
from analyser.domain.dtos import Citizen, Gender
from analyser.deserialization.schemas import CitizenSchema
from copy import copy
from datetime import datetime
from typing import Any


relatives_ids = [uuid.uuid4() for _ in range(3)]
citizen_id = uuid.uuid4()

citizen_as_dict: dict[str, Any] = {
    "town": "some_town",
    "building": "some_building",
    "street": "some_street",
    "apartment": "7",
    "name": "some_name",
    "birth_date": "18.04.2002",
    "gender": "male",
    "relatives": relatives_ids,
    "citizen_id": citizen_id,
}

original_citizen: Citizen = Citizen(
    town="some_town",
    street="some_street",
    building="some_building",
    apartment=7,
    name="some_name",
    birth_date=datetime.strptime("18.04.2002", "%d.%m.%Y").date(),
    gender=Gender.MALE,
    relatives=tuple(relatives_ids),
    citizen_id=citizen_id,
)


def test_citizen_deserialization() -> None:
    schema: CitizenSchema = CitizenSchema()
    after = schema.load(citizen_as_dict)
    msg: str = f"{citizen_as_dict=}\n{after=}\n{original_citizen=}"
    assert after == original_citizen, msg


def test_wrang_apartment_type() -> None:
    before: dict[str, str] = copy(citizen_as_dict)
    schema: CitizenSchema = CitizenSchema()
    before["apartment"] = "asdf"
    with pytest.raises(ValidationError):
        schema.load(before)

