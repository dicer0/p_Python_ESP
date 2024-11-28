#IMPORTACIÓN DE LIBRERÍAS:
import cv2 as cv #Librería OpenCV: Sirve para todo tipo de operaciones de visión artificial


#RECONOCIMIENTO FACIAL:
#Documentación de la base de datos de OpenCV para realizar el reconocimiento facial:
#https://github.com/opencv/opencv/tree/master
#HAAR CASCADES: Algoritmo de reconocimiento facial, para poder hacer el reconocimiento facial se debe hacer la extracción de la 
#base de datos de haarcascade, de sus archivos xml es de donde se saca la información para poder realizar un correcto 
#reconocimiento facial, en específico se jala el archivo haarcascade_frontalface_default.xml que se encuentra en el siguiente 
#link, para verlo después como un texto normal y copiarlo a un bloc de notas, se debe dar clic en Raw y pegarlo en un documento 
#del bloc de notas, este archivo será utilizado después, es recomendable tener una copia local para el reconocimiento facial por 
#cualquier problema de conexión, actualización de la base de datos, etc. Para identificar cada parte distinta del rostro se deben 
#usar diferentes bases de datos dentro de la documentación de OpenCV.

#PARÁMETROS DEL RECONOCIMIENTO FACIAL
color_rectangulo_rostro = (0, 0, 255) #Color BGR del borde del rectángulo de reconocimiento facial para rostros
grosor_rectangulo_rostro = 2 #Grosor del borde del rectángulo que identifica rostros
color_circulo_ojo = (255, 255, 0) #Color BGR del borde del rectángulo de reconocimiento facial para ojos
grosor_circulo_ojo = 2 #Grosor del borde del rectángulo que identifica ojos

#1.- Recopilación de imágenes.
img1 = cv.imread('0.-Img/Familia.jpg', 1) #Imagen RGB obtenida con el método imread()

#2.- Conversión a escala de grises: Porque es más sencillo analizar una matriz a analizar 3 sobrepuestas.
#cvtColor(): Método de la librería OpenCV que recibe como primer parámetro una imagen RGB y en su segundo parámetro recibe un
#atributo de OpenCV llamado cv.COLOR_BGR2GRAY para convertir una imagen RGB a su escala de grises.
img_gray = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)

#cv.CascadeClassifier(): Este es un clasificador en cascada, esto se refiere a que dependiendo de ciertas características del 
#reconocimiento facial, puede ir segmentando hasta identificar un rostro, ya sea de hombre, mujer, perro, gato, etc. porque cada 
#uno tiene características especiales, para que funcione esto, se debe indicar como parámetro del método la base de datos 
#descargada de la documentación de Github de OpenCV con extensión xml.
#https://docs.opencv.org/3.4/db/d28/tutorial_cascade_classifier.html
#Para la identificación de rostros, específicamente se utiliza la base de datos llamada haarcascade_frontalface_default.xml:
#https://github.com/opencv/opencv/tree/4.x/data/haarcascades
clasificador_caras = cv.CascadeClassifier('7.-API_Reconocimiento_Facial/7.- Reconocimiento facial OpenCV - Rostros.xml')

#objetoCascadeClassifier.detectMultiScale(): Con este método se accede a la base de datos de reconocimiento facial de OpenCV 
#para el reconocimiento de rostros, a este se le pasa como parámetro la imagen que se quiere analizar, pero antes se debió haber
#obtenido la escala de grises de la imagen y jalado con el método cv.CascadeClassifier() la base de datos de reconocimiento de 
#rostros.
caras = clasificador_caras.detectMultiScale(img_gray)

