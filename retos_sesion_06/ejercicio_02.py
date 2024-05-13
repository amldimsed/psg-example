# XNOR
# (A * B) + (¬A * ¬B) = A ⊕ B

a = False
b = False
print((a and b) or (not a and not b) )
a = False
b = True
print((a and b) or (not a and not b) )
a = True
b = False
print((a and b) or (not a and not b) )
a = True
b = True
print((a and b) or (not a and not b) )