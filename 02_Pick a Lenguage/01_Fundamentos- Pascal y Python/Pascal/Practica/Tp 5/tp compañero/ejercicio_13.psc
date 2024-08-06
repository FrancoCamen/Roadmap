Algoritmo ejercicio_13
	//En una fábrica hay 4.000 obreros distribuidos en cinco secciones. Se requiere
	//determinar cuántos obreros hay y el promedio de edad de los mismos por cada
	//sección. Asumir que se tiene como entrada los siguientes datos para cada obrero: Nº
	//de empleado, sección a la que pertenece y edad.
	
	Definir i,nume,sec,sec1,sec2,sec3,sec4,sec5,edad1,edad2,edad3,edad4,edad5,cont1,cont2,cont3,cont4,cont5 Como Entero
	Definir prom1,prom2,prom3,prom4,prom5 Como Real
	i=1;
	sec1=0;
	sec2=0;
	sec3=0;
	sec4=0;
	sec5=0;
	Mientras i<=4000 Hacer
		nume=azar(4000)+1;
		Escribir "Obrero N°: ",nume;
		
		Escribir "Ingrese su sección de trabajo(1-5): ";
		Leer sec;
		Segun sec hacer
			1: sec1=sec1+1;
				Escribir "Ingrese su edad: ";
				Leer edad1;
			2: sec2=sec2+1;
				Escribir "Ingrese su edad: ";
				Leer edad2;
			3: sec3=sec3+1;
				Escribir "Ingrese su edad: ";
				Leer edad3;
			4: sec4=sec4+1;
				Escribir "Ingrese su edad: ";
				Leer edad4;
			5: sec5=sec5+1;
				Escribir "Ingrese su edad: ";
				Leer edad5;
		FinSegun
		cont1=(cont1+edad1);
		cont2=(cont2+edad2);
		cont3=(cont3+edad3);
		cont4=(cont4+edad4);
		cont5=(cont5+edad5);
		i=i+1;
	Fin Mientras
	
	Si sec1>=1 Entonces
		prom1=(prom1)+cont1/sec1;
	SiNo
		Si sec2>=1 Entonces
			prom2=(prom2)+cont2/sec2;
		Sino 
			Si sec3>=1 Entonces
				prom3=(prom3)+cont3/sec3;
				Sino 
					Si sec4>=1 Entonces
						prom4=(prom4)+cont4/sec4;
						Sino 
							Si sec5>=1 Entonces
								prom5=(prom5)+cont5/sec5;
							FinSi
						FinSi
					FinSi
				FinSi
			FinSi
			
		Escribir "La cantidad de obreros en la seccion 1 es: ",sec1; 
		Escribir "Su promedio de edad es: ",prom1;
		Escribir "La cantidad de obreros en la seccion 2 es: ",sec2;
		Escribir "Su promedio de edad es: ",prom2;
		Escribir "La cantidad de obreros en la seccion 3 es: ",sec3;
		Escribir "Su promedio de edad es: ",prom3;
		Escribir "La cantidad de obreros en la seccion 4 es: ",sec4; 
		Escribir "Su promedio de edad es: ",prom4;
		Escribir "La cantidad de obreros en la seccion 5 es: ",sec5; 
		Escribir "Su promedio de edad es: ",prom5;
FinAlgoritmo
