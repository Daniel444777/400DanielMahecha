class Queue:
    def __init__(self, DanielMahecha):
        self.DanielMahecha = DanielMahecha
    def increment(self):
        if self.DanielMahecha < 31:
            self.DanielMahecha += 1

DanielMahecha = Queue(0)
DanielMahecha.increment()
print(DanielMahecha.DanielMahecha)
