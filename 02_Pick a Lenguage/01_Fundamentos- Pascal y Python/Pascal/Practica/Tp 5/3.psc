Algoritmo sin_titulo
	x = 0
	maximo = 0
	posicion = 0
	Mientras x < 475 Hacer
		n = Azar(475)
		si n > maximo Entonces
			maximo = n
			posicion = x + 1
		FinSi
		x = x +1
	Fin Mientras
	Escribir "El numero maxino del conjunto es : " maximo
	Escribir "La posicion en la que fue enmitida es : " posicion
	
FinAlgoritmo
