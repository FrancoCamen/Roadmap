from cola import Cola
from pila import Pila
from random import randint

cola = Cola()
pila= Pila()

palabra = input("Ingrese palabra")

for i in range(len(palabra)):
    cola.arrive(palabra[i])
    print(f"Valor generado: {palabra[i]}")

for i in range (cola.size()):
    valor = cola.move_to_end()
    pila.push(valor)

palindromo = "no"
while cola.size() > 0:
    valor1 = cola.atention()
    valor2 = pila.pop()
    if valor1 != valor2:
        print("La palabra no es palidromo")
        palindromo = "no"
        break
    else:
        palindromo = "si"

if palindromo == "si":
    print("La palabra es palindromo")

