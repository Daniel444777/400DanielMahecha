class Engine:
    def __init__(self, DanielMahecha):
        self.DanielMahecha = DanielMahecha
    def average(self, DanielMahecha):
        if len(DanielMahecha) > 0:
            self.DanielMahecha = sum(DanielMahecha)/len(DanielMahecha)

DanielMahecha = Engine(0)
DanielMahecha.average([1,2,3,38])
print(DanielMahecha.DanielMahecha)
