# initialize variables
a, b = 0, 1

# the loop range 20
for i in range(20):
    print(a, end="-")
    # calculate the variable and save for next
    aux = a + b
    a = b
    b = aux