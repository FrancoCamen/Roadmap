Algoritmo sin_titulo
	Definir n1, n2 ,n3 Como Entero
	Escribir "Ingresar tres numeros enteros positivos distintos"
	Leer n1, n2, n3
	Si n1>0 y n2>0 y n3>0 Entonces
		Si n1>n2 y n1>n3 Entonces
			Escribir n1 " es el mayor"
		SiNo
			Si n2>n1 y n2>n3 Entonces
				Escribir n2 " es el mayor"
			SiNo
				Escribir n3 " es el mayor"
			FinSi
			
		FinSi
	FinSi
FinAlgoritmo
