Algoritmo ejercicio_14
	//Construir un algoritmo que muestre por pantalla las tablas de multiplicar usuales hasta el Nº 10.
	//5 por 1 es 5,5 por 2 es 10,5 por 3 es 15
	Definir i,n1,n2, c,c1,c2,f,f1,f2,s,s1,s2,mult Como Entero
	i=1;
	n1=2;
	n2=1;
	Mientras i<=10 Hacer
		mult=(n1*n2);
		Escribir n1, " por ", n2 " es: ", mult;
		i=i+1;
		n2=n2+1;
	Fin Mientras
	Escribir "----------------";
	c=1;
	c1=3;
	c2=1;
	Mientras c<=10 Hacer
		mult=(c1*c2);
		Escribir c1, " por ", c2 " es: ", mult;
		c=c+1;
		c2=c2+1;
	Fin Mientras
	Escribir "----------------";
	f=1;
	f1=4;
	f2=1
	Mientras f<=10 Hacer
		mult=(f1*f2);
		Escribir f1, " por ", f2 " es: ", mult;
		f=f+1;
		f2=f2+1;
	Fin Mientras
	Escribir "----------------";
	s=1;
	s1=5;
	s2=1;
	Mientras s<=10 Hacer
		mult=(s1*s2);
		Escribir s1, " por ", s2 " es: ", mult;
		s=s+1;
		s2=s2+1;
	Fin Mientras
	
	
	
FinAlgoritmo
