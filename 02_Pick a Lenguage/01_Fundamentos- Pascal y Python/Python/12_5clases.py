class Restaurante:        

    def __init__(self, nombre, apellido, edad):    
        self.nombre = nombre  
        self.apellido = apellido
        self.__edad = edad  # Defaultd: public, _Protected, __Private
    
    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}, Apellido: {self.apellido}, Edad: {self.__edad}")
    
    def get_edad(self):
        print(self.__edad)
    def set_edad(self, edad):
        self.__edad = edad
    

#Crear una clase hijo de Restaurante
class Hotel(Restaurante):
    def __init__(self, nombre, apellido, edad):
        super().__init__(nombre, apellido, edad)

hotel = Hotel("5soles", "hospedaje", "5 años")
hotel.mostrar_informacion()