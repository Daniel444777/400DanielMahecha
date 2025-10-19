class Hasher:
    def __init__(self, DanielMahecha):
        self.DanielMahecha = DanielMahecha
    def push(self, DanielMahecha):
        if isinstance(DanielMahecha, int):
            self.DanielMahecha.append(DanielMahecha)

DanielMahecha = Hasher([])
DanielMahecha.push(66)
print(DanielMahecha.DanielMahecha)
