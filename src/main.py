from fastapi import FastAPI
from typing import List
from pydantic import BaseModel

app = FastAPI()

class LikeRequest(BaseModel):
    likeList: List[str]
    likeItem: str

# like_in 처리
@app.post("/inLike")
async def inLike(data : LikeRequest):
    pass

# like_out 처리
@app.post("/outLike")
async def outLike(data : LikeRequest):
    pass

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)