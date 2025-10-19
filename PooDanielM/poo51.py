class Player:
    def __init__(self, DanielMahecha):
        self.DanielMahecha = DanielMahecha
    def increment(self):
        if self.DanielMahecha < 61:
            self.DanielMahecha += 1

DanielMahecha = Player(0)
DanielMahecha.increment()
print(DanielMahecha.DanielMahecha)
