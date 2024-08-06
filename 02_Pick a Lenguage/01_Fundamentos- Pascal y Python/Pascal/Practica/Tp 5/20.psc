Algoritmo sin_titulo
	Definir n Como Entero
	cant = 0
	suma = 0
	Escribir "Ingrese una lista de enteros y coloque # cuando finalice"
	Repetir
		Leer n
		suma = suma + n
		cant = cant + 1
		num = ConvertirATexto(n)
	Hasta Que num = "#"
	Escribir "La cantidad de valores introducidos es " cant
	Escribir "La suma de los valores introducidos es " suma
FinAlgoritmo
