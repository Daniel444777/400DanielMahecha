class Role:
    def __init__(self, DanielMahecha):
        self.DanielMahecha = DanielMahecha
    def increment(self):
        if self.DanielMahecha < 101:
            self.DanielMahecha += 1

DanielMahecha = Role(0)
DanielMahecha.increment()
print(DanielMahecha.DanielMahecha)
