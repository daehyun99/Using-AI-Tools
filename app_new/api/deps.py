# ======================================================= #
### import ###
# Pydantic
from pydantic import BaseModel, EmailStr
from fastapi import UploadFile

# ======================================================= #

class MessaggingUserRequest(BaseModel):
    email: EmailStr

class MessaggingDocumentRequest(BaseModel):
    id: str
    pw: str


