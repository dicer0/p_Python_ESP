# -*- coding: utf-8 -*-
#Comentario de una sola linea con el simbolo #, en Python para nada se deben poner acentos sino el programa
#puede fallar o imprimir raro en consola, la primera línea de código es para que no tenga error, pero aún
#así al poner un ángulo saldrá raro en consola, la línea debe ponerse tal cual como aparece y justo al inicio.

#ANÁLISIS DE IMAGEN: Las imágenes digitales son una matriz 3D de tres capas, la R, G y B, estas son analizadas desde la primera
#posición de su pixel, que siempre se considera como el pixel superior izquierdo, para analizar una imagen se deben seguir los 
#siguientes pasos, considerando que el pixel es la unidad mínima de una imagen digital: 
# 1.- Captura de imagen: Se refiere a la recopilación por medio de fotos o video.
# 2.- Muestreo de imagen: Se refiere al analisis de los pixeles de la imagen y sus vecindarios.
# 3.- Cuantificación: Se convierte la imagen a una escala de grises y se analiza su histograma para identificar el umbral.
# 4.- Codificación: Se aplica filtros dependiendo de la condición de brillo y contraste de la imagen original, para finalmente 
#binarizarla y de esta manera separar el fondo del objeto que se quiere identificar.  

#2.- VECINDARIOS: Los pixeles tienen vecindarios, estos se refieren a los pixeles que rodean a uno solo que se está analizando, 
#existen dos tipos considerando una matriz de 3X3 para crear un vecindario de 9 pixeles en total y teniendo en cuanta que el 
#pixel central es el que se está analizando, realizando así el muestreo de la imagen:
# - Vecindarios de 4 pixeles: Considera los 4 pixeles que se encuentren rodeando al pixel central, ya sea en forma de cruz (osea 
# en forma horizontal) o en forma de tache (osea en forma inclinada). 
# - Vecindarios de 8 pixeles: Considera los 8 pixeles que rodeen al pixel central tomando en cuenta que la vecindad se compone 
# de 3 filas y 3 columnas donde el pixel central se debe encontrar en medio.

#3.- ESCALA DE GRISES: Las imágenes digitales en forma matemática son una matriz 3D que consta de tres capas de varias filas y 
#columnas, estas capas son las R, G y B. Esto implica que cuando se realiza el análisis de las imágenes se deben procesar estas 
#tres matrices sobrepuestas, para mejorar en la velocidad del análisis, se transforma a una escala de grises para que se analice 
#una sola capa que represente las 3 anteriores.
#Se cuenta con 3 tipos de imagenes:
# - RGB: Matriz 3D con una matriz 2D que represente cada color primario RGB en la imagen digital.
# - Escala de grises: Una sola matriz de dimensión 2D.
# - Imagenes binarias: Matriz donde solo se tiene ceros y unos, osea blancos y negros intensos.

#3.- HISTOGRAMA: Es una gráfica que representa los distintos tonos de Rojo, Verde o Azul en una imagen, en el eje horizontal 
#se representa cada uno de los tonos del color yendo de 0 a 255 (llamado luminosidad) y en el eje vertical se representa el 
#número de pixeles que corresponden a cada tono de cada capa (llamado porcentaje). El tono de cada color va de 0 a 255 porque 
#cada color se representa con 8 bits, 2^8 = 256, pero en este número también se considera el cero como valor. La forma de 
#interpretar el resultado del histograma es la siguiente:
#Cada capa RGB de la imagen cuando se descompone va de 0 a 255, esto es porque en cada capa mientras más se acerque al valor 
#255 (osea el blanco) es porque más presente se encuentra ese color en la imagen, por lo que en el histograma la gráfica que 
#más se acerque al 255 en el eje horizontal es la que representa el color que más se encuentra presente en la imagen no 
#importando su amplitud, ya que la amplitud representa cuantos pixeles cuentan con el mismo tono de cada color RGB o también 
#se puede realizar para escala de grises, al usarse el histograma en una escala de grises se reconoce el brillo y contraste de 
#la imagen.

