#IMPORTACIÓN DE LIBRERÍAS:
import cv2      #Librería OpenCV: Sirve para todo tipo de operaciones de visión artificial
import os       #os: Librería que permite acceder a funciones y métodos relacionados con el sistema operativo.
import imutils  #imutils: Librería que se utiliza para simplificar y acelerar el procesamiento de imágenes.

#Creación de la ruta donde guardará el programa los datos faciales del usuario para que lo reconozca.
usuario = "di_cer0"
ruta = "C:/Users/diego/OneDrive/Documents/The_MechaBible/p_Python_ESP/5.-Inteligencia Artificial/ReconocimientoFacial_AsistenteVirtual_MarkI"
usuarioPath = ruta + "/" + usuario

#os.path.exists(): Método que comprueba si un directorio existe en mi ordenador.
#os.makedirs(): Método que crea un nuevo directorio en mi ordenador.
if not os.path.exists(usuarioPath): #Evalúa si existe el path con la cara del usuario y sino lo crea.
    os.makedirs(usuarioPath)

#cv2.VideoCapture(): Método de python para acceder a la webcam, como parámetro solo se enlista el número de 
#webcams a las que se quiere acceder, empezando a contar desde el índice 0, 1, 2, etc. O se le puede pasar 
#entre comillas la ruta de un video para que lo reproduzca.
#Este será el video que el reconocimiento facial utilizará para reconocer un rostro, pero para que funcione 
#mejor se recomienda tomar el video con una alta calidad, buena iluminación y realizar la grabación en el 
#mismo lugar donde se vaya a utilizar el asistente virtual.
rostro = cv2.VideoCapture("C:/Users/diego/Pictures/Camera Roll/Rostro_di_cer0.mp4")

#RECONOCIMIENTO DE ROSTROS CON OPENCV:
#Documentación de la base de datos de OpenCV para realizar el reconocimiento facial:
#https://github.com/opencv/opencv/tree/master
#HAAR CASCADES: Algoritmo de reconocimiento facial, para poder hacer el reconocimiento facial se debe hacer la 
#extracción de la base de datos de haarcascade, de sus archivos xml es de donde se saca la información para 
#realizar un correcto reconocimiento facial separando el rostro de una persona de su fondo o demás elementos 
#del video o imagen, en específico se utiliza el archivo haarcascade_frontalface_default.xml que se encuentra 
#en el siguiente link, es recomendable tener una copia local del archivo para el reconocimiento facial por 
#cualquier tema de conexión, actualización de la base de datos, etc. Para identificar cada parte distinta del 
#rostro se deben usar diferentes bases de datos dentro de la documentación de OpenCV.

#cv.CascadeClassifier(): Este es un clasificador en cascada, osea que dependiendo de ciertas características 
#del reconocimiento facial, puede ir segmentando el video o imagen hasta identificar un rostro, ya sea de 
#hombre, mujer, perro, gato, etc. porque cada uno tiene características especiales, para que funcione esto, 
#se debe indicar como parámetro del método la base de datos descargada de la documentación de Github de OpenCV 
#con extensión xml.
#https://docs.opencv.org/3.4/db/d28/tutorial_cascade_classifier.html
#Para la identificación de rostros, específicamente se utiliza la base de datos llamada 
#haarcascade_frontalface_default.xml:
#https://github.com/opencv/opencv/tree/4.x/data/haarcascades
rutaDatosEntrenamientoFacial = "C:/Users/diego/OneDrive/Documents/The_MechaBible/p_Python_ESP/5.-Inteligencia Artificial/API_Keys/haarcascade_frontalface_default.xml"
clasificacionFacial = cv2.CascadeClassifier(rutaDatosEntrenamientoFacial)
numeroCara = 0

#.isOpened(): Método que se aplica a un objeto de OpenCV que haya abierto una webcam, este identifica si la 
#ventana de la webcam está abierta o no, para que se realice el análisis de la imagen en el video.
if not rostro.isOpened():
    #Mensaje que se imprimirá en consola cuando no se pueda abrir la webcam del ordenador.
    print("No es posible abrir la cámara")
    exit()
