Algoritmo ejercicio_11
	//Se leen 50 pares de Números, c/u de los cuales tienen 2 valores: x e y distintos. Se pide contar en cuantos pares x>y y en cuantos y>x.
	Definir n1, n2, cantx, canty Como Entero
	contx=0;
	conty=0;
	i=0;
	Mientras i<=50 Hacer
		n1=azar(100)+1;
		n2= azar(100)+1;
		Si n1<>n2 Entonces
			Si n1>n2 Entonces
				contx=contx+1;
			SiNo
				Si n1<n2 Entonces
					conty=conty+1;
				FinSi
			Fin Si
		Fin Si
		i=i+1;
	Fin Mientras
	Escribir "La cantidad de x>y es: ", contx;
	Escribir "La cantidad de y>x es: ", conty;
FinAlgoritmo
