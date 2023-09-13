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
#pywhatkit: Pywhatkit es una biblioteca de Python que permite enviar mensajes de texto a través de WhatsApp 
#incluso si no estás en su lista de contactos, realizar búsquedas en la web, reproducir canciones en YouTube, 
#realizar búsquedas en Wikipedia, ejecutar comandos en consola, etc.
import pywhatkit 

#IMPORTACIÓN DE CLASES: Cuando se quiera importar una clase, el nombre de esta no puede empezar con un número, 
#sino cuando la quiera importar obtendré un error y se va accediendo a las carpetas o también llamados paquetes 
#en la programación orientada a objetos (POO), por medio de puntos:
# - Directorio normal:      carpeta1/carpeta2/carpeta3
# - Directorio paquetes:    carpeta1.carpeta2.carpeta3
#La parte del directorio se coloca después de la palabra reservada from y la clase a importar después de import.
from POO_AsistenteVirtualMarkI.oidoAsistente import EscucharMicrofono
from POO_AsistenteVirtualMarkI.vozAsistente import vozWindows
from POO_AsistenteVirtualMarkI.cerebroLangchainAsistente import cerebro_OpenAI

#IMPORTACIÓN DE LIBRERÍAS:
#IMPORTACIÓN DE LLAVE: Cuando se quiera utilizar una API que utiliza un key, por seguridad es de buenas 
#prácticas declararla en un archivo externo, además cabe mencionar que el nombre de dicho archivo y constante no 
#pueden empezar con un número, sino cuando la quiera importar obtendré un error y se va accediendo a sus carpetas 
#por medio de puntos:
# - Directorio normal:      carpeta1/carpeta2/carpeta3
# - Directorio paquetes:    carpeta1.carpeta2.carpeta3
#La parte del directorio se coloca después de la palabra reservada import y posteriormente se manda a llamar sus 
#variables o constantes de igual manera a través de un punto.
import API_Keys.Llaves_ChatGPT_Bard
#ChatGPT API key
ApiKey = API_Keys.Llaves_ChatGPT_Bard.LlaveChatGPT 

#__name__ == __main__: Método main, esta función es super importante ya que sirve para instanciar las clases del 
#programa y ejecutar sus métodos, en python pueden existir varios métodos main en un solo programa, aunque no es 
#una buena práctica.
if (__name__ == "__main__"):
    oidoAsistenteVirtual = EscucharMicrofono()  #Instancia de la clase propia EscucharMicrofono.
    vozAsistenteVirtual = vozWindows() #Instancia de la clase propia vozWindows.
    cerebroAsistenteVirtual = cerebro_OpenAI(ApiKey)  #Instancia de la clase propia cerebro_OpenAI.
    vozAsistenteVirtual.hablar("Hola soy TIMI Mark 1, tu asistente virtual, puedo responder tus preguntas con ChatGPT y reproducir canciones en YoTube, en que te puedo ayudar?")
    while True:
        try:
            #EscucharMicrofono.oidoAsistenteVirtual(): Método propio de la clase EscucharMicrofono que se encarga 
            #de escuchar lo que dice el usuario, almacenar eso en un archivo temporal y luego pasárselo al modelo
            #Whisper para que lo transcriba a texto.
            preguntaUsuario = oidoAsistenteVirtual.oidoAsistenteVirtual()
            print(str(preguntaUsuario) + "\n\n")
            #Si se reconoce que el usuario dice bye Timmy, se rompe el bucle while y se termina la ejecución del 
            #programa.
            if (preguntaUsuario == " adiós, timmy." or preguntaUsuario == " bye, timmy." or preguntaUsuario == " bye timmy"  or preguntaUsuario == " adiós timmy" or preguntaUsuario == " adiós, tímí." or preguntaUsuario == " adiós, dimi." or preguntaUsuario == " adiós, teamy." or preguntaUsuario == " ¡bye, timmy!" or preguntaUsuario == " bye, timmy!"):
                vozAsistenteVirtual.hablar("Bye di0, un gusto haberte ayudado...")
                print("---------------------------Bye di_cer0, un gusto haberte ayudado...---------------------------")
                break
            #Si se reconoce que el usuario dice la palabra reproduce, el asistente virtual por medio de la 
            #librería pywhatkit reproduce el video que el usuario dijo en YouTube. 
            elif (("reproduce") in preguntaUsuario):
                #.replace().lower(): Lo que hace el método replace() es reemplazar todas las palabras que 
                #aparezcan en un string en otra cadena específica y el método lower() sirve para convertir todas 
                #las letras de una cadena en minúsculas, esto es importante hacerlo porque al reproducir una 
                #canción o mandar una búsqueda a internet, siempre es mejor tener puras minúsculas. 
                cancionYoutube = preguntaUsuario.replace('reproduce', '').lower()
                vozAsistenteVirtual.hablar("Ok di0, voy a reproducir una canción en YouTube")
                #pywhatkit.playonyt(): El método playonyt() de la librería pywhatkit permite  reproducir un 
                #video de YouTube en el navegador web predeterminado del sistema.
                pywhatkit.playonyt(cancionYoutube)
                print("----------Ok di_cer0, ya reproducí la canción del artista que pediste en YouTube...-----------")
            #Si no se reconoce que el usuario diga ninguna de las palabras reservadas de arriba, el asistente 
            #virtual por medio de la librería de langchain y openai responde la pregunta hecha por el usuario.
            else:
                #En Python algunos métodos devuelven más de un valor, si queremos almacenar los valores provenientes 
                #de dicho método que devuelve más de 1 valor se utiliza la siguiente sintaxis:
                #   variable1, variable2 = Clase.MétodoVariasVariables()
                #Pero si alguno de estos valores no nos interesa que se almacene en una variable, simplemente se 
                #coloca un guión bajo para indicar eso:
                #   variable1, _ = Clase.MétodoVariasVariables()
                respuestaAsistenteVirtual, _, _ = cerebroAsistenteVirtual.preguntarChatbot(preguntaUsuario)
                vozAsistenteVirtual.hablar(respuestaAsistenteVirtual)
                print(respuestaAsistenteVirtual)
        except Exception as errorEjecucion:
            vozAsistenteVirtual.hablar("Lo siento, no escuché bien lo que dijiste debido a este error...")
            print(errorEjecucion)
            continue
#El límite de la duración de audio que puede procesar T.I.M.M.Y. en las instrucciones que se le manda es de 15 
#segundos y el Mark I en sus respuestas tiene un delay de:
# - tiny:   Delay de 2  segundos cuando le mando un comando hablado usando el comando.
# - base:   Delay de 5  segundos cuando le mando un comando hablado usando el comando.
# - small:  Delay de 10 segundos cuando le mando un comando hablado usando el comando.