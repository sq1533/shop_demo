from pydantic import BaseModel, EmailStr, Field, ConfigDict
from enum import Enum

class authMethod(str, Enum):
    GOOGLE = "google"
    NAVER = "naver"
    KAKAO = "kakAO"

class userBase(BaseModel):
    email: EmailStr
    username: str

class userCreate(userBase):
    auth_provider: authMethod = Field(..., description="인증 제공자 (google, naver, kakao)")
    provider_id: str = Field(..., description="제공자(Provider)의 고유 사용자 ID")

class userUpdate(BaseModel):
    email: EmailStr | None = None
    username: str | None = None
    is_active: bool | None = None

class user(userBase):
    id: int
    is_active: bool = True
    auth_provider: authMethod = Field(..., description="사용자가 가입한 인증 방식")
    model_config = ConfigDict(from_attributes=True)