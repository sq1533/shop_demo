import flet
import json
from shop_demo.src.widget.appBar import nonLoginAppBar, loginAppBar
from shop_demo.src.widget.bottomBar import nonLoginbottom, loginbottom
from shop_demo.src.widget.homeWidget import Vanner, nonLoginItemCardWidget, LoginItemCardWidget

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

    #main Page 설정
    def home_main(user : dict | None, itemCards) -> flet.Container:
        home_main = flet.Container(
            width = 600,
            content = flet.Column(
                alignment = flet.MainAxisAlignment.START,
                horizontal_alignment= flet.CrossAxisAlignment.CENTER,
                controls = [
                    Vanner(page=page, recommend=product["recommend"]),
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

    # 페이지 라우트
    def route_change(e) -> None:
        page.views.clear()
        itemID = page.route.split("/")[-1]

        top_bar = loginAppBar(page=page, user=None, readProduct=product["logo"]) if login else nonLoginAppBar(page=page, readProduct=product["logo"])
        bottom_bar = loginbottom() if login else nonLoginbottom()
        item_cards = LoginItemCardWidget(page=page, user=None, item=product["item"]) if login else nonLoginItemCardWidget(page=page, item=product["item"])
        if page.route == "/":
            page.views.append(home(
                top = top_bar,
                bottom = bottom_bar,
                body = home_main(user = None, itemCards = item_cards)
                ))
        elif page.route == f"/items/{itemID}":
            page.views.append(itemsPage(
                top = top_bar,
                bottom = bottom_bar,
                body = itemsPage_main(itemID=itemID)
                ))
        page.update()

    # 페이지 이동
    def view_pop(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    # 페이지 설정
    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

if __name__ == "__main__":
    flet.app(target = main, port = 8501)