Algoritmo ejercicio_23
	//Dada una lista de valores enteros positivos, hallar cuántos valores mayores que 1.000 hay. 
	//Si la cantidad es menor que 20 calcular su factorial.
	Definir num,i,cont,fact,d Como Entero
	fact=1;
	Repetir
		num= azar(1500)+1;
		i=i+1;
		Si num>1000 Entonces
			cont=cont+1;
		FinSi
	Hasta Que i=40 
	
	Si cont<20 Entonces
		d=cont
		Mientras d>0 Hacer
			fact=(fact*d);
			d=d-1;
		FinMientras
		Escribir "El factorial es: ", fact;
	FinSi
	Escribir "La cantidad de valores mayores que 1000 son: ",cont;
	
	
FinAlgoritmo
