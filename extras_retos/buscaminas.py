# Este codigo ha sido generado por el modulo psexport 20230113-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).

from random import randint

# En python no hay forma de elegir como pasar una variable a una
# funcion (por referencia o por valor). Las variables "inmutables"
# (str, int, float, bool) se pasan siempre por copia mientras que
# las demas (listas, objetos, etc.) se pasan siempre por referencia.
# Esto coincide con el comportamiento por defecto en pseint, pero
# cuando utiliza las palabras clave "Por Referencia" para
# alterarlo la traduccion no es correcta.

# ################################################################################
# Funci�n max: Funci�n auxiliar que calcula el m�ximo de dos n�meros
# ################################################################################
def max(num1, num2):
	num = int()
	if num1>num2:
		num = num1
	else:
		num = num2
	return num

# ################################################################################
# Funci�n min: Funci�n auxiliar que calcula el m�nimo de dos n�meros
# ################################################################################
def min(num1, num2):
	num = int()
	if num1<num2:
		num = num1
	else:
		num = num2
	return num

# ################################################################################
# Funci�n IncializarTablero: Funci�n que recibe las dos talbas: tablero, visible
# Incializa tablero con valores 0
# Incializa visible con valores Falso, indicando que est�n ocultas
# ################################################################################
def inicializartablero(tablero, visible):
	fila = int()
	colum = int()
	# Incializo el tablero con valor 0
	for fila in range(0,10):
		for colum in range(0,10):
			tablero[fila-1][colum-1] = 0
	ponerminas(tablero)
	# Incializo la tabla visible a falso indicando que ninguna celda est� descubierta
	for fila in range(0,10):
		for colum in range(0,10):
			visible[fila-1][colum-1] = False

# ################################################################################
# Funci�n PonerMinas: Funci�n que recibe el tablero (tabla 10x10) por referencia
# Genera 10 posiciones de la tabla e incializa esas posiciones con minas (valor 9)
# Debe asegurar que se ponen 10 minas.
# Cada vez que se pone una mina se incrementa en 1 el valor de las celdas vecinas,
# si no son una mina
# ################################################################################
def ponerminas(tablero):
	num_minas = int()
	fila = int()
	colum = int()
	fila2 = int()
	colum2 = int()
	num_minas = 0
	# Vamos a poner 10 minas en el tablero
	while num_minas<10:
		# Me aseguro que no haya ya una mina en la posici�n que se genera aleatoriamente
		while True:# no hay 'repetir' en python
			fila = randint(0,9)
			colum = randint(0,9)
			if tablero[fila-1][colum-1]!=9: break
		# Reperesentamos la mina con el n�mero 9
		tablero[fila-1][colum-1] = 9
		# Ahora incremento el n�mero de minas cercanas en las casillas vecinas
		for fila2 in range(max(0, fila-1),min(9, fila+1)+1):
			for colum2 in range(max(0, colum-1),min(9, colum+1)+1):
				if tablero[fila2-1][colum2-1]!=9:
					tablero[fila2-1][colum2-1] = tablero[fila2-1][colum2-1]+1
		num_minas = num_minas+1

# ################################################################################
# Funci�n DestaparCelda: Funcion que recibe por referencia las dos tablas y la
# fila y columna que se debe destapar.
# Si es una casilla que se puede destapar (la posici�n de la tabla visible es Falso)
# Se destapa (posici�n de la tabla visible a Verdadero)
# Si no hay minas cerca tengo que intentar destapar las vecinas
# Si la celda vecina no es una mina, la destapo
# Funci�n recursiva
# ################################################################################
def destaparcelda(tablero, visible, fila, colum):
	fila2 = int()
	colum2 = int()
	# Si es una casilla que se puede destapar
	if visible[fila-1][colum-1]==False:
		visible[fila-1][colum-1] = True
		# Si no hay minas cerca tengo que intentar destapar las vecinas
		if tablero[fila-1][colum-1]==0:
			for fila2 in range(max(0, fila-1),min(9, fila+1)+1):
				for colum2 in range(max(0, colum-1),min(9, colum+1)+1):
					if tablero[fila2-1][colum2-1]!=9:
						destaparcelda(tablero, visible, fila2, colum2)

