from fastapi import FastAPI
from app.api.propostas import router

app = FastAPI()
app.include_router(router)
