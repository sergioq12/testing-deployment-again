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