from fastapi import APIRouter, HTTPException, Depends, Query
from pydantic import BaseModel
import requests
import os
from dotenv import load_dotenv
from typing import List, Optional
from app.auth import get_current_user

load_dotenv()

SPOONACULAR_API_KEY = os.getenv("SPOONACULAR_API_KEY")

router = APIRouter()

@router.get("/search")
def search_recipes(
    ingredients: Optional[List[str]] = Query(None),
    cuisine: Optional[str] = None,
    dietary_restrictions: Optional[str] = None
):
    url = f"https://api.spoonacular.com/recipes/complexSearch"
    params = {
            "apiKey": SPOONACULAR_API_KEY
            }

    response = requests.get(url, params=params)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Error fetching recipes")
    return response.json()
