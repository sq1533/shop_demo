import flet

def main(page: flet.Page):

    # 페이지 설정
    page.bgcolor = flet.Colors.BROWN_100
    page.window.max_width = 600
    page.window.alignment = flet.alignment.top_center
    page.scroll = flet.ScrollMode.ALWAYS


    mainPage = flet.Container(
        alignment=flet.alignment.top_center,
        expand=True,
        content = flet.Column(
            alignment = flet.MainAxisAlignment.START,
            horizontal_alignment= flet.CrossAxisAlignment.CENTER,
            controls = [],
            )
        )

    page.add(mainPage)

if __name__ == "__main__":
    flet.app(target = main, port = 8501)