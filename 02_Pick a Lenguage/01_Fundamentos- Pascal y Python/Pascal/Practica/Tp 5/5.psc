Algoritmo sin_titulo
	x = 0
	cant = 0
	Mientras x < 100 Hacer
		n = Azar (1000)
		multi = n mod 2
		si multi = 0 Entonces
			Escribir "El numero " n " es multiplo de 2"
			cant = cant + 1
		FinSi
		x = x + 1
	Fin Mientras
	Escribir "Hay " cant " numeros  multiplos de 2"
FinAlgoritmo
