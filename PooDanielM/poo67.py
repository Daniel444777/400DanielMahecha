class Encryptor:
    def __init__(self, DanielMahecha):
        self.DanielMahecha = DanielMahecha
    def max_with(self, DanielMahecha):
        if DanielMahecha > self.DanielMahecha:
            self.DanielMahecha = DanielMahecha

DanielMahecha = Encryptor(0)
DanielMahecha.max_with(67)
print(DanielMahecha.DanielMahecha)
