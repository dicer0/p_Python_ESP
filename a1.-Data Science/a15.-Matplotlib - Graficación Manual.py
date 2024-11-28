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

#GRAFICACIÓN CON MATPLOTLIB:
#Hay dos formas de graficar, una al estilo de matlab y la segunda al estilo pyplot que está basada en la 
#programación orientada a objetos:
import matplotlib.pyplot as plt #matplotlib: Librería de graficación matemática.
import numpy as np #numpy: Librería que realiza operaciones matemáticas complejas (matriciales).

#Generamos un arreglo de numpy de 100 elementos desde el valor 0 al 10
#numpy.linspace(): Método que rellena de números un vector, indicando su número de inicio, número final y número 
#de datos.
x = np.linspace(0,10,100) #Vector que va del número 0 al 10 y se compone de 100 datos.
#print(): Imprimir un mensaje en consola.
print(x)



#GRÁFICA ÚNICA TIPO MATPLOTLIB:
#matplotlib.figure(): Método para ordenar los figures (ventanas) donde se muestran las diferentes gráficas.
plt.figure(1)
#matplotlib.grid(): Método que recibe un valor booleano para indicar si aparece una rejilla o no en la gráfica, 
#por default está en valor False.
plt.grid(True) #La rejilla es visible en la gráfica.
#matplotlib.plot(): Método usado para crear la gráfica, indicando como primer parámetro su eje horizontal, luego 
#su eje vertical y finalmente el estilo de la gráfica.
# - Colores:             C1: color naranja, r: color rojo, b: color azul, g: verde, c: cyan, m: morado, 
#   y: amarillo, k: negro, w: blanco.
# - Tipo de marcadores:  o: círculos, +: símbolos de más, .; puntos, v: Triángulo hacia abajo, h: Hexágono, 
#   s: cuadrados, etc.
# - Tipo de Líneas:      -: sólida, --: punteada (líneas), :: punteada (puntos), -.: línea y punto, 'or': Nada.
#numpy.sin(x): Con la librería numpy se pueden crear los datos de amplitud de la gráfica del seno por medio de 
#un vector x que indique los datos del eje horizontal.
plt.plot(x,np.sin(x), 'rh-', label=r'$sin(x)$')#'rh-' significa r: color rojo, h: simbolo hexágonos, -: línea sólida 
#numpy.cos(x): Con la librería numpy se pueden crear los datos de amplitud de la gráfica del coseno por medio 
#de un vector x que indique los datos del eje horizontal.
plt.plot(x,np.cos(x), 'bs:', label=r'$cos(x)$')#'bs:' significa b: color azul, s: simbolo cuadrado, -: línea punteada (puntos)
plt.title(r'Funciones armonicas') #matplotlib.title(): Método que indica el título del figure.
plt.xlabel(r'$x$') #matplotlib.xlabel(): Método que indica el texto que aparece en el eje horizontal.
plt.ylabel(r'$y$') #matplotlib.ylabel(): Método que indica el texto que aparece en el eje vertical.
#matplotlib.legend(): La leyenda de un gráfico es un componente que proporciona información individualmente 
#sobre los diferentes elementos o series presentes en el gráfico, el método permite personalizar dicha 
#leyenda a través de los siguientes parámetros:
# - labels: Se refiere a los nombres que se les puede poner para las leyendas de los distintos elementos del 
#   gráfico. 
#           - Las etiquetas se generan automáticamente pero se pueden colocar manualmente de la siguiente manera: 
#             labels=['Etiqueta 1', 'Etiqueta 2']
# - loc: Indica la ubicación de la leyenda en el gráfico. Se puede indicar con una cadena de texto o un código 
#   numérico que represente una posición específica.
#           - "best": Coloca la leyenda en la mejor ubicación posible, evitando superponerse con otros elementos.
#           - "upper right": Coloca la leyenda en la esquina superior derecha del gráfico.
#           - "upper left": Coloca la leyenda en la esquina superior izquierda del gráfico.
#           - "lower right": Coloca la leyenda en la esquina inferior derecha del gráfico.
#           - "lower left": Coloca la leyenda en la esquina inferior izquierda del gráfico.
#           - "right": Coloca la leyenda en el lado derecho del gráfico, centrada verticalmente.
#           - "center left": Coloca la leyenda en el lado izquierdo del gráfico, centrada verticalmente.
#           - "center right": Coloca la leyenda en el lado derecho del gráfico, centrada verticalmente.
#           - "center": Coloca la leyenda en el centro del gráfico.
plt.legend(loc = "best")
#matplotlib.show(): Método para mostrar la gráfica creada.
plt.show()



