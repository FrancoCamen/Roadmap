Algoritmo sin_titulo
	contador = 0
	n1 = 0
	n2 = 0
	Mientras contador < 50 Hacer
		valor_x = Azar(101)
		valor_y = Azar(101)
		si valor_x > valor_y Entonces
			n1 = n1 + 1
		SiNo
			si valor_x < valor_y Entonces
				n2 = n2 + 1
			FinSi
		FinSi
		contador = contador + 1
	Fin Mientras
	Escribir "En " n1 " pares en valor x > y"
	Escribir "En " n2 " pares el valor x < y"
	
FinAlgoritmo
