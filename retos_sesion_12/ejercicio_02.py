print("""
        ------------------------------------
        ---    WEB....WEB...WEB...WEB    ---
        ------------------------------------

    """)

#registro en datos
password = "estas son las cosas q creo q son_por_defecto"
usu_nom = "miaunomas_por_defecto"
correo = "AmantesDeLaComida@DinoViejo.miau"

print("-----ELIJA UNA OPCION------")
print("1.- Iniciar Secion: ")
print("2.- Registrarse: ")

uno = input("introduzca un numero")
numero = int(float(uno))

if numero == 1:
    usuario = input("ingrese usuario o correo: ")
    clave = input("ingrese contraseña: ")

    if (usuario != "" and clave != ""): 
        if (clave == password and (usuario == usu_nom or usuario == correo)):
            print("CORRECTO")
        else:
            print("NO EXISTE EN REGISTRO")
    else:
        print("clave o contraseña vacio")

elif numero == 2:
    usu_nom = input("ingrese NUEVO usuario: ")
    correo = input("ingrese NUEVO correo: ")
    password = input("ingrese NUEVA contraseña: ")
    print("*************FIN*************")

    usuario = input("ingrese usuario o correo: ")
    clave = input("ingrese contraseña: ")

    if (usuario != "" and clave != ""): 
        if (clave == password and (usuario == usu_nom or usuario == correo)):
            print("CORRECTO")
        else:
            print("NO EXISTE EN REGISTRO")
    else:
        print("clave o contraseña vacio")

else:
   print("NUMERO INCORRECTO")