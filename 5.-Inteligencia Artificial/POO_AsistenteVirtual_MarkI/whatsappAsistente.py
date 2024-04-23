#IMPORTACIÓN DE LIBRERÍAS:
import webbrowser   #webbrowser: Librería que permite abrir y utilizar navegadores web en Python.
import pyautogui    #pyautogui: Librería para controlar el mouse y teclado de la computadora con Python.
import time         #time: Librería del manejo de tiempos, como retardos, contadores, etc.

class widgetWhatsApp:
    #CONSTRUCTOR O INICIALIZADOR DE LA CLASE: En él se declaran los parámetros que recibe la clase, que además se 
    #utilizarán en los demás métodos, estos a fuerza deben tener un valor.
    #self: La instrucción self se utiliza para hacer referencia al objeto que se está manipulando cuando se instancía 
    #la clase. Por eso es que a través de la misma nomenclatura de un punto se accede a los distintos atributos y/o 
    #métodos con un objeto desde fuera de la clase.
    def __init__(self, parametro_de_la_clase):
        #ChatGPT API key
        self.contacto = parametro_de_la_clase
    
    def mandarMensaje(self, mensaje):
        respuestaWhatsApp = ""
        #Bucle for que recorre la respuesta del modelo de chat de OpenAI que viene en forma de lista para mandar cada 
        #línea de texto en un mensaje diferente, ya que no es posible de forma gratuita mandar todo el texto en un 
        #solo mensaje respetando los saltos de línea del texto.
        for i in range(len(mensaje)):
            #Solo en la primera línea de texto se abre el navegador y se espera que se habra bien para mandar el 
            #primer mensaje.
            if(i == 0):
                #webbrowser.open(): Método que abre el navegador web predeterminado del sistema operativo en la 
                #dirección URL especificada. El truco que se realiza para mandar mensajes de whatsapp es que la URL de 
                #su sitio permite ingresar el mensaje y teléfono de la persona a la que se busca mandar el WhatsApp.
                webbrowser.open(f"https://web.whatsapp.com/send?phone={self.contacto}&text={mensaje[i]}")
                #time.sleep(): Método que permite detener el programa cierto número de segundos.
                time.sleep(15)
                #pyautogui.press(): Método que simula presionar una tecla del teclado. El parámetro obligatorio que 
                #recibe es el nombre de la tecla, que puede ser una cadena o un valor ASCII. El método también acepta 
                #un parámetro opcional llamado interval, que especifica el intervalo de tiempo en segundos entre 
                #presionar la tecla y soltarla. 
                pyautogui.press("enter")
            #Los demás mensajes simplemente se mandar al introducir cada línea de mensaje en la página de Whatsapp 
            #Web y presionar rápidamente la tecla de enter después de introducir cada línea del mensaje.
            else:
                pyautogui.write(mensaje[i])
                pyautogui.press("enter")
        #Finalmente se espera un tiempo y se cierra el navegador donde se encuentra abierta la pestaña.
        pyautogui.write("----------------------MENSAJE DE T.I.M.M.Y. RECIBIDO CORRECTAMENTE----------------------")
        pyautogui.press("enter")
        time.sleep(2)
        respuestaWhatsApp = "Hola di0, ya te mandé un Whats con mi respuesta a tu cel."
        return respuestaWhatsApp