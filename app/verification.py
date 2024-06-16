from fastapi import Depends, Security
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import os
from dotenv import load_dotenv
from app.exceptions import InvalidCredentialsException

security = HTTPBasic()

load_dotenv()

def verify_password(credentials: HTTPBasicCredentials = Depends(security)):
    """
    Verify the provided password against the one stored in environment variables.

    Parameters:
        credentials (HTTPBasicCredentials): The credentials containing the username and password provided by the user.

    Returns:
        str: The username if the password is correct.

    Raises:
        InvalidCredentialsException: If the provided password does not match the correct password.
    """
    correct_password = os.getenv("AUTHENTICATION_PASSWORD")
    if credentials.password != correct_password:
        raise InvalidCredentialsException()
    return credentials.username