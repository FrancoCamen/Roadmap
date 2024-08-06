Algoritmo sin_titulo
	Definir i, may, men, num Como Entero
	Escribir "Ingrese la cantidad de numeros de la lista"
	Leer cant_num
	i = 1
	Mientras cant_num >= i Hacer
		Escribir "Ingrese un numero"
		leer num
		si i = 1 Entonces
			may = num
			men = num
		SiNo
			si num >= may Entonces
				may = num
			SiNo
				si num <= men Entonces
					men = num
				FinSi
			FinSi
		FinSi
		i = i + 1
	FinMientras
	Escribir "El numero mayor de la lista es: " may
	Escribir "El numero menor de la lista es: " men
	Escribir "El rango de numeros es: " may-men
FinAlgoritmo
