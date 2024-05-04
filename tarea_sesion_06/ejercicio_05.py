print("""
    Comparar los números 123 y 890, comprobar si tienen 
    la misma paridad ambos pares o ambos impares
    """)
a = 123 % 2 == 0
b = 890 % 2 == 0

print("123 == ", a," and ", " 890 == ", b, " ==> ", a == b )

# xd if disfrazado, acortador
a == b and print("ambos numeros cumplen la paridad")
a != b and print("no cumplen la paridad")
