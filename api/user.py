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

# step 1.
@router.post("/email", response_class=HTMLResponse)
async def email(request: Request, email: Annotated[signupEmail, Form(...)]):
    # 이메일 요청 보낼시, state 설정 및 검증 필요
    try:
        return templates.TemplateResponse(
            request = request,
            name = "signup_emailC.html",
            context={"email":email.email}
            )
    except Exception as e:
        print(e)

# step 2.
@router.post("/{email}/emailCheck", response_class=HTMLResponse)
async def emailCheck(request: None):
    pass