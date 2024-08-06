Algoritmo sin_titulo
	Escribir "Ingrese el valor n para  h(n)=1 + ½ + 1/3 + ... + 1/n"
	Leer n
	denominador = 1
	Mientras denominador <= n Hacer
		Result = Result + 1/denominador
		denominador = denominador + 1
	Fin Mientras
	Escribir "El resultado es : " Result
FinAlgoritmo
