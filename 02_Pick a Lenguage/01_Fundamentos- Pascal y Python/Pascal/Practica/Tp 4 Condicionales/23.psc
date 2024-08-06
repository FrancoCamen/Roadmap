Algoritmo sin_titulo
	Escribir "Ingrese la cantidad de preguntas"
	Leer cant
	Escribir "Ingrese la cantidad de respuestas correctas"
	Leer resp
	Nota = (resp * 100) / cant
	si nota  >= 90 Entonces
		Result = "Muy bueno"
	SiNo
		si nota >= 70 Entonces
			Result = "Bueno"
		SiNo
			si nota >= 50
				Result = "Regular"
			SiNo
				Result = "Malo"
			FinSi
		FinSi
	FinSi
	Escribir "Nivel registrado en la prueba: " Result
FinAlgoritmo
