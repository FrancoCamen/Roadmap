Algoritmo ejercicio_1
	//ngresar 5 pares de valores, en cada oportunidad emitir ambos valores y si ambos son positivos, emitir tambi�n su promedio.
	Definir n1, n2,prom Como Real
	Para i<-1 Hasta 5 Con Paso 1 Hacer
		Escribir "Ingrese un n�mero: ";
		Leer n1;
		Escribir "Ingrese otro n�mero: ";
		Leer n2;  
		Si n1>0 Entonces
			Si n2>0 Entonces
				prom= (n1+n2)/2;
				Escribir "El primer n�mero ingresado es: ",n1;
				Escribir "El segundo n�mero ingresado es: ",n2;
				Escribir "Su promedio es: ",prom;
			FinSi
		SiNo
			Escribir "Uno de los n�meros es negativo";
		FinSi
	Fin Para
	
FinAlgoritmo
