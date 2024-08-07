import sys

def factorial(num):     
    # Función para calcular el factorial de un número
    if num < 0: 
        print("Factorial de un número negativo no existe")
    elif num == 0: 
        return 1
    else: 
        fact = 1
        while(num > 1): 
            fact *= num 
            num -= 1
        return fact 

while True:
    # Verificar si se proporciona un argumento en la línea de comandos
    if len(sys.argv) == 1:
        try:
            # Solicitar al usuario que ingrese un rango
            rango = input("Por favor, ingrese un rango (desde-hasta) para calcular los factoriales: ")
            # Caso -hasta
            if rango.startswith("-"):
                desde = 1
                hasta = int(rango.split("-")[1])
            # Caso desde-
            elif rango.endswith("-"):
                desde = int(rango.split("-")[0])
                hasta = 60
            # Caso desde-hasta
            elif "-" in rango:
                desde, hasta = map(int, rango.split("-"))
            else:
                raise ValueError
            break
        except ValueError:
            print("¡Debe ingresar un rango válido en el formato 'desde-hasta', '-hasta' o 'desde-'!")
    else:
        # Si se proporciona un argumento en la línea de comandos, lo interpreta como un rango automáticamente
        rango = sys.argv[1]
        # Caso -hasta
        if rango.startswith("-"):
            desde = 1
            hasta = int(rango.split("-")[1])
        # Caso desde-
        elif rango.endswith("-"):
            desde = int(rango.split("-")[0])
            hasta = 60
        # Caso desde-hasta
        elif "-" in rango:
            desde, hasta = map(int, rango.split("-"))
        break

print("Los factoriales en el rango", desde, "-", hasta, "son:")
for num in range(desde, hasta + 1):
    print("Factorial", num, "! es", factorial(num))



