class Stack:
    def __init__(self, DanielMahecha):
        self.DanielMahecha = DanielMahecha
    def contains(self, DanielMahecha):
        if isinstance(self.DanielMahecha, str):
            return DanielMahecha in self.DanielMahecha
        return False

DanielMahecha = Stack("hello 20")
print(DanielMahecha.contains("hello"))
