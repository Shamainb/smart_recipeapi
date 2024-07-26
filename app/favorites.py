from fastapi import APIRouter, Depends, HTTPException
from firebase_admin import firestore
from app.auth import get_current_user
from fastapi import Depends

router = APIRouter()
db = firestore.client()

@router.post("/{recipe_id}")
def add_favorite(recipe_id: str, user_id: str = Depends(get_current_user)):
    try:
        favorites_ref = db.collection("users").document(user_id).collection("favorites").document(recipe_id)
        favorites_ref.set({"recipe_id": recipe_id})
        return {"msg": "Recipe added to favorites"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/{recipe_id}")
def remove_favorite(recipe_id: str, user_id: str = Depends(get_current_user)):
    favorites_ref = db.collection("users").document(user_id).collection("favorites").document(recipe_id)
    favorites_ref.delete()
    return {"msg": "Recipe removed from favorites"}

@router.get("/")
def get_favorites(user_id: str = Depends(get_current_user)):
    favorites_ref = db.collection("users").document(user_id).collection("favorites")
    favorites = favorites_ref.stream()
    return [favorite.id for favorite in favorites]
