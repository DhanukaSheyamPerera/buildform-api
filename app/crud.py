from app.database import form_collection
from app.schemas import FormData
from bson.objectid import ObjectId

async def create_form_data(data: FormData) -> dict:
    
    new_data = await form_collection.insert_one(data.dict())
    created_data = await form_collection.find_one({"_id": new_data.inserted_id})
    return created_data