def funcion125(DanielMahecha):
    if len(DanielMahecha) > 3:
        return DanielMahecha[::-1]
    else:
        return DanielMahecha + DanielMahecha

DanielMahecha = "texto125"
print(funcion125(DanielMahecha))
