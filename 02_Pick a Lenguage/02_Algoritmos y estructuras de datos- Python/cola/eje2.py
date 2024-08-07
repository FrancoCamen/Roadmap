from cola import Cola
from pila import Pila


cola = Cola()
pila= Pila()

for i in range(1, 11):
    valor = i
    cola.arrive(valor)
    print(f"Valor generado: {valor}")

while cola.size() > 0:
    pila.push(cola.atention())

while pila.size() > 0:
    cola.arrive(pila.pop())

while cola.size() > 0:
    print(cola.atention())

