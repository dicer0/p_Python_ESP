# -*- coding: utf-8 -*-

#En Python se introducen comentarios de una sola linea con el simbolo #.
#La primera línea de código incluida en este programa se conoce como declaración de codificación o codificación 
#de caracteres. Al especificar utf-8 (caracteres Unicode) como la codificación, nos aseguramos de que el archivo 
#pueda contener caracteres especiales, letras acentuadas y otros caracteres no ASCII sin problemas, garantizando 
#que Python interprete correctamente esos caracteres y evite posibles errores de codificación.
#Se puede detener una ejecución con el comando [CTRL] + C puesto en consola, con el comando "cls" se borra su 
#historial y en Visual Studio Code con el botón superior derecho de Play se corre el programa.
#Para comentar en Visual Studio Code varias líneas de código se debe pulsar:
#[CTRL] + K (VSCode queda a la espera). Después pulsa [CTRL] + C para comentar y [CTRL] + U para descomentar.

#IMPORTACIÓN DE LIBRERÍAS:
import io       #io: Librería que permite la manipulación de los archivos y carpetas de nuestro ordenador.
#AudioSegment: Clase de la librería pydub que permite tomar el audio que perciba el micrófono del ordenador y 
#luego que eso se pueda convertir en un archivo mp3 o wav.
import pydub    #pydub: Librería para procesar y exportar a un archivo datos de audio.
import speech_recognition as sr #sr: Librería que permite recabar audio del micrófono en tiempo real.
import whisper  #whisper: Librería de OpenAI que permite hacer la transcripción de audio o video a texto.
import tempfile #tempfile: Librería que crea y maneja archivos temporales.
import os       #os: Librería que permite acceder a funciones y métodos relacionados con el sistema operativo.
import pyttsx3  #pyttsx3: Biblioteca que sirve para generar una voz disponible en el sistema operativo.
#pywhatkit: Pywhatkit es una biblioteca de Python que permite enviar mensajes de texto a través de WhatsApp 
#incluso si no estás en su lista de contactos, realizar búsquedas en la web, reproducir canciones en YouTube, 
#realizar búsquedas en Wikipedia, ejecutar comandos en consola, etc.
import pywhatkit 

#CREACIÓN DE ARCHIVO TEMPORAL:
#tempfile.mkdtemp(): El método mkdtemp() crea un directorio temporal en la carpeta predeterminada del sistema 
#operativo, la cual es llamada temp y es una ubicación en el sistema operativo donde se almacenan archivos 
#temporales generados por diversas aplicaciones y procesos.
archivoTemporal = tempfile.mkdtemp()
#os.path.join(): El método join() se utiliza para unir varios componentes de ruta (variables y constantes) en 
#una sola ruta. Esto se utilizará para crear el archivo wav o mp3 que guardará un pedazo de la instrucción del 
#usuario. Cabe mencionar que WAV es un formato de archivo de audio sin pérdidas, lo que significa que todos los 
#datos de audio originales se conservan. Esto hace que los archivos WAV sean de mayor calidad que los archivos 
#MP3, pero también los hace más grandes y pesados.
rutaArchivo = os.path.join(archivoTemporal, 'audioTemporal.wav')
print("Esta es la ruta del archivo temporal de las instrucciones recibidas en audio:\n" + str(rutaArchivo))

#RECONOCIMIENTO DE LAS INSTRUCCIONES DADAS AL USUARIO:
#speech_recognition.Recognizer(): El objeto Recognizer() se utiliza para crear un reconocedor de voz, el cual 
#puede utilizarse para reconocer instrucciones dadas al asistente virtual por medio del habla humana.
listenerInstrucciones = sr.Recognizer()

