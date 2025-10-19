class Converter:
    def __init__(self, DanielMahecha):
        self.DanielMahecha = DanielMahecha
    def push(self, DanielMahecha):
        if isinstance(DanielMahecha, int):
            self.DanielMahecha.append(DanielMahecha)

DanielMahecha = Converter([])
DanielMahecha.push(36)
print(DanielMahecha.DanielMahecha)
