class Student:
    def __init__(self, DanielMahecha):
        self.DanielMahecha = DanielMahecha
    def is_even(self):
        return self.DanielMahecha % 2 == 0

DanielMahecha = Student(14)
print(DanielMahecha.is_even())