#Bucle for para obtener las coordenadas y dimensiones de las caras
for (x, y, ancho, alto) in caras:
    #cv.rectangle(): Con este método perteneciente a la librería OpenCV se puede crear un rectángulo, en él se indica primero 
    #en que imagen obtenida con el método imread() se va a dibujar la figura, luego las coordenadas iniciales x,y de la imagen 
    #en donde se va a dibujar la esquina superior izquierda del rectángulo, que en este caso son las coordenadas x,y obtenidas 
    #con el reconocimiento facial, seguido de las coordenadas finales x,y que son las que incluyen el ancho y alto del rostro 
    #identificado, posteriormente se indica su color y si se quiere que sea hueco o sólido el rectángulo, si se buscara que fuera 
    #sólido se pondría un -1, si fuera hueco, en esta parte se indicaría el los pixeles del grosor del borde del rectángulo.
    cv.rectangle(img1, (x, y), (x + ancho, y + alto), color_rectangulo_rostro, grosor_rectangulo_rostro)
    #Para cada parte del rostro que se quiera identificar se debe crear un clasificador, todos alimentándose de la misma base de 
    #datos, pero usándose para identificar distintas partes del rostro, para la parte específica de los ojos se usa la base de 
    #datos llamada haarcascade_eye.xml de la documentación de OpenCV que se encuentra en el siguiente link:
    #https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_eye.xml
    clasificador_ojos = cv.CascadeClassifier('7.-API_Reconocimiento_Facial/7.- Reconocimiento facial OpenCV - Ojos.xml')
    #Extraer las coordenadas de la matriz cara desde la coordenada "y" hasta "y + alto" y la coordenada "x" hasta "x + ancho" de 
    #la imagen en escala de grises 
    caraIndividual = img_gray[y:y+alto, x:x+ancho]
    #objetoCascadeClassifier.detectMultiScale(): Con este método se accede a la base de datos de reconocimiento facial de OpenCV 
    #para el reconocimiento de ojos, a este se le pasa como parámetro la imagen que se quiere analizar, pero antes se debió 
    #haber obtenido la colección de datos de identificación de rostros y jalado con el método cv.CascadeClassifier() la base de 
    #datos de reconocimiento ocular. Si no se está haciendo correctamente el análisis del rostro, en esta parte es donde se puede
    #sintonizar la detección de rostros para mejorarla con los siguientes parámetros:
    # - Matriz a analizar: Que en el caso de los ojos es una submatriz de la matriz que identifica rostros.
    # - Factor de escala: Parámetro que especifica cuánto se reduce el tamaño de la imagen en cada escala de la imagen original, 
    #   el factor de escala por default es de 1.1 (scaleFactor). Este valor se sube para que detecte cosas más grandes y se reduce 
    #   cuando se quiere identificar partes más pequeñas.
    # - Vecindario mínimo: Parámetro que especifica cuántos pixeles vecinos debe tener cada rectángulo candidato para conservarlo,
    #   el vecindario mínimo por default es de 3 (minNeighbors).
    # - Tamaño mínimo: Tamaño mínimo posible del vecindario (minSize).
    ojos = clasificador_ojos.detectMultiScale(caraIndividual, scaleFactor = 1.01, minNeighbors = 8, minSize = (10, 10))
    #Con la imagen 'Lena.jpg': scaleFactor = 1.1, minNeighbors = 10, minSize = (10, 10)
    #Con la imagen 'Familia.jpg': scaleFactor = 1.01, minNeighbors = 8, minSize = (10, 10)
    for (x1, y1, ancho1, alto1) in ojos:
        #cv.circle(): Con este método perteneciente a la librería OpenCV se puede crear un círculo, en él se indica primero en 
        #que imagen obtenida con el método imread() se va a dibujar la figura, luego la coordenada x,y de la imagen en donde se 
        #va a mostrar, el radio en pixeles del círculo, su color y si se quiere que sea hueco o sólido el círculo, como se busca 
        #que sea sólido se pone -1, si fuera hueco, en esta parte se indicaría los pixeles del perímetro (borde) del círculo.
        #En la interfaz se mostrará un círculo para mostrar de dónde se está obteniendo el color de la imagen.
        radio = int((ancho1 + alto1)/4)
        cv.circle(img1, (x+x1+radio, y+y1+radio), radio, color_circulo_ojo, grosor_circulo_ojo)

cv.imshow("Rostros", img1) #Mostrar una ventana que tenga como título el 1er parametro y muestre la imagen del 2do
#NO DEJAR QUE SE CIERREN LAS VENTANAS: Las siguientes dos líneas de código sirven para que no se cierre la ventana.
cv.waitKey(0) #Mostrar la ventana hasta que se presione la tecla X
cv.destroyAllWindows() #Destruir todas las ventanas después de cerrarlas con el comando


#También el reconocimiento facial se puede hacer a través de las siguientes herramientas:
# - OpenCV: https://docs.opencv.org/3.4/da/d60/tutorial_face_main.html
# - Python: https://pypi.org/project/face-recognition/