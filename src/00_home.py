import flet
import shop_demo.src.widget as WG

async def main(page: flet.Page):
    page.window.max_width = 600
    page.window.resizable = True

    def page_resize() -> list:
        new_width = page.window.width * 0.8
        new_height = new_width * 0.6
        newSize = [new_width, new_height]
        page.update()
        return newSize

    page.on_resized = page_resize()

    initial_width = page_resize()[0] * 0.8
    initial_height = page_resize()[1] * 0.6

    mainPage = flet.Container(
        alignment=flet.alignment.top_center,
        expand=True,
        border = flet.border.all(
            width = 2,
            color=flet.Colors.BLACK45
        ),
        content = flet.Column(
            [
                WG.vannerBox(
                    image = 'assets/01_itemRecommend/G250319001.jpg',
                    width = initial_width,
                    height = initial_height
                ),
            ],
        )
    )

    page.add(mainPage)

if __name__ == "__main__":
    flet.app(target = main)