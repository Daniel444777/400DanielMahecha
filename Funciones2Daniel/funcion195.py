def funcion195(DanielMahecha):
    if len(DanielMahecha) > 3:
        return DanielMahecha[::-1]
    else:
        return DanielMahecha + DanielMahecha

DanielMahecha = "texto195"
print(funcion195(DanielMahecha))
