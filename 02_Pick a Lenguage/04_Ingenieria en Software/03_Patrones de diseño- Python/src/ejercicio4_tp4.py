class Component():
    
    def imprimir(self) -> int:
        pass

class Numero(Component):

    def operation(self, int) -> int:
        return int

class Decorator(Component):

    _component: Component = None

    def __init__(self, component: Component) -> None:
        self._component = component

    @property
    def component(self) -> Component:
        return self._component

    def operation(self, int):
        return self._component.operation(int)
    
class Sumarle2(Decorator):
    def operation(self, int):
        return self.component.operation(int) + 2

class MultiplicarPor2(Decorator):
    def operation(self, int):
        return self.component.operation(int) * 2

class DividirPor3(Decorator):
    def operation(self, int):
        return self.component.operation(int) / 3

def client_code(component: Component, num: int) -> None:

    print(f"Valor: {component.operation(num)}", end="")

if __name__ == "__main__":

    #Componenete simple: numero cualquiera
    numero = Numero()
    print("Se printea el numero base")
    client_code(numero, 3)
    print("\n")

    #Se le suma 2 usando un ConcreteDecorator
    print("Se lo multiplica por 2")
    multiplicar2 = MultiplicarPor2(numero)
    client_code(multiplicar2, 3)
    print("\n")
    print("Se le suma 2:")
    suma2 = Sumarle2(multiplicar2)
    client_code(suma2, 3)
    print("\n")
    print("Se lo multiplica por 2")
    multiplicar2 = MultiplicarPor2(suma2)
    client_code(multiplicar2, 3)
    print("\n")
    print("Se le suma 2:")
    suma2 = Sumarle2(multiplicar2)
    client_code(suma2, 3)
    print("\n")
    print("Se lo divide por 3")
    dividir3 = DividirPor3(suma2)
    client_code(dividir3, 3)
    print("\n")
   
    


    
    
    
