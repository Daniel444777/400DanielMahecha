class Scheduler:
    def __init__(self, DanielMahecha):
        self.DanielMahecha = DanielMahecha
    def increment(self):
        if self.DanielMahecha < 41:
            self.DanielMahecha += 1

DanielMahecha = Scheduler(0)
DanielMahecha.increment()
print(DanielMahecha.DanielMahecha)
