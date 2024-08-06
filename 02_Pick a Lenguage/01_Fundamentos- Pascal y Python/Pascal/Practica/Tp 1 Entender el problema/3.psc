Algoritmo sin_titulo
	Definir a, b, x Como Entero
	x = 0
	Mientras x = 0
		Escribir "Ingrese valor de A para comparar"
		leer a
		Escribir "Ingrese valor de B para comparar"
		leer b
		Si a = b Entonces
			Escribir "Los valores ingresados son iguales, por favor intente nuevamente"
		SiNo
			Si a > b Entonces
				Escribir "El valor de A es mayor que el valor de B"
				x = 1
			SiNo
				Escribir "El valor de B es mayor que el de A"
				x = 1
			FinSi
		FinSi
	FinMientras
FinAlgoritmo
