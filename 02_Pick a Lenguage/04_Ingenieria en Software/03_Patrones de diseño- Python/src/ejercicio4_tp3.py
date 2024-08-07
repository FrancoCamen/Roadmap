from __future__ import annotations
from abc import ABC, abstractmethod

class Creator(ABC):
    """
    Clase Abstracta que define metodos abstractos que sus subclases deben implementar.
    """
    @abstractmethod
    def factory_method(self, importe, condicion):
        pass

class ConcreteCreator1(Creator):
    """
    Contiene la implementacion para un tipo de Creator en concreto
    """
    #Obtiene el importe como argumento y lo utiliza para implementar el metodo heredado
    def factory_method(self, importe):
        print(f"El importe es {importe} y la condicion impositiva IVA responsable")

class ConcreteCreator2(Creator):
    """
    Contiene la implementacion para un tipo de Creator en concreto
    """
    #Obtiene el importe como argumento y lo utiliza para implementar el metodo heredado
    def factory_method(self, importe):
        print(f"El importe es {importe} y la condicion impositiva IVA no inscripto")
    
class ConcreteCreator3(Creator):
    """
    Contiene la implementacion para un tipo de Creator en concreto
    """
    #Obtiene el importe como argumento y lo utiliza para implementar el metodo heredado
    def factory_method(self, importe):
        print(f"El importe es {importe} y la condicion impositiva IVA exento")
    
def client_code(creator: Creator, importe):
    """
    Obtiene una instancia de Creator sin saber cual, pero ejecuta su metodo factory_method
    """
    print(f"{creator.factory_method(importe)}")

if __name__ == "__main__":

    print("\n\n")
    print("Generando factura con importe 700 y condicion impositiva IVA responsable")
    client_code(ConcreteCreator1(), 700)
    print("\n")

    print("Generando factura con importe 700 y condicion impositiva IVA no inscripto")
    client_code(ConcreteCreator2(), 700)
    print("\n")

    print("Generando factura con importe 700 y condicion impositiva IVA exento")
    client_code(ConcreteCreator3(), 700)
    