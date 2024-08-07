# Diseñar un algoritmo que elimine todas las vocales que se encuentren en una lista de caracteres.
from lista import Lista
from random import randint

lista = Lista()

# Cargar Lista
for i in range(10):
    lista.insert(chr(randint(97, 122)))

lista.barrido()
print("")

for letra in ["a", "e", "i", "o", "u"]:
    while True:
        delete = lista.delete(letra)
        if delete != letra:
            break

print("Lista sin vocales")
lista.barrido()



