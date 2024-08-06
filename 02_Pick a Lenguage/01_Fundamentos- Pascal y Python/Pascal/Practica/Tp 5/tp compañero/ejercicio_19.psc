Algoritmo ejercicio_19
	Definir num,cont Como Entero
	Repetir
		Escribir "Ingrese un número: ";
		Leer num;
		Si num<0 Entonces
			cont= cont+1;
		FinSi
	Hasta Que num=0
	Escribir "La cantidad de números negativos ingresados es: ", cont;
FinAlgoritmo
