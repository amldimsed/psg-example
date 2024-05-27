productos = ["leche", "pan", "huevo", "chocolate", "miel"]
precio = [5.50, 0.50, 1.0, 15.0, 57.0]

#Agregar 5 productos nuevos al final de las listas
nuevo_prod = ["galletas", "aceite", "te", "fideos", "dulce de leche"]
nuevo_prec = [5.50, 16.0, 2.50, 4.50, 18.0]

productos.extend(nuevo_prod)
precio.extend(nuevo_prec)

print(productos)
print(precio)

#Eliminar el producto con el nombre "Leche" de las listas
x = "Leche".lower()

indice = productos.index(x)

productos.pop(indice)
precio.pop(indice)

print(productos)
print(precio)

#¿Cuanto cuesta el producto "Pan" y "Huevo"?
px = "Pan".lower()
py = "Huevo".lower()

indice_px = productos.index(px)
indice_py = productos.index(py)

print("el pancito: ", precio[indice_px], "ctvs\n", "el huevo: ", precio[indice_py], "Bs")

#¿Cual es el producto más caro y más barato?
prod = productos.copy()
prec = precio.copy()

prec.sort()

min_precio = prec[0]
max_precio = prec[len(prod)-1]

min_indice = precio.index(min_precio)
max_indice = precio.index(max_precio)

print("mas barato: ", productos[min_indice], " ", min_precio, "ctvs")
print("mas caro: ", productos[max_indice], " ",max_precio, "Bs")

#¿Cuántos productos tienes en total?
print("menos uno eliminado: ",len(prod), " productos")

#¿Cuanto cuesta el total de los productos?
print("total menos uno eliminado: ", sum(precio), "Bs")

#Ordena los productos alfabéticamente y precios si es posible
# 9.4. Una opcion para ordenar alfabeticamente es hacer una copia y 
# ordenarla despues buscar los indices y con eso reordenar los precios,
# si seria limitada al tamaño de la lista, muchas veces es bueno 
# concentrarse en lo que se te 
# pide y no pensar en N casos xq puede ser mas facil de lo que creemos

# no, no se puede es bien tedioso, no vivo sin los bucles
# me volvi al final cheems no mas, .....estoy cansado jefe.......

# Copia del inicio, productos y precios
#*************METODO INSERT SHORT****************
orden_producto = productos.copy()
orden_precios = precio.copy()
for i in range(1, len(prod)):
    insert_sort_prod = orden_producto[i]
    insert_sort_prec = orden_precios[i]
    # guardamos en j el indice de elemento anterior
    j = i - 1
    # movemos todos los elementos de la lista hacia delante
    # si son mayores que el elemto a insertar
    while j >= 0 and orden_producto[j] > insert_sort_prod:
        # ambos son del mismo tamaño precio y producto
        orden_producto[j + 1] = orden_producto[j]
        orden_precios[j + 1] = orden_precios[j]
        j -= 1
    # insertamos el elemto ambos
    orden_producto[j + 1] = insert_sort_prod
    orden_precios[j + 1] = insert_sort_prec

#prod.sort()
print(orden_producto)
print(orden_precios)

#Eliminar todos los productos de las listas
prod.clear()
prec.clear()
print("todo eliminado: ", "productos: ", prod, "precios: ", prec)


