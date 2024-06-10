"""
Crear una función que reciba una cadena y devuelva la cadena invertida
"""

def invertir(p):
    """
    invierte la palabra
    """
    inv = ""
    inv = p[::-1]  
    return inv

def invertir2(p:list):
    """
    invierte el orden de palabra
    estas son las cosas que creo q son
    son q creo que cosas las son estas
    """
    inv = ""
    aux_palabra = ""
    
    for i in range(len(p)):
        if p[i] != " ":
            aux_palabra += p[i]
        else:
            inv = " " + aux_palabra + inv
            aux_palabra = ""
    inv = aux_palabra + inv
    return inv


palabra = str(input("ingrese una palabra: "))

print(invertir(palabra))
print(invertir2(palabra))