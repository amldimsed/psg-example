
valor = True
while True:
    # si me equivoco y es con decimales.....
    numero = int(float(input("ingrese numero: ")))
    if numero == 0:
        break
    if numero != 1 and numero != 2:
        for dato in range(2, numero):
            if numero % dato == 0:
                valor = False
                divisible = dato
                break
        if valor:
            print(numero, " :ES PRIMO")
        else:
            print(numero, " :NO ES PRIMO, es divisible por -> ", divisible, " resto 0")
        valor = True
    else:
        print("Es primo si contamos el ",numero)

