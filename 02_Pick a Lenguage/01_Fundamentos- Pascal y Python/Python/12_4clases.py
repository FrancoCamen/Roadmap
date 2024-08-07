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
    

#instanciar la clase   
restaurant = Restaurante("Franco", "Camen", 17)
#restaurant.__edad = 18  no se podra modificar xq es __PRIVATE
restaurant.mostrar_informacion()
restaurant.set_edad(18)
restaurant.get_edad()


restaurant2 = Restaurante("Julio", "Espinosa", 38)                 
restaurant2.mostrar_informacion()  
restaurant2.set_edad(39)
restaurant2.get_edad()
