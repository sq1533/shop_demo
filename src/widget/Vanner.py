import flet
from dataSet import product

recommend = product["recommend"]
itemList = list(recommend.keys())

bigBox = flet.Image(
    fit = flet.ImageFit.FILL,
    src = recommend["item_1"]["src"],
    )

smallBoxRow = flet.Row(
    spacing = 0,
    expand = True,
    expand_loose = True,
    scroll = flet.ScrollMode.ALWAYS,
    )

for i in itemList:
    img = flet.Image(
        width = 100,
        height = 100,
        fit = flet.ImageFit.FILL,
        src = recommend[i]["src"],
    )
    smallBoxRow.controls.append(img)

vanner = flet.Column(
    spacing = 0,
    controls = [
        bigBox,
        smallBoxRow,
    ]
)