#Bucle while: Cuando se analice un video, se debe realizar dentro de un bucle while para que se ejecute 
#hasta que la ventana donde se muestra el video se cierre.
while True:
    #.read(): Método que se aplica a un objeto de OpenCV que haya abierto una webcam, este método obtiene 
    #dos resultados: 
    # - ret: Variable booleana que puede ser true si hay un video (fotograma) capturado y false si no hay 
    #   fotograma que leer, este se usa más que nada para crear un if cuando se quiere leer un video ya 
    #   existente en vez de grabar y mostrar uno nuevo o si se quiere asegurar que la webcam está grabando.
    # - frame: La variable frame devuelve el video capturado.
    ret, frame = rostro.read()
    #Condicional que se ejecuta cuando no se pudo obtener un fotograma.
    if not ret:
        print("No es posible obtener la imagen")
        break
    #imutils.resize(): Método para redimensionar una imagen en Python. 
    frame = imutils.resize(frame, width = 640)
    #cvtColor(): Método de la librería OpenCV que recibe como primer parámetro una imagen RGB y en su 
    #segundo parámetro recibe un atributo de OpenCV llamado cv2.COLOR_BGR2HSV para convertir una imagen 
    #RGB a su formato de colores HSV, escala de grises, etc.
    img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #copy(): Método que crea una copia de la imagen.
    imagenAuxiliar = frame.copy()

    #objetoCascadeClassifier.detectMultiScale(): Con este método se accede a la base de datos de 
    #reconocimiento facial de OpenCV para el reconocimiento de rostros, a este se le pasa como parámetro 
    #la imagen que se quiere analizar, pero antes se debió haber obtenido la escala de grises de la imagen 
    #y jalado con el método cv.CascadeClassifier() la base de datos de reconocimiento de rostros, después 
    #para mejorar la detección de rostros se puede indicar un factor de escala que se encargue de reducir el 
    #tamaño de la imagen en cada búsqueda durante la detección de caras y finalmente el mínimo número de 
    #vecinos para que una región sea considerada una detección válida, donde un valor más alto requiere que 
    #más comprobaciones correctas para ser considerada como una detección válida. Esto ayuda a eliminar 
    #detecciones falsas.
    caras = clasificacionFacial.detectMultiScale(img_gray, 1.3, 7)
    
    #Bucle for que dibuja un rectángulo alrededor del rostro identificado, para ello debe reconocer el ancho 
    #y alto del rostro.
    color_rectangulo = (176, 224, 17) #El color se guarda en una lista, se maneja como BGR en OpenCV
    grosor_rectangulo = 2 #Grosor del rectángulo en píxeles
    for (x, y, ancho, altura) in caras:
        #cv.rectangle(): Con este método perteneciente a la librería OpenCV se puede crear un rectángulo, en 
        #él se indica primero en que imagen obtenida con el método imread() se va a dibujar la figura, luego 
        #las coordenadas iniciales x,y de la imagen en donde se va a dibujar la esquina superior izquierda del 
        #rectángulo, seguido de las coordenadas x2,y2 que consideran el tamaño de la imagen, su color y si se 
        #quiere que sea hueco o sólido el rectángulo, si se buscara que fuera sólido se pondría un -1, si 
        #fuera hueco, en esta parte se indicaría el los pixeles del grosor del borde del rectángulo.
        cv2.rectangle(frame, (x, y), (x + ancho, y + altura), color_rectangulo, grosor_rectangulo)
        #Recordemos que la imagen en realidad es una matriz, entonces para acceder a solo una parte de ella, 
        #se indica que de la matriz, osea del numpy array, solo se tome un rango de valores que vayan desde x 
        #hasta ancho en la parte horizontal de las 3 capas y de las coordenadas y hasta altura en la parte 
        #vertical de las 3 capas que conforman la imagen digital. 
        cara = imagenAuxiliar[y:y + altura, x:x + ancho]
        #resize(): Lo que hace este método es cambiar el tamaño de una imagen, para ello recibe como primer 
        #parámetro la variable que almacena la imagen y como segundo parámetro indica la magnitud de la nueva 
        #imagen, como segundo parámetro se le da un nuevo tamaño de 150x150 pixeles y finalmente el parámetro
        #opcional interpolation sirve para ajustar los valores de píxeles en la matriz de la nueva imagen 
        #para que no se pierda su calidad y esencia.
        cara = cv2.resize(cara, (150, 150), interpolation = cv2.INTER_CUBIC)
        #imwrite(): Método de la librería OpenCV que sirve para guardar una imagen, como primer parámetro 
        #tengo que poner el nombre con el que se guardará la imagen con todo y extensión y en el segundo debo
        #poner la variable de la que se extrae la imagen.
        cv2.imwrite(usuarioPath + f"/cara_{numeroCara}.jpg", cara)
        numeroCara += 1
    #imshow(): Con el método se puede mostrar una imagen, el primer parámetro es el nombre de la ventana donde 
    #aparecerá la imagen y el segundo parámetro es la imagen recopilada.
    cv2.imshow('Reconocimiento facial', frame)

    #waitKey(): Método que permite a los usuarios mostrar una ventana durante un número de milisegundos 
    #determinados si su parámetro es un número mayor a 1 o hasta que se presione cualquier tecla. Toma 
    #tiempo en milisegundos como parámetro y espera el tiempo dado para destruir la ventana: 
    # - Si se pasa 0 como argumento, espera hasta que se presiona cualquier tecla.
    # - Si se pasa 1 como argumento, espera hasta que se presione una tecla específica para cerrar la 
    #   ventana.
    #El método waitKey() está monitoreando si se presiona una tecla o no, este modo se activa si se le 
    #pasa como parámetro un número 1, de esta manera:
    # - Si no se presiona una tecla retorna un valor -1 
    # - Si se presiona una tecla, retorna un valor ASCII correspondiente a la tecla que se oprimió, con 
    #   el método ord() podemos indicar el código ASCII de la letra del teclado que indiquemos en su 
    #   parámetro.  
    if (cv2.waitKey(1) == ord('r')) or (numeroCara >= 300): #Se cierra el programa cuando se presione la letra q
        #cv2.VideoCapture().release(): Con este método se libera la webcam, tanto en software como en 
        #hardware.
        rostro.release()
        #destroyAllWindows(): Función que permite a los usuarios destruir todas las ventanas en 
        #cualquier momento. No toma ningún parámetro y no devuelve nada, esto se incluye para que al 
        #cerrar la ventana después del método waitKey() se destruyan para poder utilizarse en otra cosa.
        cv2.destroyAllWindows()
        break