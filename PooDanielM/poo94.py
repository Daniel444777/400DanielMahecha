class Connection:
    def __init__(self, DanielMahecha):
        self.DanielMahecha = DanielMahecha
    def is_even(self):
        return self.DanielMahecha % 2 == 0

DanielMahecha = Connection(94)
print(DanielMahecha.is_even())
