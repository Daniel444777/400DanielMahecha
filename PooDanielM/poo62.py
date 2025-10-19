class Session:
    def __init__(self, DanielMahecha):
        self.DanielMahecha = list(DanielMahecha)
    def add_if_not_present(self, DanielMahecha):
        if DanielMahecha not in self.DanielMahecha:
            self.DanielMahecha.append(DanielMahecha)

DanielMahecha = Session([1,2,3])
DanielMahecha.add_if_not_present(4)
print(DanielMahecha.DanielMahecha)
