Algoritmo sin_titulo
	x = 0
	n1 = 0
	n2 = 0
	n3 = 0
	Mientras x < 120 Hacer
		respuesta = Aleatorio(1,3)
		Segun respuesta Hacer
			1:
				n1 = n1 + 1
			2:
				n2 = n2 + 1
			3:
				n3 = n3 + 1
		Fin Segun
		x = x +1
	Fin Mientras
	Escribir "Respuestas para sistema 1 = " n1
	Escribir "Respuestas para sistema 2 = " n2
	Escribir "Respuestas para sistema 3 = " n3
	si n1 > n2 y n1 > n3 Entonces
		Escribir "EL sistemas mas elegido es el 1"
	SiNo
		si n2 >n1 y n2> n3 Entonces 
			Escribir "El sistema mas elegido es el 2"
		SiNo
			si n3> n1 y n3 > n2 Entonces
				Escribir "El sistemas mas elegido es el 3"
			FinSi
		FinSi
	FinSi
FinAlgoritmo
