from pila import Pila
from random import randint
import re

# Pilas
vocales = Pila()
consonantes = Pila()
other = Pila()
aux = Pila()

# Cargar lista de consonantes
csnt = []
for i in range (65, 91):
    csnt.append(chr(i))
for i in range (97, 123):
    csnt.append(chr(i))



# texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut vestibulum metus sed ligula consectetur, sit amet malesuada ligula semper. Quisque orci metus, feugiat commodo tortor a, dictum 9 sollicitudin augue. Fusce porttitor finibus tortor sit amet consequat. Morbi sollicitudin eleifend neque gravida hendrerit. Aliquam eget purus sagittis, condimentum zdui a, consequat magna."
texto = input("Ingresa un texto")
print(texto)

for i in range(0,len(texto)-1):
    caracter = texto[i]
    if caracter in ['A', 'E', 'I', 'O', 'U', "a", "e", "i", "o", "u"]:
        vocales.push(caracter)
    elif caracter in csnt:
        consonantes.push(caracter)
    else:
        other.push(caracter)

# Cantidad de caracteres en cada pila
print()
print(f"Cantidad de vocales: {vocales.size()}")
print()
print()
print(f"Cantidad de consonantes: {consonantes.size()}")
print()
print()
print(f"Cantidad de otros caracteres: {other.size()}")
print()

# Cantida de espacios en blanco
print()
espacios = 0;
while other.size() > 0:
    element = other.pop()
    if element == " ":
        espacios += 1
    aux.push(element)
while aux.size() > 0:
    other.push(aux.pop())
if espacios != 0:
    print(f"Hay {espacios} espacios en blanco")
else:
    print("No hay espacios en blanco dentro del texto")
print()

# Porcentaje
print()
porcentaje = "{:.2f}".format(((vocales.size()/len(texto)*100)))
print(f"Las vocales representan un {porcentaje}% del texto")
porcentaje = "{:.2f}".format(((consonantes.size()/len(texto)*100)))
print(f"Las consonantes representan un {porcentaje}% del texto")
print()

# Contar numero
print()
contador = 0;
while other.size() > 0:
    element = other.pop()
    if re.search(r'\d+', element):
        contador += 1
    aux.push(element)
while aux.size() > 0:
    other.push(aux.pop())
if contador == 0:
    print("No hay numeros en el texto")
else:
    print(f"Hay {contador} numeros dentro del texto")
print()

# Comparan cantidad de vocales y otros caracteres
print()
if vocales.size() == other.size():
    print("La cantidad de vocales y de otros caracteres son iguales")
else:
    print("La cantidad de vocales y de otros caracteres no son iguales")
print()

# Ver si existe alguna z en el texto
contador = 0
while consonantes.size() > 0:
    element = consonantes.pop()
    if element == "z" or element == "Z":
        contador += 1
    aux.push(element)
while aux.size() > 0:
    consonantes.push(aux.pop())
if contador == 0:
    print("No hay ´Z´ en el texto")
else:
    print(f"Existen {contador} ´Z´ en el texto")

