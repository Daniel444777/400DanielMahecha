class Builder:
    def __init__(self, DanielMahecha):
        self.DanielMahecha = DanielMahecha
    def increment(self):
        if self.DanielMahecha < 91:
            self.DanielMahecha += 1

DanielMahecha = Builder(0)
DanielMahecha.increment()
print(DanielMahecha.DanielMahecha)
