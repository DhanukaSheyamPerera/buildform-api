from fastapi import Depends, Security
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import os
from dotenv import load_dotenv
from app.exceptions import InvalidCredentialsException

security = HTTPBasic()

load_dotenv()

def verify_password(credentials: HTTPBasicCredentials = Depends(security)):
    correct_password = os.getenv("DELETE_METHOD_PASSWORD")
    if credentials.password != correct_password:
        raise InvalidCredentialsException()
    return credentials.username