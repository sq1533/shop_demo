from typing import Union, List
from pydantic import BaseModel, EmailStr

#회원가입 정보
class userIn(BaseModel):
    email : EmailStr
    password : str

class userOut(BaseModel):
    email : str