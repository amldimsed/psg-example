# Eres NOE y tienes que guardar dos animales de cada especie en un arca, 
# crea un diccionario con las especies

arca = {"perro" : 2, "gato" : 2, "tigre" : 2, "mono" : 2, "unicornio" : 0, "jirafa" : 1}

#1 Añade al arca 2 especies más usando update()
arca.update(raton = 2, lorito = 2)
print(arca,"\n")

#2 Toma lista de los animales en el arca iterando el diccionario

arca_dic = arca.copy()
iterador = arca_dic.items()
lista = list(iterador)
print(lista,"\n")

#3 Existe en el arca la especie 'dragon'?
dato = arca.get('dragon')

dato == None and print('No, no existe dragon\n')
dato != None and print(f'Existe {dato}\n')

#4 Elimina la especie 'unicornio' del arca
del arca["unicornio"]
print(arca,'\n')

#5 Modifica el valor de la especie 'jirafa' por 2
arca["jirafa"] = 2
print(arca,'\n')

#6 Vacía el arca después del diluvio
arca.clear()
print(arca)
