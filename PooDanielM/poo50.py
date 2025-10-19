class Game:
    def __init__(self, DanielMahecha):
        self.DanielMahecha = DanielMahecha
    def contains(self, DanielMahecha):
        if isinstance(self.DanielMahecha, str):
            return DanielMahecha in self.DanielMahecha
        return False

DanielMahecha = Game("hello 50")
print(DanielMahecha.contains("hello"))
