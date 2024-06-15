from app.database import form_collection
from app.schemas import FormData
from bson.objectid import ObjectId

from motor.motor_asyncio import AsyncIOMotorCursor
from typing import Optional

async def create_form_data(data: FormData) -> dict:

    new_data = await form_collection.insert_one(data.dict())
    created_data = await form_collection.find_one({"_id": new_data.inserted_id})
    
    if created_data:
        created_data["_id"] = str(created_data["_id"])
    return created_data

async def get_form_data(id: str) -> dict:
    data = await form_collection.find_one({"_id": ObjectId(id)})
    if data:
        data['_id'] = str(data['_id'])
    return data

async def get_all_form_data(limit: Optional[int] = None) -> list:
    cursor: AsyncIOMotorCursor = form_collection.find().limit(limit) if limit else form_collection.find()
    data = await cursor.to_list(None)
    for item in data:
        item['_id'] = str(item['_id'])
    return data