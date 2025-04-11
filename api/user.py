from firebase_admin import auth
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
        auth.get_user_by_email(email=email.email)
        existsError = """
        <div>이미 사용중인 이메일 입니다.</div>
        """
        return HTMLResponse(content=existsError)
    except auth.UserNotFoundError:
        request.session["registration_email"] = email.email
        return templates.TemplateResponse(
            request = request,
            name = "signup_emailC.html",
            context={"email":email.email}
            )
    except Exception as e:
        print(e)

# step 2.
@router.post("/emailCheck", response_class=HTMLResponse)
async def emailCheck(request: Request, check: Annotated[signupEmailCheck, Form(...)]):
    # state 및 인증번호 확인 사항 체크
    try:
        listenEmail = request.session.get("registration_email")
        if listenEmail != check.email:
            wrongEmail = """
            <div>세션 정보 오류</div>
            """
            raise HTMLResponse(content=wrongEmail)
        return templates.TemplateResponse(
            request = request,
            name = "signup_password.html",
            context={"email":check.email}
            )
    except Exception as e:
        print(e)

# step 3.
@router.post("/password", response_class=HTMLResponse)
async def emailCheck(request: Request, password: Annotated[signupPassword, Form(...)]):
    # 비밀번호 영문 + 숫자 + 특수문자 조합 검증
    try:
        listenEmail = request.session.get("registration_email")
        if listenEmail != password.email:
            wrongEmail = """
            <div>세션 정보 오류</div>
            """
            raise HTMLResponse(content=wrongEmail)
        return templates.TemplateResponse(
            request = request,
            name = "signup_info.html",
            context={"email":password.email}
            )
    except Exception as e:
        print(e)

# step 4.
@router.post("/userInfo", response_class=HTMLResponse)
async def emailCheck(request: Request, userInfo: Annotated[signupUserInfo, Form(...)]):
    # 유저 닉네임, 주소 정보 입력
    try:
        listenEmail = request.session.get("registration_email")
        if listenEmail != userInfo.email:
            wrongEmail = """
            <div>세션 정보 오류</div>
            """
            raise HTMLResponse(content=wrongEmail)
        pass
    except Exception as e:
        print(e)
