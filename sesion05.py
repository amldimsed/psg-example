print ( type (1) )

# Variable 20 Entero
variable_2 = int (20)
print (variable_2)
print ( type (variable_2) )

# Valor 10 en base decimal
print ("Base decimal")
print (10)
# Valor 10 en binario
print ("Base binaria")
print (0b1010)
# Valor 10 en octal
print ("Base octal")
print (0o12)
# Valor 10 en hexadecimal
print ("Base hexadecimal")
print (0xa)

# Entero con 60 dígitos
variable_3 = 123456789012345678901234567890123456789012345678901234567890
print (variable_3)
print ( type (variable_3) )

# Valor 0.5 Flotante
print (0.5)
print ( type (0.5) )

# Variable 0.100546 Flotante
variable_4 = 0.100546
print (variable_4)
print ( type (variable_4) )
# Variable 1 Flotante
variable_7 = float (1)
print(variable_7)
print ( type (variable_7) )

# Precisión de 17 decimales
variable_5 = 0.99999999999999999
print(variable_5)
print ( type (variable_5) )

# Valor 2.0e-3 Flotante
variable_6 = 2.0e-3
print(variable_6)
print ( type (variable_6) )

# Operadores aritméticos
a = 10
b = 3
# Suma
print ("Suma")
print (a + b)
# Resta
print ("Resta")
print (a - b)
# Multiplicación
print ("Multiplicación")
print (a * b)

print ("División")
print (a / b)

# Potencia
print ("Potencia")
print (a ** b)
# Módulo o residuo
print ("Módulo o residuo")
print (a % b)

print ("División entera")
print (a // b)

print((3600*60)+300)

minutos = 300
segundos = 3600
horas = (minutos/60)+(segundos/3600)
print ("Horas: ", horas)
print ((300+(3600//60))//60)

# Operaciones más complejas
minutos = 300
tiempo_extra_segundos = 3600
horas = (minutos + tiempo_extra_segundos / 60) / 60
print (horas)

print ("Operadores de comparación int - float")
entero = 10
flotante = 10.0
print (entero < flotante)
print (entero > flotante)
print (entero == flotante)
print (entero <= flotante)
print (entero >= flotante)
print (entero != flotante)
numero_1 = 10
numero_2 = 5
print ((numero_1 / 2)% 2 == 0)
print ((numero_1 / 2)% 2 == 1)
print(True if 5%2!=0 else False)
# https://study.pylapaz.org/content/sesion05/#/48