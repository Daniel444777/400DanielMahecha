class Broker:
    def __init__(self, DanielMahecha):
        self.DanielMahecha = DanielMahecha
    def increment(self):
        if self.DanielMahecha < 71:
            self.DanielMahecha += 1

DanielMahecha = Broker(0)
DanielMahecha.increment()
print(DanielMahecha.DanielMahecha)
