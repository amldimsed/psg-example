""""
Crea un diccionario con las siguientes tuplas de animales
tupla = (('perro', '🐶') , ('gato','🐱') , ('aves',['🐦','🦅']))
Del diccionario obtén y elimina el valor de la clave 'aves'
Modifica el valor de la clave 'gato' por '🐈'
Cambia la clave perro por perros y su valor por ['🐶','🐕']
"""
# Crea un diccionario con las siguientes tuplas de animales
tupla = (('perro', '🐶') , ('gato','🐱') , ('aves',['🐦','🦅']))
diccionario = dict(tupla)
print(diccionario)

#1 Del diccionario obtén y elimina el valor de la clave 'aves'
dato = diccionario.pop('aves')
print(dato," ",diccionario,'\n')

#2 Modifica el valor de la clave 'gato' por '🐈'
diccionario['gato'] = '🐈'
print(diccionario)

#3 Cambia la clave perro por perros y su valor por ['🐶','🐕']
diccionario['perros'] = ['🐶','🐕']
del diccionario['perro']
print(diccionario)