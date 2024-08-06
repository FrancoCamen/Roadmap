Algoritmo sin_titulo
	Escribir "Ingrese 3 numeros"
	Leer n1, n2, n3
	Si n1 > n2 y n1 > n3 Entonces
		May = n1
		Si n2>n3
			Med = n2
			Men = n3
		SiNo
			Men = n3
			Men = n2
		FinSi
	SiNo
		Si n2>n1 y n2>n3 Entonces
			May = n2
			Si n1>n3 Entonces
				Med = n1
				Men = n3
			SiNo
				Med = n3
				Men = n2
			FinSi
		SiNo
			May = n3
			Si n1>n2 Entonces
				Med = n1
				Men = n2
			SiNo
				Med = n2
				Men = n1
			FinSi
		FinSi
		

	FinSi
	Escribir "Mayor: " May ", Medio: " Med ", Menor: " Men 
	
FinAlgoritmo
