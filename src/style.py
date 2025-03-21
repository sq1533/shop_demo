import flet

class MyButton(flet.ElevatedButton):
    def __init__(self, text):
        super().__init__()
        self.bgcolor = flet.Colors.ORANGE_300
        self.color = flet.Colors.GREEN_800
        self.text = text