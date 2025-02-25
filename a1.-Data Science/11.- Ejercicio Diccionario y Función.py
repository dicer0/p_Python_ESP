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

#EJERCICIO DICCIONARIO Y FUNCIONES:
#Con la palabra reservada def se declara una función
def char_frequency(st):
    #La declaración de un diccionario se hace con llaves de apertura y cierre {} 
    diccionario = {}
    #Los bucles for-each son muy buenos para recorrer elementos de una lista o diccionario.
    for letra in st:
        #print(): Imprimir un mensaje en consola.
        print(letra)
        #diccionario.keys(): Con este el método keys() que se aplica a un diccionario obtenemos todas sus keys.
        llaves = diccionario.keys()
        if(letra in llaves):
            diccionario[letra] += 1
        else:
            #Agregamos letras al diccionario
            diccionario[letra] = 1
    return diccionario

#Manda a llamar la función char_frequency
print(char_frequency("google.com"))