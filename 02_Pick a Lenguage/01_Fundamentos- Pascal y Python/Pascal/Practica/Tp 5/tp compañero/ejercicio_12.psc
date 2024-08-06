Algoritmo ejercicio_12
	Definir num,cont1,cont2,cont3 Como Entero
	cont1=0;
	cont2=0;
	cont3=0;
	i=1;
	Mientras i<=1000 Hacer
		num=azar(3)+1;
		Si num=1 Entonces
			cont1=cont1+1;
		SiNo
			Si num=2 Entonces
				cont2=cont2+1;
			SiNo
				Si num=3 Entonces
					cont3=cont3+1;
				FinSi
			FinSi
		Fin Si
		i=i+1;
	Fin Mientras
	Escribir "La cantidad de alumnos con código 1 es: ",cont1;
	Escribir "La cantidad de alumnos con código 2 es: ", cont2;
	Escribir "La cantidad de alumnos con código 3 es: ",cont3;
FinAlgoritmo
