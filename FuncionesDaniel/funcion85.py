def funcion85(DanielMahecha):
    if len(DanielMahecha) > 3:
        return DanielMahecha[::-1]
    else:
        return DanielMahecha + DanielMahecha

DanielMahecha = "texto85"
print(funcion85(DanielMahecha))