#GRÁFICA ÚNICA TIPO PYPLOT:
fig = plt.figure(2) #Creación de un objeto pyplot del figure 2 que instancíe la librería matplotlib.
ax = plt.axes() #Objeto ax que instancíe la librería matplotlib por medio del método axes().
ax.plot(x,np.sin(x), 'C1o-.', label=r'$sin(x)$')#'C1o-' significa C1: color naranja, o: simbolo redondito, -.: línea y punto
ax.plot(x,np.cos(x), 'w+--', label=r'$cos(x)$')#'w+--' significa w: color blanco, +: simbolo de más, --: línea punteada (líneas)
ax.set_title(r'Funciones armonicas') #matplotlib.axes().title(): Método que indica el título del figure.
ax.set_xlabel(r'$x$') #matplotlib.axes().set_xlabel(): Método setter que indica el texto del eje horizontal.
ax.set_ylabel(r'$y$') #matplotlib.axes().set_ylabel(): Método setter que indica el texto del eje vertical.
#axes.set_facecolor(): Método para indicar el color de fondo de la gráfica, el cual puede ser indicado por los 
#mismos colores previamente mencionados en el método plot() o se pueden usar los siguientes con el código xkcd:
# - Colores: xkcd:aqua, xkcd:aquamarine, xkcd:azure, xkcd:beige, etc. Los colores se pueden obtener de este link:
#https://matplotlib.org/stable/tutorials/colors/colors.html
ax.set_facecolor('xkcd:lime')
ax.legend(loc = "best")#Con esto se muestra en detalle cuál es cuál de las gráficas mostradas en el figure
plt.show()#Con esto se muestra la gráfica creada



#GRÁFICA DOBLE TIPO MATPLOTLIB:
plt.figure(3)
#Primera gráfica:
plt.subplot(2,1,1)#2 renglones, 1 columna y primera gráfica
plt.plot(x, np.sin(x), 'k.-')#'k.-' significa k: color negro, .: simbolo de punto, -: línea sólida
plt.xlabel(r'$x_{1}$')#Texto que aparece en el eje horizontal, lo que exista dentro de las llaves es un subindice
plt.ylabel(r'$y_{1}$')#Texto que aparece en el eje vertical, lo que exista dentro de las llaves es un subindice
plt.title(r'Funciones armonicas')#Título del figure completo
#Primera gráfica:
plt.subplot(2,1,2)#2 renglones, 1 columna y segunda gráfica
plt.plot(x, np.cos(x), 'mo:')#'C1o-' significa C1: color morado, o: simbolo de círculo, :: línea punteada (puntos)
plt.xlabel(r'$x_{2}$')#Texto que aparece en el eje horizontal, lo que exista dentro de las llaves es un subindice
plt.ylabel(r'$y_{2}$')#Texto que aparece en el eje vertical, lo que exista dentro de las llaves es un subindice
plt.show()#Con esto se muestra la gráfica creada



#GRÁFICA DOBLE TIPO PYPLOT:
fig,ax = plt.subplots(2) #Esto indica que se van a hacer 2 gráficas, no se puede indicar el número de figure
#Primera gráfica:
ax[0].plot(x,np.sin(x), r'wv-')#'wv-' significa w: color blanco, v: simbolo de triángulo hacia abajo, -: línea sólida
ax[0].set_ylabel(r'$y_{1}$')#Texto que aparece en el eje verical, de la gráfica indicada dentro de las llaves
ax[0].set_title(r'$Funciones$')#Título del figure completo
ax[0].set_facecolor('xkcd:black')#Color de fondo de la gráfica 1
#Segunda gráfica:
ax[1].plot(x,np.cos(x), r'r.-.')#'r.-.' significa r: color rojo, .: simbolo de puntos, -.: línea y punto
ax[1].set_ylabel(r'$y_{2}$')#Texto que aparece en el eje verical, de la gráfica indicada dentro de las llaves
ax[1].set_xlabel(r'$x$')#Texto que aparece en el eje horizontal
ax[1].set_facecolor('xkcd:cyan')#Color de fondo de la gráfica 2
plt.show()#Con esto se muestra la gráfica creada