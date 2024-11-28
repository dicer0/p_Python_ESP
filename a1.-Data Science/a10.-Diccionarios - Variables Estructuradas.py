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

#DICCIONARIOS: Los diccionarios en Python sirven para organizar datos, así se llama el tipo de variable que 
#almacena datos de esta forma, consisten de una llave única (key) y de un valor o valores asociados a esta llave 
#única, muy parecidos a la estructura que tienen los JSON en JavaScript.
#Ejemplo diccionario RAE:
diccionario_RAE = {'Café': ["Cafeto", "Bebida", "Color"]}
print(diccionario_RAE)
print(diccionario_RAE["Café"][1])

#Ejemplo diccionario de temperaturas:
temps = {'Oslo': 13, 'Londres': 15.4, 'Paris': 17.5}
print(temps)

#Agregamos una llave al diccionario, por ejemplo CDMX:
temps['CDMX'] = 20
print(temps)

if(temps["Londres"] == 15.4):
    print("Oliwis")

#Operación para imprimir de una por una las ciudades del diccionario:
for ciudad in temps:
    print(ciudad)
#Operación para imprimir de una por una las temperaturas del diccionario:
for ciudad in temps:
    print(temps[ciudad])

#Corroborar que existe una key en el diccionario:
if ('Berlín' in temps):
    print("Si está Berlín en el diccionario")
else:
    print("Berlín no se encuentra en el diccionario")

#Corroborar que existe un valor en el diccionario opción 1:
for ciudad in temps:
    if(temps[ciudad] == 13):
        print("Se encontró el valor 13")
#Corroborar que existe un valor en el diccionario opción 2:
lista_valores_diccionario = temps.values()
print(lista_valores_diccionario)
for valor_individual in lista_valores_diccionario:
    if(17.5 == valor_individual):
        print("Se encontró el valor de 17.5")
#Corroborar que existe un valor en el diccionario opción 3:
if(15.4 in lista_valores_diccionario):
    print("Se encontró el valor de 15.4")

#Obtención de una lista con todas las llaves del diccionario:
llaves = temps.keys()
print(llaves)
if('Oslo' in llaves):
    print("Se encontró el key de Oslo")

#Quitar una pareja key-value del diccionario
del temps['Oslo']
print(temps)

#Ejemplo evaluación de un polinomio particular p(x), osea cuando se le dan valores a x
#Un polinomio tiene la forma p(x) = a0+a1*x^1+a2*x^2+...+an*x^n
#Ejemplo evaluación de polinomio p(x) = -1+x^2+3*x^7
#El coeficiente con grado 0 tiene coeficiente -1, el coeficiente con grado 2 tiene coeficiente 2 y 
#el coeficiente con grado 7 tiene coeficiente 1
p = {0:-1,2:1,7:3} #Note que la key es la potencia del polinomio
#Función que recibe dos parámetros y retorna un valor
def poly_dict(p,x):
    summa = 0
    for grado in p:
        #Se eleva a potencias en python con **, no con ^
        summa = summa + p[grado]*x**grado
    return summa

print("p(x=2) = ", poly_dict(p,2))