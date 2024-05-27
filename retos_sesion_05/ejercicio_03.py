
dia:int
hora:int
minuto:int
rest_hora:int
rest_min:int
rest_seg:int

minuto = 288325 // 60
rest_seg = 288325 % 60
hora = minuto // 60
rest_min = minuto % 60
dia = hora // 24
rest_hora = hora % 24
print("son ", dia, "dias", rest_hora, "horas", rest_min, "minutos", rest_seg, "segundos")