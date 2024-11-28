#IMPORTACIÓN DE LIBRERÍAS:
import pyttsx3  #pyttsx3: Biblioteca que sirve para generar una voz disponible en el sistema operativo.

#VOZ UTILIZADA POR EL ASISTENTE VIRTUAL:
#pyttsx3.init(): El método pyttsx3.init() se utiliza para inicializar el motor de texto a voz, el cual dará la 
#habilidad de hablar al asistente virtual, convirtiendo el texto retornado por el modelo de Whisper en audio que 
#salga de la computadora.
motorVoz = pyttsx3.init()
#pyttsx3.init().getProperty("voices"): El método getProperty() se utiliza para obtener una lista de las voces 
#disponibles en el motor de texto a voz incluidos en el sistema operativo del ordenador.
voz_AsistenteVirtual = motorVoz.getProperty("voices")
#Bucle for para mostrar todas las opciones de sintetizadores de voz disponibles en el sistema operativo, el 
#número de opciones dependerá de los lenguajes que pueda manejar el sistema operativo de la computadora que 
#digan text to speech y se pueden ver al ingresar a la opción de: Windows -> Configuración -> Hora e Idioma -> 
#Idioma y Región -> Idioma -> Idiomas que diga texto a voz. Si se quiere se podría agregar más idiomas.
for i in range(len(voz_AsistenteVirtual)):
    print(voz_AsistenteVirtual[i])
#pyttsx3.init().setProperty(): Este método toma dos parámetros y no devuelve ningún valor porque indica las 
#siguientes características del sintetizador de voz del asistente virtual:
# - name: El nombre de la propiedad que se desea establecer.
#   - rate:     Indica la velocidad de la voz en palabras por minuto.
#   - volume:   El volumen de la voz, de 0 a 1.
#   - voices:   Lista de todas las voces disponibles.
#   - voice:    La voz que se utilizará para hablar.
#   - langauge: El idioma que se utilizará para hablar.
#   - engine:   Controlador de voz que se utilizará.
#   - debug:    Variable booleana que indica si se debe habilitar el modo de depuración o no.
# - value: El valor de la propiedad que se desea establecer.
motorVoz.setProperty("rate", 190)
motorVoz.setProperty("voice", voz_AsistenteVirtual[3].id)

#vozWindows: Clase propia que utiliza una de las voces incluidas en los lenguajes descargados en el sistema 
#operativo Windows para lograr así que el asistente virtual hable.
class vozWindows:
    #hablar(textoAsistente): Función propia que permite al asistente virtual hablar por medio de la bocina del 
    #ordenador.
    def hablar(self, textoAsistente):
        #pyttsx3.init().say(): El método say() se utiliza para convertir texto en audio y emitirlo a través del 
        #altavoz del sistema. 
        motorVoz.say(textoAsistente)
        #pyttsx3.init().runAndWait(): El método runAndWait() bloquea la ejecución del programa hasta que el motor 
        #de texto a voz haya terminado de hablar.
        motorVoz.runAndWait()