from fastapi import FastAPI
from loguru import logger

from db.mappers import start_mappers

start_mappers()
app = FastAPI()
log = logger

