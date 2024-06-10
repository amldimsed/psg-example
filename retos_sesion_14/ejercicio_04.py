"""
(A = π r²)
"""
import math

circulo = lambda radio: math.pi * radio ** 2

n = 4
area = circulo(n)
print(f"Area de un circulo cor radio = {n}: A = " "%.3f" %area)