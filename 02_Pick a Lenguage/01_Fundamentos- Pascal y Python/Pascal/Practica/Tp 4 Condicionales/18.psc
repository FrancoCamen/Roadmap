Algoritmo sin_titulo
	Escribir "Ingrese dos numeros"
	Leer n1, n2
	Si (n1 mod n2) = 0 Entonces
		Escribir "El primer numero es divisivle por el segundo"
		si (n1 mod 2) = 0 Entonces
			Escribir "El numero: " n1 " es un numero par"
		SiNo
			Escribir "El numero: " n1 " es un numero impar"
		FinSi
	Sino 
		Escribir "El primer numero no es dividivle por el segundo"
	FinSi
FinAlgoritmo
