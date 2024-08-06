Algoritmo sin_titulo
	Escribir "Ingrese el primer numero"
	Leer n1
	Escribir "Ingrese el segundo numero"
	Leer n2
	Si (n1 mod 2) = 0 Entonces
		x = n1
		n1 = n2
		n2 = x
		Escribir "El nuevo valor del primer numero es: " n1
		Escribir "El nuevo valor del segundo numero es: " n2
	SiNo
		Escribir "El primer numero no es divisible por el segundo"
	FinSi
FinAlgoritmo
