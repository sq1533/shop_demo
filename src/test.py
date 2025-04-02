import flet
import requests
import json
from widget.signUp import signUpForm

# 상품 로드
with open(file="../storage/data/products.json", mode="r",encoding="utf-8") as product:
    product = json.load(fp=product)

with open(file="../storage/data/user.json", mode="r",encoding="utf-8") as user:
    user = json.load(fp=user)

# APP 구동
def main(page: flet.Page):
    
    #클릭 이벤트
    def on_clicked():
        pass
    home_main = flet.ElevatedButton(
        text = '버튼 클릭',
        on_click=on_clicked,
    )

    page.add(home_main)

if __name__ == "__main__":
    flet.app(target = main, port = 8501)