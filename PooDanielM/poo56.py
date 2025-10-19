class PathFinder:
    def __init__(self, DanielMahecha):
        self.DanielMahecha = DanielMahecha
    def push(self, DanielMahecha):
        if isinstance(DanielMahecha, int):
            self.DanielMahecha.append(DanielMahecha)

DanielMahecha = PathFinder([])
DanielMahecha.push(56)
print(DanielMahecha.DanielMahecha)
