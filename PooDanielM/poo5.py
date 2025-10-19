class Animal:
    def __init__(self, DanielMahecha):
        self.DanielMahecha = DanielMahecha
    def scale(self, DanielMahecha):
        if DanielMahecha > 0:
            self.DanielMahecha *= DanielMahecha

DanielMahecha = Animal(2)
DanielMahecha.scale(3)
print(DanielMahecha.DanielMahecha)
