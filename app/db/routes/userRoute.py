from fastapi import APIRouter, HTTPException
from typing import List
from db.models.userModel import UserSchema
from db.schemas.userSchema import create_user, get_users  

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/create")
async def add_user(user: UserSchema):
    return  await create_user(user)

@router.get("/get")
async def fetch_users():
    users= await get_users()
    if not users:
        raise HTTPException(status_code=404, detail="No users found")
    return users
