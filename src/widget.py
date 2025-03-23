import flet

def vannerBox(image:str, width, height) -> flet.Image:
    return flet.Image(
        src = image,
        fit = flet.ImageFit.FILL,
        width = width,
        height = height,
    )

def itemBox(image:str) -> flet.Card:
    return flet.Card(
        content = flet.Container(
            content = flet.Column(
                controls = [
                    flet.Image(
                        src = image,
                        width = 300,
                        height = 200
                    ),
                    flet.ListTile(
                        leading=flet.Icon(flet.Icons.ALBUM),
                        title=flet.Text("The Enchanted Nightingale"),
                        subtitle=flet.Text(
                            "Music by Julie Gable. Lyrics by Sidney Stein."
                        ),
                    ),
                    flet.Row(
                        [flet.TextButton("Buy tickets"), flet.TextButton("Listen")],
                        alignment=flet.MainAxisAlignment.END,
                    ),
                ]
            ),
            width = 400,
            height = 800,
        )
    )