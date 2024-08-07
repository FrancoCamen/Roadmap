import sys
sys.path.append('sources')
from singleton import SingletonMeta

class SingletonFactorial(metaclass=SingletonMeta):
    """
    La clase SingletonFactorial implementa el comportamiento singleton de la metaclase singleton meta.
    Permitiendo que solo exista una instancia de esta clase
    """
    #Este metodo realiza el calculo del factorial de un numero y retorna el resultado
    def calcular_factorial(self, numero):
        if numero < 0:
            raise ValueError("El numero ingresado es negativo. Intente nuevamente")
        elif numero == 0:
            self.factorial = 1
            return self.factorial
        else:
            self.factorial = numero * self.calcular_factorial(numero - 1)
            return self.factorial

if __name__ == "__main__":
    """
    Se instancia un objeto SingletonFactorial unico y se calcula factorial pasandole como parametro un numero
    """
    s1 = SingletonFactorial()
    resultado = s1.calcular_factorial(6)
    print(s1.factorial)






