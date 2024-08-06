Algoritmo sin_titulo
	Escribir "Ingrese la cantidad de alumnos promocionados"
	Leer pro
	Escribir "Ingrese la cantidad de alumnos regularizados"
	Leer reg
	Escribir "Ingrese la cantidad de alumnos desaprobados"
	Leer des
	Escribir "Ingrese la cantidad de alumnos libres"
	Leer lib
	Alum_total = pro + reg + des + lib
	porc_pro = (pro * Alum_total) / 100
	porc_reg = (reg * Alum_total) / 100
	porc_des = (des * Alum_total) / 100
	porc_lib = (lib * Alum_total) / 100
	Escribir "El procentaje de alumnos promocionados es: " porc_pro
	Escribir "El procentaje de alumnos regularizados es: " porc_reg
	Escribir "El procentaje de alumnos desaprobados es: " porc_des
	Escribir "El procentaje de alumnos libres es: " porc_lib
FinAlgoritmo
