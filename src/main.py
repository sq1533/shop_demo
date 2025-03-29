from fastapi import FastAPI
import json
from pydantic import BaseModel
import secrets

# 상품 로드
with open(file="../storage/data/products.json", mode="r",encoding="utf-8") as product:
    product = json.load(fp=product)
# 유저 로드
with open(file="../storage/data/user.json", mode="r",encoding="utf-8") as user:
    user = json.load(fp=user)

solt = secrets.token_hex(8)

app = FastAPI()

# 사용자 로그인 시도 정보
class goLoginRequset(BaseModel):
    id : str
    passward : str

# 유저 like 정보
class LikeRequest(BaseModel):
    user: dict
    likeItem: str

# login 요청
@app.post("/goLogin")
async def goLogin(userPass : goLoginRequset):
    if userPass["id"] in user.keys() and userPass["passward"] == user[userPass["id"]]["passward"]:
        return {"state":"ok", "user":user[userPass["id"]]}
    else:
        return {"state":"false"}
# like_in 처리
@app.post("/inLike/{userID}")
async def inLike(data : LikeRequest) -> None:
    if data["user"].keys() in user.keys():
        inLike = data["likeList"].append(data["likeItem"])
        result = list(set(inLike))


# like_out 처리
@app.post("/outLike/{userID}")
async def outLike(data : LikeRequest) -> None:
    if data["user"].keys() in user.keys():
        outLike = data["likeList"].remove(data["likeItem"])
        result = list(set(outLike))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)