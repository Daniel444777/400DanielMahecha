class Rectangle:
    def __init__(self, DanielMahecha):
        self.DanielMahecha = DanielMahecha
    def push(self, DanielMahecha):
        if isinstance(DanielMahecha, int):
            self.DanielMahecha.append(DanielMahecha)

DanielMahecha = Rectangle([])
DanielMahecha.push(26)
print(DanielMahecha.DanielMahecha)
