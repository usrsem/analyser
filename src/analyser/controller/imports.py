from dataclasses import asdict

from fastapi.params import Depends
from analyser import factories
from analyser.domain import mappers
from analyser.domain.dtos import ImportDto
from analyser.domain.pydantic import ImportModel
from analyser.loader import app, log

from analyser.service.imports_service import ImportsService


@app.post("/imports")
async def add_imports(
    import_model: ImportModel,
    service: ImportsService = Depends(factories.get_imports_service)
) -> dict:
    import_dto: ImportDto = mappers.import_model_to_dto(import_model)
    log.info(f"Adding {import_dto=}")
    await service.add_import(import_dto)
    return asdict(import_dto.import_id)


