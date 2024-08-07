from cola import Cola
from random import randint

cola = Cola()
aux = Cola()

# Carga
for i in range(10):
    num = randint(1, 50)
    cola.arrive(num)

# Muestra valores de la cola
print("Valores de la cola")
for i in range(cola.size()):
    print(cola.move_to_end())



# for i in range(cola.size() - 1):
#     for j in range(cola.size() - 1 - i):
#         elemento1 = cola.atention()
#         elemento2 = cola.atention()

#         if elemento1 > elemento2:
#             cola.arrive(elemento1)
#             cola.arrive(elemento2)
#         else:
#             cola.arrive(elemento2)
#             cola.arrive(elemento1)
#     cola.arrive(cola.atention())

# # Muestra valores de la cola
# print("Valores de la cola")
# for i in range(cola.size()):
#     print(cola.move_to_end())

def ordenar_cola(cola):
    longitud = cola.size()
    for i in range(longitud - 1):
        for j in range(longitud - i -1):
            elemento1 = cola.atention()
            elemento2 = cola.atention()

            if elemento1 > elemento2:
                cola.arrive(elemento2)
                cola.arrive(elemento1)
            else:
                cola.arrive(elemento1)
                cola.arrive(elemento2)
        
        elemento_grande = cola.atention()
        cola.arrive(elemento_grande)

ordenar_cola(cola)
ordenar_cola(cola)
ordenar_cola(cola)
ordenar_cola(cola)
ordenar_cola(cola)
print("Cola ordenada:", [cola.atention() for _ in range(cola.size())])

