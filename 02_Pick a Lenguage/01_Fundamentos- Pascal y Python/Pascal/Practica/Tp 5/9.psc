Algoritmo sin_titulo
	x = 0
	opcion1 = 0
	opcion2 = 0
	opcion3 = 0
	Mientras x < 100 Hacer
		n = Aleatorio(1,100)
		si n > 15 Entonces
			opcion1 = opcion1 + 1
			si n > 50 Entonces
				opcion2 = opcion2 + 1
			FinSi
			si n > 25 y n < 45 Entonces
				opcion3 = opcion3 + 1
			FinSi
		FinSi
		x = x + 1
	Fin Mientras
	Escribir "Numeros mayores a 15: " opcion1
	Escribir "Numeros mayores a 50: " opcion2
	Escribir "Numeros entre 25 y 45: " opcion3
FinAlgoritmo
