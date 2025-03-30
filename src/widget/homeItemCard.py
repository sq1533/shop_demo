import flet
import httpx

# 유저 비로그인
def nonLoginItemCardWidget(page: flet.Page, item: dict) -> flet.Row:
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
    for i in list(item.keys()):
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
                            src = item[i]["src"],
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
                                    item[i]["name"],
                                    color = flet.Colors.WHITE,
                                    weight = flet.FontWeight.W_500,
                                    ),
                                flet.Row(
                                    alignment = flet.MainAxisAlignment.SPACE_BETWEEN,
                                    controls = [
                                        flet.Text(
                                            f"{item[i]["price"]:,}",
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
def LoginItemCardWidget(page : flet.Page, user : dict, item: dict) -> flet.Row:

    # itemCard Row
    itemRow = flet.Row(expand=True, expand_loose=True)

    # like 아이콘
    async def likeIcon(itemID) -> flet.Icons:
        if itemID in user["like"]:
            return flet.Icons.FAVORITE
        else:
            return flet.Icons.FAVORITE_BORDER


    # like 클릭 이벤트
    async def favoriteIcon(e, itemID):
        icon_widget = e.control.content
        if icon_widget.name == flet.Icons.FAVORITE_BORDER:
            icon_widget.name = flet.Icons.FAVORITE
            async with httpx.AsyncClient():
                await httpx.AsyncClient().post(url = f"ip/{user.keys()}/inLike", json = {"user":user, "likeItem":itemID})
        else:
            icon_widget.name = flet.Icons.FAVORITE_BORDER
            async with httpx.AsyncClient():
                await httpx.AsyncClient().post(url = f"ip/{user.keys()}/outLike", json = {"user":user, "likeItem":itemID})
        page.update()

    # itemCard 목록
    for i in list(item.keys()):
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
                            src = item[i]["src"],
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
                                    item[i]["name"],
                                    color = flet.Colors.WHITE,
                                    weight = flet.FontWeight.W_500,
                                    ),
                                flet.Row(
                                    alignment = flet.MainAxisAlignment.SPACE_BETWEEN,
                                    controls = [
                                        flet.Text(
                                            f"{item[i]["price"]:,}",
                                            color = flet.Colors.WHITE,
                                            weight = flet.FontWeight.W_900,
                                            ),
                                        flet.Container(
                                            on_click = favoriteIcon,
                                            content = flet.Icon(
                                                name = likeIcon,
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