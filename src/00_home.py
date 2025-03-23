import flet
import shop_demo.src.widget as WG

async def main(page: flet.Page):
    page.window.max_width = 600
    page.window.resizable = True

    mainPage = flet.Container(
        alignment=flet.alignment.top_center,
        expand=True,
        border = flet.border.all(
            width = 2,
            color=flet.Colors.BLACK45
        ),
        content = flet.Column(
            controls = [],
        )
    )

    page.add(mainPage)

if __name__ == "__main__":
    flet.app(target = main)