# ################################################################################
# Funci�n ContarCeldasDestapadas: Funcion que recibe la tabla visible
# Recorre la tabla y cuenta los valores Verdaderos, este valor se devuelve
# Si el contador es 90 significa que hemos destapado todas las casillas: hemos ganado
# ################################################################################
def contarceldasdestapadas(visible):
	num = int()
	fila = int()
	colum = int()
	num = 0
	for fila in range(0,10):
		for colum in range(0,10):
			if visible[fila-1][colum-1]:
				num = num+1
	return num

# ################################################################################
# Funci�n ComprobarTablero: Funcion que recibe por referencia las dos tablas y la
# fila y columna que se debe destapar.
# Si la posici�n a destapar es una mina (=9) devuelve -1 (hemos perdido)
# SiNo destapo la casilla correspondiente y cuento las casillas detapadas y se devuelve
# ################################################################################
def comprobartablero(tablero, visible, fila, colum):
	resultado = int()
	# Si es una mina devuelvo -1
	if tablero[fila-1][colum-1]==9:
		# Destapo la celda con la mina
		visible[fila-1][colum-1] = True
		resultado = -1
	else:
		destaparcelda(tablero, visible, fila, colum)
		resultado = contarceldasdestapadas(visible)
	return resultado

# ################################################################################
# Funci�n EscribirTablero: Funcion que las dos tablas 
# Recorre las tablas y las muestras en pantalla
# Dependiendo del valor de cada posici�n de la tabla visible, muestra la posici�n
# de la tabla resultado.
# Si la posici�n est� destapada (verdadero):
# Si no tiene minas alrededor (valor 0) muestra un hueco
# Si es una mina, muestro un *
# SiNo muetro el valor de la casilla (indica cuantas minas tiene alrededor)
# SiNo la posici�n no es visible y muestro un #
# ################################################################################
def escribirtablero(tablero, visible):
	fila = int()
	colum = int()
	titfilas = str()
	titcolum = str()
	titfilas = "0123456789"
	titcolum = "    0 1 2 3 4 5 6 7 8 9"
	print(titcolum)
	print("")
	# Recorro las tablas
	for fila in range(0,10):
		print(titfilas[fila-1:fila],"   ", end="")
		for colum in range(0,10):
			# Si la celda es visible (est� destapada)
			if visible[fila-1][colum-1]:
				# Celda que no tiene minas alrededor
				if tablero[fila-1][colum-1]==0:
					print("  ", end="")
				else:
					# Es una mina
					if tablero[fila-1][colum-1]==9:
						print("* ", end="")
						# Muestro el n�mero de minas que hay en los vecinos	
					else:
						print(tablero[fila-1][colum-1]," ", end="")
				# La casilla no es visible
			else:
				print("# ", end="")
		print("")

# ################################################################################
# Programa BuscaMina
# Incilizo las tablas: tablero y visible
# Se repite:
# Mostrar el tablero
# Pedir fila y columna de casilla a destapar
# Comprobar tablero
# Hasta que la comprobaci�n = -1 (has perdido hay una mina)
# O hasta que haya destapada todas las casillas (Has ganado)
# ################################################################################
if __name__ == '__main__':
	tablero = int()
	fila = int()
	colum = int()
	resultado = int()
	tablero = [[int() for ind0 in range(10)] for ind1 in range(10)]
	visible = bool()
	visible = [[bool() for ind0 in range(10)] for ind1 in range(10)]
	inicializartablero(tablero, visible)
	while True:# no hay 'repetir' en python
		escribirtablero(tablero, visible)
		# Pedir fila y columna de casilla a destapar
		while True:# no hay 'repetir' en python
			print("Indica fila:", end="")
			fila = int(input())
			if fila>=0 and fila<=9: break
		while True:# no hay 'repetir' en python
			print("Indica columna:", end="")
			colum = int(input())
			if colum>=0 and colum<=9: break
		# Comprobamos el tablero
		resultado = comprobartablero(tablero, visible, fila, colum)
		print("") # no hay forma directa de borrar la pantalla con Python estandar
		if resultado==-1 or resultado==90: break
	escribirtablero(tablero, visible)
	# Has destapado una mina
	if resultado==-1:
		print("Has pisado una mina!!!!!")
		print("GAME OVER")
		# has destapado todas las casillas
	else:
		print("YOU ARE THE PLAYER ONE!!!")

