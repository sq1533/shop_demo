import flet

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
            bgcolor = flet.Colors.BROWN_400,
            actions = [
                flet.Container(
                    url = '/login',
                    url_target = flet.UrlTarget.TOP,
                    content = flet.Text(
                        "Login / 회원가입"
                        ),
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
        bgcolor = flet.Colors.DEEP_ORANGE_700,
        shape = flet.NotchShape.CIRCULAR,
        content = flet.Row(
            alignment = flet.MainAxisAlignment.SPACE_EVENLY,
            controls=[
                flet.IconButton(icon=flet.Icons.MENU, icon_color=flet.Colors.WHITE),
                flet.IconButton(icon=flet.Icons.SEARCH, icon_color=flet.Colors.WHITE),
                flet.IconButton(icon=flet.Icons.FAVORITE, icon_color=flet.Colors.WHITE),
            ]
        ),
    )

def vannerBox(image:dict, width, height) -> flet.Image:
    return flet.Image(
        src = image["src"],
        fit = flet.ImageFit.FILL,
        width = width,
        height = height,
    )

def itemBox(image:dict, hoverE, clickE) -> flet.Card:
    return flet.Card(
        color = flet.Colors.BROWN_100,
        clip_behavior = flet.ClipBehavior.HARD_EDGE,
        elevation = 3,
        width = 180,
        height = 300,
        content = flet.Column(
            alignment = flet.MainAxisAlignment.START,
            controls = [
                flet.Container(
                    alignment = flet.alignment.center,
                    height = 180,
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
                    margin = flet.margin.only(10, 0, 0, 0),
                    content = flet.Column(
                        alignment = flet.MainAxisAlignment.START,
                        controls = [
                            flet.Text(
                                image["name"],
                                color = flet.Colors.GREY_700,
                                weight = flet.FontWeight.W_500,
                                ),
                            flet.Text(
                                f"{image["price"]:,}",
                                color = flet.Colors.GREY_700,
                                weight = flet.FontWeight.W_900,
                                ),
                            ],),
                        ),
                flet.Container(
                    alignment = flet.alignment.center_left,
                    margin = flet.margin.only(0, 0, 10, 0),
                    content = flet.Row(
                        alignment = flet.MainAxisAlignment.END,
                        controls = [
                            flet.Container(
                                on_click = clickE,
                                content = flet.Icon(
                                    name = flet.Icons.FAVORITE_BORDER,
                                    color = flet.Colors.RED_700,
                                    size = 30,
                                ),
                            ),
                        ],)
                )   ,
                ],),
        )