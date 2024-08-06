Algoritmo ejercicio_5
	//Hacer un programa que lea 100 Números, indique cuáles son múltiplos de 2 y contarlos.
	cont=0;
	i=0;
	Repetir
		n1= azar(100)+1;
		Si n1 mod 2=0 Entonces
			cont=cont+1;
			Escribir n1 " Es multiplo de 2";
		Fin Si
		i=i+1;
	Hasta Que i=100;
		Escribir "La cantidad de multiplos de 2 es: ", cont;
FinAlgoritmo
