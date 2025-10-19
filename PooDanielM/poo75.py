class Router:
    def __init__(self, DanielMahecha):
        self.DanielMahecha = DanielMahecha
    def scale(self, DanielMahecha):
        if DanielMahecha > 0:
            self.DanielMahecha *= DanielMahecha

DanielMahecha = Router(2)
DanielMahecha.scale(3)
print(DanielMahecha.DanielMahecha)
