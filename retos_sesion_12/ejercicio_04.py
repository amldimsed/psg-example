"""
Una tienda ofrece descuentos a sus clientes, 
si el cliente es mayor de edad y tiene una compra mayor a 1000, 
se le aplica un descuento del 10%, 
si es menor de edad y tiene una compra mayor a 500 se le aplica un descuento del 5%, 
si no cumple ninguna condición se le aplica un descuento del 2%
"""
dato_comp = input("ingrese total compra: ")
dato_edad = input("ingrese edad: ")

compra = int(float(dato_comp))
edad = int(float(dato_edad))

"""
compra----->100%
x   ----->10%
x = compra*10%/100
total = compra - x

"""

if edad >= 60 and compra >= 1000:
    x = (compra*10)/100
    descuento = compra - x
    print("total a pagar con descuento 10%: ", descuento)
elif edad < 60 and compra >= 500:
    x = (compra*5)/100
    descuento = compra - x
    print("total a pagar con descuento 5%: ", descuento)
else:
    x = (compra*2)/100
    descuento = compra - x
    print("total a pagar con descuento 2%: ", descuento)