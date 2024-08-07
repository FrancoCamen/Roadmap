import sys
sys.path.append('sources')
from singleton import SingletonMeta

class Tax_singleton(metaclass=SingletonMeta):
    """
    La clase Tax_singleton implementa el comportamiento singleton de la metaclase singletonmeta.
    Permitiendo que solo exista una instancia de esta clase
    """
    #Metodo que calcula los diferentes taxs partiendo de un parametro base
    def calcular_tax(self, base):
        iva = base * 0.21
        iibb = base * 0.05
        muni = 0.012
        taxs = iva + iibb + muni
        return taxs

if __name__ == "__main__":

    tax1 = Tax_singleton()
    print(f"Calculo de impuestos : {tax1.calcular_tax(124)}")
