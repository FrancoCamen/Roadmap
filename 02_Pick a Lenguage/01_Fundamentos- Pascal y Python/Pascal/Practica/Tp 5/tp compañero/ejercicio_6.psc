Algoritmo ejercicio_6
	// Hacer un programa que lea 8 caracteres e indique que cantidad de ?*? y que cantidad de letras ?a? aparecen.
	Definir c1 Como Caracter
	i=0;
	f="a";
	g="*";
	contf=0;
	contg=0;
	Repetir
		Escribir "Ingrese un caracter: ";
		Leer c1;
		i=i+1;
		Si c1=f Entonces
			contf=contf+1;
		SiNo
			Si c1=g Entonces
				contg=contg+1;
			FinSi
		Fin Si
	Hasta Que i=8
	Escribir "La cantidad de (a) es: ",contf;
	Escribir "La cantidad de (*) es: ", contg;
FinAlgoritmo
