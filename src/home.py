import flet
from widget.NavBar import APPBar, bottomBar
from dataSet import product

def main(page: flet.Page):

    # 페이지 설정
    page.bgcolor = flet.Colors.BROWN_100
    page.window.max_width = 600
    page.window.alignment = flet.alignment.top_center
    page.scroll = flet.ScrollMode.ALWAYS
    page.appbar = APPBar
    page.bottom_appbar = bottomBar

    # 메인 페이지
    def home(box):
        return flet.View(
            route = "/",
            controls = [box],
            )
    # 아이템 페이지
    def itemsPage(item, box):
        return flet.View(
            route = f"/items/{item}",
            controls = [box]
            )

    # like 클릭 이벤트
    def favoriteIcon(e):
        icon_widget = e.control.content
        if icon_widget.name == flet.Icons.FAVORITE_BORDER:
            icon_widget.name = flet.Icons.FAVORITE
        else:
            icon_widget.name = flet.Icons.FAVORITE_BORDER
        e.control.page.update()

    # item 카드설정
    items = product["item"]
    itemList = list(items.keys())
    
    itemRow = flet.Row(expand=True, expand_loose=True)

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
                        on_click = lambda _: page.go(f"/items/{items[i]["src"]}"),
                        image = flet.DecorationImage(
                            src = items[i]["src"],
                            fit = flet.ImageFit.FILL,
                            opacity = 1,
                        ),),
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
        # itemRow 포함
        itemRow.controls.append(itemCard)

    home_main = flet.Container(
        alignment=flet.alignment.top_center,
        expand=True,
        content = flet.Column(
            alignment = flet.MainAxisAlignment.START,
            horizontal_alignment= flet.CrossAxisAlignment.CENTER,
            controls = [itemRow],
            )
        )
    
    itemsPage_main = flet.Container()

    def route_change(e):
        page.views.clear()
        if page.route == "/":
            page.views.append(home(box=home_main))
        elif page.route == f"/items/":
            item = page.route.split("/")[-1]
            page.views.append(itemsPage(item=item,box=itemsPage_main))
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