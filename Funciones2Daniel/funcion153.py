def funcion153(DanielMahecha):
    if isinstance(DanielMahecha, str):
        return DanielMahecha.upper()
    else:
        return str(DanielMahecha)

DanielMahecha = "153texto"
print(funcion153(DanielMahecha))
