Algoritmo ejercicio_22
	//Dada una lista de valores num�ricos, hallar su rango, es decir la diferencia entre su valor m�ximo y su valor m�nimo
	Definir i,may,men,num,cantnum Como Entero
	Escribir "Ingrese la cantidad de n�meros a evaluar: ";
	Leer cantnum;
	i=0;
	Repetir
		Escribir "Ingrese un n�mero: ";
		Leer num;
		Si i=1 Entonces
			may=num;
			men=num;
		SiNo
			Si num>=may Entonces
				may=num;
			SiNo
				Si num<=men Entonces
					men=num;
				FinSi
			FinSi
		FinSi
		i=i+1
	Hasta Que i=cantnum
	Escribir "El n�mero mayor de la lista es: ",may;
	Escribir "El n�mero menor de la lista es: ",men;
	Escribir "El rango es: ", may-men;
FinAlgoritmo
