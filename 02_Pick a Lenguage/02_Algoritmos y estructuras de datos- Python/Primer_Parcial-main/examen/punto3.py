from pila import Pila

bitacora = Pila()
aux = Pila()

class Registros():
    def __init__(self, planeta, captura, costo):
        self.planeta = planeta
        self.captura = captura
        self.costo = costo

    def __str__(self):
        return f"{self.planeta} - {self.captura} - {self.costo}"

registros = [["Tatooine", "Han Solo", 100000],
             ["Coruscant", "Greedo", 50000],
             ["Endor", "Wicket W. Warrick", 25000],
             ["Hoth", "General Veers", 75000],
             ["Bespin", "Lando Calrissian", 1500],]

for registro in registros:
    bitacora.push(Registros(registro[0], registro[1], registro[2]))

print("___ Pila con los registros ___")
while bitacora.size() > 0:
    valor = bitacora.pop()
    print(valor)
    aux.push(valor)
while aux.size() > 0:
    bitacora.push(aux.pop())

# Muestra planetas visitados en orden
def mostrar_planetas(bitacora, aux):
    print("____ Planetas visitados en orden ____")
    while bitacora.size() > 0:
        valor = bitacora.pop()
        print(valor.planeta)
        aux.push(valor)
    while aux.size() > 0:
        bitacora.push(aux.pop())

# Determina creditos totales
def creditos(bitacora):
    total = 0
    while bitacora.size() > 0:
        valor = bitacora.pop()
        total = total + valor.costo
        aux.push(valor)
    while aux.size() > 0:
        bitacora.push(aux.pop())
    print(f"____ Los creditos obtenidos en total fueron {total} ____")

def cap_han(bitacora):
    lugar = 0
    planeta = ""
    while bitacora.size() > 0:
        lugar = bitacora.size()
        registro = bitacora.pop()
        if "Han Solo" == registro.captura:
            planeta = registro.planeta
            break
    while aux.size() > 0:
        bitacora.push(aux.pop())
    
    print(f"____ El numero de la mision donde fue capturado Han Solo fue la {lugar}, en el planeta {planeta} ____")

print()
mostrar_planetas(bitacora, aux)
print()
creditos(bitacora)
print()
cap_han(bitacora)
print



