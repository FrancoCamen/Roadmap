# Eliminar de una pila todos los elementos impares, es decir que en la misma solo queden números pares.
from pila import Pila
from random import randint

stack = Pila();
stack_aux = Pila();

# Carga
for i in range(10):
    valor = randint(0,20);
    stack.push(valor);
    print(f"valor generado: {valor}")

# Eliminar impares
while stack.size() > 0:
    numero = stack.pop();
    if numero % 2 == 0:
        stack_aux.push(numero);

# Carga pares y los muestra
print("Pila con numeros pares");
while stack_aux.size() > 0:
    numero = stack_aux.pop();
    stack.push(numero);
    print(numero);
    



