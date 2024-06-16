# from typing import Any, Dict
# from typing_extensions import Annotated, Doc
from fastapi import HTTPException, status

class FormDataNotFoundException(HTTPException):
    def __init__(self):
        super().__init__(status_code=status.HTTP_404_NOT_FOUND, detail="Form data not found")

class FormCreationFailedException(HTTPException):
    def __init__(self):
        super().__init__(status_code=status.HTTP_400_BAD_REQUEST, detail="Form could not create")

class FormRecordsNullExceptionn(HTTPException):
    def __init__(self):
        super().__init__(status_code=status.HTTP_204_NO_CONTENT, detail="Form records do not exist")

class InvalidCredentialsException(HTTPException):
    def __init__(self):
        super().__init__(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect password")