#3.- BRILLO: El brillo se refiere a la luminosidad de la imagen, osea que tan obscuros o claros son los pixeles que la conforman.
#Se logra aumentar el brillo cuando se le suma a una imagen un número entre 1 y 255, si se quiere reducir el brillo se deberá 
#restar en vez de sumar.

#3.- CONTRASTE: El contraste no es otra cosa que el efecto que se produce al destacar un elemento visual en comparación con 
#otro en una misma imagen. El contraste puede darse bien sea por la combinación de diferentes colores, intensidad de luces y 
#sombras, diferencias de tamaño, textura, o cualquier otro elemento visual. Su efectividad depende directamente de los valores 
#del histograma de la imagen.
#Se logra aumentar el contraste en el código cuando se multiplica la matriz que representa una imagen digital por un número entre 
#1 y 2, donde la parte decimal indicará el porcentaje de aumento del contraste, por ejemplo si se multiplica una imagen por 1.5 
#se estaría aumentando en un 50% el contraste. Si se quiere reducir el contraste se deberá multiplicar por un número entre 0 y 1.

#Para poder realizar un buen contraste se debe contar con una imagen cuyo histograma no esté muy cargado de pixeles blancos, osea 
#con la mayoría de sus valores cercanos al valor 255 (del lado derecho de la gráfica) ni muy cargado de pixeles negros, osea muy 
#cargado de valores cercanos al valor 0 (del lado izquiero de la gráfica), la situación ideal para poder procesar y analizar de 
#buena manera una imagen, es que el histograma de la imagen cuente con una distribución homogenea de pixeles, ni tan cargados del 
#lado derecho (claros) ni del izquierdo (obscuros). Si este no fuera el caso, se debería pasar la imagen por algún filtro para 
#poder analizar la imagen y separar el fondo del objeto que se busca analizar, que es una operación muy común en visión 
#artificial, para ello se declara una ecuación donde f(x,y) es la matriz de la imagen, C es el contraste y B es el brillo:
# I(x,y) = f(x,y) = C * I(x,y) + B

#3.- COMPLEMENTO: Lo que hace es restar el valor máximo de la matriz menos la función de la imagen original y de esta manera se 
#obtiene el inverso de la imagen original, en donde si antes había un color blanco, ahora habrá un color negro y viceversa: 
# finv(x,y) = fmax - f(x,y)

#4.- UMBRALIZAR: Cuando el histograma se utiliza en una imagen con escala de grises se puede indicar su contraste y brillo 
#(iluminación), al hacer esto se puede umbralizar la imagen, osea indicar que a partir de cierto valor de un tono de gris, se 
#diferencíe el fondo del objeto que se quiere identificar en la imagen. Al umbralizar normalmente se crean imagenes binarias, 
#donde al objeto normalmente se le asigna un valor de 1 y al fondo se le asigna un valor de 0, aunque puede ser viceversa, el 
#chiste es diferenciar uno del otro a partir de cierto umbral reconocido en el histograma de la imagen. El umbral es un número 
#entero que puede valer de 0 a 255.

#4.- ADAPTACIÓN AUTOMÁTICA AL CONTRASTE: Para que se mejore de forma automática un poco el contraste y la definición de la 
#imagen, se debe aplicar la siguiente ecuación considerando un rango de tono de grises en el contraste que solamente se quiere 
#tomar en cuenta llamados fH y fL:
# fac(x,y) = f(x,y) - fmin * (fmax - fmin)/(fH - fL)

#4.- OPERACIONES LÓGICAS ARITMÉTICAS: La suma o resta de dos imágenes sirve para segmentación de ciertos objetos en la imagen, 
#esto es para reconocimiento de patrones, con el fin de reconocer objetos específicos en una imagen, detección de movimiento o 
#posiciones y también para meter o quitar ruido. Cuando se vaya a sumar o restar imágenes, primero estas se deben ajustar para 
#que tengan un tamaño igual, ya que sino se perderá mucha información

