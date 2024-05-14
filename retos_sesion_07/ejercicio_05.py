#Anita lava la Tina
letra = input("palindromo al revez, ingrese frase: ")
letra = letra.lower().replace(" ", "")
aux = letra[::-1].replace(" ", "")
print(letra == aux, aux, " ", letra)
