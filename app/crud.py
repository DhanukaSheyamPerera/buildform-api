from app.database import form_collection
from app.schemas import FormData
from bson.objectid import ObjectId

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