Algoritmo ejercicio_20
	//Escribir un algoritmo que permita leer una serie de enteros. Contar el Nº de valores introducidos y su suma.
	Definir c,n,cont,cont1,sum Como Entero
	t= azar(6)+2;
	Repetir
		Escribir "Ingrese un número: ";
		Leer n;
		cont=cont+1;
		sum=sum+n;
		c=c+1;
	Hasta Que c=t;
	Escribir "La cantidad de calores introducidos es: ",cont;
	Escribir "La suma de los valores ingresados es: ",sum;
FinAlgoritmo
