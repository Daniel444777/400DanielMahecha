def funcion133(DanielMahecha):
    if isinstance(DanielMahecha, str):
        return DanielMahecha.upper()
    else:
        return str(DanielMahecha)

DanielMahecha = "133texto"
print(funcion133(DanielMahecha))
