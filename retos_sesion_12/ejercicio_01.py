numero = input("ingrese numero: ")

entero = int(float(numero))

resultado = f"el numero {entero} es PAR" if entero % 2 == 0 else f"el numero {entero} es IMPAR"
print(resultado)