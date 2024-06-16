"""
Simular un cajero automático que solicite un monto a retirar,
si el monto es mayor al saldo lanzar una excepción
personalizada y si el monto es mayor a 1000 lanzar
una excepción genérica
"""
class cantidad_retiro(Exception):
    pass
capacidad = 1000.0
saldo = 850.0
monto = 0.0

while True:
    try:
        mont = str(input("Introduce un monto o salir: "))
        if mont == "salir":
            break
        if float(mont) <= saldo and float(mont) < capacidad:
            saldo -= float(mont)
        elif float(mont) >= capacidad:
            raise Exception
        else:
            raise cantidad_retiro("no tienes saldo suficien, eres pobre:")
    except cantidad_retiro as e:
        print("🙀😿 Efectivo Bajo", e)
    except Exception as e:
        print("👀🧠 el cajero no dispone de suficiente cantidad", e)
    finally:
        print("saldo total: ", saldo)


