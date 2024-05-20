#Cada uno quiere saber en que parte del mundo ha estado 
#el otro que el no haya visitado

mochilero_a = {"París", "Londres", "Nueva York", "Tokio",
               "Peru", "Chile", "Colombia", "Bolivia"}

mochilero_b = {"Londres", "Roma", "Nueva York", "Sidney",
               "Argentina","Brasil","Panama","Bolivia"}

para_a = mochilero_a.difference(mochilero_b)
para_b = mochilero_b.difference(mochilero_a)

#b no esta en a
#a no esta en b

B_No_Visito = para_a.copy()
A_No_Visito = para_b.copy()

print("mochilero_B no visito de mochilero_A: ", B_No_Visito)
print("mochilero_A no visito de mochilero_B: ", A_No_Visito)