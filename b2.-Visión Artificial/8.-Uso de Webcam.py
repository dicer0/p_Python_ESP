# -*- coding: utf-8 -*-
#Comentario de una sola linea con el simbolo #, en Python para nada se deben poner acentos sino el programa
#puede fallar o imprimir raro en consola, la primera línea de código es para que no tenga error, pero aún
#así al poner un ángulo saldrá raro en consola, la línea debe ponerse tal cual como aparece y justo al inicio.

#IMPORTACIÓN DE LIBRERÍAS:
import cv2 as cv #Librería OpenCV: Sirve para todo tipo de operaciones de visión artificial


#SINTONIZACIÓN DE UMBRALES MÉTODO CANNY SIN SUAVIZADO GAUSSIANO:
#cv.namedWindow(): Sirve para crear una ventana donde se podrá mostrar un video o imagen recopilada, se debe declarar desde 
#este punto para crear barras que varíen el valor de los umbrales del filtro Canny, para ver cómo se debe sintonizar para 
#obtener de mejor manera los bordes, dando valores de 0 a 255
cv.namedWindow('Webcam - Canny') #Ventana que muestra los bordes Canny
#cv.createTrackbar(): Este método sirve para crear y mostrar una barra sobre una ventana específica que muestra una imagen o 
#video, esto para variar cierto valor en tiempo real, este recibe los siguientes parámetros:
#   - Nombre de la barra (Track bar)
#   - Ventana a la cual se aplicará, esta debe tener el mismo nombre que la ventana creada con el método cv.namedWindow() y a la 
#   cual se aplicará el método canny.
#   - Valor mínimo de la barra.
#   - Valor máximo de la barra.
#   - Función que a fuerza se debe ejecutar cuando se mueva la barra, esta puede ejecutar una acción o en este caso solo se 
#   declara y no hace nada.
#Se debe crear la función que no hace nada en este caso para que se pueda crear la barra en la ventana antes de usar el método 
#cv.createTrackbar().
def nothing (x):
    pass
#Se crea una barra con el método cv.createTrackbar() para variar el umbral inferior y superior del método Canny
cv.createTrackbar('Umbral inferior', 'Webcam - Canny', 0, 255, nothing)
cv.createTrackbar('Umbral superior', 'Webcam - Canny', 0, 255, nothing)


#SINTONIZACIÓN DE UMBRALES MÉTODO CANNY CON SUAVIZADO GAUSSIANO:
cv.namedWindow('Webcam - Canny Suavizado') #Creación de ventana
def nothing2 (x): #Función que no hace nada, para poder crear las barras en la ventana
    pass
cv.createTrackbar('Umbral inferior suavizado', 'Webcam - Canny Suavizado', 0, 255, nothing2)
cv.createTrackbar('Umbral superior suavizado', 'Webcam - Canny Suavizado', 0, 255, nothing2)


#SINTONIZACIÓN DE UMBRALIZACIÓN Y OBTENCIÓN DE BORDES:
cv.namedWindow('Webcam - Umbralizacion y obtencion de bordes') #Creación de ventana
def nothing3 (x): #Función que no hace nada, para poder crear las barras en la ventana
    pass
cv.createTrackbar('Umbralizacion', 'Webcam - Umbralizacion y obtencion de bordes', 0, 255, nothing3)


