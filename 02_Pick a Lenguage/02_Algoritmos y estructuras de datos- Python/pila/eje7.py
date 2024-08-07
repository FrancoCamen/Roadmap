# Eliminar el i-ésimo elemento debajo de la cima de una pila de palabras.
from pila import Pila

pila_palabras = Pila();
pila_aux = Pila();

# Carga de la pila
for i in range(0, 10):
    palabra = "palabra" + f"{i}";
    pila_palabras.push(palabra);

# Mostramos elementos de la pila_palabra;
print ("Pila de palabras")
while pila_palabras.size() > 0:
    palabra = pila_palabras.pop();
    pila_aux.push(palabra);
    print(palabra);
while pila_aux.size() > 0:
    palabra = pila_aux.pop();
    pila_palabras.push(palabra);
    

# Posicion de la palabra que desea eliminar
i = pila_palabras.size();
while i > (pila_palabras.size()-1):
    i = int(input("Ingrese la posicion del i-ésimo elemento debajo de la cima de la pila que desea elimininar"));
    if i <= (pila_palabras.size()-1):
        break
    else:
        print("La posicion ingresada es mayor al tamaño de la pila");

# Desapilar palabras de pila_palabras hasta posicion i
for x in range(0, i+1):
    pila_aux.push(pila_palabras.pop());

# Cargamos elementos de pila_aux en pila_palabras menos el elemento i-ésimo
elemento_i_ésimo = pila_aux.pop();
while pila_aux.size() > 0:
    pila_palabras.push(pila_aux.pop());

# Mostramos elementos de pila_palabras
while pila_palabras.size() > 0:
    print(pila_palabras.pop());
