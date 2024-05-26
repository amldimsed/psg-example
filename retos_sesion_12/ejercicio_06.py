"""
Número 1: 10
Número 2: 5
Operación: +
-------------
Resultado: 15
"""

num1 = input('Número 1: ')
num2 = input('Número 2: ')
operador = input('Operación: ')
#truthy no funciona con input, supuestamente deberia ser string null=='' pero no reconoce
if num1 == '':
    num1 = '0.0'
if num2 == '':
    num2 = '0.0'

numer1 = float(num1)
numer2 = float(num2)

if operador == '':
    resultado = 'No hay operador +, -, *, /'
elif operador == '+':
    resultado = numer1 + numer2
elif operador == '-':
    resultado = numer1 - numer2
elif operador == '/':
    if numer2 != 0:
        resultado = numer1 / numer2
    else:
        resultado = 'infinito'
elif operador == '*':
    resultado = numer1 * numer2
else:
    resultado = 'Error de operador'        
print('----------------')
print('Resultado:',resultado)