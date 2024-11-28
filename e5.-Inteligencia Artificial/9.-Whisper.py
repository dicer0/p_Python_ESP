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
import whisper #whisper: Librería de OpenAI que permite hacer la transcripción de audio o video a texto.

#whisper.load_model(): Con el método load_model() se pueden cargar los diferentes modelos de lenguaje de la 
#librería whisper, si se elige un modelo muy simple, se tendrá un peor desempeño, pero mientras más complejo sea 
#el modelo, más se tardará en procesar el audio, a esto dentro de la librería se le llama Parameter y Relative 
#Speed, donde a un mayor número de parámetros, se tendrá mayor capacidad de aprendizaje en el modelo y la  
#velocidad relativa indica la rapidez con la que el modelo puede generar texto, esta se calcula dividiendo el 
#tiempo que tarda el modelo en generar una palabra entre el número de palabras que genera. Las características 
#de los modelos disponibles son las siguientes:
# - tiny:   Parameter = 39M,    Memoria que consume = 1GB   y Relative Speed = 32x.
# - base:   Parameter = 74M,    Memoria que consume = 1GB   y Relative Speed = 16x.
# - small:  Parameter = 244M,   Memoria que consume = 2GB   y Relative Speed = 6x.
# - medium: Parameter = 769M,   Memoria que consume = 5GB   y Relative Speed = 2x.
# - large:  Parameter = 1550M,  Memoria que consume = 10GB  y Relative Speed = 1x.
#Cuando el programa sea ejecutado por primera vez empezará a descargar el modelo para poderlo utilizar, este 
#proceso tarda un poco en terminar, pero después identificará por sí solo el lenguaje y las palabras dichas en 
#el audio, no importando si este tenga ruido o si es de alguna canción con instrumentos detrás. 
Modelo = whisper.load_model("small")
#whisper.load_model().transcribe(): El método transcribe() sirve para escuchar el audio de un archivo y 
#transcribirlo a texto a través del modelo elegido con el método load_model(). El proceso de carga tarda un poco 
#y el tiempo que el modelo se tarda en procesar el audio depende de su duración. Los parámetros que recibe el 
#método son la ubicación del archivo de audio que quiere transcribir y el parámetro fp16 que indica si el 
#cálculo se realizará en formato de punto flotante de 16 bits (FP16), pero como en algunas CPUs no se admite 
#esta funcionalidad, se coloca como False, por lo que se está utilizando punto flotante de 32 bits (FP32) en su 
#lugar. Además cabe mencionar que el audio escuchado por el método será recortado en cachos de 30 segundos y 
#estos cachos serán igualmente divididos en los pedazos que los conforman. 
TranscripcionAudio_a_Texto = Modelo.transcribe("C:/Users/diego/OneDrive/Documents/The_MechaBible/p_Python_ESP/5.-Inteligencia Artificial/0.-Archivos_Ejercicios_Python/Till I Collapse - Eminem.mp3", fp16 = False)
#print(): Método para imprimir un mensaje en consola y después dar un salto de línea (Enter).
print("\n\nDiccionario generado por Whisper:\n" + str(TranscripcionAudio_a_Texto) + "\n\n")
print("Texto traducido por Whisper de un audio de música:\n" + str(TranscripcionAudio_a_Texto["text"]) + "\n")
print("El lenguaje del audio es:\n" + str(TranscripcionAudio_a_Texto["language"]) + "\n\n")
print("Texto separado en cachos dentro de un segmento de 30 segundos del audio:\n" + str(TranscripcionAudio_a_Texto["segments"]) + "\n\n")



#DataFrame: Un DataFrame es una estructura de datos de dos dimensiones que se utiliza para almacenar datos en 
#forma de tablas donde las filas representan las observaciones de los datos, y las columnas representan las 
#variables de los datos de manera similar a las hojas de cálculo de Excel. En este caso se podría utilizar 
#para observar en consola de mejor manera los pedazos separados dentro de los 30 segundos de audio.
import pandas as pd
#pd.DataFrame(): El constructor del objeto DataFrame() permite desplegar en forma de tabla los datos de un 
#diccionario que reciba como parámetro, pudiendo después indicar a través de una lista anidada que esté 
#después del método, exáctamente cuales son los keys que quiero observar en la tabla.
DataFrameAudio = pd.DataFrame(TranscripcionAudio_a_Texto["segments"])[['start', 'end', 'text']]
print("DataFrame del texto separado en cachos:\n" + str(DataFrameAudio) + "\n\n")