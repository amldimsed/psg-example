
cad = input("ingresa cadena: ")

#cadena = list()
#cadena.append(cad)

tupla = tuple(cad)

concatenar1 = ('¡', ) + tupla + ('!', )

concatenar1 *= 3
print(concatenar1)