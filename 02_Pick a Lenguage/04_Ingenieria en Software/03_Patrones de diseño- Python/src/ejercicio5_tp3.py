import os
#*--------------------------------------------------------------------
#* La clase Director orquesta la construcción del objeto indicando 
#* el orden en que deben llamarse sus componentes, los mismos son
#* genéricos y dependerán del builder específico utilizado sus
#* valores concretos
#*--------------------------------------------------------------------
class Director:
   __builder = None
   
   def setBuilder(self, builder):
      self.__builder = builder
	   
   def getAvion(self):
      avion = Avion()
      
      # Primero el body
      body = self.__builder.getBody()
      avion.setBody(body)

      #Luego 2 turbinas
      i = 0
      while i < 2:
        turbina = self.__builder.getTurbina()
        avion.attachTurbina(turbina)
        i += 1

      #Luego 2 alas
      i = 0
      while i < 2:
        ala = self.__builder.getAla()
        avion.attachAla(ala)
        i += 1

      # Por ultima el tren de aterrizaje
      tren = self.__builder.getTren()
      avion.setTren(tren)

      # Retorna el vehiculo completo
      return avion

#*----------------------------------------------------------------
#* Esta es la definición de un objeto avion inicializando 
#* todos sus atributos
#*----------------------------------------------------------------
class Avion:
   def __init__(self):
      self.__turbina = list()
      self.__ala = list()
      self.__tren = None
      self.__body = None

   def setBody(self, body):
      self.__body = body

   def attachTurbina(self, turbina):
      self.__turbina.append(turbina)

   def attachAla(self, ala):
      self.__ala.append(ala)

   def setTren(self, tren):
      self.__tren = tren

   def specification(self):
      print ("chasis shape: "  + self.__body.shape)
      print ("turbinas potence:" + self.__turbina[0].potence)
      print ("tren modelo: " + self.__tren.modelo)
      print ("alas size: " + self.__ala[0].size)

#*-----------------------------------------------------------------
#* Builder
#* Clase genérica que solo define la interfaz de los métodos que el
#* Builder específico tiene que implementar
#*-----------------------------------------------------------------
class Builder:
	
      def getTren(self): pass
      def getAla(self): pass
      def getBody(self): pass
      def getTurbina(self): pass
      
#*-----------------------------------------------------------------
#* Esta es la hoja de ruta para construir un Avion
#* Establece instancias para tomar tren, ala, body y turbina
#* estableciendo las partes específicas que (en un Avion) 
#* deben tener esas partes
#*-------------------------------------------------------
class AvionBuilder(Builder):
   def getTren(self):
      tren = Tren()
      tren.modelo = "modelo 2.0"
      return tren
   
   def getAla(self):
      ala = Ala()
      ala.size = "25"
      return ala
   
   def getBody(self):
      body = Body()
      body.shape = "SUV"
      return body
   
   def getTurbina(self):
      turbina = Turbina()
      turbina.potence = "500hp"
      return turbina

#*----------------------------------------------------------------
#* Define partes genéricas para un Avion (sin inicializar)
#*----------------------------------------------------------------
class Tren:
   modelo = None

class Ala:
   size = None

class Body:
   shape = None

class Turbina:
   potence = None

#*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=
#* Esta es la estructura main()
#*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=
def main():

#*----------------------------------------------------------------
#* Instancia la clase que será el resultado y la que guiará el 
#* proceso de construcción
#*----------------------------------------------------------------
   avionBuilder = AvionBuilder() # initializing the class
   director = Director()

#*----------------------------------------------------------------
#* Pasa al director la hoja de ruta para construir un Avion
#*----------------------------------------------------------------   
   director.setBuilder(avionBuilder)

#*----------------------------------------------------------------
#* Ordena al director agregar los componentes de un Avion según
#* la hoja de ruta
#*----------------------------------------------------------------
   avion = director.getAvion()

#*---------------------------------------------------------------
#* Finalizada la construcción verifica que sea completa
#*---------------------------------------------------------------
   avion.specification()
   print ("\n\n")

#*----------------------------------------------------------------------
#* Se detecta el entry point y se lo deriva a una sección main() propia
#*----------------------------------------------------------------------
if __name__ == "__main__":
   os.system("clear")
   print("Ejemplo de un patrón de tipo builder aplicado a la construcción de un vehículo\n")

   main()