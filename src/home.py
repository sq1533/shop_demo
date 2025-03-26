import flet
from dataSet import product, user

def main(page: flet.Page):

    # userLogin 회원 인증을 거쳐, 회원 정보를 불러온다.
    def userInfo(getUser):
        if getUser in user.keys():
            loginUser = user[getUser]
            return loginUser
        else:
            return None

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
                on_click = None,
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


    # Vanner 설정(이벤트 / 추천 상품)
    # data loads
    recommend = product["recommend"]
    recommendList = list(recommend.keys())

    # big vanner
    bigBox = flet.Image(
        fit = flet.ImageFit.FILL,
        src = recommend[recommendList[0]]["src"],
        )

    # option vanner
    smallBoxRow = flet.Row(
        spacing = 0,
        expand = True,
        expand_loose = True,
        scroll = flet.ScrollMode.ALWAYS,
        )

    # vanner 목록
    for i in recommendList:
        img = flet.Image(
            width = 100,
            height = 100,
            fit = flet.ImageFit.FILL,
            src = recommend[i]["src"],
        )
        smallBoxRow.controls.append(img)

    # main vanner
    vanner = flet.Column(
        spacing = 0,
        controls = [
            bigBox,
            smallBoxRow,
        ],)


    # itemCard
    # data loads
    items = product["item"]
    itemList = list(items.keys())

    # main itemCard
    itemRow = flet.Row(expand=True, expand_loose=True)

    # like 클릭 이벤트
    def favoriteIcon(e):
        icon_widget = e.control.content
        if icon_widget.name == flet.Icons.FAVORITE_BORDER:
            icon_widget.name = flet.Icons.FAVORITE
        else:
            icon_widget.name = flet.Icons.FAVORITE_BORDER
        e.control.page.update()

    # itemCard 목록
    for i in itemList:
        itemCard = flet.Card(
            color = flet.Colors.ORANGE_800,
            clip_behavior = flet.ClipBehavior.HARD_EDGE,
            elevation = 3,
            width = 200,
            height = 280,
            content = flet.Column(
                alignment = flet.MainAxisAlignment.START,
                controls = [
                    flet.Container(
                        alignment = flet.alignment.center,
                        height = 200,
                        on_click = lambda _: page.go(f"/items/{i}"),
                        image = flet.DecorationImage(
                            src = items[i]["src"],
                            fit = flet.ImageFit.FILL,
                            opacity = 1,
                        ),
                        ),
                    flet.Container(
                        alignment = flet.alignment.center_left,
                        margin = flet.margin.only(10, 0, 10, 0),
                        content = flet.Column(
                            alignment = flet.MainAxisAlignment.START,
                            controls = [
                                flet.Text(
                                    items[i]["name"],
                                    color = flet.Colors.WHITE,
                                    weight = flet.FontWeight.W_500,
                                    ),
                                flet.Row(
                                    alignment = flet.MainAxisAlignment.SPACE_BETWEEN,
                                    controls = [
                                        flet.Text(
                                            f"{items[i]["price"]:,}",
                                            color = flet.Colors.WHITE,
                                            weight = flet.FontWeight.W_900,
                                            ),
                                        flet.Container(
                                            on_click = favoriteIcon,
                                            content = flet.Icon(
                                                name = flet.Icons.FAVORITE_BORDER,
                                                color = flet.Colors.WHITE,
                                                size = 30,
                                                ),
                                            ),
                                ],),
                            ],),
                        ),
            ],),
        )
        # itemRow.append
        itemRow.controls.append(itemCard)

    #main Page 설정
    home_main = flet.Container(
        width = 600,
        content = flet.Column(
            alignment = flet.MainAxisAlignment.START,
            horizontal_alignment= flet.CrossAxisAlignment.CENTER,
            controls = [
                vanner,
                itemRow,
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
                controls = [
                    flet.Text(
                        items[itemID]["name"],
                        color = flet.Colors.WHITE,
                        weight = flet.FontWeight.W_500,
                        ),
                    flet.Row(
                        alignment = flet.MainAxisAlignment.SPACE_BETWEEN,
                        controls = [
                            flet.Text(
                                f"{items[itemID]["price"]:,}",
                                color = flet.Colors.WHITE,
                                weight = flet.FontWeight.W_900,
                                ),
                            flet.Container(
                                on_click = favoriteIcon,
                                content = flet.Icon(
                                    name = flet.Icons.FAVORITE_BORDER,
                                    color = flet.Colors.WHITE,
                                    size = 30,
                                    ),
                                ),
                        ],),
                ],),
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