Algoritmo sin_titulo
	x = 1
	Mientras x < 4 Hacer
		Escribir "Ingrese el nombre del prodcuto"
		Leer nombre
		Escribir "Ingrese el porcentaje de aceptacion"
		Leer porc
		si x == 1 Entonces
			nameMay = nombre
			porcMay = porc
			nameMen = nombre
			porcMen = porc
		SiNo
			si porc > porcMay Entonces
				porcMay = porc
				nameMay = nombre
			SiNo
				si porc < porcMen Entonces
					porcMen = porc
					nameMen = nombre
				FinSi
			FinSi
		FinSi
		x = x + 1
	Fin Mientras
	Escribir "El producto mejor aceptado es: " nameMay ", con un porcentaje del: " porcMay "%"
	Escribir "El producto peor aceptado es: " nameMen ", con un porcentaje del: " porcMen "%"
FinAlgoritmo