#cv.VideoCapture(): Método de python para acceder a la webcam, como parámetro solo se enlista el número de webcams a las que 
#se quiere acceder, empezando a contar desde el índice 0, 1, 2, etc. O se le puede pasar entre comillas la ruta de un 
#video para que lo reproduzca
videito = cv.VideoCapture(0)
#cv.VideoWriter(): Método que sirve para guardar un video, en este se pasan varios parámetros: 
# 1.- Nombre del archivo que guardará el video con todo y extensión.
# 2.- Código de 4 caracteres con el que se identifica cada códec, se realiza con el método cv.VideoWriter_fourcc(), este lo que 
#hace es dar un código para indicar la extensión del video dependiendo de cual se haya elegido:
#       - cv2.VideoWriter_fourcc(*'mp4v'): Para archivos .mp4, .mkv, .mov, .wmv
#       - cv2.VideoWriter_fourcc(*'DIVX'): Para archivos .avi, .mkv, .mov, .wmv
#       - cv2.VideoWriter_fourcc(*'XVID'): Para archivos .avi, .mkv, .mov, .wmv. Si es que el método anterior no funcionó.
# 3.- Velocidad de fotogramas por segundo en la secuencia del video grabado. La velocidad de fotograma estándar que solemos ver 
#en los vídeos es de 24 fotogramas por segundo, si grabamos a 1 fotograma por segundo, se vería terriblemente entrecortado.
# 4.- Tamaño de los frames que componen el video, el ancho y alto en unidad de pixeles de las imagenes que conforman el video.
# 5.- Booleano que indica si queremos que el video se guarde en escala de grises o a color: True: color, False: escala de grises. 
guardarVideo = cv.VideoWriter('0.-Img/Videito.avi', cv.VideoWriter_fourcc(*'XVID'), 10, (640, 480))


