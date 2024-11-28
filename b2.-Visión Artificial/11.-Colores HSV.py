# -*- coding: utf-8 -*-
#Comentario de una sola linea con el simbolo #, en Python para nada se deben poner acentos sino el programa
#puede fallar o imprimir raro en consola, la primera línea de código es para que no tenga error, pero aún
#así al poner un ángulo saldrá raro en consola, la línea debe ponerse tal cual como aparece y justo al inicio.

#CÓDIGO QUE SIRVE PARA DETECTAR LAS CAPAS DE COLORES HSV

#IMPORTACIÓN DE LIBRERÍAS:
import cv2 #Librería OpenCV: Sirve para todo tipo de operaciones de visión artificial
import numpy as np #Librería numpy: Realiza operaciones matemáticas complejas


#DETECCIÓN DE OBJETOS CON WEBCAM:
matiz_objetivo = 0 #Variable que almacena una parte de la imagen hsv obtenida de la imagen original.
rango = 5 #Rango que aumenta o disminuye el valor de la Trackbar en la ventana.
max_rango = 50 #Valor máximo de la Trackbar.
color = (0, 0, 255) #Color BGR del borde del círculo de reconocimiento de objetos.
grosor = 2 #Grosor del borde del círculo que identifica objetos.


#selecciona_color(): Función para que cada que se de clic sobre la imagen, se obtengan las capas hsv de la parte en donde se dio 
#clic, para ello se debe recibir como parámetros: 
# - El evento del mouse: Este evento forma parte de los eventos descritos por la librería OpenCV.
# - Las coordenadas en x y y de la parte de la imagen donde se dió clic: Obtenidas de la imagen ya que esta es una matriz.
# - Bandera: Indica cuando ya se realizó el evento del mouse
# - el frame que indica la ventana donde aparece la imagen
def selecciona_color(evento, x, y, flags, frame):
    #Se debe declarar una variable llamada igual que la variable que almacena la imagen original obtenida con el método imread(), 
    #sea declara como tipo global para que se pueda ver o alcanzar desde cualquier parte del código.
    global matiz_objetivo
    
    #Los eventos que se van a manejar son parte de la librería OpenCV:
    # - EVENT_LBUTTONDOWN: Indica que el botón izquierdo del ratón está presionado.
    if (evento == cv2.EVENT_LBUTTONDOWN):
        #OBTENCIÓN DE COLORES HSV:
        #cvtColor(): Método de la librería OpenCV que recibe como primer parámetro una imagen RGB y en su segundo parámetro recibe 
        #un atributo de OpenCV llamado cv.COLOR_BGR2HSV para convertir una imagen RGB a su formato de colores HSV.
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        #CAPAS HSV DE LAS IMAGENES
        #split(): Método que extrae los diferentes colores de la imagen en 3 distintas variables, guardándo primero la variable 
        #hue, luego la saturación y finalmente el valor, específicamente en ese órden. Las capas que extrae depende del tipo de 
        #imagen.
        h, s, v = cv2.split(hsv)
        #Recordemos que la imagen es tal cual una matriz y esta se puede manejar como tal, de esta manera cuando se realice el 
        #evento de clic en la imagen, podemos obtener las coordenadas xy de la parte donde se dió clic de la imagen.
        #.toList(): Este método se aplica a una variable de tipo array para convertirla en una lista, específicamente en visión 
        #artificial esto se usa para poder acceder a las coordenadas x,y de las 3 capas o dimensiones RGB y guardarlas en una 
        #serie de valores BGR, ya que en un inicio cuando son de tipo numpy array (osea un array proveniente de la librería numpy), 
        #solo vienen uno tras otro pero no organizados, como se muestra en el siguiente ejemplo y recordando que en python se 
        #accede a los colores RGB en el orden BGR:
        # - color = img[x, y].toList()
        # - h  = img[x, y][0]
        # - s  = img[x, y][1]
        # - v  = img[x, y][2]
        matiz_objetivo = h[y, x]


