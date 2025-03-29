import flet
import json
import httpx
from widget.appBar import nonLoginAppBar, loginAppBar
from widget.bottomBar import nonLoginbottom, loginbottom
from widget.itemCard import nonLoginItemCardWidget, LoginItemCardWidget
from widget.vanner import Vanner

# 상품 로드
with open(file="../storage/data/products.json", mode="r",encoding="utf-8") as product:
    product = json.load(fp=product)

# APP 구동
def main(page: flet.Page):

    # 메인 페이지
    def home(top, bottom, body) -> flet.View:
        page.window.width = 600,
        return flet.View(
            route = "/",
            appbar = top,
            bottom_appbar = bottom,
            controls = [body],
            scroll = flet.ScrollMode.ALWAYS,
            vertical_alignment = flet.MainAxisAlignment.START,
            horizontal_alignment = flet.CrossAxisAlignment.CENTER,
            bgcolor = flet.Colors.BROWN_100,
            decoration = flet.BoxDecoration(
                border = flet.border.all(width=2, color=flet.Colors.AMBER)
            ),
            spacing = 0,
            )

    # 아이템 페이지
    def itemsPage(top, bottom, body):
        itemID = page.route.split("/")[-1]
        return flet.View(
            route = f"/items/:{itemID}",
            appbar = top,
            bottom_appbar = bottom,
            controls = [body],
            scroll = flet.ScrollMode.ALWAYS,
            vertical_alignment = flet.MainAxisAlignment.START,
            horizontal_alignment = flet.CrossAxisAlignment.CENTER,
            decoration = flet.BoxDecoration(
                bgcolor = flet.Colors.BROWN_100,
                border = flet.border.all(width=2, color=flet.Colors.AMBER)
            ),
            spacing = 0,
            )
    
    # 로그인 페이지
    def loginPage(top, bottom, body):
        return flet.View(
            route = f"/loginPage",
            appbar = top,
            bottom_appbar = bottom,
            controls = [body],
            scroll = flet.ScrollMode.ALWAYS,
            vertical_alignment = flet.MainAxisAlignment.START,
            horizontal_alignment = flet.CrossAxisAlignment.CENTER,
            decoration = flet.BoxDecoration(
                bgcolor = flet.Colors.BROWN_100,
                border = flet.border.all(width=2, color=flet.Colors.AMBER)
            ),
            spacing = 0,
            )
    
    # 유저 로그 인/아웃 분류
    login = False

    # 로그인 페이지
    async def login_clicked(id:str, passward:str) -> bool:
        async with httpx.AsyncClient():
            responed = await httpx.AsyncClient().post(url = "ip/goLogin", json = {"id":id, "passward":passward})
            responed.status_code()
        if responed["state"] == "ok":
            login = True
            return login
        else:
            login = False
            return login


    #main Page 설정
    def home_main(user : dict | None, itemCards) -> flet.Container:
        home_main = flet.Container(
            width = 600,
            content = flet.Column(
                alignment = flet.MainAxisAlignment.START,
                horizontal_alignment= flet.CrossAxisAlignment.CENTER,
                controls = [
                    Vanner(page),
                    itemCards,
                    ],
                )
            )
        return home_main

    #item Page 설정
    def itemsPage_main(itemID) -> flet.Container:
        itemsPage_main = flet.Container(
            width = 600,
            bgcolor = flet.Colors.AMBER,
            content = flet.Column(
                alignment = flet.MainAxisAlignment.START,
                controls = [],
                ),
        )
        return itemsPage_main

    def route_change(e):
        page.views.clear()
        itemID = page.route.split("/")[-1]
        if page.route == "/" and login:
            page.views.append(home(top=loginAppBar, bottom=loginbottom, body=home_main(user = None, itemCards = LoginItemCardWidget(page=page, user=None, item=product["item"]))))
        elif page.route == "/" and not login:
            page.views.append(home(top=nonLoginAppBar, bottom=nonLoginbottom, body=home_main(user = None, itemCards = nonLoginItemCardWidget(page=page, item=product["item"]))))
        elif page.route == f"/items/{itemID}" and login:
            page.views.append(itemsPage(top=loginAppBar, bottom=loginbottom, body=itemsPage_main(itemID=itemID)))
        page.update()

    def view_pop(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

if __name__ == "__main__":
    flet.app(target = main, port = 8501)