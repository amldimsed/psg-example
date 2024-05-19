productos = ["leche","pan","huevo","chocolate","miel"]
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
#se podria si se haria manualmente, para ambos se puede, lo haria pero un poquito me olvide y repasar el sueño me vence y no me deja
#una razon mas por q no es bueno hacer con metodos propios del lenguaje, igual me paso para un jueguito en c++ con unreal y otros
prod.sort()
print(prod)

#Eliminar todos los productos de las listas
prod.clear()
prec.clear()
print("todo eliminado: ", "productos: ", prod, "precios: ", prec)


