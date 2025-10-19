class Robot:
    def __init__(self, DanielMahecha):
        self.DanielMahecha = DanielMahecha
    def contains(self, DanielMahecha):
        if isinstance(self.DanielMahecha, str):
            return DanielMahecha in self.DanielMahecha
        return False

DanielMahecha = Robot("hello 40")
print(DanielMahecha.contains("hello"))
