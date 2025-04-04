from pydantic import BaseModel
from datetime import datetime

class UserSchema(BaseModel):
    id: int
    name: str
    email: str
    created_at: int = int(datetime.timestamp(datetime.now()))
    updated_at: int = int(datetime.timestamp(datetime.now()))

