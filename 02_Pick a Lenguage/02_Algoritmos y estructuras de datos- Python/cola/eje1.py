from cola import Cola
from random import randint


cola = Cola()
cola_aux = Cola()

# Carga
for i in range(10):
    valor = chr(randint(65, 90))
    cola.arrive(valor)
    print(f"Valor generado: {valor}")

# Busca vocales, si el valor no es una vocal lo mueve al final de la cola
while cola.size() > 0:
    valor = cola.atention()
    if valor not in ["A", "E", "I", "O", "U"]:
        cola_aux.arrive(valor)

while cola_aux.size() > 0:
    cola.arrive(cola_aux.atention())


while cola.size() > 0:
    print(cola.atention())
