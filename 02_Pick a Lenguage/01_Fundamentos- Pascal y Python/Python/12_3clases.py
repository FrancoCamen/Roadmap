class Restaurante:        

    def __init__(self, nombre, apellido, edad):    
        self.nombre = nombre  
        self.apellido = apellido
        self.__edad = edad  # Defaultd: public, _Protected, __Private
    
    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}, Apellido: {self.apellido}, Edad: {self.__edad}")
    

#instanciar la clase   
restaurant = Restaurante("Franco", "Camen", 17)
restaurant.mostrar_informacion()
restaurant.__edad = 18  #no se podra modificar xq es __PRIVATE
print(restaurant.__edad)

restaurant2 = Restaurante("Julio", "Espinosa", 38)                 
restaurant2.mostrar_informacion()  
restaurant2.__edad = 39
print(restaurant2.__edad)