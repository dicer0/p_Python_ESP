# -*- coding: utf-8 -*-
#Comentario de una sola linea con el simbolo #, en Python para nada se deben poner acentos sino el programa
#puede fallar o imprimir raro en consola, la primera línea de código es para que no tenga error, pero aún
#así al poner un ángulo saldrá raro en consola, la línea debe ponerse tal cual como aparece y justo al inicio.

#IMPORTACIÓN DE LIBRERÍAS:
import cv2 as cv #Librería OpenCV: Sirve para todo tipo de operaciones de visión artificial
import numpy as np #Librería numpy: Realiza operaciones matemáticas complejas
import math #Librería math: Para aplicar funciones matemáticas básicas.




#OBTENCIÓN DE BORDES:
#imread(): Sirve para leer la imagen de un directorio especificado, si en el segundo parámetro se pone un 1, la imagen se 
#obtendrá en forma de matriz 3D RGB y si se pone un 0 se obtendrá en escala de grises, obteniendo una matriz 2D.
#Para leer una imagen o cualquier otro archivo se usa la dirección relativa del directorio, la cual es una dirección que 
#se busca desde donde se encuentra la carpeta del archivo python actualmente, esta se debe colocar entre comillas simples 
#o dobles:
#   ..      : Significa que nos debemos salir de la carpeta donde nos encontramos actualmente.
#   /       : Sirve para introducirnos a alguna carpeta cuyo nombre se coloca después del slash.
#   .ext    : Se debe colocar siempre el nombre del archivo + su extensión.
#El error que se puede experimentar cuando se usa una ruta relativa es que está configurada en relación con el directorio
#de trabajo actual, por lo que si el programa se ejecuta desde una ubicación diferente a la carpeta donde se encuentra  
#este archivo, el programa no podrá abrir ninguno de los archivos indicados y arrojará una excepción.
img1 = cv.imread('0.-Img/Lena.jpg', 0)
#FILTRO CANNY: El filtro de Canny sirve para la identificación de bordes, esto para segmentar figuras en la imagen.
#Lo que hace el detector Canny es mejorar la detección de bordes, ya que quita los bordes que no nos interesan y deja solamente 
#los que si nos interesan, haciendo que el borde sea una sola línea en vez de varias como lo muestran otros detectores de líneas 
#como lo es el operador Sobel.
#El operador Canny ya que realizó la identificación de bordes, ejecutará un proceso llamado umbral de histéresis que hace uso de 
#dos umbrales, para preservar solamente los bordes más pronunciados y quitar los bordes que no nos interesan. Para saber cuales 
#son los valores que se quiere obtener de los bordes, se puede obtener el histograma de la imagen obtenida con los bordes y ver 
#que tonos de gris son los que representan la mayoría de los bordes que queremos preservar.
#cv.Canny(): Aplica el filtro de Canny realizando los siguientes pasos de analisis de imagen: 
# 1.	Suavizar la imagen (difuminarla): Reducción de ruido por medio del filtro Gaussiano.
# 2.	Operador sobel (detección de bordes): Gradiente y orientación del primer borde obtenido de la imagen.
# 3.	Detector Canny: Identificar mejor los bordes de una imagen y aplicar el umbral de histéresis para preservar solamente los 
#       bordes más pronunciados y quitar los bordes que no nos interesan.
#Los parámetros que recibe el método son los siguientes:
# - Como primer parámetro se le pasa una imagen obtenida previamente con el método imread()
# - Como segundo y tercer parámetro se le pasan umbrales para el filtrado de histéresis de la imagen, con ellos obtendremos 
#   ciertos bordes solamente y despreciaremos los demás, el primer umbral es el inferior y el segundo el superior.
# - Como tercer parámetro necesitamos indicar los bordes y apertura de la imagen para el operador Sobel. 
img_canny = cv.Canny(img1, 50, 200, None, 3)
#imshow(): Con el método se puede mostrar una imagen, el primer parámetro es el nombre de la ventana donde aparecerá la imagen 
#y el segundo parámetro es la imagen recopilada con el método imread()
cv.imshow('Imagen original escala de grises', img1)
cv.imshow('Filtro de Canny - Bordes', img_canny) #Mostrar una ventana que tenga como título el 1er parametro y muestre la imagen del 2do




