import flet
import time
from dataSet import product


def vannerBox(image:dict) -> flet.Image:
    return flet.Image(
        src = image["src"],
        fit = flet.ImageFit.FILL,
    )

def vannerSmallBox(image:str) -> flet.Image:
    return flet.Image(
        src = image["src"],
        fit = flet.ImageFit.FILL,
    )

bottomRow = flet.Row(
        expand = True,
        expand_loose = True,
        controls = []
    )

productCount = list(product["recommend"]).__len__()

for i in range(1, productCount+1):
    item = vannerSmallBox(image=product["recommend"][f"item_{i}"])
    bottomRow.controls.append(item)


def vanner(self) -> flet.Column:
    Vanner = flet.Column(controls=[])
    start = 1
    if start < productCount+1:
        Vanner.controls.append([vannerBox(image=product["recommend"][f"item_{start}"]), bottomRow])
        start += 1
        self.flet.Page.update()
        time.sleep(10)
    else:
        start == 1
        Vanner.controls.append([vannerBox(image=product["recommend"][f"item_{start}"]), bottomRow])
        start += 1
        self.flet.Page.update()
        time.sleep(10)
    return Vanner