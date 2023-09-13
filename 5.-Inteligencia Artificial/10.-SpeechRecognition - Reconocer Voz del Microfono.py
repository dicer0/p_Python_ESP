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
import speech_recognition   #SpeechRecognition: Librería para recabar audio del micrófono en tiempo real.
import time                 #time: Librería de manejo de tiempos, como retardos, contadores, etc.

#speech_recognition.Recognizer(): El objeto Recognizer() se utiliza para crear un reconocedor de voz, el cual 
#puede utilizarse para reconocer instrucciones dadas al asistente virtual por medio del habla humana.
listenerAudio = speech_recognition.Recognizer()
print("Inicializando listener con la librería speech_recognition")

#Bucle indeterminado while para ejecutar siempre este programa que reconozca el audio del usuario hasta que 
#diga bye Timmy.
while True:
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
        with speech_recognition.Microphone() as microfono:
            #speech_recognition.Recognizer().adjust_for_ambient_noise(): El método adjust_for_ambient_noise() 
            #sirve para aplicar un filtro a la señal de sonido que quite el ruido de fondo recibido en su 
            #parámetro.
            listenerAudio.adjust_for_ambient_noise(microfono, duration = 0.2)
            print("Quitando ruido de fondo... ya puedes hablar.")
            #time.time(): El método time() se utiliza para devolver un valor de tipo flotante que representa la 
            #cantidad de segundos transcurridos desde el 1 de enero de 1970 a las 00:00:00 horas (UTC) hasta el 
            #momento actual donde se ejecute este método, pero eso no es tan importante, sino que con este se 
            #pueden medir intervalos de tiempo al declararlo dos veces y realizar una resta.
            tiempoInicio = time.time()
            #speech_recognition.Recognizer().listen(): El método listen() sirve para poder escuchar de una 
            #fuente de audio en tiempo real y convertirlo a texto, para ello primero se tuvo que haber 
            #instanciado la clase Recognizer.
            audioMic = listenerAudio.listen(microfono, timeout = 5, phrase_time_limit = 5)
            print("Microfono encendido y escuchando...")
            tiempoFinal = time.time()
            intervaloTiempoQuitarRuido = tiempoInicio - tiempoFinal
            print("El tiempo que se tardó en configurarse el método adjust_for_ambient_noise() fue de: " + str(intervaloTiempoQuitarRuido))
            #speech_recognition.Recognizer().recognize_google(): El método recognize_google() utiliza el 
            #servicio de Google para convertir el audio en texto, la desventaja de usar este es que no se corre 
            #de manera local, a fuerza debemos estar conectados a internet para que esto se ejecute, este recibe 
            #como parámetro un objeto de la librería speech_recognition al que se le haya aplicado la función 
            #listen().
            texto = listenerAudio.recognize_google(audioMic)
            print("Traduciendo microfono a texto... Texto reconocido:\n\t" + str(texto))
            #Si se reconoce que el usuario dice bye Timmy, se rompe el bucle while y se termina la ejecución del 
            #programa.
            if (texto == "bye Timmy"):
                break
    #Para identificar el tipo de excepción que ha ocurrido y utilizarlo en la instrucción except, se puede 
    #utilizar la clase Exception, que es una clase incorporada en Python utilizada para describir todos los 
    #tipos de excepciones, luego de colocar el nombre de la clase Exception se usa la palabra reservada "as" 
    #seguida de un nombre de variable, esto nos permitirá acceder a la instancia de la excepción y utilizarla 
    #dentro del except.
    except Exception as error:
        #Si ocurre un error, se imprime en consola el mensaje de Podrías repetir lo que dijiste? y además se 
        #vuelve a crear el objeto speech_recognition.Recognizer() para volver a intentar escuchar lo que el 
        #usuario dijo.
        listenerAudio = speech_recognition.Recognizer()
        print("Podrías repetir lo que dijiste? Ocurrió un error: " + str(error))
        continue