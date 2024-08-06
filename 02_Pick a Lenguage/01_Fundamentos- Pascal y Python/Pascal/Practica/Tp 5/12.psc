Algoritmo sin_titulo
	Dimension alumnos(1000)
	Para i<-1 Hasta 1000 Con Paso 1 Hacer
		alumnos(i) = Aleatorio(1,3)
	Fin Para
	calificacion_1 = 0
	calificacion_2 = 0
	calificacion_3 = 0
	x = 1
	Mientras x < 1001 Hacer
		Segun alumnos(x) Hacer
			1:
				calificacion_1 = calificacion_1 + 1
			2:
				calificacion_2 = calificacion_2 + 1
			3:
				calificacion_3 = calificacion_3 + 1
		Fin Segun
		x = x + 1
	Fin Mientras
	Escribir "Hay " calificacion_1 " alumnos con calificacion 1"
	Escribir "Hay " calificacion_2 " alumnos con calificacion 2"
	Escribir "Hay " calificacion_3 " alumnos con calificacion 3"
FinAlgoritmo
