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
cv.namedWindow('Identificación de Rostros') #Ventana que muestra los bordes Canny
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
cv.createTrackbar('Vecindario mínimo', 'Identificación de Rostros', 3, 30, nothing)


#DETECCIÓN DE ROSTROS CON WEBCAM:
color_rectangulo_rostro = (0, 0, 255) #Color BGR del borde del rectángulo de reconocimiento facial para rostros
grosor_rectangulo_rostro = 2 #Grosor del borde del rectángulo que identifica rostros
color_circulo_ojo = (255, 255, 0) #Color BGR del borde del círculo de reconocimiento facial para ojos
grosor_circulo_ojo = 2 #Grosor del borde del círculo que identifica ojos


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
guardarVideo = cv.VideoWriter('0.-Img/Deteccion_Rostros.avi', cv.VideoWriter_fourcc(*'XVID'), 10, (640, 480))


#Bucle while: Cuando se analice un video, se debe realizar dentro de un bucle while para que se ejecute hasta que la ventana 
#donde se muestra el video se cierre.
#.isOpened(): Método que se aplica a un objeto de OpenCV que haya abierto una webcam, este identifica si la ventana de la 
#webcam está abierta o no, para que se realice el análisis de la imagen en el video.
while(videito.isOpened() == True):
    #SINTONIZACIÓN DE UMBRALES MÉTODO CANNY:
    #cv.getTrackbarPos(): Este método lo que hace es obtener el valor donde se encuentra la barra creada con el método 
    #cv.createTrackbar(), como primer parámetro recibe el nombre de la barra y como segundo parámetro la ventana donde fue creada
    vecindario_min = cv.getTrackbarPos('Vecindario mínimo', 'Identificación de Rostros')

    #.read(): Método que se aplica a un objeto de OpenCV que haya abierto una webcam, este método obtiene dos resultados: 
    # - ret: Variable booleana que puede ser true si hay un video (fotograma) capturado y false si no hay fotograma que leer, 
    #este se usa más que nada para crear un if cuando se quiere leer un video ya existente en vez de grabar y mostrar uno nuevo
    #o si se quiere asegurar que la webcam está grabando.
    # - frame: La variable frame devuelve el video capturado.
    ret, frame = videito.read()
    if(ret == True):
        #OBTENCIÓN DE ESCALA DE GRISES:
        #cvtColor(): Método de la librería OpenCV que recibe como primer parámetro una imagen RGB y en su segundo parámetro recibe 
        #un atributo de OpenCV llamado cv.COLOR_BGR2GRAY para convertir una imagen RGB a su escala de grises.
        img_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        cv.imshow('Escala de grises', img_gray)

        #DETECCIÓN DE ROSTROS:
        #cv.CascadeClassifier(): Este es un clasificador en cascada, esto se refiere a que dependiendo de ciertas características 
        #del reconocimiento facial, puede ir segmentando hasta identificar un rostro, ya sea de hombre, mujer, perro, gato, etc. 
        #porque cada uno tiene características especiales, para que funcione esto, se debe indicar como parámetro del método la 
        #base de datos descargada de la documentación de Github de OpenCV con extensión xml.
        #https://docs.opencv.org/3.4/db/d28/tutorial_cascade_classifier.html
        #Para la identificación de rostros, específicamente se utiliza la base de datos llamada haarcascade_frontalface_default.xml:
        #https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml
        clasificador_caras = cv.CascadeClassifier('7.-API_Reconocimiento_Facial/7.- Reconocimiento facial OpenCV - rostros.xml')

        #objetoCascadeClassifier.detectMultiScale(): Con este método se accede a la base de datos de reconocimiento facial de 
        #OpenCV para el reconocimiento de rostros, a este se le pasa como parámetro la imagen que se quiere analizar, pero antes se 
        #debió haber obtenido la escala de grises de la imagen y jalado con el método cv.CascadeClassifier() la base de datos de 
        #reconocimiento de rostros. 
        caras = clasificador_caras.detectMultiScale(img_gray)

        #Bucle for para obtener las coordenadas y dimensiones de las caras
        for (x, y, ancho, alto) in caras:
            #cv.rectangle(): Con este método perteneciente a la librería OpenCV se puede crear un rectángulo, en él se indica 
            #primero en que imagen obtenida con el método imread() se va a dibujar la figura, luego las coordenadas iniciales x,y 
            #de la imagen en donde se va a dibujar la esquina superior izquierda del rectángulo, que en este caso son las 
            #coordenadas x,y obtenidas con el reconocimiento facial, seguido de las coordenadas finales x,y que son las que 
            #incluyen el ancho y alto del rostro identificado, posteriormente se indica su color y si se quiere que sea hueco o 
            #sólido el rectángulo, si se buscara que fuera sólido se pondría un -1, si fuera hueco, en esta parte se indicaría  
            #los pixeles del grosor del borde del rectángulo.
            cv.rectangle(frame, (x, y), (x + ancho, y + alto), color_rectangulo_rostro, grosor_rectangulo_rostro)
            #Para cada parte del rostro que se quiera identificar se debe crear un clasificador, todos alimentándose de la misma 
            #base de datos, pero usándose para identificar distintas partes del rostro, para la parte específica de los ojos se usa 
            #la base de datos llamada haarcascade_eye.xml de la documentación de OpenCV que se encuentra en el siguiente link:
            #https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_eye.xml
            clasificador_ojos = cv.CascadeClassifier('7.-API_Reconocimiento_Facial/7.- Reconocimiento facial OpenCV - ojos.xml')
            #Extraer las coordenadas de la matriz cara desde la coordenada "y" hasta "y + alto" y la coordenada "x" hasta 
            #"x + ancho" de la imagen en escala de grises: 
            caraIndividual = img_gray[y:y+alto, x:x+ancho]
            #objetoCascadeClassifier.detectMultiScale(): Con este método se accede a la base de datos de reconocimiento facial de 
            #OpenCV para el reconocimiento de ojos, a este se le pasa como parámetro la imagen que se quiere analizar, pero antes 
            #se debió haber obtenido la colección de datos de identificación de rostros y jalado con el método cv.CascadeClassifier() 
            #la base de datos de reconocimiento ocular. Si no se está haciendo correctamente el análisis del rostro, en esta parte 
            #es donde se puede sintonizar la detección de rostros para mejorarla con los siguientes parámetros:
            # - Matriz a analizar: Que en el caso de los ojos es una submatriz de la matriz que identifica rostros.
            # - Factor de escala: Parámetro que especifica cuánto se reduce el tamaño de la imagen en cada escala de la imagen 
            #   original, el factor de escala por default es de 1.1 (scaleFactor). Este valor se sube para que detecte cosas más 
            #   grandes y se reduce cuando se quiere identificar partes más pequeñas.
            # - Vecindario mínimo: Parámetro que especifica cuántos pixeles vecinos debe tener cada rectángulo candidato para 
            #   conservarlo, el vecindario mínimo por default es de 3 (minNeighbors).
            # - Tamaño mínimo: Tamaño mínimo posible del vecindario (minSize).
            ojos = clasificador_ojos.detectMultiScale(caraIndividual, scaleFactor = 1.01, minNeighbors = vecindario_min, minSize = (10, 10))
            #Con la imagen 'Lena.jpg': scaleFactor = 1.1, minNeighbors = 10, minSize = (10, 10)
            #Con la imagen 'Familia.jpg': scaleFactor = 1.01, minNeighbors = 8, minSize = (10, 10)
            for (x1, y1, ancho1, alto1) in ojos:
                #cv.circle(): Con este método perteneciente a la librería OpenCV se puede crear un círculo, en él se indica primero 
                #en que imagen obtenida con el método imread() se va a dibujar la figura, luego la coordenada x,y de la imagen en 
                #donde se va a mostrar, el radio en pixeles del círculo, su color y si se quiere que sea hueco o sólido el círculo, 
                #como se busca que sea sólido se pone -1, si fuera hueco, en esta parte se indicaría los pixeles del perímetro 
                #(borde) del círculo.
                #En la interfaz se mostrará un círculo para mostrar de dónde se está obteniendo el color de la imagen.
                radio = int((ancho1 + alto1)/4)
                cv.circle(frame, (x+x1+radio, y+y1+radio), radio, color_circulo_ojo, grosor_circulo_ojo)

        cv.imshow("Identificación de Rostros", frame) #Mostrar una ventana que tenga como título el 1er parametro y muestre la imagen del 2do

        #GUARDAR VIDEO:
        #.write(): Con este método se guarda el video recopilado, para ello se debe haber usado antes el método cv.VideoWriter() 
        #donde se especifican las características de cómo se va a guardar el video y al método .write() se le pasa como parámetro 
        #la variable frame que devuelve el video capturado por medio del método .read()
        guardarVideo.write(frame)

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
        
        #GUARDAR UNA FOTO DEL VIDEO: Cuando se presione la tecla a, toma una foto del video
        if (cv.waitKey(1) == ord('a')):
            print("Captura de video tomada cuando se presionó la letra a")
            #GUARDAR UNA FOTO DEL VIDEO:
            #imwrite(): Método de la librería OpenCV que sirve para guardar una imagen, como primer parámetro tengo que poner el 
            #nombre con el que se guardará la imagen con todo y extensión y en el segundo debo poner la variable de la que extrae 
            #la imagen.
            cv.imwrite("0.-Img/Fotovideo.jgp", frame)
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
#CLASIFICADOR EN CASCADA: Clasificador que se usa en la identificación de rostros
#https://docs.opencv.org/3.4/db/d28/tutorial_cascade_classifier.html
#https://docs.opencv.org/3.4/d1/de5/classcv_1_1CascadeClassifier.html#aaf8181cb63968136476ec4204ffca498

#BASE DE DATOS DE RECONOCIMIENTO FACIAL:
#https://github.com/opencv/opencv/tree/master/data/haarcascades

#IDENTIFICACIÓN DE ROSTROS POR MEDIO DE UNA LIBRERÍA DE PYTHON QUE NO ES OPENCV: 
#https://pypi.org/project/face-recognition/