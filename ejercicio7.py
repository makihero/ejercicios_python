list1 = input("Ingrese una lista de numeros separadas por espacios: ")
numeros_list1 = [int(numero) for numero in list1.split()]

list2 = input("Ingrese otra lista de numeros separadas por espacios: ")
numeros_list2 = [int(numero2) for numero2 in list2.split()]

suma = []
for i in range(len(numeros_list1)):
    sumar = numeros_list1[i] + numeros_list2[i]
    suma.append(sumar)
print(numeros_list1)
print(numeros_list2)
print("La suma de las dos listas: ", suma)    