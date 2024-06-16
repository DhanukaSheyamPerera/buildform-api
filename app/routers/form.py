from fastapi import APIRouter, Depends, HTTPException
from app.schemas import FormData, FormDataResponse
from app.crud import create_form_data, get_form_data, get_all_form_data, delete_form_data, count_records, update_form_data
from app.exceptions import FormDataNotFoundException, FormCreationFailedException, FormRecordsNullException
from app.verification import verify_password


router = APIRouter()

@router.post("/forms", response_model=FormDataResponse)
async def submit_form(form_data: FormData):
    """
    Submit a new form entry.

    Parameters:
        form_data (FormData): The form data to be submitted.

    Returns:
        FormDataResponse: The created form data with an ID.

    Raises:
        FormCreationFailedException: If the form data could not be created.
        HTTPException: If an unexpected error occurs.
    """
    try:
        created_data = await create_form_data(form_data)
        if not created_data:
            raise FormCreationFailedException()
        return created_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/forms/{id}", response_model=FormData)
async def get_form(id: str):
    """
    Retrieve a single form entry by its ID.

    Parameters:
        id (str): The unique identifier of the form entry.

    Returns:
        FormData: The requested form data.

    Raises:
        FormDataNotFoundException: If the form data with the given ID is not found.
        HTTPException: If an unexpected error occurs.
    """
    try:
        data = await get_form_data(id)
        if not data:
            raise FormDataNotFoundException()
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/forms/", response_model=list[FormDataResponse])
async def get_all_forms(limit: int = None):
    """
    Retrieve all form entries with an optional limit.

    Parameters:
        limit (int, optional): The maximum number of form entries to retrieve. Defaults to None.

    Returns:
        list[FormDataResponse]: A list of all retrieved form entries.

    Raises:
        HTTPException: If an unexpected error occurs.
    """
    try:
        forms = await get_all_form_data(limit)
        return forms
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/forms/{id}", response_model=dict)
async def delete_form(id: str, username: str = Depends(verify_password)):
    """
    Delete a single form entry by its ID.

    Parameters:
        id (str): The unique identifier of the form entry to be deleted.
        username (str): The username of the user performing the deletion. Verified by `verify_password`.

    Returns:
        dict: A message indicating successful deletion.

    Raises:
        FormDataNotFoundException: If the form data with the given ID is not found.
        HTTPException: If an unexpected error occurs.
    """
    try:
        deleted = await delete_form_data(id)
        if not deleted:
            raise FormDataNotFoundException()
        return {"message": "Form deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



@router.put("/forms/{id}", response_model=FormData)
async def update_record(id: str, data: FormData, username: str = Depends(verify_password)):
    """
    Update an existing form entry by its ID.

    Parameters:
        id (str): The unique identifier of the form entry to be updated.
        data (FormData): The new data for updating the form entry.
        username (str): The username of the user performing the update. Verified by `verify_password`.

    Returns:
        FormData: The updated form data.

    Raises:
        FormDataNotFoundException: If the form data with the given ID is not found.
        HTTPException: If an unexpected error occurs.
    """
    try:
        updated = await update_form_data(id, data)
        if not updated:
            raise FormDataNotFoundException()
        return updated
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/forms-count", response_model=dict)
async def get_form_count():
    """
    Retrieve the total count of all form entries.

    Returns:
        dict: A dictionary containing the count of records.

    Raises:
        FormRecordsNullException: If there are no records found.
        HTTPException: If an unexpected error occurs.
    """
    try:
        count = await count_records()
        if not count:
            raise FormRecordsNullException()
        return {"records_count": count}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
