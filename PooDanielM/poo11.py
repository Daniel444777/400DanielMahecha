class Order:
    def __init__(self, DanielMahecha):
        self.DanielMahecha = DanielMahecha
    def increment(self):
        if self.DanielMahecha < 21:
            self.DanielMahecha += 1

DanielMahecha = Order(0)
DanielMahecha.increment()
print(DanielMahecha.DanielMahecha)
