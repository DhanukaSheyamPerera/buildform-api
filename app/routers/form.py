from fastapi import APIRouter, Depends, HTTPException
from app.schemas import FormData, FormDataResponse
from app.crud import create_form_data, get_form_data, get_all_form_data, delete_form_data, count_records
from app.exceptions import FormDataNotFoundException, FormCreationFailedException, FormRecordsNullExceptionn
from app.verification import verify_password


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
    
@router.delete("/forms/{id}", response_model=dict)
async def delete_form(id: str, username: str = Depends(verify_password)):
    try:
        deleted = await delete_form_data(id)
        if not deleted:
            raise FormDataNotFoundException()
        return {"message": "Form deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get("/forms-count", response_model=dict)
async def get_form_count():
    try:
        count = await count_records()
        if not count:
            raise FormRecordsNullExceptionn()
        return {"records_count": count}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
