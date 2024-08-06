Algoritmo sin_titulo
	Escribir "Ingrese el nombre, edad y direccion del primer socio"
	Leer name1, edad1, direc1
	Escribir "Ingrese el nombre, edad y direccion del segundo socio"
	Leer name2, edad2, direc2
	Si edad1 < edad2 Entonces
		Escribir "Nombre: " name1
		Escribir "Edad: " edad1
		Escribir "Direccion: " direc1
	SiNo
		si edad1 > edad2 Entonces
			Escribir "Nombre: " name2
			Escribir "Edad: " edad2
			Escribir "Direccion: " direc2
		SiNo
			Escribir "Ambos socios tienen la misma edad"
			Escribir "Primer socio"
			Escribir "Nombre: " name1
			Escribir "Edad: " edad1
			Escribir "Direccion: " direc1
			Escribir "Segundo socio"
			Escribir "Nombre: " name2
			Escribir "Edad: " edad2
			Escribir "Direccion: " direc2
			
		FinSi
	FinSi
FinAlgoritmo
