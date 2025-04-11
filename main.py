import os
import firebase_admin
from firebase_admin import credentials, auth
from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.middleware import Middleware
from starlette.middleware.sessions import SessionMiddleware
from api import user

# Fast API 수명, 시작시 firebase 연결, 종료시 firebase 종료
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Fast API 실행시 FireBase의 초기 설정을 수행하기 위함
    # startup 이벤트는 app실행시 단 한번만 실행되며, FireBase 초기화가 진행된다.
    # FireBase 초기화 이유
    # - 요청 처리 준비 및 글로벌 접근 준비
    # 초기화 미진행할 경우, 요청마다 초기화 시도 / 초기화 실패 가능성 / 코드 중복 발생
    try:
        path = credentials.Certificate(cert=secretKeyPath)
        firebase_admin.initialize_app(credential=path)
        print("FireBase 앱 초기화 완료")
    except Exception as e:
        print(f"false : {e}")
    yield

# FireBase secret_keys
secretKeyPath = os.path.join(os.path.dirname(__file__),"storage","secrets","firebaseKey.json")

# Fast API app 정의 및 라우터
app = FastAPI(
    lifespan=lifespan,
    middleware=[
        Middleware(SessionMiddleware, secret_key=os.urandom(16).hex())
        ]
    )

app.include_router(user.router)

# HTML templates, jinjaTemplates
templates = Jinja2Templates(directory="templates")


# mainHome 페이지
@app.get("/", response_class=HTMLResponse)
async def home(request:Request):
    return templates.TemplateResponse(
        request=request,
        name="mainPage.html"
        )

# 회원가입 페이지
@app.get("/goSignup", response_class=HTMLResponse)
async def home(request:Request):
    return templates.TemplateResponse(
        request=request,
        name="signup_email.html"
        )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)