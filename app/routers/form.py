from fastapi import APIRouter, HTTPException
from app.schemas import FormData, FormDataResponse
from app.crud import create_form_data, get_form_data, get_all_form_data
from app.exceptions import FormDataNotFoundException, FormCreationFailedException


router = APIRouter()

@router.post("/submit-form", response_model=FormDataResponse)
async def submit_form(form_data: FormData):
    try:
        created_data = await create_form_data(form_data)
        if not created_data:
            raise FormCreationFailedException()
        return created_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/forms/{id}", response_model=FormData)
async def get_form(id: str):
    try:
        data = await get_form_data(id)
        if not data:
            raise FormDataNotFoundException()
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/forms/", response_model=list[FormDataResponse])
async def get_all_forms(limit: int = None):
    try:
        forms = await get_all_form_data(limit)
        return forms
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))