#Bucle while: Cuando se analice un video, se debe realizar dentro de un bucle while para que se ejecute hasta que la ventana 
#donde se muestra el video se cierre.
#.isOpened(): Método que se aplica a un objeto de OpenCV que haya abierto una webcam, este identifica si la ventana de la 
#webcam está abierta o no, para que se realice el análisis de la imagen en el video.
while(videito.isOpened() == True):
    #SINTONIZACIÓN DE UMBRALES MÉTODO CANNY:
    #cv.getTrackbarPos(): Este método lo que hace es obtener el valor donde se encuentra la barra creada con el método 
    #cv.createTrackbar(), como primer parámetro recibe el nombre de la barra y como segundo parámetro la ventana donde fue creada 
    UmbInf = cv.getTrackbarPos('Umbral inferior', 'Webcam - Canny')
    UmbSup = cv.getTrackbarPos('Umbral superior', 'Webcam - Canny')

    #SINTONIZACIÓN DE UMBRALES MÉTODO CANNY CON SUAVIZADO GAUSSIANO:
    UmbInfSuav = cv.getTrackbarPos('Umbral inferior suavizado', 'Webcam - Canny Suavizado')
    UmbSupSuav = cv.getTrackbarPos('Umbral superior suavizado', 'Webcam - Canny Suavizado')

    #SINTONIZACIÓN DE UMBRALIZACIÓN Y OBTENCIÓN DE BORDES:
    umbral = cv.getTrackbarPos('Umbralizacion', 'Webcam - Umbralizacion y obtencion de bordes')

    #.read(): Método que se aplica a un objeto de OpenCV que haya abierto una webcam, este método obtiene dos resultados: 
    # - ret: Variable booleana que puede ser true si hay un video (fotograma) capturado y false si no hay fotograma que leer, 
    #este se usa más que nada para crear un if cuando se quiere leer un video ya existente en vez de grabar y mostrar uno nuevo
    #o si se quiere asegurar que la webcam está grabando.
    # - frame: La variable frame devuelve el video capturado.
    ret, frame = videito.read()
    if(ret == True):
        #FILTRO CANNY PARA DETECCIÓN DE BORDES: Lo que hace el detector Canny es mejorar la detección de bordes, ya que quita los 
        #bordes que no nos interesan y deja solamente los que si nos interesan.
        #cv.Canny(): Aplica el filtro de Canny realizando los siguientes pasos de analisis de imagen: 
        # 1. Suavizar la imagen (difuminarla): Reducción de ruido por medio del filtro Gaussiano.
        #cv.blur(): El método recibe la imagen o video original y luego el tamaño del Kernel que va a aplicar para realizar el 
        #filtro Gaussiano de suavizado, que puede ser una matriz de tamaño: 3X3, 5X5, 7X7 o 31X31.
        suavizado = cv.blur(frame, (5, 5))
        # 2. Operador sobel (detección de bordes): Gradiente (magnitud) y orientación (ángulo) del primer borde obtenido de la 
        #    imagen.
        # 3. Detector Canny: Identificar mejor los bordes de una imagen y aplicar el umbral de histéresis para preservar solamente 
        #    ciertos bordes y quitar los bordes que no nos interesan.
        #cv.Canny(): Los parámetros que recibe el método son los siguientes:
        # - Como primer parámetro se le pasa una imagen obtenida previamente con el método imread() o video obtenido con el 
        #   método VideoCapture().
        # - Como segundo y tercer parámetro se le pasan umbrales para el filtrado de histéresis de la imagen, con ellos obtendremos 
        #   ciertos bordes solamente y despreciaremos los demás, el primer umbral es el inferior y el segundo el superior.
        # - Como tercer parámetro necesitamos indicar los bordes y apertura de la imagen para el operador Sobel.
        bordeCanny = cv.Canny(frame, UmbInf, UmbSup) #Filtro Canny aplicado a video original
        bordeCannyBlur = cv.Canny(suavizado, UmbInfSuav, UmbSupSuav) #Filtro Canny aplicado a video con suavizado Gaussiano
        #imshow(): Con el método se puede mostrar una ventana con una imagen o video, el primer parámetro es el nombre de la 
        #ventana donde aparecerá la imagen o video y el segundo parámetro es la imagen recopilada con el método cv.imread() o el 
        #video recopilado con el método .read() aplicado a un video obtenido con el método cv.VideoCapture()
        cv.imshow('Webcam', frame)
        cv.imshow('Webcam - Canny', bordeCanny)
        cv.imshow('Webcam - Canny Suavizado', bordeCannyBlur)

        #OBTENCIÓN DE CAPAS RGB:
        #split(): Método que extrae los diferentes colores de la imagen en 3 distintas variables, guardándo primero el color azul, 
        #luego el verde y finalmente el rojo, específicamente en ese órden.
        b, g, r = cv.split(frame)
        #cv.imshow('Capa de azules', b) #Mostrar una ventana que tenga como título el 1er parametro y muestre la imagen del 2do
        #cv.imshow('Capa de verdes', g) #Mostrar una ventana que tenga como título el 1er parametro y muestre la imagen del 2do
        #cv.imshow('Capa de rojos', r) #Mostrar una ventana que tenga como título el 1er parametro y muestre la imagen del 2do

        #OBTENCIÓN DE ESCALA DE GRISES
        #cvtColor(): Método de la librería OpenCV que recibe como primer parámetro una imagen RGB y en su segundo parámetro recibe 
        #un atributo de OpenCV llamado cv.COLOR_BGR2GRAY para convertir una imagen RGB a su escala de grises.
        img_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        #cv.imshow('Escala de grises', img_gray)

        """ 
        #El realizar el filtro de máximos, mínimos y media en video consume muchos recursos y alenta la ejecución del programa, 
        #pero realiza su función correctamente.
        #FILTRO DE MÁXIMOS: Vuelve todo el ruido en tonos blancos, obteniendo así mayor definición en los tonos blancos de la 
        #imagen original, quitando negros y maximizando blancos, en función del tamaño del filtro. Recordemos que el tamaño del 
        #filtro se refiere al tamaño de la vecindad que rodea cada píxel de analisis en la imagen, mientras más pequeño sea el 
        #tamaño del vecindario, es aplicado de manera más fina el filtro. El tamaño del filtro puede ser decimal.
        mask = 3.1416 #Al tamaño del filtro se le puede llamar máscara, este puede ser entero o decimal.
        img2 = scipy.ndimage.maximum_filter(frame, size = mask)
        cv.imshow('Imagen sin ruido - Filtro maximo', img2)

        #FILTRO DE MÍNIMOS: Vuelve todo el ruido en tonos negros, obteniendo así mayor definición en los tonos negros de la imagen 
        #original, quitando blancos y maximizando negros, en función del tamaño de la máscara del filtro. El tamaño del filtro 
        #puede ser decimal.
        img3 = scipy.ndimage.minimum_filter(frame, size = mask)
        cv.imshow('Imagen sin ruido - Filtro minimo', img3)

        #FILTRO DE MEDIA: Este filtro como los dos pasados, analiza los tonos de los pixeles incluidos en la vecindad de cada píxel 
        #analizado, luego hace un promedio con el tono de gris de estos pixeles y deja pasar ese tono, en específico este filtro 
        #trata de remover el ruido de una imagen con escala de grises, conservando su forma y color original, el problema con este 
        #filtro es que difumina más la imagen mientras sea mayor el tamaño de la vecindad, a esto se le llama suavizado de imagen. 
        #El tamaño del filtro NO puede ser decimal.
        img4 = scipy.ndimage.median_filter(frame, size = 6)
        cv.imshow('Imagen sin ruido - Filtro medio', img4)
        """

        #GUARDAR VIDEO:
        #.write(): Con este método se guarda el video recopilado, para ello se debe haber usado antes el método cv.VideoWriter() 
        #donde se especifican las características de cómo se va a guardar el video y al método .write() se le pasa como parámetrsso 
        #la variable frame que devuelve el video capturado por medio del método .read()
        guardarVideo.write(frame)

        #UMBRALIZACIÓN Y OBTENCIÓN DE BORDES:
        color_contorno = (0, 0, 255) #Variable que almacena un color BGR
        grosor = 3
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
        cv.drawContours(frame, contornos, -1, color_contorno, grosor)
        cv.imshow('Webcam - Umbralizacion y obtencion de bordes', img_umbral) #Mostrar una ventana que tenga como título el 1er parametro y muestre la imagen del 2do
        cv.imshow('Imagen contornos', frame) #Mostrar una ventana que tenga como título el 1er parametro y muestre la imagen del 2do

        #Se utiliza un condicional if para saber cuando se debe dejar de mostrar el video, para ello se usan los siguientes 
        #métodos:
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
        if(cv.waitKey(1) == ord('s')):
            #print(): Imprime en consola el mensaje que se incluya dentro de su paréntesis en forma de string
            print("cv.waitKey(1): " + str(cv.waitKey(1)))
            print("cv.waitKey(0): " + str(cv.waitKey(0)))
            break #Cuando se presione la tecla s, se cerrará la ventana del video.
    else:
        break

