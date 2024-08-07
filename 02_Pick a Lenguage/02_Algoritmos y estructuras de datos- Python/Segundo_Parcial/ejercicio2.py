
from grafo import Grafo
from random import randint
grafo = Grafo(dirigido=False)

# Carga de los personajes
personajes = ["Luke Skywalker",
             "Darth Vader", 
             "Yoda", 
             "Boba Fett", 
             "C 3PO", 
             "Princess Leia", 
             "Rey", 
             "Kylo Ren", 
             "Chewbacca", 
             "Han Solo", 
             "R2 D2", 
             "BB 8"
             ]
for personaje in personajes:
    grafo.insert_vertice(personaje)


def ejercice_a():
    j=0
    for personaje in personajes:
        pos = grafo.search_vertice(personaje)
        point = grafo.get_element_by_index(pos)

        if point[1].size() < 4:
            k = 0
            while j == 0:
                if k >= len(personajes):
                    j=1
                else:
                    place = personajes[k]
                    posb = grafo.search_vertice(place)
                    pointb = grafo.get_element_by_index(posb)
                    checker = grafo.is_adyacent(point[0],pointb[0])
                    grafo.mark_as_not_visited()
                    if pointb[1].size() < 3 and point[0] != pointb[0] and checker == False:
                        value = randint(1, 20)
                        grafo.insert_arist(point[0], pointb[0], value)
                        if point[1].size() == 3:
                            j=1
                    k += 1
            j=0

ejercice_a()

grafo.barrido()
tree_min = grafo.kruskal()

i=0
def ejercice_BC():
    max_value = 0
    max_node = list
    for tree in tree_min:
        print("Arbol Minimo")
        for node in tree.split(";"):
            value = node.split("-")
            print(node)
            if value[0]=="Yoda" or value[1]=="Yoda":
                i = 1
            if int(value[2])>max_value:
                max_node = value
        if i ==1:
            print("Yoda existe en el arbol minimo")
            print(f"Esta es la arista de valor maximo {max_node[0]} y {max_node[1]} comparten {max_node[2]} episodios")
ejercice_BC()