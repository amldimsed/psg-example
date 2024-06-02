
blanco = "#"
negro = "*"
n = 8
for i in range(n):
    for j in range(n):
        if j % 2 == 0:
            print(blanco, end=" ")
        else:
            print(negro, end=" ")
    print()
    aux = blanco
    blanco = negro
    negro = aux
    