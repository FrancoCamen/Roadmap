Algoritmo sin_titulo
	Dimension obreros[4000, 3]
	Para contador<-1 Hasta 4000 Con Paso 1 Hacer
		obreros[contador,1] = contador
		obreros[contador,2] = Aleatorio(1,5)
		obreros[contador,3] = Aleatorio(18, 65)
	Fin Para
	Dimension Trabajadores(5)
	Dimension A�os(5)
	
	x = 1
	Mientras x < 4001 Hacer
		Segun obreros[x,2] Hacer
			1:
				Trabajadores(1) = Trabajadores(1) + 1
				A�os(1) = A�os(1) + obreros[x, 3]
			2:
				Trabajadores(2) = Trabajadores(2) + 1
				A�os(2) = A�os(2) + obreros[x, 3]
			3:
				Trabajadores(3) = Trabajadores(3) + 1
				A�os(3) = A�os(3) + obreros[x, 3]
			4:
				Trabajadores(4) = Trabajadores(4) + 1
				A�os(4) = A�os(4) + obreros[x, 3]
			5:	
				Trabajadores(5) = Trabajadores(5) + 1
				A�os(5) = A�os(5) + obreros[x, 3]
		Fin Segun
		x = x + 1
	FinMientras
	Escribir "Cantidad de trabajadores y promedio de sus edades segun su seccion"
	Escribir "Seccion 1: " Trabajadores(1) " obreros con un promedio de: " A�os(1)/Trabajadores(1) " a�os"
	Escribir "Seccion 1: " Trabajadores(2) " obreros con un promedio de: " A�os(2)/Trabajadores(2) " a�os"
	Escribir "Seccion 1: " Trabajadores(3) " obreros con un promedio de: " A�os(3)/Trabajadores(3) " a�os"
	Escribir "Seccion 1: " Trabajadores(4) " obreros con un promedio de: " A�os(4)/Trabajadores(4) " a�os"
	Escribir "Seccion 1: " Trabajadores(5) " obreros con un promedio de: " A�os(5)/Trabajadores(5) " a�os"
FinAlgoritmo
