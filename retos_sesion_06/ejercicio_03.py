print("""
    Una puerta tiene dos interruptores
    que controlan dos luces la puerta sólo debe 
    abrirse cuando las dos luces están apagadas o las 
    dos están encendidas, caso contrario la puerta no 
    se abre, ¿qué operador lógico se puede utilizar
    """)

print("R: XNOR ==> "," (A * B) + (¬A * ¬B) = A ⊕ B")
print("luz1,luz2 ==> apagado = False; prendido = True")
print("puerta ==> cerrado = False; abierto = True")
luz1 = False
luz2 = False
puerta_val = (luz1 and luz2) or (not luz1 and not luz2)
print("luz1 = ",luz1, "y ","luz2 = ", luz2, " ==> ","puerta =", puerta_val)
luz1 = False
luz2 = True
puerta_val = (luz1 and luz2) or (not luz1 and not luz2)
print("luz1 = ",luz1, "y ","luz2 = ", luz2, " ==> ","puerta =", puerta_val)
luz1 = True
luz2 = False
puerta_val = (luz1 and luz2) or (not luz1 and not luz2)
print("luz1 = ",luz1, "y ","luz2 = ", luz2, " ==> ","puerta =", puerta_val)
luz1 = True
luz2 = True
puerta_val = (luz1 and luz2) or (not luz1 and not luz2)
print("luz1 = ",luz1, "y ","luz2 = ", luz2, " ==> ","puerta =", puerta_val)
