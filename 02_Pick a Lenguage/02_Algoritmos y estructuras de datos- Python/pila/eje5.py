# Determinar si una cadena de caracteres es un palíndromo.
from pila import Pila
from random import randint

stack = Pila();

cadena = input("Ingrese cadena de caracteres");

# Carga de la cadena en una pila
for i in range (0, len(cadena)):
    stack.push(cadena[i]);

coincidencias = 0;
# Compa la cadena desde su ultima posicion hasta la primera con la pila 
while stack.size() > 0:
    letra = stack.pop();
    if letra == cadena[stack.size()]:
        coincidencias = coincidencias + 1;

if coincidencias == len(cadena):
    print("La palabra es un palindromo");
else:
    print("La palabra no es palindromo");





