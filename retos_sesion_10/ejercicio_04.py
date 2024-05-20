#Ahora quieren saber en que ciudades 
#han estado ambos mochileros

mochilero_a = {"París", "Londres", "Nueva York", "Tokio",
               "Peru", "Chile", "Colombia", "Bolivia"}

mochilero_b = {"Londres", "Roma", "Nueva York", "Sidney",
               "Argentina","Brasil","Panama","Bolivia"}

ambos = mochilero_a.intersection(mochilero_b)

print("ambos visitaron: ",ambos)