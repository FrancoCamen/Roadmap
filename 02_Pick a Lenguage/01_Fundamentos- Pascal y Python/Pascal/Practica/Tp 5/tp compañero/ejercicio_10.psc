Algoritmo ejercicio_10
	Definir n,f Como Entero
	Definir sum Como Real
	f=1;
	i=0;
	sum=0;
	Escribir "Ingrese el valor de N en h(n)=1 + ½ + 1/3 + ... + 1/n: ";
	Leer n;
	Repetir
		sum=sum+1/f;
		f=f+1;
		i=i+1;
	Hasta Que i=n
	
	Escribir "El resultado es: ",sum;
	
FinAlgoritmo
