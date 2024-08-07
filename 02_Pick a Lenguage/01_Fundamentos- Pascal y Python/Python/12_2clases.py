class Restaurante:        

    def __init__(self, nombre, apellido, edad):    
        self.nombre = nombre  
        self.apellido = apellido
        self.edad = edad
    
    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}, Apellido: {self.apellido}, Edad: {self.edad}")

#instanciar la clase   
restaurant = Restaurante("Franco", "Camen", 17)                
restaurant.mostrar_informacion()  

restaurant2 = Restaurante("Julio", "Espinosa", 38)                 
restaurant2.mostrar_informacion()   
