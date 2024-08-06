Algoritmo ejercicio_17
	//Construir un algoritmo que, dada una secuencia de enteros acabada con el valor cero, devuelva el mayor de ellos. 
	//Determinar cuántos números negativos han aparecido.
	Definir num,n, cont Como Entero
	n=0;
	Repetir
		Escribir "Ingrese un Número (negativo o positivo): ";
		Leer num;
		Si num>n Entonces
			n=num;
		FinSi
		Si num<0 Entonces
			cont=cont+1
		Fin Si
	Hasta Que num=0
	Escribir "El mayor valor ingresado es: ",n;
	Escribir "La cantidad de números negativos ingresados es: ", cont;
FinAlgoritmo
