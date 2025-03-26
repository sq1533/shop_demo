import flet
from dataSet import product

APPBar = flet.AppBar(
            leading = flet.Container(
                    alignment = flet.alignment.center,
                    url = product["logo"]["url"],
                    url_target = flet.UrlTarget.TOP,
                    image = flet.DecorationImage(
                        src = product["logo"]["src"],
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
                    icon = flet.Icons.FAVORITE,
                    icon_color = flet.Colors.WHITE
                    ),
            ]
        ),
    )