#.release(): Con este método se libera la webcam, tanto en forma de software como de hardware.
guardarVideo.release() #Dejar de tener acceso al directorio donde se guardará el video.
videito.release() #Dejar de tener acceso a la webcam.
#destroyAllWindows(): Función que permite a los usuarios destruir todas las ventanas en cualquier momento. No toma ningún 
#parámetro y no devuelve nada, esto se incluye para que al cerrar la ventana después del método waitKey() se destruyan para 
#poder utilizarse en otra cosa.
cv.destroyAllWindows()

#El video se cierra al presionar la letra S, no cuando se presiona el tache.
#La documentación para realizar todas las operaciones de este ejercicio son las siguientes:
#FILTRO DE MÁXIMOS, MÍNIMOS Y MEDIA: Para quitar ruido.
#https://docs.scipy.org/doc/scipy/reference/generated/scipy.ndimage.maximum_filter.html#scipy.ndimage.maximum_filter

#MÉTODOS PARA CONTROLAR LOS EVENTOS DEL MOUSE: Para ver cuando se haya dado clic, se suelte el clic del mouse, etc.
#https://docs.opencv.org/3.4/d0/d90/group__highgui__window__flags.html#gga927593befdddc7e7013602bca9b079b0ad3419100fc2d7688c6dbe3da030fbfd9

#FILTRO CANNY: Detección de bordes.
#https://docs.opencv.org/4.x/dd/d1a/group__imgproc__feature.html#ga2a671611e104c093843d7b7fc46d24af

#TRANSFORMADA DE HOUGH: Detección de líneas.
#https://docs.opencv.org/3.4/d9/db0/tutorial_hough_lines.html
#https://docs.opencv.org/3.4/dd/d1a/group__imgproc__feature.html#ga46b4e588934f6c8dfd509cc6e0e4545a

#CONTOURS: Operaciones para medir las figuras en la imagen donde ya se haya identificado los bordes.
#https://docs.opencv.org/4.x/dd/d49/tutorial_py_contour_features.html