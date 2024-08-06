Algoritmo sin_titulo
	may = 0
	negativos = 0
	Escribir "Ingrese una secuencia de numeros enteros acaba en cero"
	Repetir
		Leer num
		si num > may Entonces
			may = num
		FinSi
		Si num < 0 Entonces
			negativos = negativos + 1
		FinSi
	Hasta Que num = 0
	Escribir "El numero mayor es  " may
	Escribir "Hay " negativos " numeros negativos"
	
FinAlgoritmo
