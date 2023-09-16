entrada = input("Agrega números a la lista separados por espacio: ")
numeros = [int(i) for i in entrada.split()] 

suma = 0
for numero in numeros:
    suma += numero
print("La suma de la lista de números es: ", suma)    