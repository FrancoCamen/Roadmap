Algoritmo ejercicio_7
	//¿A cuánto asciende la suma de los números pares comprendidos entre 300 y 1232?	
	i=300;
	sum=0;
	Repetir
		Si i mod 2=0 Entonces
			sum=(sum+i);
		Fin Si
		i=i+1;
	Hasta Que i=1232
	Escribir "La suma asciende a: ", sum;
FinAlgoritmo
