from cola import Cola
from random import randint

cola = Cola()

# Carga
for i in range(10):
    num = randint(1, 10)
    cola.arrive(num)

# Muestra valores de la cola
print("Valores de la cola")
for i in range(cola.size()):
    print(cola.move_to_end())


numero = int(input("De que valor de la cola desea obtener las ocurrencias?"))
ocurrencias = 0
for i in range(cola.size()):
    valor = cola.move_to_end()
    if numero == valor:
        ocurrencias += 1

if ocurrencias == 0:
    print("Este valor no tiene ocurrencias en la Cola")
else:
    print(f"El valor se repite {ocurrencias} veces en la Cola")




