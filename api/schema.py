from typing import Union, List
from pydantic import BaseModel, EmailStr, Field
import secrets


# step 1. 이메일
class signupEmail(BaseModel):
    email : EmailStr

# step 2. 이메일 검증
class signupEmailCheck(BaseModel):
    email : EmailStr
    access : str = Field(..., min_length=6, max_length=6)