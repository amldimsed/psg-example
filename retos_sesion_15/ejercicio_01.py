def imprimir(dato1:float, dato2:float, resultado:float, ope:str):
    print("    ",dato1)
    print("  ", ope, dato2)
    print("-------------")
    print("   %.3f"%resultado)

while True:
    try:
        num1 = input("Ingrese el primer número: ")
        if num1 == "salir":
            break
        num2 = input("Ingrese el segundo número: ")
        if num2 == "salir":
            break
        num3 = input("Ingrese el operdaor: ")
        if num3 == "salir":
            break

        dato1 = float(num1)
        dato2 = float(num2)
        if num3 == "+":
            resultado = dato1 + dato2
            imprimir(dato1, dato2, resultado, "+")
        elif num3 == "-":
            resultado = dato1 - dato2
            imprimir(dato1, dato2, resultado, "-")
        elif num3 == "*":
            resultado = dato1 * dato2
            imprimir(dato1, dato2, resultado, "*")
        elif num3 == "/":
            resultado = dato1 / dato2
            imprimir(dato1, dato2, resultado, "/")
        else:
            print("operador incorrecto")
    except ZeroDivisionError as e:
        print("0️⃣ Error:", e)
    except Exception as e:
        print("💀 Error:", e)
        