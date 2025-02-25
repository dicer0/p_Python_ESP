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

#Comparador con y sin Tolerancia: Cuando se compara de forma muy rigida dos valores decimales entre sí, puede 
#existir un error al realizar su comparación, por esta razón es que es recomendable indicar una tolerancia y 
#realizar la comparación respecto a ella, para así evitar errores. 
#La comparación "diferente a" con tolerancia se efectúa al realizar una resta entre los valores comparados, 
#indicando que si el resultado de dicha resta es menor a la tolerancia declarada, los valores son distintos.
a = 1/947.0*947
b = 1

#Esto es de gran utilidad cuando se crea un código que funcione con elementos electrónicos que interactúen con 
#magnitudes de la vida real como sensores.
#Comparador sin tolerancia:
if(a != b):
    print("Resultado incorrecto")

#Comparador con tolerancia: En este caso se está dando una tolerancia de 1e-8 = 0.00000001.
#abs(): Método que saca el valor absoluto de un número, volviéndolo positivo aunque sea originalmente negativo.
#El método abs() saca el valor absoluto de la comparación para que esta sea más precisa, de esta forma la 
#tolerancia aplica hacia ambos lados.
# - Si la comparación da como resultado False es porque "a" no está ni cerca de ser igual a "b", osea: a != b, 
# - Si da True es porque se encuentra dentro del rango de la tolerancia o es exactamente igual, osea: a == b.
if(abs(a-b) < 1e-8):
    print("Resultado correcto")