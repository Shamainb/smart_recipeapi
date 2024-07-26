import pyrebase
from fastapi import APIRouter, HTTPException, Depends
from firebase_admin.exceptions import AlreadyExistsError
from pydantic import BaseModel
import firebase_admin
from firebase_admin import credentials, auth
import jwt
import os
import requests
from dotenv import load_dotenv

load_dotenv()

firebaseConfig = {
        'apiKey': os.getenv("FIREBASE_API_KEY"),
        'authDomain': os.getenv("FIREBASE_AUTH_DOMAIN"),
        'projectId': os.getenv("FIREBASE_PROJECT_ID"),
        'storageBucket': os.getenv("FIREBASE_STORAGE_BUCKET"),
        'messagingSenderId': os.getenv("FIREBASE_MESSAGING_SENDER_ID"),
        'databaseURL': os.getenv("FIREBASE_DATABASE_URL")
}
firebase = pyrebase.initialize_app(firebaseConfig)

cred = credentials.Certificate("/home/shamain/smart_recipeapi/app/serviceAccountKey.json")
firebase_admin.initialize_app(cred)

router = APIRouter()

SECRET_KEY = os.getenv("SECRET_KEY")
if not SECRET_KEY:
    raise ValueError("No SECRET_KEY set for JWT token encoding")
ALGORITHM = "HS256"

class User(BaseModel):
    email: str
    password: str

def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get("sub")
        if user_id is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        return user_id
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

def get_current_user(token: str = Depends(verify_token)):
    user_id = verify_token(token)
    return user_id

@router.post("/signup")
def signup(user: User):
    try:
        user_record = auth.get_user_by_email(user.email)
        if not user_record:
            raise HTTPException(status_code=400, detail="Invalid credentials")

        token = jwt.encode({"sub": user_record.uid}, SECRET_KEY, algorithm=ALGORITHM)
        return {"access_token": token, "token_type": "bearer"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
