# Invertir el contenido de una pila, solo puede utilizar una pila auxiliar como estructura extra
from pila import Pila
from random import randint

pila = Pila();
pila_invertida = Pila();

# Carga
for i in range(10):
    valor = randint(0,20);
    pila.push(valor);

# Ver valor on top de la pila
num = pila.on_top();
print(f"Valor on top de la pila {num}");

# Invertir valores
while pila.size() > 0:
    pila_invertida.push(pila.pop());

# Ver valor on top de la pila invertida
num = pila_invertida.on_top();
print(f"Valor on top de la pila invertida {num}");

# Ver pila invertida
while pila_invertida.size() > 0:
    print(pila_invertida.pop());


