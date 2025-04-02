from typing import Union
from pydantic import BaseModel, EmailStr

#회원가입 정보
class signUp(BaseModel):
    email : EmailStr