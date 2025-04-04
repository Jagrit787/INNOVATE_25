import os
from motor.motor_asyncio import AsyncIOMotorClient

uri = os.getenv("MONGODB_URI")

client = AsyncIOMotorClient(uri)
db = client['MyDatabase']
try:
    client.admin.command('ping')
    print("Connected to MongoDB!")
except Exception as e:
    print(f"MongoDB Connection Error: {e}")
