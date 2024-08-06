Algoritmo ejercicio_18
	//Dada una secuencia de caracteres acabada en punto, obtener un algoritmo que 
	//determine cuantas veces aparece un determinado carácter, el cual será leído previamente
	Definir n, c Como Caracter
	Escribir "Ingrese el valor que quiera evaluar: ";
	Leer n;
	Repetir
		Escribir "Ingrese un valor: ";
		Leer c;
		Si c=n Entonces
			cont=cont+1;
		FinSi
	Hasta Que c="."
	Escribir "La cantidad de veces que aparece, " n ," , es: " cont;
	
	
FinAlgoritmo