#4.1.- OPERACIÓN DE MEZCLADO ALFA EN SUMAS O RESTAS DE IMÁGENES: Se refiere a una proporción α, esto implica cuánto porcentaje 
#de una imagen se suma o resta respecto a otra, que igual está siendo multiplicada respecto a el porcentaje restante del 100%
#en la imagen resultante Ir(x,y) cuando se hace una suma o resta de dos imágenes IA e 1B.
# Ir(x,y) = (1-α) * IA(x,y) ± α * IB(x,y)

#4.- FILTROS ESPACIALES: Los filtros espaciales son aquellos donde el pixel nuevo obtenido después de haber aplicado el filtro 
#no es nadamás resultado de la operación matemática sobre el mismo pixel de análisis sino de la aportación de los pixeles de su 
#vecindario, en filtros lineales es importante considerar el tamaño del filtro y vecindario que puede tener el siguiente número 
#de filas y columnas en la vecindad de analisis: 3X3, 5X5, 7X7 o 31X31. Esto se utiliza para dar un suavizado a la imagen. 
#Los filtros espaciales se llevan a cabo por la aplicación de una convolución entre el pixel de interés, sus vecindarios y los 
#coeficientes de la matriz de coeficientes del filtro.
#CONVOLUCIÓN: Una convolución es un operador matemático que transforma dos funciones f y g en una tercera función que en cierto 
#sentido representa la magnitud en la que se superponen f y una versión trasladada e invertida de g.


#IMPORTACIÓN DE LIBRERÍAS:
import cv2 as cv #Librería OpenCV: Sirve para todo tipo de operaciones de visión artificial
import numpy as np #Librería numpy: Realiza operaciones matemáticas complejas
import os as os #Librería os (operating system): Sirve para indicar una ruta de directorio donde se encuentra algún archivo 


#IMAGEN RGB:
#Función para obtener imagen de Lena.jpg
def lenaJPG():
    #Para leer una imagen o cualquier otro archivo se usa la dirección relativa del directorio, la cual es una dirección que 
    #se busca desde donde se encuentra la carpeta del archivo python actualmente, esta se debe colocar entre comillas simples 
    #o dobles:
    #   ..      : Significa que nos debemos salir de la carpeta donde nos encontramos actualmente.
    #   /       : Sirve para introducirnos a alguna carpeta cuyo nombre se coloca después del slash.
    #   .ext    : Se debe colocar siempre el nombre del archivo + su extensión.
    #El error que se puede experimentar cuando se usa una ruta relativa es que está configurada en relación con el directorio
    #de trabajo actual, por lo que si el programa se ejecuta desde una ubicación diferente a la carpeta donde se encuentra  
    #este archivo, el programa no podrá abrir ninguno de los archivos indicados y arrojará una excepción.
    path = "0.-Img/Lena.jpg"
    #imread(): Sirve para leer la imagen de un directorio especificado, si en el segundo parámetro se pone un 1, la imagen se 
    #obtendrá en forma de matriz 3D RGB y si se pone un 0 se obtendrá en escala de grises, obteniendo una matriz 2D.
    img = cv.imread(path, 1)
    return img
#Ejecución de la función lenaJPG() que obtiene una imagen de un directorio en específico
img = lenaJPG()
#imshow(): Con el método se puede mostrar una imagen, el primer parámetro es el nombre de la ventana donde aparecerá la imagen 
#y el segundo parámetro es la imagen recopilada con el método imread()
cv.imshow('RGB', img)
#Estas dos líneas de código sirven para que no se cierre la ventana inmediatamente después de abrirse, solo cuando se dé 
#clic en el tache de la ventana, son parte de la librería OpenCV:
#waitKey(): Método que permite a los usuarios mostrar una ventana durante un número de milisegundos determinados o hasta que se 
#presione cualquier tecla. Toma tiempo en milisegundos como parámetro y espera el tiempo dado para destruir la ventana, o si se 
#pasa 0 en el argumento, espera hasta que se presiona cualquier tecla.
cv.waitKey(0)
#destroyAllWindows(): Función que permite a los usuarios destruir todas las ventanas en cualquier momento. No toma ningún 
#parámetro y no devuelve nada, esto se incluye para que al cerrar la ventana después del método waitKey() se destruyan para 
#poder utilizarse en otra cosa.
cv.destroyAllWindows()




