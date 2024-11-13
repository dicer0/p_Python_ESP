# -*- coding: utf-8 -*-
#Comentario de una sola linea con el simbolo #, en Python para nada se deben poner acentos sino el programa
#puede fallar o imprimir raro en consola, la primera línea de código es para que no tenga error, pero aún
#así al poner un ángulo saldrá raro en consola, la línea debe ponerse tal cual como aparece y justo al inicio.

#IMPORTACIÓN DE LIBRERÍAS:
import cv2 as cv #Librería OpenCV: Sirve para todo tipo de operaciones de visión artificial

#OBTENCIÓN DE LA GEOMETRÍA DE OBJETOS POR MEDIO DE UMBRALIZACIÓN Y SINTONIZACIÓN CON BARRA DE VALOR VARIABLE:
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
img1 = cv.imread('0.-Img/Monedas.jpg', 1) #Imagen RGB obtenida con el método imread()
#shape: Atributo extraído de una variable obtenida con el método cv.imread(), indica distintas características de la imagen y 
#las guarda en 3 distintas variables, guardándo primero el ancho, luego el alto y finalmente el número de canales, 
#específicamente en ese órden.
alto, ancho, canales = img1.shape
#Se analizó el tamaño de la imagen para ver si es necesario utilizar el método resize que cambia el tamaño de la imagen, esto se 
#hace porque si la imagen es demasiado pequeña, no podrá aparecer la barra que varía el valor del umbral correctamente, por lo 
#cual no se podrá sintonizar la imagen correctamente, específicamente se realiza esto cuando el alto y ancho de la imagen es menor
#a 200 pixeles correspondientemente.
if((alto < 200) or (ancho < 200)):
    #resize(): Lo que hace este método es cambiar el tamaño de una imagen obtenida con el método imread(), para ello recibe como 
    #primer parámetro la variable que almacena la imagen y como segundo parámetro indica la magnitud de la nueva imagen. 
    #Si el ancho o alto de la imagen es menor a 200 pixeles, se le da un nuevo tamaño de 500x500 pixeles.
    img1_bigger = cv.resize(img1, (500, 500))
    img1_modificada = img1_bigger
else:
    #Si el ancho o alto de la imagen no es menor a 200 pixeles en cualquiera de las dos magnitudes, se deja el tamaño tal cual está
    img1_modificada = img1
#copy(): Este método se debe aplicar a un objeto de la librería OpenCV y sirve para crear una copia del objeto al que se esté 
#aplicando para poder guardarse en una variable extra.
#Se crea una copia de la imagen original para que cuando se modifique la imagen original, de donde se obtendrá el resultado del 
#color, y cuando ya no quiera que se vea esa modificación, debe haber una imagen que refresque la interfaz y muestre la imagen 
#original, por eso es que se creó esta copia.
img_copy = img1_modificada.copy()
#cvtColor(): Método de la librería OpenCV que recibe como primer parámetro una imagen RGB y en su segundo parámetro recibe un
#atributo de OpenCV llamado cv.COLOR_BGR2GRAY para convertir una imagen RGB a su escala de grises, este método debe recibir la 
#imagen original, no importando el tamaño de la imagen que se quiere mostrar con el navbar porque sino se modificará toda la 
#identificación de la geometría de los objetos en la imagen.
img_gray = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)

#Función para umbralizar y crear una imagen binaria:
def Imagen_Binaria(umbral):
    global img_umbral
    #cv.threshold(): Este método sirve para umbralizar una imagen, en ella se le pasa como primer parámetro la imagen en escala de 
    #grises que va a umbralizar, a continuación se indica el valor del umbral, el valor máximo que puede alcanzar el umbral y se 
    #especifica que el resultado debe ser una imagen binaria con un atributo de OpenCV llamado cv.THRESH_BINARY o si se quiere el 
    #inverso se puede usar cv.THRESH_BINARY_INV, en este caso se usa un guión bajo antes del nombre de la variable, porque esta es 
    #una variable interna.
    #El guión bajo también usa para ignorar valores específicos, si no se necesita algún valor en específico del método, o no usa 
    #estos valores, simplemente se asignan estos valores a la "variable" representada con un guión bajo, en python el orden del 
    #guión importa, ya que indica qué variable es la que será interna.
    _, img_umbral = cv.threshold(img_gray, umbral, 255, cv.THRESH_BINARY)
    #imshow(): Con el método se puede mostrar una imagen, el primer parámetro es el nombre de la ventana donde aparecerá la imagen 
    #y el segundo parámetro es la imagen recopilada con el método imread()
    cv.imshow('Umbralizacion', img_umbral) #Mostrar una ventana que tenga como título el 1er parametro y muestre la imagen del 2do

