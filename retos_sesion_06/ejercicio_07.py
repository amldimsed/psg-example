#Falso (a+b)²-----a²+b²
print("¿El cuadrado y la suma de 2 y 2 son iguales?")

a = 2
b = 2
cuadrado = (a + b)**2
suma = 2**2 + 2**2
resultado = cuadrado == suma
# xd if disfrazado, acortador
cuadrado == suma and print(resultado, "son iguales")
cuadrado != suma and print(resultado, "son diferentes")