#VOZ UTILIZADA POR EL ASISTENTE VIRTUAL:
#pyttsx3.init(): El método pyttsx3.init() se utiliza para inicializar el motor de texto a voz, el cual dará la 
#habilidad de hablar al asistente virtual, convirtiendo el texto retornado por el modelo de Whisper en audio que 
#salga de la computadora.
motorVoz = pyttsx3.init()
#pyttsx3.init().getProperty("voices"): El método getProperty() se utiliza para obtener una lista de las voces 
#disponibles en el motor de texto a voz incluidos en el sistena operativo del ordenador.
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
motorVoz.setProperty("rate", 145)
motorVoz.setProperty("voice", voz_AsistenteVirtual[3].id)

#hablar(textoAsistente): Función propia que permite al asistente virtual hablar por medio de la bocina del 
#ordenador.
def hablar(textoAsistente):
    #pyttsx3.init().say(): El método say() se utiliza para convertir texto en audio y emitirlo a través del 
    #altavoz del sistema. 
    motorVoz.say(textoAsistente)
    #pyttsx3.init().runAndWait(): El método runAndWait() bloquea la ejecución del programa hasta que el motor 
    #de texto a voz haya terminado de hablar.
    motorVoz.runAndWait()

#escuchaInstrucciones(textoAsistente): Función propia que se encarga de escuchar y reconocer el audio por medio 
#del micrófono del ordenador las palabras dichas por el usuario, esto se tarda un poco en cargar la primera vez 
#que se corre el programa debido a que el método speech_recognition.Recognizer().listen() necesita un tiempo para 
#inicializarse y configurarse; si se está utilizando una computadora con poca potencia o micrófonos de baja 
#calidad, es posible que se necesite esperar más tiempo.
def escuchaInstrucciones():
    #MANEJO DE EXCEPCIONES: Es una parte de código que se conforma de dos partes, try y except: 
    # - Primero se ejecuta el código que haya dentro del try y si es que llegara a ocurrir una excepción durante 
    #   su ejecución, el programa brinca al código del except.
    # - En la parte de código donde se encuentra la palabra reservada except, se ejecuta cierta acción cuando 
    #   ocurra el error esperado. 
    #Se utiliza esta arquitectura de código cuando se quiera efectuar una acción donde se espera que pueda 
    #ocurrir un error durante su ejecución.
    try:
        #with as source: La instrucción with se utiliza para definir una variable que tiene asignada un método 
        #o recurso específico, el cual puede ser un archivo, una conexión a una base de datos, la cámara, 
        #micrófono o cualquier otro objeto que requiera ser cerrado. La palabra clave as se utiliza para asignar 
        #dicho recurso a una variable que puede utilizarse para acceder al recurso dentro del bloque with. 
        #Dentro del manejo de excepciones la instrucción with as source: asegura que se cierre el recurso, 
        #incluso si se produce un error dentro del bloque try.
        #speech_recognition.Microphone(): El objeto Microphone puede utilizarse para grabar audio. 
        with sr.Microphone() as microfono:
            print("\n\n----------Hola soy T.I.M.M.Y. Mark I tu asistente virtual, en que te puedo ayudar?...---------")
            #speech_recognition.Recognizer().adjust_for_ambient_noise(): El método adjust_for_ambient_noise() 
            #sirve para aplicar un filtro a la señal de sonido que quite el ruido de fondo recibido en su 
            #parámetro.
            listenerInstrucciones.adjust_for_ambient_noise(microfono)
            print("Quitando ruido de fondo... ya puedes hablar.")
            #speech_recognition.Recognizer().listen(): El método listen() sirve para poder escuchar de una 
            #fuente de audio en tiempo real y convertirlo a texto, para ello primero se tuvo que haber 
            #instanciado la clase Recognizer.
            textoInstruccionUsuario = listenerInstrucciones.listen(microfono)
            print("Microfono encendido y escuchando...")
            #io.BytesIO(): Método que sirve para crear un flujo de bytes en memoria que puede utilizarse para 
            #almacenar datos binarios, como imágenes, audio y video.
            #speech_recognition.Recognizer().listen().get_wav_data(): El método get_wav_data() se utiliza para 
            #almacenar el texto recibido en el micrófono del ordenador en un flujo de datos binarios que se 
            #puedan guardar en un archivo de audio con extensión wav.
            datosAudio = io.BytesIO(textoInstruccionUsuario.get_wav_data())
            #pydub.AudioSegment().from_file(): El método from_file() perteneciente a la clase AudioSegment se 
            #utiliza para cargar solamente los datos de audio donde se escuche la voz del usuario, logrando así 
            #que no se haga nada cuando el usuario está en silencio. 
            archivoAudio = pydub.AudioSegment.from_file(datosAudio)
            print("Mandando texto del microfono a un archivo de audio wav...")
            #pydub.AudioSegment().from_file().export(path, file_type): Lo que hace el método export() es 
            #exportar un segmento de audio a un archivo.
            archivoAudio.export(rutaArchivo, format = 'wav')
            print("Texto del microfono guardado en un archivo de audio temporal tipo wav...")
    #Para identificar el tipo de excepción que ha ocurrido y utilizarlo en la instrucción except, se puede 
    #utilizar la clase Exception, que es una clase incorporada en Python utilizada para describir todos los 
    #tipos de excepciones, luego de colocar el nombre de la clase Exception se usa la palabra reservada "as" 
    #seguida de un nombre de variable, esto nos permitirá acceder a la instancia de la excepción y utilizarla 
    #dentro del except.
    except Exception as error:
        print(error)
    #Se retorna la ruta del archivo de la función porque de ahí extraerá el archivo de audio el modelo Whisper
    #para procesarlo.
    return rutaArchivo

