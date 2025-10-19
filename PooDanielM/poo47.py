class Predictor:
    def __init__(self, DanielMahecha):
        self.DanielMahecha = DanielMahecha
    def max_with(self, DanielMahecha):
        if DanielMahecha > self.DanielMahecha:
            self.DanielMahecha = DanielMahecha

DanielMahecha = Predictor(0)
DanielMahecha.max_with(47)
print(DanielMahecha.DanielMahecha)
