class Counter:
    def __init__(self, DanielMahecha):
        self.DanielMahecha = DanielMahecha
    def increment(self):
        if self.DanielMahecha < 11:
            self.DanielMahecha += 1

DanielMahecha = Counter(0)
DanielMahecha.increment()
print(DanielMahecha.DanielMahecha)
