Algoritmo ejericio_2
	//Calcular la suma y el producto de los n�meros pares comprendidos entre 20 y 500.
	Definir sum, i Como Entero
	prod=2;
	Para i<-20 Hasta 500 Con Paso 2 Hacer
		Si i mod 2=0 Entonces
			sum=(sum+i);
			prod=(prod*i);
		FinSi
	Fin Para
	Escribir "La suma de los N�meros pares es: ", sum;
	Escribir "El producto de los N�meros pares es: ",prod;
	
FinAlgoritmo
