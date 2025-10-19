class Middleware:
    def __init__(self, DanielMahecha):
        self.DanielMahecha = DanielMahecha
    def max_with(self, DanielMahecha):
        if DanielMahecha > self.DanielMahecha:
            self.DanielMahecha = DanielMahecha

DanielMahecha = Middleware(0)
DanielMahecha.max_with(77)
print(DanielMahecha.DanielMahecha)
