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

import math #math: Librería que proporciona funciones y constantes matemáticas como seno, π, logaritmo, etc.
import numpy as np #numpy: Librería que realiza operaciones matemáticas complejas (matriciales).
import tabulate #tabulate: Librería que permite crear tablas con varios formatos conocidos.
import matplotlib.pyplot as plt #matplotlib: Librería de graficación matemática.

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

#5.- CAMPANA DE GAUSS: La campana de Gauss o también llamada distribución normal es una representación gráfica 
#que muestra una distribución de datos en torno a un valor central llamado media, con la Campana de Gauss es 
#posible establecer una serie de parámetros que ayudan a predecir y racionalizar lo que aparentemente son 
#resultados aleatorios, obteniendo una versión más clara y visual de la distribución de un conjunto de números. 
#Esta herramienta se utiliza para representar la dispersión de los datos y su tendencia, con el fin de detectar 
#patrones o comportamientos en diferentes situaciones, por lo cual es muy utilizada en estadística, 
#probabilidad, filtros, visión artificial, etc. En su expresión más sencilla:
# - a = Representa el valor más alto (amplitud) de la campana de Gauss.
#       - Mientras menor sea el valor de σ, mayor será la amplitud de la función.
# - b = Es la posición del centro de la campana.
#       - b = μ = m: Esta variable es llamada media.
#       - La función es simétrica respecto a la media µ.
#       - Su valor máximo se encuentra en la media µ.
# - c = Controla el ancho de la campana de Gauss (desviación estándar).
#       - c^2 = σ^2 = s^2: Esta variable es llamada varianza.
#       - En las coordenadas de µ − σ y µ + σ se presentan los puntos de inflexión de la curva.
#G(x) = (a)e^[(-(x-b)^2)/(2c^2)] = (1/(σ√2π))e^[(-(x-μ)^2)/(2σ^2)] = (1/(s√2π))e^[-1/2*((x-m)/s)^2].

#a) Escribe una Función en Python llamada gauss(x, m = 0, s = 1) para calcular el resultado de una función 
#Gaussiana.
#La función gaussiana recibe 3 parámetros:
# - x: Eje horizontal.
# - m: Media, es el punto central de la función.
# - s: Varianza, dicta el ancho de la función.
#G(x) = (1/s√2π)*exp(-1/2*((x-m)/s)^2)
def gauss(x, m , s ):
    resultado = []              #Lista vacía que almacena el resultado de la función Gaussiana.
    #BUCLE FOR EACH: Es un tipo especial de bucle for que sirve para recorrer todos los elementos de una lista, 
    #tupla o diccionario, su sintaxis es la siguiente: 
    # - for i in lista: 
    #La instrucción del Bucle for each es equivalente a poner la instrucción: 
    # - for i in range(0, len(lista)):
    #Es importante mencionar que al usar el bucle for each, la variable del Bucle ahora será manejada como si 
    #fuera una lista en sí a la cual se le están accediendo todos sus valores, por lo cual ahora usar esta 
    #variable corresponde a haber accedido a cada valor de la lista que recorra el bucle:
    # - i = lista[i]
    for i in x:                 #Bucle for each que recorre todos los puntos del eje x.
        var_temporal = []       #Variable intermedia que almacena cada coordenada (x, G) de la función Gauss.
        #math.sqrt(x) = √x = x**1/2: Método que saca la raíz cuadrada de un número.
        #math.pi(): Constante pi (π) de la librería math.
        #math.exp(x) = e^x = e**x: Método que devuelve el valor exponencial de un número con base "e".
        #G(x) = (1/s√2π)*exp((-1/2)*((x-m)/s)^2)
        G = (1/(s*math.sqrt(2*math.pi)))*(math.exp((-1/2)*((i-m)/s)**2))
        #append(): Método que sirve para agregar valores a una lista, tupla, numpy array o diccionario.
        #Dentro de la lista de variable temporal primero se agregan los valores del eje x y luego los resultados 
        #de la función Gaussiana correspondiente para cada uno.
        #Colocar primero .append(i) y luego .append(G) no es lo mismo a poner .append([i, G]), ya que con la 
        #segunda instrucción se estará creando una lista interna innecesaria que estará causando problemas al 
        #intentar crear la tabla de datos con la librería tabulate.
        var_temporal.append(i)
        var_temporal.append(G)
        #Al final el resultado de la variable temporal que contiene los valores de x y G se agrega a la lista de 
        #resultado, para que de esta manera se cree una lista anidada que contenga las coordenadas de todos los 
        #puntos de la función Gaussiana.
        #Otra forma de lograr lo mismo sin haber usado una variable intermedia fue haber aplicado el método 
        #.append([i, G]) directamente al vector resultado.
        resultado.append(var_temporal)
    print("Coordenadas del vector Var temporal:\n", var_temporal, "\n")
    print("Vector Resultado G(x):\n", resultado, "\n")
    return resultado

