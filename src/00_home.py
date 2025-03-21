import flet
import shop_demo.src.style as style

async def main(page: flet.Page):
    page.window.max_width = 800
    page.scroll = 'always'
    image_urls = [f'assets/01_itemRecommend/G25031900{i}.jpg' for i in range(1, 6)]
    current_index = 0

    event_image = flet.Image(
        src = image_urls[current_index],
        width = page.window.width * 0.8,
        height = page.window.width * 0.6,
        fit = flet.ImageFit.FILL,
        opacity = 1,
        animate_opacity = flet.animation.Animation(duration=300, curve=flet.AnimationCurve.EASE_IN_OUT),
    )

    eventVanner = flet.Row(
        controls = [event_image],
        expand = 1,
        wrap = False,
        scroll = 'always',
        alignment = flet.MainAxisAlignment.CENTER,
    )

    pageContainer = flet.Container(
            alignment = flet.alignment.center,
            border = flet.border.all(width=2,color=flet.Colors.BLACK45),
            content = flet.Column(
                [
                    eventVanner,
                    style.MyButton(
                        text='test',
                    )
                ],
                alignment= flet.MainAxisAlignment.START,
                horizontal_alignment=flet.CrossAxisAlignment.CENTER
            )
        )

    page.add(pageContainer)

if __name__ == "__main__":
    flet.app(target = main)