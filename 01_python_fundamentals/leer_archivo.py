with open("datos.txt", "r", encoding="utf-8") as archivo:
    for linea in archivo:
        nombre = linea.strip()
        if nombre:
            print("Usuario:", nombre)
