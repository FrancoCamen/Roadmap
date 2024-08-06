Algoritmo sin_titulo
	x = 0
	Mientras x < 5 Hacer
		Escribir "Ingrese un par de numeros"
		Leer n1, n2
		Result1 = n1 mod 2
		Result2 = n2 mod 2
		Si Result1 = 0 y Result2 = 0 Entonces
			Escribir "Ambos valores, " n1 " y " n2 " ,son positivos"
			
		SiNo
			Escribir "Ambos valores, " n1 " y " n2 " , no son positivos"
		Fin Si
		Promedio = n1 + n1 / 2
		Escribir "Su promedio es: " Promedio
		x = x +1
	Fin Mientras
FinAlgoritmo
