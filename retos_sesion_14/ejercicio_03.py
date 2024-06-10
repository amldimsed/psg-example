"""
Crear una función recursiva para obtener 
el N número de la serie de Fibonacci
"""
L = [0, 1]
def Memoria_Fibonaci(n):
    """
    utilizando una lista
    exite ya 0 o 1 ya calculado en una rama del arbol al disminuir n
    """
    if n == 0:
        return L[0]
    if n == 1:
        return L[1]
    #exite ya 0 o 1 ya calculado en una rama del arbol al disminuir n
    if n < len(L):
        return L[n-1] + L[n-2]
    else:
        L.append(Memoria_Fibonaci(n-1) + Memoria_Fibonaci(n-2))
        return L[n]

def Nfibonaci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return Nfibonaci(n-1) + Nfibonaci(n-2)

#Segun la definicion wiki el fibo se cuenta desde f2 como 1 y no desde f0
#Entonces el 0 no esta adoptado 1,1,2,3,5,8......
#Para este caso tomar encuenta el conteo 0 como 01234
n = int(input("ingrese un numero: "))
for i in range(n+1):
    print(Nfibonaci(i), end=", ")

numero = Nfibonaci(n)
print("\n", numero)

#Con memoria utilizando lista global
print("CON MEMORIA")
for i in range(n+1):
    print(Memoria_Fibonaci(i), end=", ")

numero = Memoria_Fibonaci(n)
print("\n", numero)