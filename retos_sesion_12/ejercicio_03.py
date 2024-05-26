JhonDoe = {'Alice', 'Bob', 'Charlie', 'David', 'Eve'}
JessDoe = {'Alice', 'Bob',  'Frank', 'Grace'}

amigos_comun = JhonDoe.intersection(JessDoe)
print(amigos_comun)

if amigos_comun:
    print("Si hay conocidos: ",amigos_comun)
else:
    print("No hay amigos en comun")
    