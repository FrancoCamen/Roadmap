# Se tienen dos pilas con personajes de Star Wars, en una los del episodio V de “The empire strikes back” y la otra los del episodio VII “The force awakens”. Desarrollar un algoritmo que permita obtener la intersección de ambas pilas, es decir los personajes que aparecen en ambos episodios
from pila import Pila

episodioV = Pila()
episodioVII = Pila()
auxV= Pila()
auxVII = Pila()
interseccion = Pila()


# Carga episodioV
episodioV.push("Luke Skywalker")
episodioV.push("Darth Vader")
episodioV.push("Princess Leia Organa")
episodioV.push("Han Solo")
episodioV.push("Chewbacca")
episodioV.push("Yoda")
episodioV.push("Lando Calrissian")
episodioV.push("Obi-Wan Kenobi")
episodioV.push("C-3PO")
episodioV.push("R2-D2")
# Carga episodioVII
episodioVII.push("Rey")
episodioVII.push("Finn")
episodioVII.push("Poe Dameron")
episodioVII.push("Kylo Ren")
episodioVII.push("General Leia Organa")
episodioVII.push("Han Solo")
episodioVII.push("Chewbacca")
episodioVII.push("Supreme Leader Snoke")
episodioVII.push("General Hux")
episodioVII.push("BB-8")

# Mostar ambas pilas
print("Personajes episodio V")
while episodioV.size()>0:
    personaje = episodioV.pop()
    print(personaje)
    auxV.push(personaje)
while auxV.size()>0:
    episodioV.push(auxV.pop())
print()
print("Personajes episodio VII")
print()
while episodioVII.size()>0:
    personaje = episodioVII.pop()
    print(personaje)
    auxVII.push(personaje)
while auxVII.size()>0:
    episodioVII.push(auxVII.pop())

# Interseccion entre ambas
while episodioV.size()>0:
    personajeV = episodioV.pop()
    while episodioVII.size()>0:
        personajeVII = episodioVII.pop()
        if personajeV == personajeVII:
            interseccion.push(personajeV)
        auxVII.push(personajeVII)
    while auxVII.size()>0:
        episodioVII.push(auxVII.pop())
    auxV.push(personajeV)
while auxV.size()>0:
    episodioV.push(auxV.pop())

print()
if interseccion.size() == 0:
    print("No hay personajes en comun en los episodios")
else:
    print(f"Los personajes en comun son: ")
    while interseccion.size()>0:
        print(interseccion.pop())
