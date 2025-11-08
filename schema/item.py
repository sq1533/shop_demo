from pydantic import BaseModel, Field, ConfigDict, HttpUrl

class itemBase(BaseModel):
    category: str = Field(..., min_length=2, max_length=30)
    color: str = Field(..., min_length=2, max_length=30)
    serises: str = Field(..., min_length=2, max_length=30)
    name: str = Field(..., min_length=2, max_length=100)
    detail: HttpUrl | None = None
    paths: list[HttpUrl] | None = None
    price: int = Field(..., gt=0, description="가격은 0보다 커야 합니다.")
    discount_rate: int = Field(0, ge=0, le=100, description="할인율은 0~100 사이여야 합니다.")
    event: str | None = Field(None, max_length=100)

class feedbackType(BaseModel):
    count: int = Field(0, description="피드백 수")
    point: int = Field(0, description="피드백 점수 합계")
    text: dict | None = Field(None, description="피드백 텍스트 모음")

class itemStatus(BaseModel):
    count: int = Field(0, description="수량")
    sales: int = Field(0, description="판매 수량")
    refund: int = Field(0, description="환불 수량")
    enabled: bool = Field(True, description="판매 가능 여부")
    feedback: feedbackType | None = Field(None, description="고객 피드백 정보")

class itemInfo(itemBase):
    id: str = Field(..., description="Firestore 문서의 고유 ID (itemID)")

    status: itemStatus | None = Field(None, description="아이템 상태 정보")
    model_config = ConfigDict(from_attributes=True) # firebase 문서(dict 객체 X)를 dict 객체로 전환