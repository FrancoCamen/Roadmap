Algoritmo sin_titulo
	Definir a,b,x Como Entero
	Definir palabra Como Caracter
	Escribir "Escribe una palabra"
	leer palabra
	b <- Longitud(palabra)
	a <- 1
	X <- 0 
	Mientras a < b Hacer
		si Subcadena(palabra,a,a) <> Subcadena(palabra,b,b) Entonces
			X <- X + 1
		FinSi
		a <- a + 1
		b <- b - 1
	FinMientras
	si x == 0 Entonces
		Escribir "La palabra " ,palabra, " es capicua"
	SiNo
		Escribir "La palabra " ,palabra, " no es capicua"
	FinSi
FinAlgoritmo