#Función para encontrar contornos de una imagen:
def Contorno():
    #cv.findContours(): Este método sirve para encontrar los contornos en una imagen, se puede utilizar en vez del filtro Canny, al 
    #método se le pasa como primer parámetro la imagen en escala de grises, en las imágenes existen varios tipos de contornos, estos 
    #pueden tener jerarquías de dentro hacia fuera o pueden no tenerlas, esto depende del segundo parámetro que se le pase en el 
    #método, en este caso vamos a utilizar el parámetro cv.RETR_LIST para que no muestre jerarquía en los bordes que encuentre, 
    #posteriormente se le debe indicar en el tercer parámetro la forma en la que se va a guardar la información recabada, ya que 
    #puede guardar todos los puntos del contorno identificado o solo guardar los puntos de las esquinas que conforman el contorno, 
    #para que guarde todos los puntos de los contornos se le indica con el atributo cv.CHAIN_APPROX_NONE, para guardar solo las 
    #esquinas se usa el atributo cv.CHAIN_APPROX_SIMPLE.
    Contornos, _ = cv.findContours(img_umbral, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
    for borde in Contornos:
        #print(): Imprime en consola el mensaje que se incluya dentro de su paréntesis en forma de string
        #Medición de distancia, area, densidad, etc. de las figuras identificadas en las imágenes, estas se hacen a partir de 
        #las herramientas de Contour Features de la librería OpenCV, cuya documentación es la siguiente:
        #https://docs.opencv.org/4.x/dd/d49/tutorial_py_contour_features.html
        #contourArea(): Función que sirve para medir áreas, para ello se debe haber obtenido el contorno de una figura en una 
        #imagen, esta se obtiene en área de pixeles, por lo que no se considera como un área tal cual del mundo real.
        print(cv.contourArea(borde))
    print("--------------------------")
    #Copia de la imagen para poder actualizarla.
    img_copy_copy = img_copy.copy()
    #cv.drawContours(): Método que sirve para dibujar los contornos recabados con el método cv.findContours(), para ello primero se 
    #debe indicar en qué imagen se va a dibujar el contorno, no debe ser la misma de la que se obtuvieron los contornos, después se 
    #indica en el segundo parámetro la variable en donde están almacenados los contornos, en el tercer parámero se establece si se 
    #quiere que sea hueco o sólido el contorno, como se busca que sea sólido se pone -1, si fuera hueco, en esta parte se indicaría 
    #los pixeles del perímetro (borde) del contorno, posteriormente se indica el color y finalmente los contornos que quiero que 
    #muestre.
    color_contorno = (10, 100, 200) #Variable que almacena un color BGR
    cv.drawContours(img_copy_copy, Contornos, -1, color_contorno, 3)
    cv.imshow('Imagen contornos', img_copy_copy) #Mostrar una ventana que tenga como título el 1er parametro y muestre la imagen del 2do

#Función que ejecuta las dos funciones anteriores, primero umbralizando la imagen y luego obteniendo sus contornos:
def Actualizar_imagen(umbral):
    Imagen_Binaria(umbral)
    Contorno()

#Ejecución de la función Actualizar_imagen() con un umbral inicial de 0, ya que este cambiará con el valor del Trackbar 
Actualizar_imagen(0)

#cv.createTrackbar(): Este método sirve para crear y mostrar una barra sobre una ventana específica que muestra una imagen o 
#video, esto para variar cierto valor en tiempo real, este recibe los siguientes parámetros:
#   - Nombre de la barra (Track bar)
#   - Ventana a la cual se aplicará, esta debe tener el mismo nombre que la ventana creada con el método cv.namedWindow() y a la 
#   cual se aplicará el método canny.
#   - Valor mínimo de la barra.
#   - Valor máximo de la barra.
#   - Función que a fuerza se debe ejecutar cuando se mueva la barra, esta puede ejecutar una acción o no hacer nada.
cv.createTrackbar('Umbral', 'Imagen contornos', 0, 255, Actualizar_imagen)

#NO DEJAR QUE SE CIERREN LAS VENTANAS: Las siguientes dos líneas de código sirven para que no se cierre la ventana.
cv.waitKey(0) #Mostrar la ventana hasta que se presione la tecla X
cv.destroyAllWindows() #Destruir todas las ventanas después de cerrarlas con el comando





#IDENTIFICACIÓN DE GEOMETRÍAS ESPECÍFICAS, YA HABIENDO OBTENIDO LA SINTONIZACIÓN: Ya que se realizó la sintonización, con los 
#valores obtenidos, se puede analizar la imagen para identificar solo ciertas figuras.
"""
Sintonización de la imagen - Identificación de monedas - Valores obtenidos:
Umbral óptimo: 118
Moneda 5$ = 9173.5
Moneda 2$ = 6812.0
Moneda 1$ = 5278.5
"""
umbral = 118
#Se va a escribir en la imagen, por lo que se debe especificar las características del texto:
grosor = 1 #Grosor de las letras, dado en pixeles
fuente = cv.FONT_HERSHEY_SIMPLEX #Fuente de la letra a utilizarse
posicion_texto_1 = (20, 30) #Posición donde se mostrará el texto cuando se identifique la moneda 1
posicion_texto_2 = (20, 70) #Posición donde se mostrará el texto cuando se identifique la moneda 2
posicion_texto_3 = (20, 110) #Posición donde se mostrará el texto cuando se identifique la moneda 3
#Colores de los textos que indican la identificación de monedas, recordemos que se indica en formato BGR:
color_texto1 = (0, 255, 255) #Color amarillo
color_texto2 = (255, 255, 255) #Color negro
color_texto3 = (255, 255, 0) #Color amazul (aqua)
#Se declaran como variables las áreas obtenidas en la sintonización, se pone un valor un poco menor para que identifique la 
#moneda considerando un margen de error:
areaMoneda1Max = 9200
areaMoneda1Min = 9000
areaMoneda2Max = 6900
areaMoneda2Min = 6700
areaMoneda3Max = 5300
areaMoneda3Min = 5100
#Variable que indica el número de monedas captadas en la imagen, en un inicio tienen valor cero
Moneda1 = 0
Moneda2 = 0
Moneda3 = 0


_, img_umbral = cv.threshold(img_gray, umbral, 255, cv.THRESH_BINARY)
Contornos, _ = cv.findContours(img_umbral, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)

for borde_moneda in Contornos:
    #abs(): Obtiene el valor absoluto de un valor, se usa el método abs() porque a veces los resultados de área vienen en valor 
    #negativo
    #contourArea(): Función que sirve para medir áreas, para ello se debe haber obtenido el contorno de una figura en una imagen, 
    #esta se obtiene en área de pixeles, por lo que no se considera como un área tal cual del mundo real.
    area = abs(cv.contourArea(borde_moneda))
    if (areaMoneda1Max>= area >= areaMoneda1Min):
        Moneda1 += 1
    elif (areaMoneda2Max>= area >= areaMoneda2Min):
        Moneda2 += 1
    elif (areaMoneda3Max>= area >= areaMoneda3Min):
        Moneda3 += 1
    
#cv.putText(): Permite colocar texto en cualquier imagen, como primer parámetro se le indica la imagen en donde se pondrá el 
#texto, luego el texto que se quiere colocar, después se indica la posición donde se colocará el texto, la fuente, escala, el 
#color y el grosor del texto.  
cv.putText(img1_modificada, "Moneda de 5$ " + str(Moneda1), posicion_texto_1, fuente, 1, color_texto1, grosor)
cv.putText(img1_modificada, "Moneda de 2$ " + str(Moneda2), posicion_texto_2, fuente, 1, color_texto2, grosor)
cv.putText(img1_modificada, "Moneda de 1$ " + str(Moneda3), posicion_texto_3, fuente, 1, color_texto3, grosor)

cv.imshow('Imagen contornos', img1_modificada) #Mostrar una ventana que tenga como título el 1er parametro y muestre la imagen del 2do
#NO DEJAR QUE SE CIERREN LAS VENTANAS: Las siguientes dos líneas de código sirven para que no se cierre la ventana.
cv.waitKey(0) #Mostrar la ventana hasta que se presione la tecla X
cv.destroyAllWindows() #Destruir todas las ventanas después de cerrarlas con el comando