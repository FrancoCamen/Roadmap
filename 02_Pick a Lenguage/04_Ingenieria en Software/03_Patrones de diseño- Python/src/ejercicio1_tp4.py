from abc import ABC, abstractmethod
import socket

class Ping(ABC):
    """
    La interfaz Ping declara operaciones comunes tanto para RealProxy como para
    el apoderado. Para que al trabajar on RealPing podeamos pasarle un proxy
    """
    @abstractmethod
    def ejecute(self, ip):
        pass

class RealPing(Ping):
    """
    Contiene la implementacion de la clase Ping.
    Esta clase seria el aplicativo o servicio de destino,
    con el cual interactuamos para generar la coneccion.
    """

    #Solo si la ip comienza con 192. realiza la coneccion
    def ejecute(self, ip):
        if ip.startswith("192."):
            self.ejecutefree(ip)
    
    #Realiza la coneccion sin checkear la ip
    #Printea resultado de la coneccion y un boolean
    def ejecutefree(self, ip):
        try:
            #socket crea una conexión TCP con un host remoto en un puerto específico.
            socket.create_connection((ip, 80), timeout=5)
            print("coneccion establecida")
            return True
        except Exception as e:
            print("No se pudo conectar:", e)
            return False

class Proxy(Ping):
    """
    Hace un checkeo de ip antes de llamar al metodo de RealPing para realizar la coneccion.
    Actua como intermediario entre el cliente y el RealPing
    """

    def __init__(self, real_ping: RealPing) -> None:
        self._real_ping = real_ping


    def ejecute(self, ip):
        #Si ckeck_ip es True se conecta a la ip de google.com sin comprobar ip
        if self.check_ip(ip):
            if self._real_ping.ejecutefree("172.217.167.196"):
                print("Coneccion con www.google.com")
        #De caso contrario se conecta a la ip checkeandola antes
        else:
            self._real_ping.ejecute(ip)

    #Checkea que la ip sea 192.168.0.254, retorna boolean
    def check_ip(self, ip):
        if ip == "192.168.0.254":
            return True
        else:
            return False

#Ejecuta el metodo ejecute sin saber nada del objeto que lo implementa
def client_code(ping: Ping, ip):
    ping.ejecute(ip)

if __name__ == "__main__":

    #Se instancia un RealPing
    real_ping = RealPing()
    #Se ejecuta client_code usando directamente el real_ping
    client_code(real_ping, "192.168.0.1")

    print("")

    #Se instancia un proxy con el objeto real_ping
    proxy = Proxy(real_ping)
    #Se ejecuta client_code para generar la coneccion pero usando un proxy de intermediario
    client_code(proxy, "192.168.0.254")
    

    