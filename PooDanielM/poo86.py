class Form:
    def __init__(self, DanielMahecha):
        self.DanielMahecha = DanielMahecha
    def push(self, DanielMahecha):
        if isinstance(DanielMahecha, int):
            self.DanielMahecha.append(DanielMahecha)

DanielMahecha = Form([])
DanielMahecha.push(86)
print(DanielMahecha.DanielMahecha)
