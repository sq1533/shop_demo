import flet
from dataSet import product

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
    flet.Page.update()

def itemCard(image:dict, hoverE, clickE) -> flet.Card:
    return flet.Card(
        color = flet.Colors.ORANGE_800,
        clip_behavior = flet.ClipBehavior.HARD_EDGE,
        elevation = 3,
        width = 200,
        height = 280,
        content = flet.Column(
            alignment = flet.MainAxisAlignment.START,
            controls = [
                flet.Container(
                    alignment = flet.alignment.center,
                    height = 200,
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
                    margin = flet.margin.only(10, 0, 10, 0),
                    content = flet.Column(
                        alignment = flet.MainAxisAlignment.START,
                        controls = [
                            flet.Text(
                                image["name"],
                                color = flet.Colors.WHITE,
                                weight = flet.FontWeight.W_500,
                                ),
                            flet.Row(
                                alignment = flet.MainAxisAlignment.SPACE_BETWEEN,
                                controls = [
                                    flet.Text(
                                        f"{image["price"]:,}",
                                        color = flet.Colors.WHITE,
                                        weight = flet.FontWeight.W_900,
                                        ),
                                    flet.Container(
                                        on_click = clickE,
                                        content = flet.Icon(
                                            name = flet.Icons.FAVORITE_BORDER,
                                            color = flet.Colors.WHITE,
                                            size = 30,
                                            ),
                                        ),
                                    ],),
                            ],),
                        ),
                ],),
        )

productCount = list(product["item"]).__len__()

itemCards = []
for i in range(1, productCount+1):
    item = itemCard(image=product["item"][f"item_{i}"], hoverE=hoverItem, clickE=favoriteIcon)
    itemCards.append(item)

item = flet.Row(controls=itemCards, expand=True, expand_loose=True)