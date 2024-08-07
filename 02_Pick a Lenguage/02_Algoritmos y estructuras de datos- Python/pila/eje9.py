# Resolver el problema del factorial de un número utilizando una pila.
from pila import Pila

elementos = Pila()

numero = int(input("Ingrese el numero del que desea calcular su factorial "))

# Carga de numero hasta 1 en la pila elementos
for i in range(0,numero):
    elementos.push(numero-i)

# Resolver factorial
resultado = 1
while elementos.size() > 0:
    resultado = resultado*elementos.pop()

print(f"Resultado {resultado}")
