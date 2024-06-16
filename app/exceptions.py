# from typing import Any, Dict
# from typing_extensions import Annotated, Doc
from fastapi import HTTPException, status

class FormDataNotFoundException(HTTPException):
    """
    Exception raised when form data is not found in the database.

    Inherits from HTTPException with a status code of 404 (Not Found) and a default detail message.
    """
    def __init__(self):
        super().__init__(status_code=status.HTTP_404_NOT_FOUND, detail="Form data not found")

class FormCreationFailedException(HTTPException):
    """
    Exception raised when a new form data entry fails to be created.

    Inherits from HTTPException with a status code of 400 (Bad Request) and a default detail message.
    """
    def __init__(self):
        super().__init__(status_code=status.HTTP_400_BAD_REQUEST, detail="Form could not create")

class FormRecordsNullException(HTTPException):
    """
    Exception raised when no form records exist in the database.

    Inherits from HTTPException with a status code of 204 (No Content) and a default detail message.
    """
    def __init__(self):
        super().__init__(status_code=status.HTTP_204_NO_CONTENT, detail="Form records do not exist")

class InvalidCredentialsException(HTTPException):
    """
    Exception raised when provided credentials are invalid during authentication.

    Inherits from HTTPException with a status code of 401 (Unauthorized) and a default detail message.
    """
    def __init__(self):
        super().__init__(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect password")
