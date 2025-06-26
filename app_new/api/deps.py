# ======================================================= #
### import ###
# Pydantic
from pydantic import BaseModel, EmailStr

# ======================================================= #

class UserRegisterRequest(BaseModel):
    email: EmailStr


