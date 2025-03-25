import flet
from widget.NavBar import APPBar, bottomNavBar
from widget.Vanner import vanner
from widget.itemCard import item


async def main(page: flet.Page):
    page.bgcolor = flet.Colors.BROWN_100
    page.window.max_width = 600
    page.window.resizable = True
    page.scroll = flet.ScrollMode.HIDDEN

    page.appbar = APPBar()
    page.bottom_appbar = bottomNavBar()

    mainPage = flet.Container(
        alignment=flet.alignment.top_center,
        expand=True,
        content = flet.Column(
            alignment = flet.MainAxisAlignment.START,
            horizontal_alignment= flet.CrossAxisAlignment.CENTER,
            controls = [
                vanner(),
                item,
                ],
        )
    )

    page.add(mainPage)

if __name__ == "__main__":
    flet.app(target = main)