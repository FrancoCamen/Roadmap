"""
*----------------------------------------------------------*
#  Franco Leonardo Camen
#  Uader Fcyt IS2
#  Trabajo Practico 2
*----------------------------------------------------------*
"""
#Se importa libreria openai
from openai import OpenAI
# Define excepciones especificas
SPECIFIC_EXCEPTIONS = (ConnectionError, TimeoutError, ValueError, TypeError)
#Se guarda la api_key
import os
API_KEY = os.environ.get('API_KEY')
#Se instancia un objeto OpenAI y el pasamos la api_key
client = OpenAI(api_key=API_KEY)
def response(consult):
    """Funcion que genera el metodo para realizar la consulta y capturar la respuesta"""
    try:
        #Se usa metodo Completion para obtener la respuesta del modelo
        respuesta = client.chat.completions.create(
            model="gpt-3.5-turbo", #modelo de openai a usar
            messages= consult, #mensaje a enviar
            temperature=1, #controla la precision(0)-creatividad(100)
            max_tokens=100, #tokens maximos por respuesta
            top_p=1,
            frequency_penalty=0, #penaliza la repeticion de palabras en la respuesta
            presence_penalty=0, #penaliza repeticion de conceptos
        )
        #retorna message.content dentro de choices[0]
        return respuesta.choices[0].message.content
    except SPECIFIC_EXCEPTIONS as ex:
        #Si ocurre una excepcion la ejecucion salta a esta linea
        print("")
        print("Ha ocurrido una excepción:", ex)
        return ex
# Mensaje de bienvenida
print("Bienveniso a chatGPT. (Ingrese exit para salir)")
# Bucle principal
CONDICION = True
while CONDICION:
    #Almacena la consulta ingresada por el usuario
    print("")
    consulta = input("Ingrese su consulta:  ")
    #Verifica si consulta contiene una cadena str
    if isinstance(consulta, str):
        #Si la consulta es exit se cierra el script
        if consulta.lower() == "exit":
            break
        #Si se ingresa --convers se activa modo conversacion
        if "--convers" in consulta:
            print("")
            print("Modo de conversacion activado. Para salir ingrese --exit")
            #Almacena cada mensaje en forma de diccionario
            #{"role" : "user/system","content" : con/res}
            historial_conversacion = []
            #Bucle para el modo conversacion
            while True:
                #Almacena la consulta ingresada por el usuario
                consulta = input("Ingrese su consulta:  ")
                #Si la consulta contiene --exit se cierra el modo conversacion
                if "--exit" in consulta:
                    CONDICION = False
                    break
                #Carga la consulta al historial
                historial_conversacion.append({"role" : "user","content" : consulta})
                try:
                    #Obtiene una respuesta enviando el historial de la conversacion
                    respos = response(historial_conversacion)
                    #Carga la respuesta a el historial con rol de system
                    historial_conversacion.append({"role" : "system","content" : respos})
                    #Printea cada mensaje de la conversacion con You/chaGPT
                    for mensaje in historial_conversacion:
                        if mensaje["role"] == "system":
                            print("")
                            print("chaGPT: " + mensaje["content"])
                        else :
                            print("")
                            print("You: " + mensaje["content"])
                except SPECIFIC_EXCEPTIONS as e:
                    #Carga la respuesta a el historial como falllida
                    historial_conversacion.append(
                        {"role" : "system","content" : "Respuesta fallido. Reintente"}
                        )
                    print("")
                    print(
                        "Se produjo un error al procesar la consulta. Intente nuevamente."
                        )
        else:
            try:
                #Se llama a response enviandole la consulta del usuario
                respons = response([{"role" : "user", "content" : consulta}])
                #Printea message.content dentro de response.choices
                print("")
                print("chatGPT: " + respons)
            except SPECIFIC_EXCEPTIONS as e:
                print("Se produjo un error al procesar la consulta. Intente nuevamente. ")
                print("")
    else:
        print("")
        print("La consulta que ingreso es invalida. Intente nuevamente: ")
