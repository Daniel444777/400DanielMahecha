class Drone:
    def __init__(self, DanielMahecha):
        self.DanielMahecha = DanielMahecha
    def increment(self):
        if self.DanielMahecha < 51:
            self.DanielMahecha += 1

DanielMahecha = Drone(0)
DanielMahecha.increment()
print(DanielMahecha.DanielMahecha)
