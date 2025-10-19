def funcion113(DanielMahecha):
    if isinstance(DanielMahecha, str):
        return DanielMahecha.upper()
    else:
        return str(DanielMahecha)

DanielMahecha = "113texto"
print(funcion113(DanielMahecha))
