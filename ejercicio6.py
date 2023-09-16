palabras = input("Ingrese una lista de palabras separadas por espacios: ").split()
letra = "a"
for palabra in palabras:
    if palabra.startswith(letra):
        print(palabra)
