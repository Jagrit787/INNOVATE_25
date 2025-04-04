from db.mongodb import db
from db.models.userModel import UserSchema
# from bson.objectid import ObjectId

async def create_user(user: UserSchema):
    user_dict =     user.model_dump()
    result =  await db.users.insert_one(user_dict)
    return {"id": str(result.inserted_id), "message": "User created successfully"}

async def get_users():
    users = await db.users.find().to_list(length=100)
    for user in users:
        user["id"] = str(user["_id"])
        del user["_id"]
    return users