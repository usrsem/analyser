from dataclasses import asdict
from uuid import UUID

from fastapi.params import Depends
from analyser import factories
from analyser.domain import mappers
from analyser.domain.dtos import ImportDto, ImportIdDto
from analyser.domain.pydantic import ImportModel
from analyser.loader import app, log

from analyser.service.imports_service import ImportsService

from typing import Optional


@app.post("/imports")
async def add_imports(
    import_model: ImportModel,
    service: ImportsService = Depends(factories.get_imports_service)
) -> dict:
    import_dto: ImportDto = mappers.import_model_to_dto(import_model)
    log.info(f"Adding {import_dto=}")
    await service.add_import(import_dto)
    return asdict(import_dto.import_id)


@app.get("/imports/{import_id}/citizens")
async def get_imports(
    import_id: UUID,
    service: ImportsService = Depends(factories.get_imports_service)
) -> Optional[ImportModel]:

    import_id_dto: ImportIdDto = ImportIdDto(import_id)
    import_dto: ImportDto = await service.get_import(import_id_dto)

    log.info(f"Get {import_dto.citizens=}")
    return mappers.import_dto_to_model(import_dto)

