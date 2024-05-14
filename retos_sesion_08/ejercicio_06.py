x1 = input("valor X1: ")
y1 = input("valor Y1: ")

x2 = input("valor X2: ")
y2 = input("valor Y2: ")

aux = list()
numX1 = float(x1)
numY1 = float(y1)
numX2 = float(x2)
numY2 = float(y2)

#no se puede convertir y adicionar a una tupla un string a numero xd
aux.append(numX1)
aux.append(numY1)
X1Y1 = tuple(aux)
aux.clear()
aux.append(numX2)
aux.append(numY2)
X2Y2 = tuple(aux)

#punto medio
#M = ((x1+x2)/2 + (y1+y2)/2)

Mx = (X1Y1[0] + X2Y2[0])/2
My = (X1Y1[1] + X2Y2[1])/2
Mtotal = (Mx + My) 


print(X1Y1,X2Y2,sum(X2Y2))
print("Punto Medio: ", Mx, ",", My, " M total: ", Mtotal)