from typing import Union, List
from pydantic import BaseModel, EmailStr, Field
import secrets


# 회원가입 요청 정보
class userIn(BaseModel):
    email : EmailStr = Field(..., description="이메일 주소")
    password :str = Field(..., min_length=8, max_length=20)

# 회원가입 응답 정보
class userOut(BaseModel):
    email : str