#transcripcionWhisper(): Función propia que se encarga de recibir el archivo de audio recortado que contiene 
#la instrucción mandada al asistente virtual para pasársela al modelo de Whisper para que la transcriba a texto.
def transcripcionWhisper(audioRecortado):    
    #whisper.load_model(): Con el método load_model() se pueden cargar los diferentes modelos de lenguaje de la 
    #librería whisper, si se elige un modelo muy simple, se tendrá un peor desempeño, pero mientras más complejo 
    #sea el modelo, más se tardará en procesar el audio, a esto dentro de la librería se le llama Parameter y 
    #Relative Speed, donde a un mayor número de parámetros, se tendrá mayor capacidad de aprendizaje en el 
    #modelo y la velocidad relativa indica la rapidez con la que el modelo puede generar texto, esta se calcula 
    #dividiendo el tiempo que tarda el modelo en generar una palabra entre el número de palabras que genera. Las 
    #características de los modelos disponibles son las siguientes:
    # - tiny:   Parameter = 39M,    Memoria que consume = 1GB   y Relative Speed = 32x.
    # - base:   Parameter = 74M,    Memoria que consume = 1GB   y Relative Speed = 16x.
    # - small:  Parameter = 244M,   Memoria que consume = 2GB   y Relative Speed = 6x.
    # - medium: Parameter = 769M,   Memoria que consume = 5GB   y Relative Speed = 2x.
    # - large:  Parameter = 1550M,  Memoria que consume = 10GB  y Relative Speed = 1x.
    #Cuando el programa sea ejecutado por primera vez empezará a descargar el modelo para poderlo utilizar, este 
    #proceso tarda un poco en terminar, pero después identificará por sí solo el lenguaje y las palabras dichas 
    #en el audio, no importando si este tenga ruido o si es de alguna canción con instrumentos detrás. 
    Modelo = whisper.load_model("small")
    #whisper.load_model().transcribe(): El método transcribe() sirve para escuchar el audio de un archivo y 
    #transcribirlo a texto a través del modelo elegido con el método load_model(). El proceso de carga tarda un 
    #poco y el tiempo que el modelo se tarda en procesar el audio depende de su duración. Los parámetros que 
    #recibe el método son la ubicación del archivo de audio que quiere transcribir y el parámetro fp16 que 
    #indica si el cálculo se realizará en formato de punto flotante de 16 bits (FP16), pero como en algunas CPUs 
    #no se admite esta funcionalidad, se coloca como False, por lo que se está utilizando punto flotante de 32 
    #bits (FP32) en su lugar. Además cabe mencionar que el audio escuchado por el método será recortado en 
    #cachos de 30 segundos y estos serán igualmente divididos en pedazos.
    TranscripcionAudio_a_Texto = Modelo.transcribe(audioRecortado, language = "spanish", fp16 = False)
    print("Interpretando texto guardado en un archivo temporal de audio wav con el modelo Whisper...\t")
    #whisper.load_model().transcribe()["text"]: Texto traducido por Whisper de un archivo de audio.
    return TranscripcionAudio_a_Texto["text"]