#OBTENCIÓN DE LÍNEAS: Se utiliza mucho para cuando la deteccción de líneas es importante, como por ejemplo en los coches 
#autónomos, detectando así carreteras, señalamientos, etc.
#TRANSFORMADA DE HUGH: Sirve para la identificación de líneas, para ello anteriormente se tuvieron que haber obtenido los bordes 
#con el método de Canny, pero no solo sirve para la identificación de líneas, sino de círculos y puntos.
# https://docs.opencv.org/3.4/d9/db0/tutorial_hough_lines.html
#cv.HoughLines(): Es un método utilizado para la obtención de líneas, para ello se deben ingresar los siguientes parámetros: 
# - Una imagen a la que se haya aplicado el método cv.Canny(), ya que para obtener las líneas de la imagen, previamente se deben 
#   haber identificado los bordes.
# - Valor rho: Resolución de la magnitud de los bordes a identificar, normalmente se pone el valor 1
# - Valor theta: Resolución de la orientación de los bordes a identificar, normalmente se pone el valor π/180 porque se quiere 
#   dar el valor en grados, usando la librería numpy para obtener el valor de pi.
# - Umbral: Es un valor a partir del cual se va a obtener las líneas recopiladas, para saber si se considera como línea o no.
# - None: Este parámetro siempre debe ser none, puede no ponerse pero si se omite, puede fallar la detección de líneas.
lineas = cv.HoughLines(img_canny, 1, np.pi/180, 150, None)
#La matriz obtenida con la matriz de Hugh es de 3 dimensiones con tamaño: 
# - i valores para cada punto en la primera dimensión.
# - Una segunda dimensión con tamaño 1, osea index 0, para acceder al vector que tiene ambos valores θ (theta) y ρ (rho) de las 
#   líneas obtenidas.
# - La tercera dimensión solo tiene 2 valores, osea index 0 y 1 para acceder con 0 al valor de rho y con 1 al valor de theta.
print("Tipo primitivo de lo que devuelve el método de la transformada de Hugh: " + str(type(lineas)))
print("Resultado del método de la transformada de Hugh: \n" + str(lineas))
print("La primera posición del valor rho de la matriz obtenida con transformada de Hugh es: " + str(lineas[0][0][0]))
#Condicional y bucle para mostrar las líneas, ya que si al correrlo no aparecen las líneas dará error el programa, para ello se 
#checa si la variable líneas no está vacía, luego se realiza un bucle que se ejecute el mismo número de veces que el tamaño de 
#lo que contenga la variable líneas, esto para calcular el valor de los tamaños de la magnitud ρ que indica la pendiente de las
#líneas detectadas, que es una matriz 3D.
if lineas is not None:
    for i in range(0, len(lineas)):
        #rho(θ) = x0*cos(θ) + y0⋅sin(θ)
        rho = lineas[i][0][0]
        theta = lineas[i][0][1]
        #Con esto se busca obtener la coordenada horizontal de la primera coordenada que describe la línea.
        a = math.cos(theta)
        x0 = a*rho
        #Con esto se busca obtener la coordenada vertical de la primera coordenada que describe la línea.
        b = math.sin(theta) 
        y0 = b*rho
        #Después se suma la coordenada siguiente para ir obteniendo los puntos de las líneas.
        punto1 = (int(x0 + 1000*b), int(y0 + 1000*a)) #x1 = rho*cos(θ) + 1000*sin(θ), y1 = rho*cos(θ) + 1000*sin(θ)
        punto2 = (int(x0 - 1000*b), int(y0 - 1000*a)) #x2 = rho*cos(θ) - 1000*sin(θ), y2 = rho*sin(θ) - 1000*cos(θ)
        #cv.line(): Con este método perteneciente a la librería OpenCV se puede crear una línea, en él se indica primero en 
        #que imagen obtenida con el método imread() se va a dibujar la figura, luego los dos puntos con coordenadas x,y de la 
        #imagen en donde se va a mostrar la línea, su color en formato BGR y el ancho en pixeles del borde de la línea.
        #En la interfaz se mostrarán líneas en los puntos dónde se hayan obteniendo las líneas en los bordes de la imagen.
        cv.line(img_canny, punto1, punto2, (0, 0, 255), 3)
cv.imshow('Transformada de Hugh - Lineas', img_canny) #Mostrar una ventana que tenga como título el 1er parametro y muestre la imagen del 2do
#NO DEJAR QUE SE CIERREN LAS VENTANAS: Las siguientes dos líneas de código sirven para que no se cierre la ventana inmediatamente 
#después de abrirse, solo cuando se dé clic en el tache de la ventana, son parte de la librería OpenCV.
#waitKey(): Método que permite a los usuarios mostrar una ventana durante un número de milisegundos determinados o hasta que se 
#presione cualquier tecla. Toma tiempo en milisegundos como parámetro y espera el tiempo dado para destruir la ventana, o si se 
#pasa 0 en el argumento, espera hasta que se presiona cualquier tecla.
cv.waitKey(0)
#destroyAllWindows(): Función que permite a los usuarios destruir todas las ventanas en cualquier momento. No toma ningún 
#parámetro y no devuelve nada, esto se incluye para que al cerrar la ventana después del método waitKey() se destruyan para 
#poder utilizarse en otra cosa.
cv.destroyAllWindows()
#Para cerrar todas las ventanas de jalón se puede usar ALT + F4 pero a veces se traba Visual Studio Code y lo debo reiniciar




