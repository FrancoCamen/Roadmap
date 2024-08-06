Algoritmo sin_titulo
	Escribir "Ingrese el monto de su producto"
	Leer monto
	si monto > 1000 Entonces
		total = monto - ((10 * monto) / 100)  
	Sino
		total = monto - ((2 * monto) / 100)
	FinSi
	Escribir "El monto total a pagar con el descuento incluido es: $" total
	
FinAlgoritmo
