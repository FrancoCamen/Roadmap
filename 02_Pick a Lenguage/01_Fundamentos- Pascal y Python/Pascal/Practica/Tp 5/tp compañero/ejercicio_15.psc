Algoritmo ejercicio_15
//Construir un algoritmo que muestre por pantalla las tablas de multiplicar usuales para valores comprendidos entre a y b. (a<b).
	Definir a,b,i,mult Como Entero
	Repetir
		Escribir "Ingrese el valor de a: ";
		Leer a;
		Escribir "Ingresar el valor de b (mayor que a): ";
		Leer b
	Hasta Que b>a;
	Repetir
		i=1;
		Mientras i<=10 Hacer
			mult=(a*i);
			Escribir a, " por " i " es: ",mult;
			i=i+1;
		Fin Mientras
		Escribir "-------------";
		a=a+1;
	Hasta Que a>b
	
FinAlgoritmo
