import secrets
import flet
from widget.itemCard import nonLoginItemCardWidget, LoginItemCardWidget
from widget.vanner import Vanner
from dataSet import product, user

NAVER_CLIENT_ID = "YOUR_NAVER_CLIENT_ID"
NAVER_REDIRECT_URI = "http://localhost:8000/naver/callback"
STATE = secrets.token_hex(8)

def main(page: flet.Page):

    # 메인 페이지
    def home(top, bottom, box) -> flet.View:
        page.window.width = 600,
        return flet.View(
            route = "/",
            appbar = top,
            bottom_appbar = bottom,
            controls = [box],
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
    def itemsPage(top, bottom, box):
        itemID = page.route.split("/")[-1]
        return flet.View(
            route = f"/items/:{itemID}",
            appbar = top,
            bottom_appbar = bottom,
            controls = [box],
            scroll = flet.ScrollMode.ALWAYS,
            vertical_alignment = flet.MainAxisAlignment.START,
            horizontal_alignment = flet.CrossAxisAlignment.CENTER,
            decoration = flet.BoxDecoration(
                bgcolor = flet.Colors.BROWN_100,
                border = flet.border.all(width=2, color=flet.Colors.AMBER)
            ),
            spacing = 0,
            )
    

    #유저 로그 인/아웃 분류
    login = False

    # 로그인 페이지
    async def login_clicked(e):
        authorization_url = f"https://nid.naver.com/oauth2.0/authorize?response_type=code&client_id={NAVER_CLIENT_ID}&redirect_uri={NAVER_REDIRECT_URI}&state={STATE}"
        await page.launch_url(authorization_url)
        login = True
        

    # APP 상단 바
    APPBar = flet.AppBar(
        leading = flet.Container(
        alignment = flet.alignment.center,
        on_click = lambda _: page.go(product["logo"]["url"]),
        image = flet.DecorationImage(
            src = product["logo"]["src"],
            fit = flet.ImageFit.FILL,
            ),
        ),
        leading_width = 100,
        center_title = False,
        bgcolor = flet.Colors.BROWN_100,
        actions = [
            flet.TextButton(
                text = 'Login / 회원가입',
                scale = 1,
                icon = flet.Icons.LOGIN,
                icon_color = flet.Colors.WHITE,
                on_click = login_clicked,
            ),
            ],)

    # APP 하단 바
    bottomBar = flet.BottomAppBar(
        bgcolor = flet.Colors.ORANGE_400,
        shape = flet.NotchShape.CIRCULAR,
        content = flet.Row(
            alignment = flet.MainAxisAlignment.SPACE_EVENLY,
            controls=[
                flet.IconButton(
                    icon = flet.Icons.MENU,
                    icon_color = flet.Colors.WHITE
                    ),
                flet.IconButton(
                    icon = flet.Icons.SEARCH,
                    icon_color = flet.Colors.WHITE
                    ),
                flet.IconButton(
                    icon = flet.Icons.HOME,
                    icon_color = flet.Colors.WHITE
                    ),
                flet.IconButton(
                    icon = flet.Icons.FAVORITE,
                    icon_color = flet.Colors.WHITE
                    ),
                flet.IconButton(
                    icon = flet.Icons.SHOPPING_CART,
                    icon_color = flet.Colors.WHITE
                    ),
            ],),
    )

    #main Page 설정
    home_main = flet.Container(
        width = 600,
        content = flet.Column(
            alignment = flet.MainAxisAlignment.START,
            horizontal_alignment= flet.CrossAxisAlignment.CENTER,
            controls = [
                Vanner(page),
                nonLoginItemCardWidget(page),
                ],
            )
        )

    #item Page 설정
    def itemIN(itemID):
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
        if page.route == "/":
            page.views.append(home(top=APPBar, bottom=bottomBar, box=home_main))
        elif page.route == f"/items/{itemID}":
            page.views.append(itemsPage(top=APPBar, bottom=bottomBar, box=itemIN(itemID=itemID)))
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