Anita = {'Sushi', 'Pizza', 'Tacos', 'Hamburguesa', 'Pasta', 'Alitas'}
Pepito = {'Pizza', 'Tacos', 'Ensalada', 'Pasta', 'Helado', 'Milanesa'}

#calculo del porcentaje
#percentage calculation
"""
100% ------total
X%   ------total_comun
X = (100% * total_comun)total
"""

total = len(Anita) + len(Pepito) #100%
comun = Anita.intersection(Pepito)
total_comun = len(comun)
x = (100 * total_comun)/total

"""
Si la cantidad platos de comida que tienen 
en comunes mayor a 50% entonces ambos seguirán saliendo
"""

print("platos en comun: ",comun)
print(x,"%", "si sale, siguen saliendo" if x > 50 else "no salen mas, triste realidad")
