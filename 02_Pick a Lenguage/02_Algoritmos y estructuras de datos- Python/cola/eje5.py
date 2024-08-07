from cola import Cola
from pila import Pila

cola = Cola()
pila = Pila()
pila_aux = Pila() #La pila auxiliar solo se usa para ver primeramente los valores de la pila sin perderlos, no para invertirlos

# Cargar pila
for i in range (10):
    valor = i
    print(f"valor: {i}")
    pila.push(i)

# Muestra valores de la pila
print("Valores de la pila")
while pila.size() > 0:
    valor = pila.pop()
    pila_aux.push(valor)
    print(valor)
while pila_aux.size() > 0:
    pila.push(pila_aux.pop())
    
# Desapila y arriva valores
while pila.size() > 0:
    valor = pila.pop()
    cola.arrive(valor)
# Atiende valores y los pushea
while cola.size() > 0:
    pila.push(cola.atention())

# Desapila valores para mostrarlos
print("Valores de la pila invertidos")
while pila.size() > 0:
    print(pila.pop())
