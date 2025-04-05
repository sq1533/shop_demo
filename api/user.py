import firebase_admin
from firebase_admin import credentials, auth
from typing import Annotated
from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from shop_demo.api.schema import *

# 회원가입
# step 1. 이메일 입력(이메일 schema 검증)
# step 2. 이메일 검증(이메일 인증 전송 기능)
# step 3. 비밀번호 설정(8자 이상, 영문+숫자+특수문자 조합)
# step 4. 회원 정보 입력

router = APIRouter(prefix="/goSignup", tags=["users"])

templates = Jinja2Templates(directory="templates")

state_store = {}

# step 1.
@router.post("/email", response_class=HTMLResponse)
async def email(request: Request, email: Annotated[signupEmail, Form(...)]):
    # 이메일 요청 보낼시, state 설정 및 검증 필요
    try:
        state = secrets.token_urlsafe(16)
        return templates.TemplateResponse(
            request = request,
            name = "signup_emailC.html",
            context={"email":email.email},
            headers={"X-State":state}
            )
    except Exception as e:
        print(e)

# step 2.
@router.post("/{email}/emailCheck", response_class=HTMLResponse)
async def emailCheck(request: Request, check: Annotated[signupEmailCheck, Form(...)]):
    # state 및 인증번호 확인 사항 체크
    try:
        state = request.headers.get("X-State")
        if state and state in state_store:
            return templates.TemplateResponse(
                request = request,
                name = "signup_password.html",
                context={"email":check.email}
                )
    except Exception as e:
        print(e)

# step 3.
@router.post("/{email}/password", response_class=HTMLResponse)
async def emailCheck(request: Request):
    pass

# step 3.
@router.post("/{email}/userInfo", response_class=HTMLResponse)
async def emailCheck(request: Request):
    pass