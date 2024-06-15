from fastapi import FastAPI
from app.routers import form

app = FastAPI()

app.include_router(form.router, prefix="/api", tags=["form"])