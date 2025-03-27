import flet
import httpx
from dataSet import product

# data loads
items = product["item"]
itemList = list(items.keys())

# 유저 비로그인
def nonLoginItemCardWidget(page : flet.Page) -> flet.Row:
    # itemCard
    # main itemCard
    itemRow = flet.Row(expand=True, expand_loose=True)

    # like 클릭 이벤트
    def favoriteIcon(e):
        icon_widget = e.control.content
        if icon_widget.name == flet.Icons.FAVORITE_BORDER:
            icon_widget.name = flet.Icons.FAVORITE
        else:
            icon_widget.name = flet.Icons.FAVORITE_BORDER
        page.update()

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

    return itemRow


# 유저 로그인
def LoginItemCardWidget(page : flet.Page, user : dict) -> flet.Row:
    # 좋아요 리스트
    likeList = user["like"]

    # itemCard Row
    itemRow = flet.Row(expand=True, expand_loose=True)

    # like 클릭 이벤트
    async def favoriteIcon(e, itemID):
        icon_widget = e.control.content
        if icon_widget.name == flet.Icons.FAVORITE_BORDER:
            icon_widget.name = flet.Icons.FAVORITE
            async with httpx.AsyncClient():
                response = await httpx.AsyncClient().post(url = "inLikeUrl", json = {"likeList":likeList, "likeItem":itemID})
                response.raise_for_status()
                return response.json()
        else:
            icon_widget.name = flet.Icons.FAVORITE_BORDER
            async with httpx.AsyncClient():
                response = await httpx.AsyncClient().post(url = "outLikeurl", json = {"likeList":likeList, "likeItem":itemID})
                response.raise_for_status()
                return response.json()
        page.update()

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

    return itemRow