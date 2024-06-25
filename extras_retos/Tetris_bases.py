"""
Desafio propuesto por ******MOUREDEV....
falta rotacion....no hay tiempito...
"""

def tetris():

    pantalla = [["🍲","🥦","🥦","🥦","🥦","🥦","🥦","🥦","🥦","🥦",],
                ["🍲","🍲","🍲","🥦","🥦","🥦","🥦","🥦","🥦","🥦",],
                ["🥦","🥦","🥦","🥦","🥦","🥦","🥦","🥦","🥦","🥦",],
                ["🥦","🥦","🥦","🥦","🥦","🥦","🥦","🥦","🥦","🥦",],
                ["🥦","🥦","🥦","🥦","🥦","🥦","🥦","🥦","🥦","🥦",],
                ["🥦","🥦","🥦","🥦","🥦","🥦","🥦","🥦","🥦","🥦",],
                ["🥦","🥦","🥦","🥦","🥦","🥦","🥦","🥦","🥦","🥦",],
                ["🥦","🥦","🥦","🥦","🥦","🥦","🥦","🥦","🥦","🥦",],
                ["🥦","🥦","🥦","🥦","🥦","🥦","🥦","🥦","🥦","🥦",],
                ["🥦","🥦","🥦","🥦","🥦","🥦","🥦","🥦","🥦","🥦",],
                ["🥦","🥦","🥦","🥦","🥦","🥦","🥦","🥦","🥦","🥦",],
                ["🥦","🥦","🥦","🥦","🥦","🥦","🥦","🥦","🥦","🥦",]]
    imprimir_pantalla(pantalla)

    #movimientos a realizar
    pantalla = movimiento(pantalla, "down")
    pantalla = movimiento(pantalla, "down")
    pantalla = movimiento(pantalla, "down")
    pantalla = movimiento(pantalla, "left")
    pantalla = movimiento(pantalla, "right")
    pantalla = movimiento(pantalla, "right")
    pantalla = movimiento(pantalla, "right")
    pantalla = movimiento(pantalla, "left")

def movimiento(pantalla:list, tipo_movent:str) -> list:
    """
    Tipo de movimiento.
    pantalla: matriz inicial
    """
    #crea una nueva pantalla al inicio
    new_pantalla = [["🥦"]*10 for i in range(12)]

    #recorre toda la matriz hasta encontrar un cubo o forma y procede a mover    
    for row_index, row in enumerate(pantalla):
        for column_index, column in enumerate(row):

            #pregunta por columna si existe bloque 🍲
            if column == "🍲":
                #nueva posicion
                new_row_index = 0
                new_column_index = 0
                
                #mover abajo
                if tipo_movent == "down":
                    new_row_index = row_index + 1
                    new_column_index = column_index
                #mover izquierda
                elif tipo_movent == "left":
                    new_row_index = row_index
                    new_column_index = column_index - 1
                #mover derecha
                elif tipo_movent == "right":
                    new_row_index = row_index
                    new_column_index = column_index + 1
                #todavia falta
                elif tipo_movent == "rotate":
                    break
                #limites del bloque para q no salga del margen
                if new_row_index > 9 or new_column_index < 0 or new_column_index >9:
                    print("No se puede mover\n")
                    return pantalla
                else:
                    new_pantalla[new_row_index][new_column_index] =  "🍲"

    imprimir_pantalla(new_pantalla)
    return new_pantalla

    
def imprimir_pantalla(pantalla:list):
    """
    imprimir pantalla de la matriz
    """
    print("\nPantalla tetris\n")
    for row in pantalla:
       #un recorido por lista y agrupar con join, uso de map
        print("".join(map(str,row)))

#inicio del tetriz
tetris()
