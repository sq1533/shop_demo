import flet

# 비로그인 APPBar
def nonLoginAppBar(page: flet.Page, readProduct: dict) -> flet.AppBar:

    # APP 상단 바
    APPBar = flet.AppBar(
        leading = flet.Container(
            alignment = flet.alignment.center,
            on_click = lambda _: page.go("/"),
            image = flet.DecorationImage(
                src = readProduct["src"],
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
                on_click = lambda _: page.go("/loginPage"),
                ),
            ],)
    return APPBar

# 로그인 APPBar
def loginAppBar(page: flet.Page, user: dict, readProduct: dict) -> flet.AppBar:

    # APP 상단 바
    APPBar = flet.AppBar(
        leading = flet.Container(
            alignment = flet.alignment.center,
            on_click = lambda _: page.go("/"),
            image = flet.DecorationImage(
                src = readProduct["src"],
                fit = flet.ImageFit.FILL,
            ),
            ),
        leading_width = 100,
        center_title = False,
        bgcolor = flet.Colors.BROWN_100,
        actions = [
            flet.TextButton(
                text = f'{user.keys()}, 환영합니다.',
                scale = 1,
                icon = flet.Icons.LOGIN,
                icon_color = flet.Colors.WHITE,
                on_click = lambda _: page.go(f"/{user.keys()}/myPage"),
                ),
            ],)
    return APPBar