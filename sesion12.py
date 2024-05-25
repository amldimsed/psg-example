lista_frutas = ["🍊","🍋","🍅","🍓","🍑","🍏","🥦","🥭","🍋"]

cesta = ['papaya', 'sandia', 'pera', 'platano']
buscar = 'manzana'
if buscar in cesta:
    print('Existe', cesta.count(buscar), 'manzanas')
else:
    cesta.append(buscar)
    cesta.append(buscar)
    print(cesta)

cesta = ['🍑','🍓','🍉']
print (cesta)
resultado = f"Hay {cesta.count('🍎')} manzanas" if '🍎' in cesta else cesta.extend(['🍎','🍎'])
print (resultado)
print (cesta)

animal = {'especie':'🐶', 'nombre': 'Firulais', 'mamifero': True}
print (animal)
if animal.get('mamifero'): # animal['mamifero']
    print ("Es un mamífero")
else:
    print ("No es un mamífero")