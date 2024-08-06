Algoritmo sin_titulo
	Definir num1,num2 como entero
	Definir  op Como Entero
	Escribir "Ingrese un valor: "
	leer num1
	Escribir "Ingrese otro valor: "
	leer num2
	op=0;
	Escribir "OPERACIONES:";
	Escribir "1. SUMAR";
	Escribir "2. RESTAR";
	Escribir "3. MULTIPLICAR";
	Escribir "4. DIVIDIR";
	Escribir "OPCION: ";
	LEER op;
	Segun op Hacer
		1:
			sum=(num1+num2);
			Escribir "El resultado de la suma es: ",sum;
		2:
			rest=(num1-num2);
			Escribir "El resultado de la resta es: ",rest;
		3:
			mult=(num1+num2);
			Escribir "El resultado de la mutiplicación es: ",mult;
		4:
			div=(num1/num2);
			Escribir "El resultado dela division es: ",div;
		De Otro Modo:
			Escribir "El valor ingresado no corresponde a una operación";
	Fin Segun
FinAlgoritmo
