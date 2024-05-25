"""
Crea un diccionario para almacenar información de comidas de animales por ejemplo
comidas = {"carne" : {"animales": ["león", "tigre"]}, "frutas" : {"animales": ["mono", "elefante"]}}
Añade al diccionario de comidas 4 alimentos más usando update(clave=valor)
Existe en el diccionario de comidas la comida 'carne'?
Elimina la comida 'frutas' del diccionario de comidas
"""
comidas = {"carne" : {"animales": ["león", "tigre"]}, "frutas" : {"animales": ["mono", "elefante"]}}
print(comidas)

#1 Añade al diccionario de comidas 4 alimentos más usando update(clave=valor)
comidas.update(plantas = {'animales':['coala','kapibara']},insectos = {'animales':['tarantula','escorpion']},miel = {'animales':['abejas','oso']},croquetas = {'mascota':['croquetas','arroz con pollito']})
print(comidas,'\n')

#2 Existe en el diccionario de comidas la comida 'carne'?
existe = comidas.get("carne")

existe != None and print(existe,'\n\n') 
existe == None and print("no existe",'\n\n')

#3 Elimina la comida 'frutas' del diccionario de comidas

dato = comidas.pop('frutas')
print(dato, ' ', comidas)