#CONVERSIÓN RGB A ESCALA DE GRIS: 
#cvtColor(): Método de la librería OpenCV que recibe como primer parámetro una imagen RGB y en su segundo parámetro recibe un
#atributo de OpenCV llamado COLOR_BGR2GRAY para convertir una imagen RGB a su escala de grises
img2 = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Escala de grises', img2) #Mostrar una ventana que tenga como título el 1er parametro y muestre la imagen del 2do
cv.waitKey(0) #Mostrar la ventana hasta que se presione la tecla X
cv.destroyAllWindows() #Destruir todas las ventanas después de cerrarlas con el comando




#IDENTIFICACIÓN DE COLORES:
#Función para obtener imagen de Figuras.png en matriz 3D RGB
def figuresPNG():
    #Para leer una imagen de forma directa, se debe encontrar justo en la misma carpeta que el código pyhton donde nos 
    #encontramos, si está en otro directorio se debe usar una función intermedia que cambie las diagonales \ por /, ya que sino 
    #el programa dará error cuando quiera leer el archivo.
    path = '0.-Img/Figuras.png'
    #imread(): Sirve para leer la imagen de un directorio especificado, si en el segundo parámetro se pone un 1, la imagen se 
    #obtendrá en forma de matriz 3D RGB y si se pone un 0 se obtendrá en escala de grises, obteniendo una matriz 2D.
    img = cv.imread(path, 1)
    return img
#Extracción de imagen con colores RGB definidos:
img3 = figuresPNG()
cv.imshow('Colores de figura', img3) #Mostrar una ventana que tenga como título el 1er parametro y muestre la imagen del 2do
cv.waitKey(0) #Mostrar la ventana hasta que se presione la tecla X
cv.destroyAllWindows() #Destruir todas las ventanas después de cerrarlas con el comando

#CAPAS RGB DE LAS IMAGENES
#split(): Método que extrae los diferentes colores de la imagen en 3 distintas variables, guardándo primero el color azul, luego 
#el verde y finalmente el rojo, específicamente en ese órden.
b, g, r = cv.split(img3)
cv.imshow('Blue', b) #Mostrar una ventana que tenga como título el 1er parametro y muestre la imagen del 2do
cv.imshow('Green', g) #Mostrar una ventana que tenga como título el 1er parametro y muestre la imagen del 2do
cv.imshow('Red', r) #Mostrar una ventana que tenga como título el 1er parametro y muestre la imagen del 2do
cv.waitKey(0) #Mostrar la ventana hasta que se presione la tecla X
cv.destroyAllWindows() #Destruir todas las ventanas después de cerrarlas con el comando




#Extracción de imagen con colores RGB no definidos:
#Esto anterior solo extrae las capas G, B y R de la imagen, si se aplica a una imagen con los colores primarios no tan definidos 
#se obtendrá una capa de cada color, donde el blanco representa el tono de cada capa RGB que más se acerque a valer 255 en el 
#rango de color de 0 a 255 para cada correspondiente color R, G o B.
azulito, verdecito, rojito = cv.split(img)
cv.imshow('Blue 2', azulito) #Mostrar una ventana que tenga como título el 1er parametro y muestre la imagen del 2do
cv.imshow('Green 2', verdecito) #Mostrar una ventana que tenga como título el 1er parametro y muestre la imagen del 2do
cv.imshow('Red 2', rojito) #Mostrar una ventana que tenga como título el 1er parametro y muestre la imagen del 2do
cv.waitKey(0) #Mostrar la ventana hasta que se presione la tecla X
cv.destroyAllWindows() #Destruir todas las ventanas después de cerrarlas con el comando




