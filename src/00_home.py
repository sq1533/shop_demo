import flet
import shop_demo.src.widget as WG
import json

with open(file="../storage/data/products.json", mode="r", encoding="utf-8") as f:
    product = json.load(fp=f)

productCount = list(product["item"]).__len__()

async def main(page: flet.Page):
    # 상품 on_hover 이벤트
    def hoverItem(e):
        e.control.image.opacity = 0.7 if e.data == "true" else 1
        e.control.update()
    # like 클릭 이벤트
    def favoriteIcon(e):
        icon_widget = e.control.content
        if icon_widget.name == flet.Icons.FAVORITE_BORDER:
            icon_widget.name = flet.Icons.FAVORITE
        else:
            icon_widget.name = flet.Icons.FAVORITE_BORDER
        page.update()

    page.window.max_width = 600
    page.window.resizable = True
    page.scroll = flet.ScrollMode.HIDDEN

    itemCards = []
    for i in range(1, productCount+1):
        item = WG.itemBox(image=product["item"][f"item_{i}"], hoverE=hoverItem, clickE=favoriteIcon)
        itemCards.append(item)

    page.appbar = WG.APPBar(image=product["logo"])
    page.bottom_appbar = WG.bottomNavBar()

    mainPage = flet.Container(
        alignment=flet.alignment.top_center,
        expand=True,
        border = flet.border.all(
            width = 2,
            color=flet.Colors.BLACK45
        ),
        content = flet.Column(
            alignment = flet.MainAxisAlignment.START,
            horizontal_alignment= flet.CrossAxisAlignment.CENTER,
            controls = [
                WG.vannerBox(image = product["recommend"]["item_1"], width=(page.window.width*0.8), height=(page.window.width*0.8)),
                flet.Row(
                    alignment = flet.MainAxisAlignment.CENTER,
                    controls = itemCards,
                    )
                ],
        )
    )

    page.add(mainPage)

if __name__ == "__main__":
    flet.app(target = main)