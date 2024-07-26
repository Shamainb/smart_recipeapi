from fastapi import APIRouter, Depends, HTTPException
from firebase_admin import firestore
from app.auth import get_current_user
import requests
import os
from dotenv import load_dotenv
from typing import List
from fastapi import Depends

router = APIRouter()
db = firestore.client()

@router.post("/")
def generate_grocery_list(recipe_ids: List[int], user_id: str = Depends(get_current_user)):
    grocery_list = set()
    for recipe_id in recipe_ids:
        url = f"https://api.spoonacular.com/recipes/{recipe_id}/information"
        params = {"apiKey": SPOONACULAR_API_KEY}
        response = requests.get(url, params=params)
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail="Error fetching recipe details")
        recipe = response.json()
        grocery_list.update(ingredient['name'] for ingredient in recipe['extendedIngredients'])

        grocery_list_ref = db.collection("users").document(user_id).collection("grocery_list").document("list")

@router.put("/purchase")
def mark_purchased(item: str, user_id: str = Depends(get_current_user)):
    grocery_list_ref = db.collection("users").document(user_id).collection("grocery_list").documen
t("list")
    grocery_list = grocery_list_ref.get().to_dict
()
    if not grocery_list:
        raise HTTPException(status_code=404, detail="Grocery list not found")
    purchased = grocery_list.get("purchased", [])
    if item not in purchased:
        purchased.append(item)
        grocery_list_ref.update({"purchased": purchased})
        return {"msg": f"Item '{item}' marked as purchased"}
    grocery_list_ref.set({"items": list(grocery_list), "purchased": []})
        return {"msg": "Grocery list generated", "grocery_list": list(grocery_list)}
