Algoritmo ejercicio_17
	//Construir un algoritmo que, dada una secuencia de enteros acabada con el valor cero, devuelva el mayor de ellos. 
	//Determinar cu�ntos n�meros negativos han aparecido.
	Definir num,n, cont Como Entero
	n=0;
	Repetir
		Escribir "Ingrese un N�mero (negativo o positivo): ";
		Leer num;
		Si num>n Entonces
			n=num;
		FinSi
		Si num<0 Entonces
			cont=cont+1
		Fin Si
	Hasta Que num=0
	Escribir "El mayor valor ingresado es: ",n;
	Escribir "La cantidad de n�meros negativos ingresados es: ", cont;
FinAlgoritmo
