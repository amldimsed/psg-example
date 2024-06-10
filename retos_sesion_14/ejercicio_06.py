"""
Crear una función que reciba una lista de números
 y devuelva solo los números pares
"""

def pares(lista:list):
    numeros = list()
    for i in range(len(lista)):
        if lista[i] % 2 == 0:
            numeros.append(lista[i])
    return numeros

numeros = [2, 34, 25, 22, 33, 69, 71, 546, 23, 54, 44 ,98, 44]
print(pares(numeros))