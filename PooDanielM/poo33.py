class Notebook:
    def __init__(self, DanielMahecha):
        self.DanielMahecha = {'value': DanielMahecha}
    def update(self, DanielMahecha):
        if DanielMahecha > self.DanielMahecha['value']:
            self.DanielMahecha['value'] = DanielMahecha

DanielMahecha = Notebook(5)
DanielMahecha.update(10)
print(DanielMahecha.DanielMahecha)
