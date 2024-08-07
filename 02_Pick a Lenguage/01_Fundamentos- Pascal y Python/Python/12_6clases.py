class Restaurante:        

    def __init__(self, nombre, apellido, edad):    
        self.nombre = nombre  
        self.apellido = apellido
        self.edad = edad  # Defaultd: public, _Protected, __Private
    
    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}, Apellido: {self.apellido}, Edad: {self.edad}")
    
    def get_edad(self):
        print(self.edad)
    def set_edad(self, edad):
        self.edad = edad
    
    

#Crear una clase hijo de Restaurante
class Hotel(Restaurante):
    def __init__(self, nombre, apellido, edad, pileta):
        super().__init__(nombre, apellido, edad)  #hace referencia a los atributos que usa del padre
        self.pileta = pileta
    
    #reescribir un metodo
    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}, Apellido: {self.apellido}, Edad: {self.edad}, Tiene pileta: {self.pileta}")
    
    #agregar un metodo que solo exista en hotel
    def get_pileta(self):
        return self.pileta


hotel = Hotel("5soles", "hospedaje", "5 años", "tiene pileta")
hotel.mostrar_informacion()
pileta = hotel.get_pileta()
print(pileta)