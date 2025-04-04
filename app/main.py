from fastapi import FastAPI
from db.mongodb import db
from db.routes.userRoute import router as user_router

app = FastAPI()

app.include_router(user_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI!"}

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: str = None):
#     return {"itemid": item_id, "q": q}

# http://127.0.0.1:8000/items/5?q=hello



