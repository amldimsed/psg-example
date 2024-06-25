"""
Desafio propuesto por ******MOUREDEV....

"""

import keyboard

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

    rotaciones = 0
    #movimientos a realizar por teclado
    #uso de flechas del alfanumerico, barra espacio rotar y esc para salir
    while(True):
        evento = keyboard.read_event()
        if evento.name == "esc":
            break
        #una sola pulsacion y no dos veces solo abajo la tecla
        elif evento.event_type == keyboard.KEY_DOWN:
            if evento.name == "down":
                (pantalla, rotaciones) = movimiento(pantalla, "down", rotaciones)
            elif evento.name == "right":
                (pantalla, rotaciones) = movimiento(pantalla, "right", rotaciones)
            elif evento.name == "left":
                (pantalla, rotaciones) = movimiento(pantalla, "left", rotaciones)
            elif evento.name == "space":
                (pantalla, rotaciones) = movimiento(pantalla, "rotate", rotaciones)

 
def movimiento(pantalla:list, tipo_movent:str, rotaciones:int) -> (list, int):
    """
    Tipo de movimiento.
    pantalla: matriz inicial
    """
    #crea una nueva pantalla al inicio
    new_pantalla = [["🥦"]*10 for i in range(12)]

    rotacion_item = 0
    rotacion = [[(1, 1), (0, 0), (-2, 0),(-1, -1)],
                [(0, 1), (-1, 0), (0, -1),(1, -2)],
                [(0, 2), (1, 1), (-1, 1),(-2, 0)],
                [(0, 1), (1, 0), (2, -1),(1, -2)]]
    
    new_rotaciones = rotaciones
    if tipo_movent == "rotate":
        new_rotaciones = 0 if rotaciones == 3 else rotaciones + 1
    
    

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
                    new_row_index = row_index + rotacion[new_rotaciones][rotacion_item][0]
                    new_column_index = column_index + rotacion[new_rotaciones][rotacion_item][1]
                    rotacion_item += 1

                #limites del bloque para q no salga del margen
                if new_row_index > 11 or new_column_index < 0 or new_column_index >9:
                    print("No se puede mover\n")
                    return (pantalla, rotaciones)
                else:
                    new_pantalla[new_row_index][new_column_index] =  "🍲"

    imprimir_pantalla(new_pantalla)
    return (new_pantalla, new_rotaciones)

    
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
