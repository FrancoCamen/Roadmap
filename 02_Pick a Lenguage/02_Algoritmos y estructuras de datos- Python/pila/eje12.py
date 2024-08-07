# Dada una pila con nombres de los personajes de la saga de Star Wars, implemente una función que permita determinar si Leia Organa o Boba Fett están en dicha pila sin perder los datos.
from pila import Pila

personajes = Pila();
aux = Pila();
resultado = 0     

# Carga de la Pila con personajes
personajes.push("Luke Skywalker")
personajes.push("Darth Vader")
personajes.push("Leia Organa")
personajes.push("Han Solo")
personajes.push("Obi-Wan Kenobi")
personajes.push("Yoda")
personajes.push("Rey")
personajes.push("Kylo Ren")
personajes.push("Chewbacca")
personajes.push("R2-D2")

# Muestra la pila de Personajes
print ("Personajes de Star Wars: ")
while personajes.size() > 0:
    p = personajes.pop();
    aux.push(p);
    print(p);
while aux.size() > 0:
    p = aux.pop();
    personajes.push(p);

# Busca los personajes
while personajes.size() > 0:
    personaje = personajes.pop()
    if personaje == "Leia Organa":
        resultado += 1
    elif personaje == "Boba Fett":
        resultado += 2
    aux.push(personaje)

if resultado == 1:
    print("Leia Organa se encuentra dentro de la Pila")
elif resultado == 2:
    print("Boba Fett se encuentra dentro de la Pila")
elif resultado == 3:
    print("Boba Fett y Leia Organa se encuentra dentro de la Pila")
else:
    print("Ninguno de los personajes buscados se encuentra en la Pila")


