lista = ["jorge","juan","lopez","carlos","perez","pablo","luis","karmen","julio","pedro"]
lista2 = lista.copy()

#Obtener una sub lista de 2 a 7
lista2 = lista2[2-1:8-1]
print(lista2)

#Buscar si existe el nombre "Jhon" en la lista original
x = "Jhon"
nombre = lista.count(x.lower())
print(nombre != 0)

lista.append(x.lower())
nombre = lista.count(x.lower())
print(nombre != 0)

#Ordenar la sub lista alfabéticamente
lista2.sort()
print("lista ordenada de menor a mayor por las iniciales\n", lista2)

#Ordenar la lista original alfabéticamente de forma descendente
lista.sort(reverse = True)
print("lista ordenada de mayor a menor por las iniciales\n", lista)