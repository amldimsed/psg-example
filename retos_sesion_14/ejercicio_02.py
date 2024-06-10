"""
Calculadora flexible: Crea una calculadora que acepte diferentes 
operaciones matemáticas como argumentos de palabras clave y realice 
los cálculos correspondientes, las operaciones son suma, resta, 
multiplicación y división
"""
def calculadora(dato1:float, dato2:float, operador:str):
    """
    calculadora para 2 numeros
        dato1: primer numero
        dato2: segundo numero
    """
    resultado = 0
    if operador == "+":
        resultado = dato1 + dato2
    elif operador == "-":
        resultado = dato1 - dato2
    elif operador == "*":
        resultado = dato1 * dato2
    elif operador == "/":
        if dato2 == 0:
            resultado = "divicion entre 0 no es posible"
        else:
            resultado = dato1 / dato2
    else:
        resultado = "operacion no valido"
    return resultado

#calculadora de dos numeros
numero1 = float(input("ingrese el primer numero: "))
numero2 = float(input("ingrese el segundo numero: "))
operador = input("ingrese un operador: ")

print("  ", numero1, f"\n {operador}", numero2)
print("---------")
print(calculadora(numero1, numero2, operador))
print(calculadora.__doc__)