#Ahora se debe crear el rango de valores para los cuales se aplicará la función Gauss, que esta estará en un 
#intervalo de:  [m - 5s, m + 5s]
m = 0                           #m = Media, indica el punto central de la función.
s = 1                           #s = Varianza, mientras mayor sea, función más ancha, pero reduce su amplitud.
n = 30                          #n = Número de valores que conforman la curva de Gauss.
r = (abs(m-5*s) + abs(m+5*s))/(n-1) #r = intervalo = [m-5s, m+5s]/(n-1)
#numpy.arange(): El método arange sirve para crear un listado de elementos indicando su punto inicial, punto 
#final e intervalo de valores; np.arange(punto_inicial, punto_final, intervalo).
xi = np.arange((m-5*s), (m+ 5*s) + r, r)

#USO DE LA FUNCIÓN gauss(): Creación de la función Gauss a través del eje horizontal x, el valor de media (m) y 
#de varianza (s).
fg = gauss(xi, m, s)            #Aplicación de la función Gauss

#BUCLE FOR EACH: Es un tipo especial de bucle for que sirve para recorrer todos los elementos de una lista, 
#tupla o diccionario, su sintaxis es la siguiente: 
# - for i in lista: 
#La instrucción del Bucle for each es equivalente a poner la instrucción: 
# - for i in range(0, len(lista)):
#Es importante mencionar que al usar el bucle for each, la variable del Bucle ahora será manejada como si fuera 
#una lista en sí a la cual se le están accediendo todos sus valores, por lo cual ahora usar esta variable 
#corresponde a haber accedido a cada valor de la lista que recorra el bucle:
# - i = lista[i]
x_graph = []                    #Lista vacía que almacenará el eje horizontal para graficar la función Gauss.
y_graph = []                    #Lista vacía que almacenará el eje vertical para graficar la función Gauss.
for j in fg:                    #Bucle for each que recorre todas las coordenadas de la función Gauss.
    #append(): Método que sirve para agregar valores a una lista, tupla, numpy array o diccionario.
    x_graph.append(j[0])        #Acceso al indice 0 (x) de la lista anidada en cada coordenada del vector fg.
    y_graph.append(j[1])        #Acceso al indice 1 (y) de la lista anidada en cada coordenada del vector fg.
#print(): Método para imprimir un mensaje en consola y después dar un salto de línea (Enter), además si se 
#quiere concatenar un mensaje (mostrar resultados de variables junto con texto estático), este se debe separar 
#entre comillas, declarando los mensajes estáticos entre comillas y los nombres de variables sin comillas.
print("x:", x_graph, "\n")      #Impresión en consola del vector x.
print("y:", y_graph, "\n")      #Impresión en consola del vector y.
print("\n")

