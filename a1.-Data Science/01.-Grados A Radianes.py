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

#CÓDIGO PARA INTRODUCIR EN CONSOLA GRADOS Y CONVERTIR A RADIANES:
#math: Importación de librería math para poder usar el valor pi.
from math import pi

#print(): Método para imprimir un mensaje en consola y después dar un salto de línea (Enter).
print("Hola mundo")

#input(): Método que sirve para imprimir en consola un mensaje y que luego se permita al usuario ingresar un valor 
#que será de tipo String y podrá ser almacenado en una variable.
#float(): Se usa el método float() para convertir un dato a numérico o string decimal.
#El tipo primitivo del input que viene siendo un String, se convertirá en decimal y se guardará en una variable:
ang_deg = float(input("Ingresa el ángulo en grados: \n"))
#Fórmula para convertir grados a radianes: rad = pi/180°.
ang_rad = ang_deg*(pi/180)

#Cuando imprimimos en consola con el comando print() y el operador de interpolación % para concatenar valores: 
# - El código %s sirve para imprimir un string en consola.
# - El código %f sirve para imprimir un número flotante en consola y si lleva un número decimal antes de la f, 
#   indica el número de decimales que se quieren mostrar, nunca muestra su resultado en formato exponencial.
# - El código %d sirve para imprimir números enteros.
# - El código %g sirve para imprimir un número decimal en formato de coma flotante, que muestra menos decimales,
#   utiliza el formato exponencial en minúsculas si el exponente es menor que -4 o no menor que la precisión.
#Fuente: https://docs.python.org/2/library/stdtypes.html#string-formatting-operations
print("El angulo en radianes es:", ang_rad)
print("El angulo en radianes es: %.2f" % ang_rad)
print("El angulo %.3f en grados convertido a radianes es: %g" % ( ang_deg, ang_rad)) #Concatenar más de un valor.