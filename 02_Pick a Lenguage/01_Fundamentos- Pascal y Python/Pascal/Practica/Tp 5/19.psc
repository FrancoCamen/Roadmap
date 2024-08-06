Algoritmo sin_titulo
	negativos = 0
	Escribir "Ingrese una lista de numeros que finalice con el numero 0"
	Repetir
		Leer n
		si n < 0 Entonces
			negativos = negativos + 1
		FinSi
	Hasta Que n = 0
	Escribir "La cantidad de numeros negativos en la lista es: " negativos 
FinAlgoritmo
