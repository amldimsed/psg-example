"""
Simular un tres en raya con funciones donde reciba las jugadas 
y devuelva el ganador hasta que alguien ingrese salir
"""
"""
00, 01, 02
10, 11, 12
20, 21, 22
"""

matriz = [["H", "H", "H"],
          ["H", "H", "H"],
          ["H", "H", "H"]]


def ganador(simbolo:str):
    """
    Existe una condicion de ganador, fila y columna en linea recta
    """
    if matriz[0][0] == simbolo and matriz[0][1] == simbolo and \
        matriz[0][2] == simbolo:
        return True 
    elif matriz[1][0] == simbolo and matriz[1][1] == simbolo and \
        matriz[1][2] == simbolo:
        return True
    elif matriz[2][0] == simbolo and matriz[2][1] == simbolo and \
        matriz[2][2] == simbolo:
        return True
    elif matriz[0][0] == simbolo and matriz[1][0] == simbolo and \
        matriz[2][0] == simbolo:
        return True
    elif matriz[0][1] == simbolo and matriz[1][1] == simbolo and \
        matriz[2][1] == simbolo:
        return True
    elif matriz[0][2] == simbolo and matriz[1][2] == simbolo and \
        matriz[2][2] == simbolo:
        return True
    elif matriz[0][0] == simbolo and matriz[1][1] == simbolo and \
        matriz[2][2] == simbolo:
        return True
    elif matriz[0][2] == simbolo and matriz[1][1] == simbolo and \
        matriz[2][0] == simbolo:
        return True
    else:
        return False

def casilla_ocupada(fila:int, columna:int):
    """
    verifica si hay casilla vacia representado por una H
    """
    if matriz[fila][columna] != "H":
        return True
    else:
        return False

def ingrese(dato:str):
    """
    Se coloca fila y columna, si esta ocupado sigue preguntando
    hasta q sea una casilla vacia
    """
    while True:
        fila = int(input("ingrese fila entre 0 y 2: "))
        columna = int(input("ingrese columna entre 0 y 2: "))
        if casilla_ocupada(fila, columna):
            print("casilla ocupada ingrese otros datos")
        else:
            matriz[fila][columna] = dato
            break

def mostrar():
    """
    muetra toda la matriz y los cambios
    """
    for i in range(3):
        for j in range(3):
            print(matriz[i][j], end=", ")
        print()
      
      
def jugando():
    #Para 9 turnos del 1 al 9
    contador = 1
    #Muestra en la primera casilla vacia representado con H
    mostrar()
    #9 turnos obligados
    while contador <= 9:
        #para salir
        dato = str(input("ingrese simbolo: "))
        if dato == "salir":
            break
        #Intercambia entre 1 y 0 obligado empieza con o y luego x
        if contador % 2 == 0:
            if dato == "x":
                print("turno de x")
                ingrese("x")
                mostrar()
                if ganador("x"):
                    print("GANADOR X")
                    break
                else:
                    contador += 1
            else:
                print("no es turno de 0, coloque x")

        if contador % 2 == 1:
            if dato == "o":
                print("turno de o")
                ingrese("o")
                mostrar()
                if ganador("o"):
                    print("GANADOR O")
                    break
                else:
                    contador += 1
            else:
                print("no es turno de x, coloque o") 

               
#Inicio
jugando()    

