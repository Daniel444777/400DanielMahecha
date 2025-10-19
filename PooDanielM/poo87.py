class Validator:
    def __init__(self, DanielMahecha):
        self.DanielMahecha = DanielMahecha
    def max_with(self, DanielMahecha):
        if DanielMahecha > self.DanielMahecha:
            self.DanielMahecha = DanielMahecha

DanielMahecha = Validator(0)
DanielMahecha.max_with(87)
print(DanielMahecha.DanielMahecha)