#OBTENCIÓN DE FIGURAS GEOMÉTRICAS POR MEDIO DE UMBRALIZACIÓN:
#UMBRALIZACIÓN: Se utiliza para indicar que, a partir de cierto valor de un tono de gris que va de 0 a 255, se diferencie el 
#fondo y el objeto que se quiere identificar en la imagen. Al umbralizar se crean imágenes binarias, donde al objeto normalmente 
#se le asigna un valor de 1 y al fondo se le asigna un valor de 0, aunque puede ser viceversa, el chiste es diferenciar uno del 
#otro a partir de cierto umbral.
#Límite superior del umbral es 28 e inferior es 0 para la imagen Figuras.png
#Límite superior del umbral es 120 e inferior es más o menos 100 para la imagen Lena.jpg
umbral = 14 #Umbral del tono de gris en la escala de grises de la imagen, va de 0 a 255
color_contorno = (0, 0, 255) #Variable que almacena un color BGR
img2 = cv.imread('0.-Img/Figuras.png', 1) #Imagen RGB obtenida con el método imread()
#cvtColor(): Método de la librería OpenCV que recibe como primer parámetro una imagen RGB y en su segundo parámetro recibe un
#atributo de OpenCV llamado cv.COLOR_BGR2GRAY para convertir una imagen RGB a su escala de grises
img_gray = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)
#cv.threshold(): Este método sirve para umbralizar una imagen, en ella se le pasa como primer parámetro la imagen en escala de 
#grises que va a umbralizar, a continuación se indica el valor del umbral, el valor máximo que puede alcanzar el umbral y se 
#especifica que el resultado debe ser una imagen binaria con un atributo de OpenCV llamado cv.THRESH_BINARY o si se quiere el 
#inverso se puede usar cv.THRESH_BINARY_INV, en este caso se usa un guión bajo antes del nombre de la variable, porque esta es 
#una variable interna.
#El guión bajo también usa para ignorar valores específicos, si no se necesita algún valor en específico del método, o no usa 
#estos valores, simplemente se asignan estos valores a la "variable" representada con un guión bajo, en python el orden del 
#guión importa.
_, img_umbral = cv.threshold(img_gray, umbral, 255, cv.THRESH_BINARY)
#cv.findContours(): Este método sirve para encontrar los contornos en una imagen, se puede utilizar en vez del filtro Canny, al 
#método se le pasa como primer parámetro la imagen en escala de grises, en las imágenes existen varios tipos de contornos, estos 
#pueden tener jerarquías de dentro hacia fuera o pueden no tenerlas, esto depende del segundo parámetro que se le pase en el 
#método, en este caso vamos a utilizar el parámetro cv.RETR_LIST para que no muestre jerarquía en los bordes que encuentre, 
#posteriormente se le debe indicar en el tercer parámetro la forma en la que se va a guardar la información recabada, ya que 
#puede guardar todos los puntos del contorno identificado o solo guardar los puntos de las esquinas que conforman el contorno, 
#para que guarde todos los puntos de los contornos se le indica con el atributo cv.CHAIN_APPROX_NONE, para guardar solo las 
#esquinas se usa el atributo cv.CHAIN_APPROX_SIMPLE.
contornos, _ = cv.findContours(img_umbral, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
#cv.drawContours(): Método que sirve para dibujar los contornos recabados con el método cv.findContours(), para ello primero se 
#debe indicar en qué imagen se va a dibujar el contorno, no debe ser la misma de la que se obtuvieron los contornos, después se 
#indica en el segundo parámetro la variable en donde están almacenados los contornos, en el tercer parámero se establece si se 
#quiere que sea hueco o sólido el contorno, como se busca que sea sólido se pone -1, si fuera hueco, en esta parte se indicaría 
#los pixeles del perímetro (borde) del contorno, posteriormente se indica el color y finalmente los contornos que quiero que 
#muestre.
cv.drawContours(img2, contornos, -1, color_contorno, 3)
cv.imshow('Umbralizacion', img_umbral) #Mostrar una ventana que tenga como título el 1er parametro y muestre la imagen del 2do
cv.imshow('Imagen contornos', img2) #Mostrar una ventana que tenga como título el 1er parametro y muestre la imagen del 2do
#NO DEJAR QUE SE CIERREN LAS VENTANAS: Las siguientes dos líneas de código sirven para que no se cierre la ventana.
cv.waitKey(0) #Mostrar la ventana hasta que se presione la tecla X
cv.destroyAllWindows() #Destruir todas las ventanas después de cerrarlas con el comando