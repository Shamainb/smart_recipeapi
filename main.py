from fastapi import FastAPI
from dotenv import load_dotenv
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.auth import router as auth_router
from app.recipes import router as recipes_router
from app.favorites import router as favorites_router
from app.grocery_list import router as grocery_list_router
from app.users import router as users_router

load_dotenv()

API_KEY = os.getenv("API_KEY")

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Smart Recipe API"}

app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(recipes_router, prefix="/recipes", tags=["recipes"])
app.include_router(favorites_router, prefix="/favorites", tags=["favorites"])
app.include_router(grocery_list_router, prefix="/grocery-list", tags=["grocery list"])
app.include_router(users_router, prefix="/users", tags=["users"])
