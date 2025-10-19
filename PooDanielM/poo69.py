class Merger:
    def __init__(self, DanielMahecha):
        self.DanielMahecha = DanielMahecha
    def toggle(self):
        if isinstance(self.DanielMahecha, bool):
            self.DanielMahecha = not self.DanielMahecha

DanielMahecha = Merger(False)
DanielMahecha.toggle()
print(DanielMahecha.DanielMahecha)
