Algoritmo Ejercicio8
	Escribir "Ingrese un numero de 3 digitos"
	Leer num
	a = Subcadena(num,1,1)
	b = Subcadena(num,2,2)
	c = Subcadena(num,3,3)
	num1 = ConvertirANumero(a)
	num2 = ConvertirANumero(b)
	num3 = ConvertirANumero(c)
	result1 = num1^3
	result2 = num2^3
	result3 = num3^3
	resultado = result1 + result2 + result3
	numIngresado = ConvertirANumero(num)
	si resultado = numIngresado Entonces
		Escribir "El numero: " numIngresado " es Amstrong"
	SiNo
		Escribir "El numero: " numIngresado " no es Amstrong"
	FinSi
	
	
FinAlgoritmo
