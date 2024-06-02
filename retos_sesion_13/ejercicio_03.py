estudiantes = [('Juan', 51), ('Pedro', 80), ('Maria', 90), 
               ('Ana', 40), ('Luis', 30)]

for i in range(len(estudiantes)):
    nota = estudiantes[i][1] 
    if nota >= 51:
        print(nota, "felicitaciones aprobacion")