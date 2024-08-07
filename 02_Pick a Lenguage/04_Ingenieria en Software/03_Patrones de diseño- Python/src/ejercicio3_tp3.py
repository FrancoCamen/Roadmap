"""
Genere una clase donde se instancie una comida rápida “hamburguesa” que
pueda ser entregada en mostrador, retirada por el cliente o enviada por
delivery. A los efectos prácticos bastará que la clase imprima el método de
entrega.
"""
from __future__ import annotations
from abc import ABC, abstractmethod

class Creator(ABC):
    """
    Declara el método de fábrica que se supone que debe devolver un
    objeto de una clase de Entrega. Las subclases de Creator proporcionan la
    implementación de este método.
    """
    @abstractmethod
    def factory_method(self):
        pass
    def some_operation(self) -> str:
        # Call the factory method to create a Entrega object.
        entrega = self.factory_method()

        # Now, use the product.
        resultado = f"Creator: {entrega.operation()}\n"

        return resultado
    
class ConcreteCreator1(Creator):
    """
    Note that the signature of the method still uses the abstract product type,
    even though the concrete product is actually returned from the method. This
    way the Creator can stay independent of concrete product classes.
    """
    def factory_method(self) -> Entrega:
        return ConcreteEntrega1()

class ConcreteCreator2(Creator):
    def factory_method(self) -> Entrega:
        return ConcreteEntrega2()
    
class ConcreteCreator3(Creator):
    def factory_method(self) -> Entrega:
        return ConcreteEntrega3()


class Entrega(ABC):
    """
    La interfaz Entrega declara las operaciones que todos las entregas concretas
    debe implementar.
    """
    @abstractmethod
    def operation(self) -> str:
        pass
"""
Concrete Entrega proporciona varias implementaciones de la interfaz de Entrega.
"""
class ConcreteEntrega1(Entrega):
    def operation(self) -> str:
        return "{Metodo de entrega: entrega en mostrador}"

class ConcreteEntrega2(Entrega):
    def operation(self) -> str:
        return "{Metodo de entrega: retiro por el cliente}"

class ConcreteEntrega3(Entrega):
    def operation(self) -> str:
        return "{Metodo de entrega: delivery}"


def client_code(creator: Creator) -> None:
    print(f"{creator.some_operation()}", end="")

if __name__ == "__main__":

    print("\n\n")
    print("Entregando hamburguesa n°1")
    client_code(ConcreteCreator1())
    print("\n")

    print("Entregando hamburguesa n°3")
    client_code(ConcreteCreator2())
    print("\n")

    print("Entregando hamburguesa n°3")
    client_code(ConcreteCreator3())


