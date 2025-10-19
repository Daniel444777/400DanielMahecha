class Signal:
    def __init__(self, DanielMahecha):
        self.DanielMahecha = DanielMahecha
    def max_with(self, DanielMahecha):
        if DanielMahecha > self.DanielMahecha:
            self.DanielMahecha = DanielMahecha

DanielMahecha = Signal(0)
DanielMahecha.max_with(57)
print(DanielMahecha.DanielMahecha)
