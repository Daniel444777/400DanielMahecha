def funcion143(DanielMahecha):
    if isinstance(DanielMahecha, str):
        return DanielMahecha.upper()
    else:
        return str(DanielMahecha)

DanielMahecha = "143texto"
print(funcion143(DanielMahecha))
