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

#CÓDIGO PARA INTRODUCIR EN CONSOLA UN NÚMERO N Y SACAR SU FACTORIAL:
#input(): Método que sirve para imprimir en consola un mensaje y que luego se permita al usuario ingresar un valor 
#que será de tipo String y podrá ser almacenado en una variable.
#int(): Se usa el método int() para convertir un dato a numérico entero.
#El tipo primitivo del input que viene siendo un String, se convertirá a numérico entero para que pueda manejar las 
#ejecuciones de un bucle.
n = int(input("Ingresa un número entero positivo n: \n"))   #Número n del cual se obtendrá su factorial

#Esta es la base del número del cual se obtendrá su factorial, a través de un condicional if y un bucle for.
factorial = 1

#La fórmula del factorial es: 
#   n! = 1*2*3*...*(n-1)*n
#Pero cuando el número n es 0 o 1, el resultado es siempre 1, por eso es que se crea un condicional.

#CONDICIONAL IF: En Python no se utilizan llaves de apertura o cierre al utilizar condiconales, solamente se 
#utilizan dos puntos para indicar el inicio del condicional y tabuladores para ver qué es lo que está dentro o 
#fuera de él, ya sea para el condicional if, else if (elif) o else.
if(n == 0 or n == 1):
    factorial = 1 #Cuando el número n es 0 o 1, el resultado es siempre 1
else:
    #BUCLE FOR: En los Bucles de Python no se utilizan llaves de apertura o cierre tampoco, solamente se utilizan 
    #dos puntos para indicar el inicio del bucle y tabuladores para diferenciar qué es lo que está dentro o fuera 
    #de él. Además, después de la palabra reservada "for" se declara una variable local numérica entera que solo 
    #existirá dentro del bucle y será la que cuente desde 0 por default o desde el primer número indicado dentro 
    #del paréntesis hasta el extremo indicado en el segundo parámetro que se encuentra dentro del paréntesis de la 
    #palabra reservada range() para terminar el bucle. En otras palabras, dentro del paréntesis de la palabra 
    #reservada "range()" se coloca el inicio y final del conteo para indicar cuantas veces se ejecutará el bucle.
    for i in range(2, n+1):
        #Como en el condicional if anterior se analizó la opción para cuando n = 0 o 1, en el bucle for se 
        #tomarán en cuenta las opciones que van desde n = 2 hasta n = n+1, porque el último número del conteo en 
        #el for nunca lo va a alcanzar y se busca que el bucle llegue hasta n.
        factorial = factorial*i

#print(): Método para imprimir un mensaje en consola y después dar un salto de línea (Enter), además si se quiere 
#concatenar un mensaje (mostrar resultados de variables junto con texto estático), este se debe separar entre 
#comillas, declarando los mensajes estáticos entre comillas y los nombres de variables sin comillas.
print("El factorial del número ", n, " es igual a : ", factorial)