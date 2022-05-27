import pytest
from datetime import date
from analyser.domain.dtos import Citizen, Gender


@pytest.fixture
def citizen():
    return Citizen(
        "town1",
        "street1",
        "building1",
        1,
        "name1",
        date.today(),
        Gender.MALE)

