from fastapi import APIRouter, HTTPException
from app.schemas import FormData
from app.crud import create_form_data


router = APIRouter()

@router.post("/submit-form")
async def submit_form(form_data: FormData):
    try:
        created_data = await create_form_data(form_data)
        if not created_data:
            raise HTTPException(status_code=400, detail="Form data could not be created.")
        return created_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))