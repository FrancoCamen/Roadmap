# Determinar el número de ocurrencias de un determinado elemento en una pila.
from pila import Pila
from random import randint

stack = Pila();
stack_aux = Pila();

# Carga
for i in range(10):
    valor = randint(0,20);
    stack.push(valor);
    print(f"valor generado: {valor}")

# Determinar repeticiones
while stack.size() > 0:
    numero_comp = stack.pop();
    repeticiones = 1;
    while stack.size() > 0:
        numero = stack.pop();
        stack_aux.push(numero);
        if numero_comp == numero:
            repeticiones = repeticiones + 1;
    while stack_aux.size() > 0:
        stack.push(stack_aux.pop());
    if repeticiones != 1:
        print(f"El numero {numero_comp} se repite {repeticiones} veces");


