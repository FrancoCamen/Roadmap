Algoritmo ejercicio_26
	Definir op,ops,edad,admin,dni,tr,gr,ope Como Entero
	Definir nom, ap,dir Como Caracter
	
	Repetir
		Escribir "===PROGRAMA DE CURRICULUM DE LA EMPRESA===";
		Escribir "    ==SELECCIONE LA OPCIÓN DESEADA==      ";
		Escribir "1. ADMINISTRATIVO";
		Escribir "2. TRANSPORTISTA";
		Escribir "3. OPERARIO";
		Escribir "4. GUARDIA DE SEGURIDAD";
		Escribir "0. SALIR";
		Escribir "OPCIÓN: ";
		Leer op;
		Segun op Hacer
			1:
				Escribir "USTED SELECCIONÓ ADMINISTRATIVO";
				Escribir "Ingrese su edad: ";
				Leer edad;
				Si edad<18 Entonces
					Escribir "USTED NO ES MAYOR DE EDAD";
				FinSi
				Si edad>=18 Entonces
					Si edad>55 Entonces
						Escribir "USTED EXCEDE EL LIMITE DE EDAD PERMITIDO";
					FinSi
					Si edad<=55 Entonces
						Escribir "¿Posee titulo en Ciclo Superior en Administración y Finanzas? ";
						Escribir "1.SI";
						Escribir "2.NO";
						Leer ops;
						Si ops=1 Entonces
							Escribir "USTED CUMPLE CON TODOS LOS REQUISITOS";
							Escribir "INGRESE SU NOMBRE: ";
							Leer nom;
							Escribir "INGRESE SU APELLIDO: ";
							Leer ap;
							Escribir "INGRESE SU DIRECCIÓN: ";
							Leer dir;
							Escribir "INGRESE SU DNI: ";
							Leer dni;
							admin=admin+1;
						SiNo
							si op=2 Entonces
								Escribir "USTED NO CUMPLE CON TODOS LOS REQUISITOS";
							FinSi
						FinSi
					FinSi
				FinSi
			2:
				Escribir "USTED SELECCIONÓ TRANSPORTISTA";
				Escribir "INGRESE SU EDAD: ";
				Leer edad;
				Si edad<18 Entonces
					Escribir "USTED ES MENOR DE EDAD";
				FinSi
				Si edad>=18 Entonces
					si edad>55 Entonces
						Escribir "USTED EXCEDE EL MAXIMO DE EDAD";
					FinSi
					Si edad<=55 Entonces
						Escribir "POSEE TITULO DE SECUNDARIO";
						Escribir "1.SI";
						Escribir "2.NO";
						Leer ops;
						si ops=1 Entonces
							Escribir "USTED POSEE TODOS LOS REQUISITOS";
							Escribir "INGRESE SU NOMBRE: ";
							Leer nom;
							Escribir "INGRESE SU APELLIDO: ";
							Leer ap;
							Escribir "INGRESE SU DIRECCIÓN: ";
							Leer dir;
							Escribir "INGRESE SU DNI: ";
							Leer dni;
							tr=tr+1;
						FinSi
					FinSi
				FinSi
			3:
				Escribir "USTED SELECCIONÓ OPERARIO";
				Escribir "INGRESE SU EDAD: ";
				Leer edad
				si edad<18 Entonces
					Escribir "USTED ES MENOR DE EDAD";
				FinSi
				Si edad>=18 Entonces
					si edad>50 Entonces
						Escribir "USTED EXCEDE EL LIMITE DE EDAD";
					FinSi
					Si edad<50 Entonces
						Escribir "POSEE TITULO DE SECUNDARIO";
						Escribir "1.SI";
						Escribir "2.NO";
						Leer ops;
						si ops=1 Entonces
							Escribir "USTED POSEE TODOS LOS REQUISITOS";
							Escribir "INGRESE SU NOMBRE: ";
							Leer nom;
							Escribir "INGRESE SU APELLIDO: ";
							Leer ap;
							Escribir "INGRESE SU DIRECCIÓN: ";
							Leer dir;
							Escribir "INGRESE SU DNI: ";
							Leer dni;
							ope=ope+1;
						FinSi
					FinSi
				FinSi
				
			4:
				Escribir "USTED SELECCIONÓ GUARDIA DE SEGURIDAD";
				Escribir "INGRESE SU EDAD: ";
				Leer edad
				si edad<18 Entonces
					Escribir "USTED ES MENOR DE EDAD";
				FinSi
				Si edad>=18 Entonces
					si edad>45 Entonces
						Escribir "USTED EXCEDE EL LIMITE DE EDAD";
					FinSi
					Si edad<=45 Entonces
						Escribir "POSEE TITULO DE SECUNDARIO";
						Escribir "1.SI";
						Escribir "2.NO";
						Leer ops;
						si ops=1 Entonces
							Escribir "USTED POSEE TODOS LOS REQUISITOS";
							Escribir "INGRESE SU NOMBRE: ";
							Leer nom;
							Escribir "INGRESE SU APELLIDO: ";
							Leer ap;
							Escribir "INGRESE SU DIRECCIÓN: ";
							Leer dir;
							Escribir "INGRESE SU DNI: ";
							Leer dni;
							gr=gr+1;
						FinSi
					FinSi
				FinSi
		Fin Segun
	Hasta Que op=0
	Escribir "Usted cuenta con " admin, " curriculums de administrativos";
	Escribir "Usted cuenta con " tr, " curriculums de transportista";
	Escribir "Usted cuenta con " ope, " curriculums de operarios";
	Escribir "Usted cuenta con " gr, " curriculums de guardia de seguridad";
	
	
FinAlgoritmo
