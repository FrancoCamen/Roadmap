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

termino = int(input("Ingrese el termino i-nesimo despues del frente de la cola que desea eliminar"))

# Eliminar termino
for i in range(cola.size()):
    if i == termino:
        valor = cola.atention()
    else:
        valor = cola.move_to_end()

# Muestra valores de la cola
print("Valores de la cola")
for i in range(cola.size()):
    print(cola.move_to_end())



