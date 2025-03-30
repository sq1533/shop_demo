import flet
import httpx

# 로그인 페이지
def loginForm(page : flet.Page) -> flet.Column:

    #로그인 클릭 및 검증
    async def loginBTN_click(id : str, pw : str):
        async with httpx.AsyncClient():
            respone = await httpx.AsyncClient().post(url = f"http://localhost:8080/goLogin", json = {"id":id, "pw":pw})
        if respone["state"] == "ok":
            page.go(route="/", login = True)
        else:
            page.add(flet.Text(value="오류"))
        page.update()

    # 로그인 전체 틀(아이디 입력창, passward 입력창, 아이디 찾기, 비밀번호 찾기)
    # 아이디 입력 단계, 이메일
    idField = flet.TextField(
        label = "아이디",
    )

    # 패스워드 입력 단계
    pwField = flet.TextField(
        label = "Password with reveal button",
        password = True,
        can_reveal_password = True,
        )

    # 로그인 버튼
    loginBTN = flet.ElevatedButton(
        text = "Log-IN",
        color = flet.Colors.WHITE,
        icon = flet.Icons.POWER_SETTINGS_NEW,
        icon_color = flet.Colors.WHITE,
        bgcolor = flet.Colors.GREEN_ACCENT,
        on_click = loginBTN_click(id=idField.value, pw=pwField.value),
        on_focus = None,
    )

    # 회원가입 페이지
    signUp = flet.ElevatedButton(
        text = "회원가입",
        on_click = lambda _: page("/goSignUp"),
    )
    # 비밀번호 요청 페이지

    # 토탈 로그인 페이지
    loginForm = flet.Column(
        alignment = flet.MainAxisAlignment.CENTER,
        horizontal_alignment = flet.CrossAxisAlignment.CENTER,
        controls = [
            idField,
            pwField,
            loginBTN
        ],
    )

    return loginForm