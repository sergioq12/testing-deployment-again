# Getting started lets gooo
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from bcrypt import gensalt, hashpw, checkpw
import jwt
import os
import sys
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from dotenv import load_dotenv

# Loads 
load_dotenv()

# Creates FastAPI app
app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000/",
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def test_endpoint():
    return {"message": "This is the main test"}

    @app.get("/testing")
async def Testing():
    """
    This is a testing endpoint that allows us to know if the API is 
    giving out responses to the corresponding call
    """
    print("Testing endpoint")
    return {
        "Status":"Success",
        "Message": "This is a testing function, it works SIUUU"
    }

# User Authentication

@app.post("/sign_in")
async def SignIn(user: User):
    """
    This is the sign in endpoint. It will receive a user and it will
    verify that the email exists, and that the password matches. It will
    give according responses to given events
    """
    print("Sign in endpoint")
    # verify that the user email does exists 
    user_in_db = mongo_functions.GetUserByEmail(user.email)
    if user_in_db:
        # verify that the passwords match
        if checkpw(user.password.encode(), user_in_db["password"]):
            # Generate JWT 
            jwt_token = jwt.encode({
                "first_name": user_in_db["first_name"],
                "last_name": user_in_db["last_name"],
                "email": user.email,
                "date": str(user.createdAt)
            }, os.getenv("JWT_KEY"), algorithm='HS256')
            return {
                "Status": "Success",
                "Message": "User signed in successfully",
                "token": jwt_token
            }
        else:
            return {
                "Status": "Failure",
                "Message": "Passwords did not match"
            }
        
    else:
        # given that the email does not exist, can't authenticate
        return {
            "Status": "Failure",
            "Message": "Email was not found"
        }