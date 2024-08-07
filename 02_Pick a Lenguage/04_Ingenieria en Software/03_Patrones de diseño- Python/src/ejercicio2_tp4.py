from __future__ import annotations
from abc import ABC, abstractmethod

class Lamina:
    """
    Abstraccion que debe si o si implementar un lamindor en su constructor.
    """
    def __init__(self, laminador: Laminador) -> None:
        self.laminador = laminador
    
    def laminar(self) -> str:
        return (f"Lamina cortada con:\n"
                f"{self.laminador.producir_lamina()}")



class Laminador(ABC):
    """
    Laminador es la clase abstracta que funciona como implementacion abstracta de cada laminador.
    """
    @abstractmethod
    def producir_lamina(self) -> str:
        pass

"""
Laminadores concretos, cada uno con una diferente implementacion del metodo laminar
"""
class LaminadorConcreto1(Laminador):
    def producir_lamina(self) -> str:
        return "Laminador 1: genera planchas de 5 metros"

class LaminadorConcreto2(Laminador):
    def producir_lamina(self) -> str:
        return "Laminador 2: genera planchas de 10 metros"
    

#Ejecuta el metodo laminar de una lamina sin saber que implementacion utiliza
def client_code(lamina: Lamina) -> None:
    print(lamina.laminar())

if __name__ == "__main__":
    """
    Se instancian dos laminas que cada una implementa un laminador diferente
    """

    laminador1 = LaminadorConcreto1()
    lamina1 = Lamina(laminador1)
    client_code(lamina1)

    print("\n")

    laminador2 = LaminadorConcreto2()
    lamina2 = Lamina(laminador2)
    client_code(lamina2)



