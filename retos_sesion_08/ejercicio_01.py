#no hay adicionar tupla si no por vector
x = input("valor X: ")
y = input("valor Y: ")
ubicacion = input("ubicacion: ")

a = list()
a.append(x)
a.append(y)
a.append(ubicacion)

tupla = tuple(a)

print(tupla)