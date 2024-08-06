Algoritmo sin_titulo
	Definir c, x Como Caracter
	Escribir "Ingresa que caracter desea econtrar en la secuencia de caracteres"
	Leer c
	cant = 0
	Escribir "Ingrese una secuencia de caracteres que acabe en un punto"
	Repetir
		Leer x
		si x = c Entonces
			cant = cant + 1
		FinSi
	Hasta Que x = "."
	Escribir "La cantidad de veces que aparece " c " es " cant
FinAlgoritmo
