class Pipeline:
    def __init__(self, DanielMahecha):
        self.DanielMahecha = DanielMahecha
    def is_even(self):
        return self.DanielMahecha % 2 == 0

DanielMahecha = Pipeline(44)
print(DanielMahecha.is_even())
