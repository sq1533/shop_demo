from typing import Union, List
from pydantic import BaseModel, EmailStr, Field
import secrets


# step 1. 이메일
class signupEmail(BaseModel):
    email : EmailStr

# step 2. 이메일 검증
class signupEmailCheck(BaseModel):
    email : EmailStr
    accessNo : str = Field(..., min_length=6, max_length=6)

# step 3. 비밀번호 설정
class signupPassword(BaseModel):
    email : EmailStr
    pw : str = Field(..., min_length=8, max_length=20, pattern=r"^[a-zA-Z0-9]\!\@\#\$+$")
    pwCheck : str = Field(..., min_length=8, max_length=20, pattern=r"^[a-zA-Z0-9]\!\@\#\$+$")

class signupUserInfo(BaseModel):
    email : EmailStr
    nickname : str = Field(..., min_length=4, max_length=18, pattern=r"^[a-zA-Z0-9]+$")
    adress : str = Field(...)