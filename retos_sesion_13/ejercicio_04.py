#Anita lava la Tina
while(True):
    palabra = str(input("ingrese palabra: "))
    if palabra.lower() == "salir":
        break

    pal_unido = palabra.lower().replace(" ","")
    pal_revez = pal_unido[::-1]

    if pal_unido == pal_revez:
        print("ES PALINDROMO:")
        print("palabra: ", pal_unido)
        print("palabra al revez: ", pal_revez)
    else:
        print("NO ES PALINDROMO")

