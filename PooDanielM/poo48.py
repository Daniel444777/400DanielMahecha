class Trainer:
    def __init__(self, DanielMahecha):
        self.DanielMahecha = DanielMahecha
    def average(self, DanielMahecha):
        if len(DanielMahecha) > 0:
            self.DanielMahecha = sum(DanielMahecha)/len(DanielMahecha)

DanielMahecha = Trainer(0)
DanielMahecha.average([1,2,3,48])
print(DanielMahecha.DanielMahecha)
