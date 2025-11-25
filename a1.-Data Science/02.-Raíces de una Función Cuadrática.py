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

#CÓDIGO PARA INTRODUCIR EN CONSOLA LOS COEFICIENTES DE UN POLINOMIO CUADRÁTICO Y CALCULAR SUS RAÍCES:
#Lectura de los coeficientes a, b y c de la fórmula cuadrática: ax2 + bx + c = 0
#input(): Método que sirve para imprimir en consola un mensaje y que luego se permita al usuario ingresar un valor 
#que será de tipo String y podrá ser almacenado en una variable.
#float(): Se usa el método float() para convertir un dato a numérico decimal.
#El tipo primitivo del input que viene siendo un String, se convertirá en decimal y se guardará en una variable:
a = float(input("Ingresa el coeficiente a: \n"))#Coeficiente a
b = float(input("Ingresa el coeficiente b: \n"))#Coeficiente b
c = float(input("Ingresa el coeficiente c: \n"))#Coeficiente c

#Para calcular las raíces de un polonomio cuadrático se utiliza la fórmula: 
#   r1,2 = -b±√(b^2-4ac)/2a
#Por lo cual es importante mencionar que en Python los exponentes se indican a través del símbolo ** en vez de ^: 
#   √(b^2-4ac) = (b^2-4ac)^1/2 = (b^2-4ac)**1/2
#Recordemos además que la jerarquía de operaciones matemáticas dicta lo siguiente, lo cual es respetado de la 
#misma forma por el código Python.
#   1.- Paréntesis: Las operaciones dentro de paréntesis se evalúan primero.
#   2.- Exponentes: Las potencias y raíces se evalúan después.
#   3.- Multiplicación y División: Estas operaciones se realizan de izquierda a derecha.
#   4.- Suma y Resta: Estas operaciones se realizan de izquierda a derecha al último.
raiz1 = (-b+(b**2-4*a*c)**(1/2))/(2*a)
raiz2 = (-b-(b**2-4*a*c)**(1/2))/(2*a)

#print(): Método para imprimir un mensaje en consola y después dar un salto de línea (Enter), además si se quiere 
#concatenar un mensaje (mostrar resultados de variables junto con texto estático), este se debe separar entre 
#comillas, declarando los mensajes estáticos entre comillas y los nombres de variables sin comillas.
print("La primera raiz r1 es = ", raiz1)
print("La segunda raiz r2 es = ", raiz2)