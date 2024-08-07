# Dada una pila de letras determinar cuántas vocales contiene.
from pila import Pila
from random import randint

letras = Pila();
letras_aux = Pila();

# Carga de letras en la Pila
for i in range(10):
    letras.push(chr(randint(65, 90)))

# Muestra eltras de la Lista
print ("Letras generadas: ")
while letras.size() > 0:
    let = letras.pop();
    letras_aux.push(let);
    print(let);
while letras_aux.size() > 0:
    let = letras_aux.pop();
    letras.push(let);

# Contar vocales de la Pila
contador_vocales = 0
while letras.size() > 0:
    valor = letras.pop()
    if valor in ['A', 'E', 'I', 'O', 'U']:
        contador_vocales += 1
print(f'la cantidad de vocales son {contador_vocales}')