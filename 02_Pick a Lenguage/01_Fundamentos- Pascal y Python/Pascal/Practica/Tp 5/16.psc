Algoritmo sin_titulo
	Definir c Como Caracter
	cant = 0
	Escribir "Ingrese una secuencia de caracteres separados que acabe con #"
	Repetir
		Leer c
		num = ConvertirANumero(c)
		si num >= 0 y num <= 9 Entonces
			cant = cant + 1
		FinSi
	Hasta Que c ="#"
	Escribir "En la secuencia de caracteres habian " cant " numeros"
FinAlgoritmo
