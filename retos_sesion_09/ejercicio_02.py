lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

sublist = lista.copy()
sublist.reverse()
sublist = sublist[3::3]

print(sublist, lista)