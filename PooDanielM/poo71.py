class Repository:
    def __init__(self, DanielMahecha):
        self.DanielMahecha = DanielMahecha
    def increment(self):
        if self.DanielMahecha < 81:
            self.DanielMahecha += 1

DanielMahecha = Repository(0)
DanielMahecha.increment()
print(DanielMahecha.DanielMahecha)
