class Restaurante:        #primera letra de la clase en mayusculas

    def agregar_restaurante(self, nombre):    #las funciones en las clases se llaman metodos
        self.nombre = nombre  #atributo
    
    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")

#instanciar la clase   
restaurant = Restaurante()                 #esto es un objeto
restaurant.agregar_restaurante("Franco")   #llamando el metodo de la clase
                                           #self se pasa solo por eso solo definimos el segundo argumento
restaurant.mostrar_informacion()

restaurant2 = Restaurante()                 
restaurant2.agregar_restaurante("Julio")   
restaurant2.mostrar_informacion()

#otra forma de mostrar la info
print(f"Tu nombre es {restaurant.nombre}")
print(f"Tu nombre es {restaurant2.nombre}")


