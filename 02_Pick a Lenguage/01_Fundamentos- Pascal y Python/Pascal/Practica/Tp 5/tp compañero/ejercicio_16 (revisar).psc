Algoritmo ejercicio_16
	Definir cont Como Entero
	Definir t Como Caracter
	num0=0;
	num9=9;
	t="#";
	Repetir
		Escribir "	Ingrese valores: "
		Leer num;
		Si num>=num0 Entonces
			cont=cont+1;
		SiNo
			Si num<=num9 Entonces
				cont=cont+1;
			FinSi
		Fin Si
	Hasta Que num=t
	
	
FinAlgoritmo
