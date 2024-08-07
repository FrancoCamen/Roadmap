import sys
class Factorial:
    def __init__(self,min,max):
        self.min = min
        self.max = max

    def calcular_factorial(self,num):
        if num < 0: 
            print("Factorial de un número negativo no existe")

        # Manejo de caso de 0
        elif num == 0:
            return 1

        # Manejo de caso numero enteros positivos
        else: 
            fact = 1
            # Iteracion calculo factorial
            while(num > 1): 
                fact *= num 
                num -= 1
            return fact 

    def run(self):
        # Itera por el intervalo
        for num in range(self.min,self.max+1):
            # Calcula usando calcular_factorial(num)
            factorial = self.calcular_factorial(num)
            # Si existe lo escribe
            if factorial is not None:
                print(f"Factorial de {num} es {factorial}")


# Verificar si se proporciona un argumento en la línea de comandos
if len(sys.argv) == 1:
    # Si no se proporciona un argumento, solicitar al usuario que ingrese el rango
    while True:
        try:
            rango = input("Ingrese un rango (desde-hasta) para calcular los factoriales: ")
            # Caso -hasta
            if rango.startswith("-"):
                desde = 1
                hasta = int(rango.split("-")[1])
                break
            # Caso desde-
            elif rango.endswith("-"):
                desde = int(rango.split("-")[0])
                hasta = 15 #se utiliza 15 para no llenar la temrinal de numeros
                break
            # Caso desde-hasta
            if "-" in rango:
                desde, hasta = map(int, rango.split("-"))
                break
            # Levantar error
            else:
                raise ValueError
        except ValueError:
            print("Debe ingresar un rango válido en el formato 'desde-hasta', '-hasta' o 'desde-'.")
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
        hasta = 15 #se utiliza 15 para no llenar la temrinal de numeros
    # Caso desde-hasta
    elif "-" in rango:
        desde, hasta = map(int, rango.split("-"))

# Crear una instancia de la clase Factorial y ejecutar el cálculo
factoriador = Factorial(desde, hasta)
factoriador.run()