#Función para obtener imagen de Figuras.png en matriz 2D escala de grises
def figuresPNGgray():
    #Para leer una imagen de forma directa, se debe encontrar justo en la misma carpeta que el código pyhton donde nos 
    #encontramos, si está en otro directorio se debe usar una función intermedia que cambie las diagonales \ por /, ya que sino 
    #el programa dará error cuando quiera leer el archivo.
    path = '0.-Img/Figuras.png'
    #imread(): Sirve para leer la imagen de un directorio especificado, si en el segundo parámetro se pone un 1, la imagen se 
    #obtendrá en forma de matriz 3D RGB y si se pone un 0 se obtendrá en escala de grises, obteniendo una matriz 2D.
    img = cv.imread(path, 0)
    return img

img4 = figuresPNGgray()
cv.imshow('Colores de figura', img4) #Mostrar una ventana que tenga como título el 1er parametro y muestre la imagen del 2do
cv.waitKey(0) #Mostrar la ventana hasta que se presione la tecla X
cv.destroyAllWindows() #Destruir todas las ventanas después de cerrarlas con el comando




#EXTRACCIÓN DE CARACTERÍSTICAS DE UNA IMAGEN:
#size: Es un atributo obtenido de una variable obtenida con el método cv.imread(), indica el tamaño de la imagen
tamano = img.size
#shape: Atributo extraído de una variable obtenida con el método cv.imread(), indica distintas características de la imagen y 
#las guarda en 3 distintas variables, guardándo primero el ancho, luego el alto y finalmente el número de canales, 
#específicamente en ese órden.
alto, ancho, canales = img.shape
#dtype: Es un atributo obtenido de una variable obtenida con el método cv.imread(), indica el tipo primitivo al que pertenece la 
#imagen
tipo = img.dtype
#Fórmula con la que se obtiene el mismo tamaño obtenido con el atributo size de la imagen
tamano2 = alto*ancho*canales
#type(): Método que identifica el tipo primitivo de la variable que se le pase como argumento.
#srt(): Convierte lo que haya en su argumento a un tipo primitivo String para que pueda ser impreso en consola o manejado como str.
#print(): Imprime en consola el mensaje que tenga como parámetro.
print("Tipo primitivo original del tamaño:          " + str(type(tamano)))
print("Tipo primitivo original del alto:            " + str(type(alto)))
print("Tipo primitivo original del ancho:           " + str(type(ancho)))
print("Tipo primitivo original de los canales:      " + str(type(canales)))
print("Tipo primitivo original del tipo primitivo:  " + str(type(tipo)))
print("El tamaño de la imagen es de ", tamano, " bytes, su alto es de", alto, "pixeles y su ancho de", ancho, "pixeles.\n"
        "Tiene ", canales, " canales, es de tipo ", tipo, " y su tamaño total es de ", tamano2, " pixeles.")




#CREACIÓN DE IMÁGENES
#CREACIÓN DE IMÁGENES SINTÉTICAS CREADAS A MANITA: Para crear imágenes simplemente se debe declarar la matriz, para esto se usa 
#la librería numpy.
#Declaración e iniciación de las matrices en un tipo de dato de Python llamado lista, siguiendo la nomenclatura descrita a 
#continuación, tomando en cuenta que el número de elementos de las filas debe ser el mismo:
#Matriz_lista = [[fila1],[fila2],...,[fila_n]], FILA X COLUMNA
#vector_renglon = [1,2,3]
#vector_columna = [[1],[2],[3]]
matriz_lista = [[0,0,0,0],
               [0,0,0,0],
               [0,0,0,0],
               [0,0,0,0]] #Matriz con tipo de dato lista, 4X4 = Filas X Columnas
