Algoritmo sin_titulo
	Definir dianuevo, mesnuevo, añonuevo Como Entero
	Escribir "Ingrese una fecha (dd/mm/aaaa)"
	Leer fecha
	dia = ConvertirANumero(Subcadena(fecha,1,2))
	mes = ConvertirANumero(Subcadena(fecha,4,5))
	año = ConvertirANumero(Subcadena(fecha,7,10))
	Segun mes Hacer
		01 o 03 o 05 o 07 o 08 o 10:
			si dia = 31 Entonces
				dianuevo = 01
				mesnuevo = mes + 01
				añonuevo = año
			SiNo
				dianuevo = dia + 1
				mesnuevo = mes
				añonuevo = año
			FinSi
		02:
			si dia = 28 Entonces
				dianuevo = 01
				mesnuevo = mes + 01
				añonuevo = año
			SiNo
				dianuevo = dia + 1
				mesnuevo = mes
				añonuevo = año
			FinSi
		04 o 06 o 09 o 11:
			si dia = 30 Entonces
				dianuevo = 01
				mesnuevo = mes + 01
				añonuevo = año
			SiNo
				dianuevo = dia + 1
				mesnuevo = mes
				añonuevo = año
			FinSi
		12:
			si dia = 31 Entonces
				dianuevo = 01
				mesnuevo = 01
				añonuevo = año + 1
			SiNo
				dianuevo = dia + 1
				mesnuevo = mes
				añonuevo = año
			FinSi
		De Otro Modo:
			Escribir "el dia ingresa en incorrecto"
	Fin Segun
	Escribir "El dia sguiente a la fecha ingresada es: " dianuevo "//" mesnuevo "//" añonuevo
	
FinAlgoritmo
