class Adapter:
    def __init__(self, DanielMahecha):
        self.DanielMahecha = DanielMahecha
    def average(self, DanielMahecha):
        if len(DanielMahecha) > 0:
            self.DanielMahecha = sum(DanielMahecha)/len(DanielMahecha)

DanielMahecha = Adapter(0)
DanielMahecha.average([1,2,3,78])
print(DanielMahecha.DanielMahecha)