#Las matrices declaradas con el método array de la librería numpy no son listas, son totalmente otro tipo de valor perteneciente 
#a la librería numpy, llamado numpy array y para declarar arrays de este tipo de dato se usa la siguiente nomenclatura:
#matriz_numpy_array = numpy.array([[fila1],[fila2],...,[fila_n]]), FILA X COLUMNA
#La diferencia con la matriz declarada en forma de lista es la siguiente:
#matriz_lista = [[fila1],[fila2],...,[fila_n]], FILA X COLUMNA
matriz_numpy_array1 = np.array(matriz_lista)
#Para que se vea la matriz como una imagen, sebe ser de tipo primitivo uint8, que significa representa un número entero de 8 bits, 
#osea que va de 0 a 2^8=256 y no tiene signo.
matriz_imagen1 = np.uint8(matriz_numpy_array1)
#Se puede mostrar la imagen sintética con el método imshow() o con el método print(), pero si se usa el método imshow() como está 
#tan chiquita la matriz que representa la imagen, esta se va a perder y con el método print mínimo se imprimirá la matriz en 
#consola.
#INSHOW()
cv.imshow('Imagen sintetica a manita', matriz_imagen1) #Mostrar una ventana que tenga como título el 1er parametro y muestre la imagen del 2do
cv.waitKey(0) #Mostrar la ventana hasta que se presione la tecla X
cv.destroyAllWindows() #Destruir todas las ventanas después de cerrarlas con el comando
#PRINT()
print('Matriz que representa una imagen sintetica creada a manita')
print(matriz_imagen1)




#CREACIÓN DE IMÁGENES SINTÉTICAS CREADAS CON MÉTODOS NUMPY EN ESCALA DE GRISES:
#zeros(): Es un método de la librería numpy que se utiliza para crear una matriz de puros ceros, en esta se le pasa como primer 
#parámetro el número de filas y columnas de la matriz entre paréntesis y como segundo parámetro el tipo de dato primitivo de la 
#matriz, el 0 en las imágenes digitales representa el color negro siempre.
#Bit: representa una variable que puede adoptar los valores 1 o 0 nadamás
#Byte: Es un conjunto de 8 bits.
#Píxel: Unidad de las imágenes digitales que comúnmente, se representa con 8 bits (28 colores), con 24 bits (224 colores, 8 bits 
#por canal de color) o con 48 bits (248 colores).
matriz_imagen2 = np.zeros((630, 630), np.uint8)
#INSHOW()
cv.imshow('Imagen sintetica creada con el metodo zeros', matriz_imagen2) #Mostrar una ventana que tenga como título el 1er parametro y muestre la imagen del 2do
cv.waitKey(0) #Mostrar la ventana hasta que se presione la tecla X
cv.destroyAllWindows() #Destruir todas las ventanas después de cerrarlas con el comando
#PRINT()
print('Matriz que representa una imagen sintetica creada con el metodo zeros')
print(matriz_imagen2)

#ones(): Es un método de la librería numpy que se utiliza para crear una matriz de puros unos, en esta se le pasa como primer 
#parámetro el número de filas y columnas de la matriz entre paréntesis y como segundo parámetro el tipo de dato primitivo de la 
#matriz, el 1 en las imágenes digitales si se multiplica por un número de 1 a 255 representará un color en la escala de grises, 
#donde 0 es negro y 255 es blanco.
matriz_imagen3 = np.ones((alto, ancho), np.uint8)*255
#INSHOW()
cv.imshow('Imagen sintetica de 1 capa creada con el metodo ones', matriz_imagen3) #Mostrar una ventana que tenga como título el 1er parametro y muestre la imagen del 2do
cv.waitKey(0) #Mostrar la ventana hasta que se presione la tecla X
cv.destroyAllWindows() #Destruir todas las ventanas después de cerrarlas con el comando
#PRINT()
print('Matriz de 1 capa que representa una imagen sintetica creada con el metodo ones')
print(matriz_imagen3)




