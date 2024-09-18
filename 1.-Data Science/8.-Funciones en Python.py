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

#FUNCIONES EN PYTHON: Las funciones en python se indican a través de la palabra reservada def, seguida del 
#nombre de la función, un paréntesis que contiene sus distintos parámetros y dos puntos para denotar su inicio,
#en Python no se utilizan llaves de apertura o cierre para su sintaxis, solamente se utilizan dos puntos para 
#indicar su inicio y tabuladores para diferenciar qué es lo que está dentro o fuera de ella.
#   - Las funciones son muy utilizadas en Python ya que sirven para volver modular nuestro código, logrando que 
#     se ejecute varias veces una misma acción sin necesidad de escribirla varias veces.
#   - Los distintos métodos que se utilizan en todos los lenguajes de programación para ejecutar distintas 
#     acciones como por ejemplo lo es el método print(), son en realidad funciones, pero que utilizan una 
#     arquitectura de programación llamada Programación Orientada a Objetos.
#   - Los parámetros que recibe una función son las variables con las que interactúa para realizar su acción, 
#     una función cualquiera puede o no recibir parámetros para ejecutarse. 
#   - Una función puede o no devolver una variable que almacene un valor resultante, esto se realiza a través 
#     de la palabra reservada "return". 
#   - Para utilizar una función en Python se debe declarar su nombre seguido de un paréntesis en donde se le 
#     pase sus parámetros, si es que recibe algunos, además su resultado puede o no guardarse en una variable 
#     dependiendo de si retorna un valor o no.

#Función que no recibe argumentos o parámetros y no retorna un valor:
def imprimir_hola():
    #print(): Método para imprimir un mensaje en consola y después dar un salto de línea (Enter).
    print("Hola!")

#BUCLE FOR: En Python no se utilizan llaves de apertura o cierre para la sintaxis de un bucle, solamente se 
#utilizan dos puntos para indicar su inicio y tabuladores para diferenciar qué es lo que está dentro o fuera 
#de él. 
#Además después de la palabra reservada "for" se declara una variable local numérica entera que solo existirá 
#dentro del bucle y será la que cuente desde 0 por default o desde el primer número indicado dentro del 
#paréntesis hasta el extremo indicado en el segundo parámetro que se encuentra dentro del paréntesis de la 
#palabra reservada range() para terminar el bucle. En otras palabras, dentro del paréntesis de la palabra 
#reservada "range()" se coloca el inicio y final del conteo para indicar cuantas veces se ejecutará el bucle.
for i in range(3):
    imprimir_hola() #Llamada a la función en un bucle for





#Función que sí recibe argumentos o parámetros y no retorna un valor:
def imprimir_argumentos(argumento_1, argumento_2):
    print(argumento_1+argumento_2)

#Llamada a la función: Uso de una función de formas muy distintas debido a sus diferentes tipos de parámetros.
imprimir_argumentos("!Hola, ", "mundo!")    #Concatenación
imprimir_argumentos(1+1j, 2+2j)             #Operación Algebráica
imprimir_argumentos([1,2,3], [4,5,6])       #Suma Vectorial (Matricial)





#Función que no recibe parámetros y sí retorna un valor:
def regresa_valor_pi():
    #BIBLIOTECA MATH: Esta librería de Python importa material para realizar operaciones matemáticas simples,
    #como lo son operaciones trigonométricas, de geométría, etc. En este caso específicamente se utiliza para 
    #obtener la constante pi solamente.
    #Para importar librerías primero esta se debe descargar con la consola de Windows CMD, Powershell o GitBash, 
    #luego se usa la palabra reservada import, el nombre de la librería, la palabra reservada "as" y el nuevo 
    #nombre con el que se quiere usar los métodos de la librería dentro del código.
    from math import pi
    return pi

#Llamada a la función: Uso de la función.
area_circulo = (regresa_valor_pi())*1*2
print(area_circulo)





#Función que recibe parámetros y retorna un valor:
def multiplica_a_y_b(a,b):
    return a*b

#Llamada a la función: Uso de la función.
var_resultado_multiplicacion_1 = multiplica_a_y_b(2,"Hola")
print(var_resultado_multiplicacion_1)
var_resultado_multiplicacion_2 = multiplica_a_y_b(2,3)
print(var_resultado_multiplicacion_2)
var_resultado_multiplicacion_3 = multiplica_a_y_b(1+1j,1-1j)
print(var_resultado_multiplicacion_3)




#Función Anónima: En este tipo de funciones se utiliza la palabra reservada "lambda" para crear funciones sin 
#nombre, mejor conocidas como "funciones lambda" o "expresiones lambda", estas son declaradas por medio de la 
#siguiente sintaxis:
#   variable = lambda       parámetros:     operación_función
square = lambda x: x**2

#Llamada a la función: Se puede llamar las funciones lambda por medio de la variable que almacena su valor 
#resultante, siguiendo la misma sintaxis de una función normal y obteniendo su resultado.
print("Función lambda:", square(25))




#Función asíncrona: 
#asyncio: Librería que facilita la escritura de código concurrente y asíncrono en Python mediante el uso de 
#corutinas, bucles de eventos y tareas.
import asyncio
#async def: Palabra reservada que se utiliza para definir una función asíncrona en Python, conocida como 
#corutina. Estas funciones permiten realizar operaciones de manera no bloqueante, facilitando la ejecución 
#concurrente de código. 
#Relación con await: Dentro de una función definida con async def, la palabra clave await se usa para llamar 
#a otras corutinas, indicando al bucle de eventos que debe esperar su resultado sin bloquear la ejecución del 
#resto del código.
async def my_coroutine():
    print("Start")
    await asyncio.sleep(1)  # Simula una espera asincrónica de 1 segundo
    print("End")

async def main():
    await my_coroutine()
asyncio.run(main())