#__name__ == __main__: Método main, esta función es super importante ya que sirve para instanciar las clases del 
#programa y ejecutar sus métodos, en python pueden existir varios métodos main en un solo programa, aunque no es 
#una buena práctica.
if (__name__ == "__main__"):
    hablar("Hola soy TIMI Mark 1, tu asistente virtual, puedo mimetizar tu voz y reproducir canciones en YoTube, en que te puedo ayudar?")
    while True:
        try:
            respuestaAsistenteVirtual = transcripcionWhisper(escuchaInstrucciones())
            hablar(respuestaAsistenteVirtual)
            print(respuestaAsistenteVirtual)
            #Si se reconoce que el usuario dice bye Timmy, se rompe el bucle while y se termina la ejecución del 
            #programa.
            if (respuestaAsistenteVirtual == " Adiós, Timmy." or respuestaAsistenteVirtual == " Bye, Timmy." or respuestaAsistenteVirtual == " Adiós, tímí." or respuestaAsistenteVirtual == " Adiós, Timí." or respuestaAsistenteVirtual == " Adiós, teamy."):
                hablar("Bye di0, un gusto haberte ayudado...")
                print("---------------------------Bye di_cer0, un gusto haberte ayudado...---------------------------")
                break
            #Si se reconoce que el usuario dice la palabra reproduce, el asistente virtual por medio de la librería 
            #pywhatkit reproduce el video que el usuario dijo en YouTube.
            elif (("reproduce" or "Reproduce") in respuestaAsistenteVirtual):
                #.replace().lower(): Lo que hace el método replace() es reemplazar todas las palabras que 
                #aparezcan en un string en otra cadena específica y el método lower() sirve para convertir todas 
                #las letras de una cadena en minúsculas, esto es importante hacerlo porque al reproducir una 
                #canción o mandar una búsqueda a internet, siempre es mejor tener puras minúsculas. 
                cancionYoutube = respuestaAsistenteVirtual.replace('reproduce', '').lower()
                hablar("Ok di0, voy a reproducir una canción del artista que pediste en YouTube")
                #pywhatkit.playonyt(): El método playonyt() de la librería pywhatkit permite  reproducir un 
                #video de YouTube en el navegador web predeterminado del sistema.
                pywhatkit.playonyt(cancionYoutube)
                print("----------Ok di_cer0, ya reproducí la canción del artista que pediste en YouTube...-----------")
        except Exception as errorEjecucion:
            hablar("Lo siento, no escuché bien lo que dijiste debido a este error...")
            print(errorEjecucion)
            continue
#El límite de la duración de audio que puede procesar T.I.M.M.Y. en las instrucciones que se le manda es de 15 
#segundos y el Mark I en sus respuestas tiene un delay de:
# - tiny:   Delay de 2  segundos cuando le mando un comando hablado usando el comando.
# - base:   Delay de 5  segundos cuando le mando un comando hablado usando el comando.
# - small:  Delay de 10 segundos cuando le mando un comando hablado usando el comando.