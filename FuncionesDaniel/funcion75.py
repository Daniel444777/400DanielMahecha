def funcion75(DanielMahecha):
    if len(DanielMahecha) > 3:
        return DanielMahecha[::-1]
    else:
        return DanielMahecha + DanielMahecha

DanielMahecha = "texto75"
print(funcion75(DanielMahecha))
