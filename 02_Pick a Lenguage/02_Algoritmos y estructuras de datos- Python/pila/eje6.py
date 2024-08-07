# Leer palabra y visualizarla de forma inversa
from pila import Pila
from random import randint

stack = Pila();

palabra = input("Ingrese palabra");
print(f"Palabra ingresada: {palabra}");

# Cargar palabra en pila
for i in range(0, len(palabra)):
    stack.push(palabra[i]);

# Invertir palabra
palabra = "";
while stack.size() > 0:
    palabra =  palabra + f"{stack.pop()}";

# Mostar palabra invertida
print(f"Palabra invertida: {palabra}");


