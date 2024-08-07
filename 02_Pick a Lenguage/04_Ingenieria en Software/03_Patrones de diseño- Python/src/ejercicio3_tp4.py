from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

class Component(ABC):

    @property
    def parent(self) -> Component:
        return self._parent

    @parent.setter
    def parent(self, parent: Component):
        self._parent = parent

    def add(self, component: Component) -> None:
        pass

    def remove(self, component: Component) -> None:
        pass

    def is_composite(self) -> bool:
        return False

    @abstractmethod
    def operation(self) -> str:
        pass

class Leaf(Component):
    def operation(self) -> str:
        return "Pieza"

class Composite(Component):

    def __init__(self) -> None:
        self._children: List[Component] = []
    
    def add(self, component: Component) -> None:
        self._children.append(component)
        component.parent = self

    def remove(self, component: Component) -> None:
        self._children.remove(component)
        component.parent = None

    def is_composite(self) -> bool:
        return True
    
    def operation(self) -> str:
        results = []
        for child in self._children:
            results.append(child.operation())
        return f"Componentes ({' + '.join(results)})"
    
def client_code(component: Component) -> None:

    print(f"Piezas de ensamble: {component.operation()}", end="")

if __name__ == "__main__":

    print("\n")

    simple = Leaf()
    print("Generando una pieza simple:")
    client_code(simple)
    print("\n")


    #Utilizando composite para lista de piezas
    print("Lista de piezas de ensamblado: ")
    print("\n")
    principal = Composite()

    print("Se agrega el primer sub conjunto: ")
    conjunto1 = Composite()
    conjunto1.add(Leaf())
    conjunto1.add(Leaf())
    conjunto1.add(Leaf())
    conjunto1.add(Leaf())
    principal.add(conjunto1)
    client_code(principal)
    print("\n")
    
    print("Se agrega el segundo sub conjunto: ")
    conjunto2 = Composite()
    conjunto2.add(Leaf())
    conjunto2.add(Leaf())
    conjunto2.add(Leaf())
    conjunto2.add(Leaf())
    principal.add(conjunto2)
    client_code(principal)
    print("\n")

    print("Se agrega el tercer sub conjunto: ")
    conjunto3 = Composite()
    conjunto3.add(Leaf())
    conjunto3.add(Leaf())
    conjunto3.add(Leaf())
    conjunto3.add(Leaf())
    principal.add(conjunto3)
    client_code(principal)
    print("\n")






   




