#IMPORTACIÓN DE LIBRERÍAS:
import io       #io: Librería que permite la manipulación de los archivos y carpetas de nuestro ordenador.
#AudioSegment: Clase de la librería pydub que permite tomar el audio que perciba el micrófono del ordenador y 
#luego que eso se pueda convertir en un archivo mp3 o wav.
import pydub    #pydub: Librería para procesar y exportar a un archivo datos de audio.
import speech_recognition as sr #sr: Librería que permite recabar audio del micrófono en tiempo real.
import whisper  #whisper: Librería de OpenAI que permite hacer la transcripción de audio o video a texto.
import tempfile #tempfile: Librería que crea y maneja archivos temporales.
import os       #os: Librería que permite acceder a funciones y métodos relacionados con el sistema operativo.

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

#EscucharMicrofono: Clase propia para escuchar las instrucciones del usuario por medio del micrófono y almacenar 
#eso en un archivo temporal, luego se transcribirá ese archivo de audio a texto a través del modelo Whisper y 
#finalmente el texto resultante será transformado a minúsculas para que sea interpretado por el programa.
class EscucharMicrofono:
    #POO: En Python cuando al nombre de una función se le ponen dos guiones bajos antes de su nombre es porque 
    #se está refiriendo a un método privado, es una buena práctica de sintaxis.
    #__escuchaInstrucciones(textoAsistente): Función propia y con modificador de acceso privado que se encarga 
    #de escuchar y reconocer el audio por medio del micrófono del ordenador las palabras dichas por el usuario, 
    #esto se tarda un poco en cargar la primera vez que se corre el programa debido a que el método 
    #speech_recognition.Recognizer().listen() necesita un tiempo para inicializarse y configurarse; si se está 
    #utilizando una computadora con poca potencia o micrófonos de baja calidad, es posible que se necesite 
    #esperar más tiempo.
    def __escuchaInstrucciones(self):
        #MANEJO DE EXCEPCIONES: Es una parte de código que se conforma de dos partes, try y except: 
        # - Primero se ejecuta el código que haya dentro del try y si es que llegara a ocurrir una excepción 
        #   durante su ejecución, el programa brinca al código del except.
        # - En la parte de código donde se encuentra la palabra reservada except, se ejecuta cierta acción 
        #   cuando ocurra el error esperado. 
        #Se utiliza esta arquitectura de código cuando se quiera efectuar una acción donde se espera que pueda 
        #ocurrir un error durante su ejecución.
        try:
            #with as source: La instrucción with se utiliza para definir una variable que tiene asignada un 
            #método o recurso específico, el cual puede ser un archivo, una conexión a una base de datos, la 
            #cámara, micrófono o cualquier otro objeto que requiera ser cerrado. La palabra clave as se utiliza 
            #para asignar dicho recurso a una variable que puede utilizarse para acceder al recurso dentro del 
            #bloque with. 
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
                #io.BytesIO(): Método que sirve para crear un flujo de bytes en memoria que puede utilizarse 
                #para almacenar datos binarios, como imágenes, audio y video.
                #speech_recognition.Recognizer().listen().get_wav_data(): El método get_wav_data() se utiliza 
                #para almacenar el texto recibido en el micrófono del ordenador en un flujo de datos binarios 
                #que se puedan guardar en un archivo de audio con extensión wav.
                datosAudio = io.BytesIO(textoInstruccionUsuario.get_wav_data())
                #pydub.AudioSegment().from_file(): El método from_file() perteneciente a la clase AudioSegment 
                #se utiliza para cargar solamente los datos de audio donde se escuche la voz del usuario, 
                #logrando así que no se haga nada cuando el usuario está en silencio. 
                archivoAudio = pydub.AudioSegment.from_file(datosAudio)
                print("Mandando texto del microfono a un archivo de audio wav...")
                #pydub.AudioSegment().from_file().export(path, file_type): Lo que hace el método export() es 
                #exportar un segmento de audio a un archivo.
                archivoAudio.export(rutaArchivo, format = 'wav')
                print("Texto del microfono guardado en un archivo de audio temporal tipo wav...")
        #Para identificar el tipo de excepción que ha ocurrido y utilizarlo en la instrucción except, se puede 
        #utilizar la clase Exception, que es una clase incorporada en Python utilizada para describir todos los 
        #tipos de excepciones, luego de colocar el nombre de la clase Exception se usa la palabra reservada "as" 
        #seguida de un nombre de variable, esto nos permitirá acceder a la instancia de la excepción y 
        #utilizarla dentro del except.
        except Exception as error:
            print(error)
        #Se retorna la ruta del archivo de la función porque de ahí extraerá el archivo de audio el modelo 
        #Whisper para procesarlo.
        return rutaArchivo

    #__transcripcionWhisper(): Función propia y con modificador de acceso privado que se encarga de recibir el 
    #archivo de audio recortado que contiene la instrucción mandada al asistente virtual para pasársela al 
    #modelo de Whisper para que la transcriba a texto.
    def __transcripcionWhisper(self, audioRecortado):
        #whisper.load_model(): Con el método load_model() se pueden cargar los diferentes modelos de lenguaje de 
        #la librería whisper, si se elige un modelo muy simple, se tendrá un peor desempeño, pero mientras más 
        #complejo sea el modelo, más se tardará en procesar el audio, a esto dentro de la librería se le llama 
        #Parameter y Relative Speed, donde a un mayor número de parámetros, se tendrá mayor capacidad de 
        #aprendizaje en el modelo y la velocidad relativa indica la rapidez con la que el modelo puede generar 
        #texto, esta se calcula dividiendo el tiempo que tarda el modelo en generar una palabra entre el número 
        #de palabras que genera. Las características de los modelos disponibles son las siguientes:
        # - tiny:   Parameter = 39M,    Memoria que consume = 1GB   y Relative Speed = 32x.
        # - base:   Parameter = 74M,    Memoria que consume = 1GB   y Relative Speed = 16x.
        # - small:  Parameter = 244M,   Memoria que consume = 2GB   y Relative Speed = 6x.
        # - medium: Parameter = 769M,   Memoria que consume = 5GB   y Relative Speed = 2x.
        # - large:  Parameter = 1550M,  Memoria que consume = 10GB  y Relative Speed = 1x.
        #Cuando el programa sea ejecutado por primera vez empezará a descargar el modelo para poderlo utilizar, 
        #este proceso tarda un poco en terminar, pero después identificará por sí solo el lenguaje y las 
        #palabras dichas en el audio, no importando si este tenga ruido o si es de alguna canción con 
        #instrumentos detrás. 
        Modelo = whisper.load_model("small")
        #whisper.load_model().transcribe(): El método transcribe() sirve para escuchar el audio de un archivo y 
        #transcribirlo a texto a través del modelo elegido con el método load_model(). El proceso de carga tarda 
        #un poco y el tiempo que el modelo se tarda en procesar el audio depende de su duración. Los parámetros 
        #que recibe el método son la ubicación del archivo de audio que quiere transcribir y el parámetro fp16 
        #que indica si el cálculo se realizará en formato de punto flotante de 16 bits (FP16), pero como en 
        #algunas CPUs no se admite esta funcionalidad, se coloca como False, por lo que se está utilizando punto 
        #flotante de 32 bits (FP32) en su lugar. Además cabe mencionar que el audio escuchado por el método será 
        #recortado en cachos de 30 segundos y estos serán igualmente divididos en pedazos.
        TranscripcionAudio_a_Texto = Modelo.transcribe(audioRecortado, language = "spanish", fp16 = False)
        print("Interpretando texto guardado en un archivo temporal de audio wav con el modelo Whisper...\t")
        #whisper.load_model().transcribe()["text"]: Texto traducido por Whisper de un archivo de audio.
        return TranscripcionAudio_a_Texto["text"]
    
    #oidoAsistenteVirtual(): Método con modificador de acceso público que permite ejecutar los métodos privados 
    #__transcripcionWhisper() para transcribir un archivo de audio a texto y __escuchaInstrucciones() para 
    #escuchar las instrucciones del usuario por medio del micrófono y almacenar eso en un archivo temporal. El
    #resultado del texto escuchado del usuario será transformado a minúsculas aplicándole el método lower().
    #self: La instrucción self se utiliza para hacer referencia al objeto que se está manipulando cuando se instancía 
    #la clase. Por eso es que a través de la misma nomenclatura de un punto se accede a los distintos atributos y/o 
    #métodos con un objeto desde fuera de la clase.
    def oidoAsistenteVirtual(self):
        return self.__transcripcionWhisper(self.__escuchaInstrucciones()).lower()