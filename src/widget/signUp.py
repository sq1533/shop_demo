import flet
import requests

# 회원가입 페이지
def signUpForm(page : flet.Page) -> flet.Column:

    # 회원가입 요청
    def signUp_click(id:str, pw:str, name:str, phone:str, adress:str):
        requests.post(url = f"http://127.0.0.1:8080/goSignUp", json = {"id":id, "pw":pw, "name":name, "phone":phone, "adress":adress})

    # 회원가입 클릭할 경우, 이메일(== id), 비밀번호, 이름(닉네임), 전화번호, 주소
    emailField = flet.TextField(
        label = "아이디",
    )

    pwField = flet.TextField(
        label = "비밀번호",
    )

    nameField = flet.TextField(
        label = "이름",
    )

    phoneField = flet.TextField(
        label = "연락처",
    )

    adressField = flet.TextField(
        label = "배송지",
    )

    signUpBTN = flet.ElevatedButton(
        text = "회원가입",
        on_click = signUp_click(id=emailField.value, pw=pwField.value, name=nameField.value, phone=phoneField.value, adress=adressField.value)
    )

    # 토탈 회원가입 페이지
    signUp = flet.Column(
        alignment = flet.MainAxisAlignment.CENTER,
        horizontal_alignment = flet.CrossAxisAlignment.CENTER,
        controls = [
            emailField,
            pwField,
            nameField,
            phoneField,
            adressField,
            signUpBTN,
        ],
    )

    return signUp