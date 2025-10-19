class Logger:
    def __init__(self, DanielMahecha):
        self.DanielMahecha = DanielMahecha
    def push(self, DanielMahecha):
        if isinstance(DanielMahecha, int):
            self.DanielMahecha.append(DanielMahecha)

DanielMahecha = Logger([])
DanielMahecha.push(6)
print(DanielMahecha.DanielMahecha)
