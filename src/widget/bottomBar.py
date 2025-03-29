import flet

# 비로그인 bottomBar
def nonLoginbottom() -> flet.BottomAppBar:

    # bottomBar 바
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
    return bottomBar

# 로그인 bottomBar
def loginbottom() -> flet.BottomAppBar:

    # bottomBar 바
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
    return bottomBar