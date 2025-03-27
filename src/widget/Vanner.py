import flet
from dataSet import product

# data loads
recommend = product["recommend"]
recommendList = list(recommend.keys())

def Vanner(page : flet.Page) -> flet.Column:
    # Vanner 설정(이벤트 / 추천 상품)
    # big vanner
    bigBox = flet.Image(
        fit = flet.ImageFit.FILL,
        src = recommend[recommendList[0]]["src"],
        )

    # option vanner
    smallBoxRow = flet.Row(
        spacing = 0,
        expand = True,
        expand_loose = True,
        scroll = flet.ScrollMode.ALWAYS,
        )

    # vanner 목록
    for i in recommendList:
        img = flet.Image(
            width = 100,
            height = 100,
            fit = flet.ImageFit.FILL,
            src = recommend[i]["src"],
        )
        smallBoxRow.controls.append(img)

    # main vanner
    vanner = flet.Column(
        spacing = 0,
        controls = [
            bigBox,
            smallBoxRow,
        ],)
    return vanner