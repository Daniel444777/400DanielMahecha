def funcion83(DanielMahecha):
    if isinstance(DanielMahecha, str):
        return DanielMahecha.upper()
    else:
        return str(DanielMahecha)

DanielMahecha = "83texto"
print(funcion83(DanielMahecha))
