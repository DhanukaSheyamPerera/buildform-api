from fastapi import APIRouter

router = APIRouter()

@router.post("/submit-form")
def submit_form():
    return {"data": "form-submitted"}