#GRAFICAR DATOS EN PYTHON:
#matplotlib.figure(): Método usado para crear la ventana de graficación (objeto pyplot).
fig = plt.figure()#Creación del objeto pyplot.
#matplotlib.axes(): Método usado para crear la rejilla en la ventana de graficación.
ax = plt.axes()#Se crea un objeto ax perteneciente de la clase axes().
#axes.plot(): Método usado para crear la gráfica en la rejilla previamente creada en la ventana de graficación, 
#indicando como primer parámetro su eje horizontal, luego su eje vertical y finalmente el estilo de la gráfica:
# - Colores:             C1: color naranja, r: color rojo, b: color azul, g: verde, c: cyan, m: morado, 
#   y: amarillo, k: negro, w: blanco.
# - Tipo de marcadores:  o: círculos, +: símbolos de más, .; puntos, v: Triángulo hacia abajo, h: Hexágono, etc.
# - Tipo de Líneas:      -: sólida, --: punteada (líneas), :: punteada (puntos), -.: línea y punto, 'or': Nada.
ax.plot(x_graph, y_graph, 'w1:')#'w1:' significa w: color blanco, 1: tri_down :: línea punteada (puntos).
#axes.set_xlabel(): Método para indicar el texto que aparece en el eje x.
ax.set_xlabel(r'$x$')#Texto que aparece en el eje horizontal
#axes.set_ylabel(): Método para indicar el texto que aparece en el eje y.
ax.set_ylabel(r'$y = G(x, m, s)$')#Texto que aparece en el eje vertical
#axes.set_facecolor(): Método para indicar el color de fondo de la gráfica, el cual puede ser indicado por los 
#mismos colores previamente mencionados en el método plot() o se pueden usar los siguientes con el código xkcd:
# - Colores: xkcd:aqua, xkcd:aquamarine, xkcd:azure, xkcd:beige, etc. Los colores se obtienen de este link:
#https://matplotlib.org/stable/tutorials/colors/colors.html
ax.set_facecolor('xkcd:crimson')
#matplotlib.show(): Método para mostrar la gráfica creada.
plt.show()

#CREAR UNA TABLA CON LA LIBRERÍA TABULATE: La tabla se mostrará hasta que cierre la ventana de la gráfica.
#tabulate.tabulate(): Método que sirve para crear una lista con los valores de un vector, dicho vector debe 
#contener listas anidadas en cada una de sus posiciones para que estas sean agrupadas en cada fila de la lista.
#Las tablas creadas con el método tabulate aceptan los siguientes parámetros:
# - tabular_data: Este parámetro especifica los datos a mostrar. Puede ser una lista de listas, una lista de 
#   diccionarios, una lista de tuplas, o una estructura de datos similar.
# - headers: Es un parámetro opcional que se utiliza para especificar los encabezados de las columnas de la 
#   tabla. Puede ser una lista de cadenas que representen los nombres de las columnas.
# - tablefmt: Es un parámetro opcional que indica el formato deseado para la tabla generada. 
#       - "plain": Sin formato adicional.
#       - "simple": Formato simple con líneas horizontales.
#       - "grid": Formato con bordes de cuadrícula.
#       - "pipe": Formato con delimitadores de tubería.
#       - "orgtbl": Formato de tabla org.
# - numalign: Este parámetro se utiliza para alinear los números en las columnas de la tabla. Puede tener los 
#   siguientes valores:
#       - "left": Alinea los números a la izquierda.
#       - "center": Centra los números en la columna.
#       - "right": Alinea los números a la derecha.
# - stralign: Este parámetro se utiliza para alinear las cadenas de texto en las columnas de la tabla. Puede 
#   tener los siguientes valores:
#       - "left": Alinea las cadenas de texto a la izquierda.
#       - "center": Centra las cadenas de texto en la columna.
#       - "right": Alinea las cadenas de texto a la derecha.
# - missingval: Este parámetro se utiliza para establecer el valor a mostrar cuando los datos son nulos o no están 
#   disponibles. Puede ser cualquier valor válido, como una cadena de texto, un número, etc. Cuando se encuentre un 
#   valor nulo en los datos, se mostrará el valor especificado en missingval.
print(tabulate.tabulate(tabular_data = fg, headers = ['x','f(x)'], tablefmt = "grid", numalign = "center", missingval = "invalid_data"))