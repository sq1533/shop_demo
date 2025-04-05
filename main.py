import firebase_admin
from firebase_admin import credentials, auth
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from api import user

# FireBase secret_keys
secretKeyPath = "/storage/secrets/firebaseKey.json"
# Fast API app 정의 및 라우터
app = FastAPI()
app.include_router(user.router)
# HTML templates, jinjaTemplates
templates = Jinja2Templates(directory="templates")

"""
# firebase 연결
@app.on_event(event_type="startup")
async def setFireBase():
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


# 프로그램 종료
@app.on_event(event_type="shutdown")
async def shutdown():
    pass
"""

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