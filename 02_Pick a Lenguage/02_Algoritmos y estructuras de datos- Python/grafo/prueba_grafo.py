from grafo import Grafo

mi_grafo = Grafo(dirigido=False)

mi_grafo.insert_vertice('T')
mi_grafo.insert_vertice('F')
mi_grafo.insert_vertice('X')
mi_grafo.insert_vertice('R')
mi_grafo.insert_vertice('Z')

mi_grafo.insert_vertice('P')
mi_grafo.insert_vertice('J')
mi_grafo.insert_arist('P', 'J', 8)
mi_grafo.insert_arist('T', 'R', 8)
mi_grafo.insert_arist('T', 'F', 3)
mi_grafo.insert_arist('T', 'X', 6)
mi_grafo.insert_arist('F', 'R', 2)
mi_grafo.insert_arist('F', 'X', 2)
mi_grafo.insert_arist('X', 'Z', 9)
mi_grafo.insert_arist('X', 'R', 5)
mi_grafo.insert_arist('R', 'Z', 4)

mi_grafo.barrido()
# origen = 'A'
# destino = 'Z'