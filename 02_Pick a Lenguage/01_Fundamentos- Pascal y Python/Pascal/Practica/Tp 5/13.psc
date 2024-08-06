Algoritmo sin_titulo
	Dimension obreros[4000, 3]
	Para contador<-1 Hasta 4000 Con Paso 1 Hacer
		obreros[contador,1] = contador
		obreros[contador,2] = Aleatorio(1,5)
		obreros[contador,3] = Aleatorio(18, 65)
	Fin Para
	Dimension Trabajadores(5)
	Dimension Años(5)
	
	x = 1
	Mientras x < 4001 Hacer
		Segun obreros[x,2] Hacer
			1:
				Trabajadores(1) = Trabajadores(1) + 1
				Años(1) = Años(1) + obreros[x, 3]
			2:
				Trabajadores(2) = Trabajadores(2) + 1
				Años(2) = Años(2) + obreros[x, 3]
			3:
				Trabajadores(3) = Trabajadores(3) + 1
				Años(3) = Años(3) + obreros[x, 3]
			4:
				Trabajadores(4) = Trabajadores(4) + 1
				Años(4) = Años(4) + obreros[x, 3]
			5:	
				Trabajadores(5) = Trabajadores(5) + 1
				Años(5) = Años(5) + obreros[x, 3]
		Fin Segun
		x = x + 1
	FinMientras
	Escribir "Cantidad de trabajadores y promedio de sus edades segun su seccion"
	Escribir "Seccion 1: " Trabajadores(1) " obreros con un promedio de: " Años(1)/Trabajadores(1) " años"
	Escribir "Seccion 1: " Trabajadores(2) " obreros con un promedio de: " Años(2)/Trabajadores(2) " años"
	Escribir "Seccion 1: " Trabajadores(3) " obreros con un promedio de: " Años(3)/Trabajadores(3) " años"
	Escribir "Seccion 1: " Trabajadores(4) " obreros con un promedio de: " Años(4)/Trabajadores(4) " años"
	Escribir "Seccion 1: " Trabajadores(5) " obreros con un promedio de: " Años(5)/Trabajadores(5) " años"
FinAlgoritmo
