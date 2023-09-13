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
#   - Las funciones son muy utilizadas en Python ya que sirven para volver modular el código, logrando así que 
#     se pueda ejecutar varias veces una misma acción sin necesidad de escribirla varias veces.
#   - Los distintos métodos que se utilizan en todos los lenguajes de programación para ejecutar acciones 
#     diferentes como por ejemplo lo es el método print(), son en realidad funciones, pero que utilizan una 
#     arquitectura de programación orientada a objetos (POO).
#   - Los parámetros que recibe una función son las variables con las que interactúa para realizar su acción, 
#     una función cualquiera puede o no recibir parámetros para ejecutarse. 
#   - Una función puede o no devolver una variable que almacene su valor resultante, esto se realiza a través 
#     de la palabra reservada "return".
#   - Para utilizar una función en Python se debe declarar su nombre seguido de un paréntesis en donde se le 
#     pase sus parámetros, si es que recibe algunos, además su resultado puede o no guardarse en una variable 
#     dependiendo de si retorna un valor o no.

#1.- ÁREA DE UN TRIÁNGULO ARBITRARIO: Cálculo con las coordenadas de sus 3 vértices
#Un triángulo arbitrario puede describirse mediante las coordenadas de sus tres vértices: (x1, y1), (x2, y2), 
#(x3, y3), numerados en sentido contrario a las agujas del reloj. El área del triángulo viene dada por la 
#fórmula:
#A = (1/2)*|x1*y2 - x1*y3 - x2*y1 + x2*y3 + x3*y1 - x3*y2|
#PRIMERO SE CREARÁ UNA FUNCIÓN QUE SE USA PARA DENOTAR DE FORMA MÁS SENCILLA LA FÓRMULA SIN USAR LISTAS:
def areaTriangulo(x1,y1,x2,y2,x3,y3):
    #float(): Método que convierte un tipo de dato cualquiera en numérico decimal.
    x1 = float(x1)  #v1 = (x1, y1)
    y1 = float(y1)
    x2 = float(x2)  #v2 = (x2, y2)
    y2 = float(y2)
    x3 = float(x3)  #v3 = (x3, y3)
    y3 = float(y3)
    
    #abs(): Método que saca el valor absoluto de un número, volviéndolo positivo aunque sea originalmente 
    #negativo.
    #A = (1/2)*|x1*y2 - x1*y3 - x2*y1 + x2*y3 + x3*y1 - x3*y2|
    Area = abs((1/2)*(x1*y2 - x1*y3 - x2*y1 + x2*y3 + x3*y1 - x3*y2))
    return Area

#USO DE LA PRIMERA FUNCIÓN SIN LISTAS:
#input(): Método que sirve para imprimir en consola un mensaje y que luego se permita al usuario ingresar un 
#valor, que será de tipo String y podrá ser almacenado en una variable.
#Coordenadas verticales y horizontales del primer vértice del triángulo
print('--------------------------------Función 1: Sin Listas--------------------------------')
x1 = input('Introduzca la coordenada x del primer vértice del triángulo: \t')     #v1 = (x1, y1)
y1 = input('Introduzca la coordenada y del primer vértice del triángulo: \t')
#Coordenadas verticales y horizontales del segundo vértice del triángulo
x2 = input('Introduzca la coordenada x del segundo vértice del triángulo: \t')    #v2 = (x2, y2)
y2 = input('Introduzca la coordenada y del segundo vértice del triángulo: \t')
#Coordenadas verticales y horizontales del tercer vértice del triángulo
x3 = input('Introduzca la coordenada x del tercer vértice del triángulo: \t')     #v3 = (x3, y3)
y3 = input('Introduzca la coordenada y del tercer vértice del triángulo: \t')

Resultado = areaTriangulo(x1,y1,x2,y2,x3,y3)
#print(): Método para imprimir un mensaje en consola y después dar un salto de línea (Enter), además si se 
#quiere concatenar un mensaje (mostrar resultados de variables junto con texto estático), este se debe separar 
#entre comillas, declarando los mensajes estáticos entre comillas y los nombres de variables sin comillas.
print('El área del triangulo con las coordenadas \n'
      ,'(', x1,', ', y1 ,'), (', x2, ', ', y2 ,') y' ,' (', x3, ', ', y3 ,')'
      , '\nEs igual a : \n'
      , Resultado)






#LISTAS: Las listas en Python son tipos de datos estructurados, parecido a lo que son los arrays en otros 
#lenguajes de programación, aunque no es el único tipo de dato agrupado que existe en Python, existen además las 
#tuplas, diccionarios y numpy arrays. A las listas también se les puede llamar vectores.
#FUNCIÓN QUE UTILIZA LA FÓRMULA USANDO LISTAS:
def areaListas(v1, v2, v3):
    #A = (1/2)*|x1*y2 - x1*y3 - x2*y1 + x2*y3 + x3*y1 - x3*y2|
    a = (1/2) * abs(v1[0]*v2[1] - v1[0]*v3[1] - v2[0]*v1[1] + v2[0]*v3[1] + v3[0]*v1[1] - v3[0]*v2[1])
    return a

#USO DE LA SEGUNDA FUNCIÓN CON LISTAS:
vertice_1 = (0, 0)   #v1 = (x1, y1)
vertice_2 = (1, 0)  #v2 = (x2, y2)
vertice_3 = (0, 2)  #v3 = (x3, y3)

triangle1 = areaListas(vertice_1, vertice_2, vertice_3)

#print(): Método para imprimir un mensaje en consola y después dar un salto de línea (Enter), además si se 
#quiere concatenar un mensaje (mostrar resultados de variables junto con texto estático), este se debe separar 
#entre comillas, declarando los mensajes estáticos entre comillas y los nombres de variables sin comillas.
print('--------------------------------Función 2: Con Listas--------------------------------')
print("El área del triángulo compuesto por los vértices \n"
      , vertice_1
      , vertice_2
      , vertice_3
      , "Es igual a: \n"
      , triangle1)