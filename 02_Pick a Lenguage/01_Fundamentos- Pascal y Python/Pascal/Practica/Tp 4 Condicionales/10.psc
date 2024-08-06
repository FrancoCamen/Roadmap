Algoritmo sin_titulo
	Escribir "Ingresa 3 letras distintas"
	Leer l1, l2, l3
	i = 1
	Dimension Lista[27]
	Lista[1]="a"
	Lista[2]="b"
	Lista[3]="c"
	Lista[4]="d"
	Lista[5]="e"
	Lista[6]="f"
	Lista[7]="g"
	Lista[8]="h"
	Lista[9]="i"
	Lista[10]="j"
	Lista[11]="k"
	Lista[12]="l"
	Lista[13]="m"
	Lista[14]="n"
	Lista[15]="o"
	Lista[16]="p"
	Lista[17]="q"
	Lista[18]="r"
	Lista[19]="s"
	Lista[20]="t"
	Lista[21]="u"
	Lista[22]="v"
	Lista[23]="w"
	Lista[24]="x"
	Lista[25]="y"
	Lista[26]="z"
	Mientras i < 27 Hacer
		Segun Lista[i] Hacer
			l1:
				Escribir "La letra " l1 " se encuentra ubicada en el alfabeto antes que las demas"
				i = 27
			l2:
				Escribir "La letra " l2 " se encuentra ubicada en el alfabeto antes que las demas"
				i = 27
			l3:
				Escribir "La letra " l3 " se encuentra ubicada en el alfabeto antes que las demas"
				i = 27
			De Otro Modo:
				i = i + 1
		Fin Segun
	Fin Mientras
FinAlgoritmo
