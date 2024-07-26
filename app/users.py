from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from firebase_admin import firestore
from app.auth import get_current_user

router = APIRouter()
db = firestore.client()

class UserProfile(BaseModel):
    preferences: list = []
    dietary_restrictions: list = []
    favorite_ingredients: list = []

@router.get("/profile")
def get_user_profile(user_id: str = Depends(get_current_user)):
    user_profile_ref = db.collection("users").document(user_id).collection("profile").document("data")
    user_profile = user_profile_ref.get()
    if not user_profile.exists:
        raise HTTPException(status_code=404, detail="Profile not found")
    return user_profile.to_dict()

@router.put("/profile")
def update_user_profile(profile: UserProfile, user_id: str = Depends(get_current_user)):
    user_profile_ref = db.collection("users").document(user_id).collection("profile").document("data")
    user_profile_ref.set(profile.dict())
    return {"msg": "Profile updated successfully"}
