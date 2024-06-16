from app.database import form_collection
from app.schemas import FormData, FormDataResponse
from bson.objectid import ObjectId

from motor.motor_asyncio import AsyncIOMotorCursor
from typing import Optional


async def create_form_data(data: FormData) -> FormDataResponse:
    """
    Create a new form data entry in the database.

    Parameters:
        data (FormData): The form data to be inserted into the database.

    Returns:
        FormDataResponse: The created form data with an ID.

    Raises:
        HTTPException: If an unexpected error occurs during insertion.
    """
    new_data = await form_collection.insert_one(data.model_dump())
    created_data = await form_collection.find_one({"_id": new_data.inserted_id})
    
    if created_data:
        created_data["_id"] = str(created_data["_id"])
    return created_data

async def get_form_data(id: str) -> dict:
    """
    Retrieve a single form data entry by its ID from the database.

    Parameters:
        id (str): The unique identifier of the form data entry.

    Returns:
        dict: The requested form data entry with its ID converted to string.

    Raises:
        HTTPException: If an unexpected error occurs during retrieval.
    """
    data = await form_collection.find_one({"_id": ObjectId(id)})
    if data:
        data['_id'] = str(data['_id'])
    return data

async def get_all_form_data(limit: Optional[int] = None) -> list[FormDataResponse]:
    """
    Retrieve all form data entries from the database with an optional limit.

    Parameters:
        limit (Optional[int], optional): The maximum number of entries to retrieve. Defaults to None.

    Returns:
        list[FormDataResponse]: A list of all retrieved form data entries with their IDs converted to string.

    Raises:
        HTTPException: If an unexpected error occurs during retrieval.
    """
    cursor: AsyncIOMotorCursor = form_collection.find().limit(limit) if limit else form_collection.find()
    data = await cursor.to_list(None)
    for item in data:
        item['_id'] = str(item['_id'])
    return data

async def delete_form_data(id: str) -> bool:
    """
    Delete a single form data entry by its ID from the database.

    Parameters:
        id (str): The unique identifier of the form data entry to be deleted.

    Returns:
        bool: True if deletion was successful, False otherwise.

    Raises:
        HTTPException: If an unexpected error occurs during deletion.
    """
    delete_result = await form_collection.delete_one({"_id": ObjectId(id)})
    return delete_result.deleted_count > 0

async def update_form_data(id: str, data: FormData) -> FormDataResponse:
    """
    Update an existing form data entry by its ID in the database.

    Parameters:
        id (str): The unique identifier of the form data entry to be updated.
        data (FormData): The new data for updating the form entry.

    Returns:
        FormDataResponse: The updated form data entry with its ID converted to string.

    Raises:
        HTTPException: If an unexpected error occurs during update.
    """
    update_result = await form_collection.update_one(
        {"_id": ObjectId(id)},
        {"$set": data.model_dump()}
    )
    updated_data = await form_collection.find_one({"_id": ObjectId(id)})
    if updated_data:
        updated_data['_id'] = str(updated_data['_id'])
    return updated_data


async def count_records() -> int:
    """
    Count the total number of form data entries in the database.

    Returns:
        int: The total count of form data entries.

    Raises:
        HTTPException: If an unexpected error occurs during counting.
    """
    count = await form_collection.count_documents({})
    return count
