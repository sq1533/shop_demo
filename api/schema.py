from typing import Union, List
from pydantic import BaseModel, EmailStr, Field
import secrets


# step 1. 이메일
class signupEmail(BaseModel):
    email : EmailStr