from fastapi import APIRouter
from app.schemas import FormData
from app.crud import create_form_data


router = APIRouter()

@router.post("/submit-form")
async def submit_form(form_data: FormData):
    created_data = await create_form_data(form_data)
    return created_data