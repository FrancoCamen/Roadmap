Algoritmo sin_titulo
	Definir km, km_exedidos Como Real
	Escribir "Ingrese los km recorridos para calcular su tarifa"
	Leer km
	Si km <= 30 Entonces
		tarifa = 20
	SiNo
		Si km <= 100 Entonces
			km_exedidos = km - 30
			tarifa = 20 + (km_exedidos * 1 )
		SiNo
			km_exedidos = km - 100
			tarifa = 20 + 70 + (km_exedidos * 0.50)
		FinSi
	FinSi
	Escribir "La tarifa a pagar es: " tarifa
FinAlgoritmo
