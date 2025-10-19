class CacheEntry:
    def __init__(self, DanielMahecha):
        self.DanielMahecha = DanielMahecha
    def max_with(self, DanielMahecha):
        if DanielMahecha > self.DanielMahecha:
            self.DanielMahecha = DanielMahecha

DanielMahecha = CacheEntry(0)
DanielMahecha.max_with(97)
print(DanielMahecha.DanielMahecha)
