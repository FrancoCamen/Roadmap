Algoritmo ejercicio_25
	//Dada una lista de precios de productos, la cual termina con un precio igual a cero. 
	//Se desea saber el monto total a pagar y la cantidad de artículos comprados.
	Definir precio,i,monto Como Entero
	Repetir
		Escribir "Ingrese el valor de un producto (ingrese 0 para finalizar): ";
		Leer precio;
		monto=(monto+precio);
		i=i+1
		Si precio=0 Entonces
			i=i-1;
		FinSi
	Hasta Que precio=0
	
	Escribir "El monto total a pagar es: ",monto;
	Escribir "La cantidad de productos comprados es: ",i;
FinAlgoritmo
