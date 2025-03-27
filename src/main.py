import httpx

from fastapi import FastAPI,  Query, HTTPException
from fastapi.responses import JSONResponse

app = FastAPI()

#네이버 개발자 등록
NAVER_CLIENT_ID = "YOUR_NAVER_CLIENT_ID"
NAVER_CLIENT_SECRET = "YOUR_NAVER_CLIENT_SECRET"
NAVER_REDIRECT_URI = "http://localhost:8000/naver/callback"

#토큰 요청
async def getToken_naver(code: str):

    token_url = "https://nid.naver.com/oauth2.0/token"

    params = {
        "grant_type": "authorization_code",
        "client_id": NAVER_CLIENT_ID,
        "client_secret": NAVER_CLIENT_SECRET,
        "redirect_uri": NAVER_REDIRECT_URI,
        "code": code,
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(token_url, params=params)
        response.raise_for_status()  # 에러 발생 시 예외 처리
        return response.json()

# 사용자 정보 요청
async def getUser_naver(token: str):

    userInfo = "https://openapi.naver.com/v1/nid/me"

    headers = {"Authorization": f"Bearer {token}"}

    async with httpx.AsyncClient() as client:
        response = await client.get(userInfo, headers=headers)
        response.raise_for_status()
        return response.json()

# 네이버 요청 콜백 처리
@app.get("/naver/callback")
async def naver_callback(code: str = Query(...)):
    try:
        token_data = await getToken_naver(code)
        access_token = token_data.get("access_token")
        if not access_token:
            raise HTTPException(status_code=400, detail="Failed to get Naver access token")

        user_info = await getUser_naver(access_token)
        return JSONResponse(content={"user_info": user_info})
    
    except Exception as e:
        raise HTTPException(detail=f"error: {e}")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)