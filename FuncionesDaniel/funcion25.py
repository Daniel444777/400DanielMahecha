def funcion25(DanielMahecha):
    if len(DanielMahecha) > 3:
        return DanielMahecha[::-1]
    else:
        return DanielMahecha + DanielMahecha

DanielMahecha = "texto25"
print(funcion25(DanielMahecha))
