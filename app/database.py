import os
from dotenv import load_dotenv
# from pymongo.mongo_client import MongoClient
from motor.motor_asyncio import AsyncIOMotorClient

load_dotenv()

MONGODB_USERNAME = os.getenv("MONGODB_USERNAME")
MONGODB_PASSWORD = os.getenv("MONGODB_PASSWORD")
MONGODB_CLUSTER_URL = os.getenv("MONGODB_CLUSTER_URL")

uri = f"mongodb+srv://{MONGODB_USERNAME}:{MONGODB_PASSWORD}@{MONGODB_CLUSTER_URL}/?retryWrites=true&w=majority&appName=Cluster0"

# client = MongoClient(uri)
client = AsyncIOMotorClient(uri)

try:
    client.admin.command("ping")
    print("Pinged the deployment. Successfully connected to MongoDB!")
except Exception as e:
    print(e)

# database = client.form_database
database = client["form_database"]
# form_collection = database.get_collection("form_data")
form_collection = database["form_data"]