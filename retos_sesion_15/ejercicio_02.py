"""
Crear un programa para crear una canasta de frutas, 
solicitar frutas por teclado y almacenar en una lista, 
si se ingresa "salir" termina la ejecución. 
Solo se permiten las siguientes frutas caso contrario 
lanzar una excepción personalizada
🍅🍇🍈🍉🍊🍌🍍🍑
"""
class ErrorFrutas(Exception):
    pass

frutas = list()
while True:
    try:
        frut = str(input("Inser una fruta: "))
        if frut == "salir":
            break
        if frut == "🍅" or frut == "🍇" \
            or frut == "🍈" or frut == "🍉" \
            or frut == "🍊" or frut == "🍌" \
            or frut == "🍍" or frut == "🍑":
            raise ErrorFrutas("estas son las cosas q creo q son")
        else:
            frutas.append(frut)
    except ErrorFrutas as e:
        print("🚫 Error:", e)
    #except Exception as e:
        #print("💀 Error en todo:", e)
    #else:
        #print("🎉 Error de palabra")
    finally:
        print("Lista: ",frutas)
    
    

    

        
        