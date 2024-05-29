
count = 1
numer = 2
valor = True
n = 20
while count <= n:
# el rango es 2 y menos el propio
# entonces todo es distinto a cero es primo pero si es igual a 0 en residuo deja de ser primo
    for i in range(2,numer):
# entra por verdad y termina el bucle, valor cambia a falso        
        if numer % i == 0:
            valor = False
            break
    if valor:
        print(numer, end=", ")
        count += 1
    else:
        #count -= 1
        valor = True
    numer += 1

        