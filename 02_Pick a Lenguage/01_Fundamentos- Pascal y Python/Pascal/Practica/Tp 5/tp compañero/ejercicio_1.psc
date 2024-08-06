Algoritmo ejercicio_1
	//ngresar 5 pares de valores, en cada oportunidad emitir ambos valores y si ambos son positivos, emitir también su promedio.
	Definir n1, n2,prom Como Real
	Para i<-1 Hasta 5 Con Paso 1 Hacer
		Escribir "Ingrese un número: ";
		Leer n1;
		Escribir "Ingrese otro número: ";
		Leer n2;  
		Si n1>0 Entonces
			Si n2>0 Entonces
				prom= (n1+n2)/2;
				Escribir "El primer número ingresado es: ",n1;
				Escribir "El segundo número ingresado es: ",n2;
				Escribir "Su promedio es: ",prom;
			FinSi
		SiNo
			Escribir "Uno de los números es negativo";
		FinSi
	Fin Para
	
FinAlgoritmo
