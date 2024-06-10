"""
Un estudiante desea saber cuál es su promedio de calificaciones en la 
materia de matemáticas, cree una función que reciba las calificaciones 
como lista y devuelva el promedio las calificaciones son 20,40,60,51,13
"""
def promedio(lista):
    """
    promedio, suma total y div cantidad
    """
    total = sum(lista)/len(lista)
    print(total)

notas = [20, 40, 60, 51, 13]
promedio("promedio: ", notas, " XD como en la vida real primera vez")
