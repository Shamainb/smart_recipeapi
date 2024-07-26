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
