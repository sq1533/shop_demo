import flet
import flet.canvas

def APPBar(image:dict) -> flet.AppBar:
    return flet.AppBar(
            leading = flet.Container(
                    alignment = flet.alignment.center,
                    url = image["url"],
                    url_target = flet.UrlTarget.TOP,
                    image = flet.DecorationImage(
                        src = image["src"],
                        fit = flet.ImageFit.FILL,
                    ),
                ),
            leading_width = 100,
            center_title=False,
            bgcolor = flet.Colors.BROWN_100,
            actions = [
                flet.TextButton(
                    text = 'Login / 회원가입',
                    scale = 1,
                    icon = flet.Icons.LOGIN,
                    icon_color = flet.Colors.WHITE,
                ),
                flet.PopupMenuButton(
                    elevation = 100,
                    icon = flet.Icons.MENU,
                    icon_color = flet.Colors.WHITE,
                    items=[
                        flet.PopupMenuItem(
                            text = "Glesses",
                            checked = False,
                            on_click = None,
                            ),
                        flet.PopupMenuItem(
                            text = "Sun Glesses",
                            checked = False,
                            on_click = None,
                        ),
                        flet.PopupMenuItem(
                            text = "Checked item",
                            checked = False,
                            on_click = None,
                        ),
                    ]
                ),
            ],
        )

def bottomNavBar() -> flet.BottomAppBar:
    return flet.BottomAppBar(
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
                    icon = flet.Icons.FAVORITE,
                    icon_color = flet.Colors.WHITE
                    ),
            ]
        ),
    )

def vannerBox(image:dict, width, height) -> flet.Image:
    return flet.Image(
        src = image["src"],
        width = width,
        height = height,
        fit = flet.ImageFit.FILL,
    )

def itemBox(image:dict, hoverE, clickE) -> flet.Card:
    return flet.Card(
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
                    url = image["url"],
                    url_target = flet.UrlTarget.PARENT,
                    on_hover = hoverE,
                    image = flet.DecorationImage(
                        src = image["src"],
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
                                image["name"],
                                color = flet.Colors.WHITE,
                                weight = flet.FontWeight.W_500,
                                ),
                            flet.Row(
                                alignment = flet.MainAxisAlignment.SPACE_BETWEEN,
                                controls = [
                                    flet.Text(
                                        f"{image["price"]:,}",
                                        color = flet.Colors.WHITE,
                                        weight = flet.FontWeight.W_900,
                                        ),
                                    flet.Container(
                                        on_click = clickE,
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