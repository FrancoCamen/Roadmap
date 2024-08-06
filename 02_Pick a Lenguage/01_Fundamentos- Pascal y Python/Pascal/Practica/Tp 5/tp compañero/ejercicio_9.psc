Algoritmo ejercicio_9
	//Desarrollar un algoritmo que determine en un conjunto de 100 números:
	//a) Cuántos son mayores que 15.
	//b) Cuántos son mayores que 50.
	//c) Cuántos están comprendidos entre 25 y 45.
	Definir i, num Como Entero
	i=0;
	cont15=0;
	cont50=0;
	cont2545=0;
	Repetir
		num=azar(100)+1;
		Si num>15 Entonces
			cont15=cont15+1;
		FinSi
		Si num>=25 Entonces
			Si num<=45 Entonces
				cont2545=cont2545+1;
			FinSi
		FinSi
		Si num>50 Entonces
			cont50=cont50+1;
		FinSi
		i=i+1;
	Hasta Que i=100
	Escribir "La cant de N° mayores que 15 es: ", cont15;
	Escribir "La cant de N° entre 25 y 45 es: ",cont2545;
	Escribir "La cant de N° mayores que 50 es: ", cont50;
	
FinAlgoritmo