#selecciona_rango(): Función utilizada por la Trackbar, osea la barra de la ventana que varía algún valor Esta lo único que hace 
#es volver global la variable rango.
def selecciona_rango(valor):
    global rango
    rango = valor


#filtra_matiz(): Función hecha para suavizar la imagen, obtener las capas hsv, binarizar y obtener bordes con el filtro Canny.
def filtra_matiz(frame):
    #cv.blur(): El método recibe la imagen o video original y luego el tamaño del Kernel que va a aplicar para realizar el 
    #filtro Gaussiano de suavizado, que puede ser una matriz de tamaño: 3X3, 5X5, 7X7, 10X10 o 31X31. 
    #En este caso se aplica el suavizado para poder identificar de mejor manera los objetos, ya que en la sintonización, pueden 
    #salir bordes separados de un mismo objeto, confundiéndolo así como si fueran varios cuando es uno solo, de esta manera se 
    #expanden los pixeles para que se vea como un solo objeto. Pero hay que tener cuidado, que si el Kernel es muy grande, no 
    #identificará los objetos. Con un Kernel de (30, 30) no lo identifica pero con uno de (10, 10) si lo identifica.
    frame_suavizado = cv2.blur(frame, (10, 10))
    #OBTENCIÓN DE COLORES HSV:
    #cvtColor(): Método de la librería OpenCV que recibe como primer parámetro una imagen RGB y en su segundo parámetro recibe 
    #un atributo de OpenCV llamado cv.COLOR_BGR2HSV para convertir una imagen RGB a su formato de colores HSV.
    hsv = cv2.cvtColor(frame_suavizado, cv2.COLOR_BGR2HSV)
    #Declaración e iniciación de las matrices en un tipo de dato de Python llamado lista, siguiendo la nomenclatura descrita a 
    #continuación, tomando en cuenta que el número de elementos de las filas debe ser el mismo:
    #Matriz_lista = [[fila1],[fila2],...,[fila_n]], FILA X COLUMNA
    #vector_renglon = [1,2,3]
    #vector_columna = [[1],[2],[3]]
    #Las matrices declaradas con el método array de la librería numpy no son listas, son totalmente otro tipo de valor 
    #perteneciente a la librería numpy, llamado numpy array y para declarar arrays de este tipo de dato se usa la siguiente 
    #nomenclatura:
    #matriz_numpy_array = numpy.array([[fila1],[fila2],...,[fila_n]]), FILA X COLUMNA
    #La diferencia con la matriz declarada en forma de lista es la siguiente:
    #matriz_lista = [[fila1],[fila2],...,[fila_n]], FILA X COLUMNA
    color_inferior = np.array([matiz_objetivo - rango, 150, 0])     #Valor inferior para umbralizar la imagen hsv
    color_superior = np.array([matiz_objetivo + rango, 255, 255])   #Valor superior para umbralizar la imagen hsv

    #cv.inRange(): Este método sirve para umbralizar una imagen hsv, en ella se le pasa como primer parámetro la imagen en colores 
    #hsv que se va a umbralizar, a continuación se indica el valor mínimo y máximo que puede alcanzar el umbral.
    mascara = cv2.inRange(hsv, color_inferior, color_superior)
    #mascara = cv2.dilate(mascara, None, iterations=4)
    #mascara = cv2.erode(mascara, None, iterations=2)

    #cv.findContours(): Este método sirve para encontrar los contornos en una imagen, se puede utilizar en vez del filtro Canny, 
    #al método se le pasa como primer parámetro la imagen umbralizada, en las imágenes existen varios tipos de contornos, estos 
    #pueden tener jerarquías de dentro hacia fuera o pueden no tenerlas, esto depende del segundo parámetro que se le pase 
    #en el método, en este caso vamos a utilizar el parámetro cv.RETR_LIST para que no muestre jerarquía en los bordes que 
    #encuentre, posteriormente se le debe indicar en el tercer parámetro la forma en la que se va a guardar la información 
    #recabada, ya que puede guardar todos los puntos del contorno identificado o solo guardar los puntos de las esquinas que 
    #conforman el contorno, para que guarde todos los puntos de los contornos se le indica con el atributo cv.CHAIN_APPROX_NONE, 
    #para guardar solo las esquinas se usa el atributo cv.CHAIN_APPROX_SIMPLE.
    contornos, _ = cv2.findContours(mascara, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

    #imshow(): Con el método se puede mostrar una ventana con una imagen o video, el primer parámetro es el nombre de la 
    #ventana donde aparecerá la imagen o video y el segundo parámetro es la imagen recopilada con el método cv.imread() o el 
    #video recopilado con el método .read() aplicado a un video obtenido con el método cv.VideoCapture()
    cv2.imshow('Mascara', mascara)
    res = cv2.bitwise_and(frame, frame, mask = mascara)
    cv2.imshow('Imagen filtrada', res) #Mostrar una ventana que tenga como título el 1er parametro y muestre la imagen del 2do
    return contornos

#cv.namedWindow(): Sirve para crear una ventana donde se podrá mostrar un video o imagen recopilada, se debe declarar desde 
#este punto para crear barras que varíen el valor de los umbrales del filtro Canny, para ver cómo se debe sintonizar para 
#obtener de mejor manera los bordes, dando valores de 0 a 255
cv2.namedWindow('webcam')
#cv.createTrackbar(): Este método sirve para crear y mostrar una barra sobre una ventana específica que muestra una imagen o 
#video, esto para variar cierto valor en tiempo real, este recibe los siguientes parámetros:
#   - Nombre de la barra (Track bar)
#   - Ventana a la cual se aplicará, esta debe tener el mismo nombre que la ventana creada con el método cv.namedWindow().
#   - Valor mínimo de la barra.
#   - Valor máximo de la barra.
#   - Función que a fuerza se debe ejecutar cuando se mueva la barra, esta puede ejecutar una acción o en este caso solo se 
#   declara y no hace nada.
#Se debe crear una función que no hace nada en este caso para que se pueda crear la barra en la ventana antes de usar el método 
#cv.createTrackbar(), en este caso esa función es selecciona_rango().
cv2.createTrackbar('Rango', 'webcam', rango, max_rango, selecciona_rango)

#cv.VideoCapture(): Método de python para acceder a la webcam, como parámetro solo se enlista el número de webcams a las que 
#se quiere acceder, empezando a contar desde el índice 0, 1, 2, etc. O se le puede pasar entre comillas la ruta de un 
#video para que lo reproduzca
camara = cv2.VideoCapture(0)

#.isOpened(): Método que se aplica a un objeto de OpenCV que haya abierto una webcam, este identifica si la ventana de la 
#webcam está abierta o no, para que se realice el análisis de la imagen en el video.
if not camara.isOpened():
    #Mensaje que se imprimirá en consola cuando no se pueda abrir la webcam del ordenador.
    print("No es posible abrir la cámara")
    exit()
#Bucle while: Cuando se analice un video, se debe realizar dentro de un bucle while para que se ejecute hasta que la ventana 
#donde se muestra el video se cierre.
while True:
    #.read(): Método que se aplica a un objeto de OpenCV que haya abierto una webcam, este método obtiene dos resultados: 
    # - ret: Variable booleana que puede ser true si hay un video (fotograma) capturado y false si no hay fotograma que leer, 
    #este se usa más que nada para crear un if cuando se quiere leer un video ya existente en vez de grabar y mostrar uno nuevo
    #o si se quiere asegurar que la webcam está grabando.
    # - frame: La variable frame devuelve el video capturado.
    ret, frame = camara.read()
    #Condicional que se ejecuta cuando no se pudo obtener un fotograma.
    if not ret:
        print("No es posible obtener la imagen")
        break
    
    #filtra_matiz(): Función hecha para suavizar la imagen, obtener las capas hsv, binarizar y obtener bordes con el filtro Canny, 
    #esta recibe como parámetro la variable frame que devuelve el video capturado.
    contornos = filtra_matiz(frame)
    if len(contornos):
        #Medición de distancia, area, densidad, etc. de las figuras identificadas en las imágenes, estas se hacen a partir de 
        #las herramientas de Contour Features de la librería OpenCV, cuya documentación es la siguiente:
        #https://docs.opencv.org/4.x/dd/d49/tutorial_py_contour_features.html
        #contourArea(): Función que sirve para medir áreas, para ello se debe haber obtenido el contorno de una figura en una 
        #imagen, esta se obtiene en área de pixeles, por lo que no se considera como un área tal cual del mundo real.
        contorno_max = max(contornos, key = cv2.contourArea)
        (x, y), radio = cv2.minEnclosingCircle(contorno_max)
        #cv.circle(): Con este método perteneciente a la librería OpenCV se puede crear un círculo, en él se indica primero en 
        #que imagen se va a dibujar la figura, luego la coordenada x,y de la imagen en donde se va a mostrar, el radio en pixeles 
        #del círculo, su color y si se quiere que sea hueco o sólido el círculo, como se busca que sea sólido se pone -1, si fuera 
        #hueco, en esta parte se indicaría los pixeles del perímetro (borde) del círculo.
        #En la interfaz se mostrará un círculo para mostrar de dónde se está obteniendo el color de la imagen.
        centro = (int (x), int (y))
        radio = int (radio)
        cv2.circle (frame, centro, radio, color, grosor)

    #imshow(): Con el método se puede mostrar una ventana con una imagen o video, el primer parámetro es el nombre de la 
    #ventana donde aparecerá la imagen o video y el segundo parámetro es la imagen recopilada con el método cv.imread() o el 
    #video recopilado con el método .read() aplicado a un video obtenido con el método cv.VideoCapture()
    cv2.imshow('webcam', frame)

    #CONFIGURACIÓN DE LA OPERACIÓN CON EL MOUSE:
    #setMouseCallback(): Se utiliza esta función para que el mouse pueda interactuar con una ventana en específico, se manda a 
    #llamar esta ventana poniendo el mismo nombre que usa en el título del método imshow() para mostrarla, además se indica la 
    #función que se va a ejecutar con el mouse dentro de la ventana y si es necesario al final se indica dónde se almacena la data
    #proveniente.
    cv2.setMouseCallback('webcam', selecciona_color, frame)
    
    #waitKey(): Método que permite a los usuarios mostrar una ventana durante un número de milisegundos determinados si su 
    #parámetro es un número mayor a 1 o hasta que se presione cualquier tecla. Toma tiempo en milisegundos como parámetro y 
    #espera el tiempo dado para destruir la ventana: 
    # - Si se pasa 0 como argumento, espera hasta que se presiona cualquier tecla.
    # - Si se pasa 1 como argumento, espera hasta que se presione una tecla específica para cerrar la ventana.
    #El método waitKey() está monitoreando si se presiona una tecla o no, este modo se activa si se le pasa como parámetro un 
    #número 1, de esta manera:
    # - Si no se presiona una tecla retorna un valor -1 
    # - Si se presiona una tecla, retorna un valor ASCII correspondiente a la tecla que se oprimió, con el método ord() podemos 
    # indicar el código ASCII de la letra del teclado que indiquemos en su parámetro.  
    if cv2.waitKey(1) == ord('q'): #Se cierra el programa cuando se presione la letra q
        break

#.release(): Con este método se libera la webcam, tanto en forma de software como de hardware.
camara.release()
#destroyAllWindows(): Función que permite a los usuarios destruir todas las ventanas en cualquier momento. No toma ningún 
#parámetro y no devuelve nada, esto se incluye para que al cerrar la ventana después del método waitKey() se destruyan para 
#poder utilizarse en otra cosa.
cv2.destroyAllWindows()