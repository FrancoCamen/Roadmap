Algoritmo Numeros_primos
	Definir n1, n2, div1, div2, Result Como Entero
	Escribir "Ingrese el primer numero"
	Leer n1
	Escribir "Ingrese el segundo numero"
	Leer n2
	div1 = 1
	div2 = 1
	Result1 = 0
	Result2 = 0
	Mientras div1 <= n1 o div2 <= n2 Hacer
		si n1 MOD div1 = 0 Entonces
			Result1 = Result1 + 1
		FinSi
		si n2 MOD div2 = 0 Entonces
			Result2 = Result2 + 1
		FinSi
		div1 = div1 + 1
		div2 = div2 + 1
	FinMientras
	Si Result1 = 2 y Result2 = 2 Entonces
		Escribir "Los numeros son primos"
	Sino 
		Escribir "Los numeros no son primos"
	FinSi
FinAlgoritmo
