from cola import Cola
from random import randint

cola = Cola()

# Carga
for i in range(10):
    num = randint(1, 50)
    cola.arrive(num)

# Muestra valores de la cola
print("Valores de la cola")
for i in range(cola.size()):
    print(cola.move_to_end())

# Encontrar el valor mas grande
mayor = 0;
for i in range (cola.size()):
    valor = cola.move_to_end()
    if i == 0:
