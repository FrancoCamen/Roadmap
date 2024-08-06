Algoritmo sin_titulo
	condicion = falso
	Repetir
		Escribir "Ingrese un valor para A"
		Leer a
		Escribir "Ingrese un valor para B"
		Leer b
		si a < b Entonces
			condicion = Verdadero
		SiNo
			Escribir "El valor de A debe ser menor que el valor de B"
		FinSi
	Hasta Que condicion
	
	Para primer_numero<-a Hasta b Con Paso 1 Hacer
		Para segundo_numero<-1 Hasta 10 Con Paso 1 Hacer
			Escribir primer_numero " por " segundo_numero " es " primer_numero * segundo_numero
		Fin Para
	Fin Para
FinAlgoritmo