#CREACIÓN DE IMÁGENES SINTÉTICAS CREADAS CON MÉTODOS NUMPY EN LAS TRES CAPAS (CANALES) RGB:
#ones(): Es un método de la librería numpy que se utiliza para crear una matriz de puros unos, en esta se le pasa como primer 
#parámetro el número de filas, columnas de la matriz y canales entre paréntesis y como segundo parámetro el tipo de dato primitivo 
#de la matriz, el 1 en las imágenes digitales si se multiplica por un número de 1 a 255 representará un color en la escala de 
#grises, donde 0 es negro y 255 es blanco.
matriz_3D_imagen = np.ones((alto, ancho, 3), np.uint8)*255
#En pyhton a las imágenes RGB se les llama al revés, osea BGR, por lo que el primer parámetro de la matriz accede al valor de los 
#azules, el segundo a los verdes y el último a los rojos. Esto solamente se hace cuando se crea una imagen de 3 canales. Con el 
#comando matriz[:] lo que se está haciendo es acceder a toda la matriz, que en este caso es una matriz 3D de 3 capas, 
#alto = 630 filas y ancho = 630 columnas, por eso es que accediendo de esta forma a la matriz 3D se puede asignar un valor a los 
#valores de sus capas, con esto se puede crear cualquier color RGB, aunque se debe poner en el orden BGR.
matriz_3D_imagen[:] = (255, 0, 0)
#INSHOW()
cv.imshow('Imagen sintetica de 3 capas creada con el metodo ones', matriz_3D_imagen) #Mostrar una ventana que tenga como título el 1er parametro y muestre la imagen del 2do
cv.waitKey(0) #Mostrar la ventana hasta que se presione la tecla X
cv.destroyAllWindows() #Destruir todas las ventanas después de cerrarlas con el comando
#PRINT()
print('Matriz 3D de 3 capas que representa una imagen sintetica creada con el metodo ones')
print(matriz_3D_imagen)




#CREACIÓN DE REJILLAS EN IMÁGENES SINTÉTICAS: Se utilizan también los métodos zeros() o ones() para dar color a la rejilla
rejilla = np.ones((alto, ancho, 3), np.uint8)*255
#Bucle for que recorre todos los pixeles de la imagen sintética para dibujar la rejilla, para dibujar la rejilla se usa el 
#operador matemático llamado módulo. 
#El símbolo % en Python se llama el Operador de Módulo y retorna el remanente de la división del operando izquierdo entre el 
#operando derecho. Se usa para obtener el residuo de un problema de división y en este caso indica que se cree los cuadros de 
#la rejilla hasta que se tenga un múltiplo de los pixeles indicados en el ancho y alto de la rejilla.
for x in range(ancho): #La operación en x afecta el alto de los cuadrados en la rejilla
    for y in range(alto): #La operación en y afecta el ancho de los cuadrados en la rejilla
        #En el condicional if se usa el operador módulo para indicar el ancho y alto de los cuadros de la rejilla, esto porque 
        #la división entre x,y y el número de su izquierda tendrá un residuo cero cuando los pixeles del alto y ancho sean 
        #iguales a los pixeles indicados.
        if((x%30 == 0) or (y%15 == 0)):
            rejilla[x, y] = (50, 120, 100) #Color BGR (Blue, Green, Red)

#INSHOW()
cv.imshow('Rejilla', rejilla) #Mostrar una ventana que tenga como título el 1er parametro y muestre la imagen del 2do
cv.waitKey(0) #Mostrar la ventana hasta que se presione la tecla X
cv.destroyAllWindows() #Destruir todas las ventanas después de cerrarlas con el comando
#PRINT()
print('Rejilla')
print(matriz_3D_imagen)
#Para cerrar todas las ventanas de jalón se puede usar ALT + F4 pero a veces se traba Visual Studio Code y lo debo reiniciar