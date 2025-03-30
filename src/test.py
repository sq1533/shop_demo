import flet
import json
from widget.loginPage import loginForm

# 상품 로드
with open(file="../storage/data/products.json", mode="r",encoding="utf-8") as product:
    product = json.load(fp=product)

# APP 구동
def main(page: flet.Page):

    home_main = flet.Container(
        width = 600,
        content = loginForm(page=page)
        )
    
    page.add(home_main)

if __name__ == "__main__":
    flet.app(target = main, port = 8501)