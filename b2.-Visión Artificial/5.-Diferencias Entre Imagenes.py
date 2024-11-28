#IMPORTACIÓN DE LIBRERÍAS:
import cv2 as cv #Librería OpenCV: Sirve para todo tipo de operaciones de visión artificial

#ENCONTRAR LAS DIFERENCIAS ENTRE DOS IMÁGENES: Se puede encontrar la diferencia entre dos imágenes simplemente restándolas.
imgu1 = cv.imread('0.-Img/UPIITA_1.jpg', 1) #Imagen RGB obtenida con el método imread()
imgu2 = cv.imread('0.-Img/UPIITA_2.jpg', 1) #Imagen RGB obtenida con el método imread()
#cv.subtract(): Método que hace la resta entre dos imágenes, en específico resta la imagen del primer parámetro menos la del 
#segundo, esto indicará las diferencias entre ellas.
imgDif = cv.subtract(imgu1, imgu2)
#imwrite(): Método de la librería OpenCV que sirve para guardar una imagen, como primer parámetro tengo que poner el 
#nombre con el que se guardará la imagen con todo y extensión y en el segundo debo poner la variable de la que extrae 
#la imagen.
cv.imwrite('0.-Img/Subtract.jpg', imgDif)
cv.imshow("Substract", imgDif) #Mostrar una ventana que tenga como título el 1er parametro y muestre la imagen del 2do
cv.imshow("Imagen 1", imgu1) #Mostrar una ventana que tenga como título el 1er parametro y muestre la imagen del 2do
cv.imshow("Imagen 2", imgu2) #Mostrar una ventana que tenga como título el 1er parametro y muestre la imagen del 2do
#NO DEJAR QUE SE CIERREN LAS VENTANAS: Las siguientes dos líneas de código sirven para que no se cierre la ventana.
cv.waitKey(0) #Mostrar la ventana hasta que se presione la tecla X
cv.destroyAllWindows() #Destruir todas las ventanas después de cerrarlas con el comando

img1 = cv.imread('0.-Img/Subtract.jpg', 1) #Imagen RGB obtenida con el método imread()
#copy(): Este método se debe aplicar a un objeto de la librería OpenCV y sirve para crear una copia del objeto al que se esté 
#aplicando para poder guardarse en una variable extra.
#Se crea una copia de la imagen original para que cuando se modifique la imagen original, de donde se obtendrá el resultado del 
#color, y cuando ya no quiera que se vea esa modificación, debe haber una imagen que refresque la interfaz y muestre la imagen 
#original, por eso es que se creó esta copia.
img_copy = img1.copy()
#cvtColor(): Método de la librería OpenCV que recibe como primer parámetro una imagen RGB y en su segundo parámetro recibe un
#atributo de OpenCV llamado cv.COLOR_BGR2GRAY para convertir una imagen RGB a su escala de grises.
img_gray = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)
#cv.blur(): El método recibe la imagen o video original y luego el tamaño del Kernel que va a aplicar para realizar el 
#filtro Gaussiano de suavizado, que puede ser una matriz de tamaño: 3X3, 5X5, 7X7, 10X10 o 31X31. 
#En este caso se aplica el suavizado para poder identificar de mejor manera los objetos, ya que en la sintonización, pueden salir 
#bordes separados de un mismo objeto, confundiéndolo así como si fueran varios cuando es uno solo, de esta manera se expanden los 
#pixeles para que se vea como un solo objeto. Pero hay que tener cuidado, que si el Kernel es muy grande, no identificará los 
#objetos. Con un Kernel de (30, 30) no lo identifica pero con uno de (10, 10) si lo identifica.
suavizado = cv.blur(img_gray, (5, 5))

#FUNCIONES DE SINTONIZACIÓN DE IMAGEN:
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
    img2 = img_copy.copy()
    #cv.drawContours(): Método que sirve para dibujar los contornos recabados con el método cv.findContours(), para ello primero se 
    #debe indicar en qué imagen se va a dibujar el contorno, no debe ser la misma de la que se obtuvieron los contornos, después se 
    #indica en el segundo parámetro la variable en donde están almacenados los contornos, en el tercer parámero se establece si se 
    #quiere que sea hueco o sólido el contorno, como se busca que sea sólido se pone -1, si fuera hueco, en esta parte se indicaría 
    #los pixeles del perímetro (borde) del contorno, posteriormente se indica el color y finalmente los contornos que quiero que 
    #muestre.
    color_contorno = (10, 100, 200) #Variable que almacena un color BGR
    cv.drawContours(img2, Contornos, -1, color_contorno, 3)
    cv.imshow('Imagen contornos', img2) #Mostrar una ventana que tenga como título el 1er parametro y muestre la imagen del 2do

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





#MOSTRAR UNA FLECHA PARA INDENTIFICAR LOS OBJETOS QUE DIFERENCÍAN UNA IMAGEN DE LA OTRA
umbral = 18 #Indica el umbral a partir del cual se identifica las diferencias de mejor manera
flecha = 40 #Indica el ancho de la flecha que queremos mostrar
grosor = 3 #Indica el grosor de la flecha
color = (0, 0, 255) #Color de la flecha en BGR

#cv.threshold(): Este método sirve para umbralizar una imagen, en ella se le pasa como primer parámetro la imagen en escala de 
#grises que va a umbralizar, a continuación se indica el valor del umbral, el valor máximo que puede alcanzar el umbral y se 
#especifica que el resultado debe ser una imagen binaria con un atributo de OpenCV llamado cv.THRESH_BINARY o si se quiere el 
#inverso se puede usar cv.THRESH_BINARY_INV, en este caso se usa un guión bajo antes del nombre de la variable, porque esta es 
#una variable interna.
#El guión bajo también usa para ignorar valores específicos, si no se necesita algún valor en específico del método, o no usa 
#estos valores, simplemente se asignan estos valores a la "variable" representada con un guión bajo, en python el orden del 
#guión importa, ya que indica qué variable es la que será interna.
_, img_umbral = cv.threshold(img_gray, umbral, 255, cv.THRESH_BINARY_INV)
#cv.findContours(): Este método sirve para encontrar los contornos en una imagen, se puede utilizar en vez del filtro Canny, al 
#método se le pasa como primer parámetro la imagen en escala de grises, en las imágenes existen varios tipos de contornos, estos 
#pueden tener jerarquías de dentro hacia fuera o pueden no tenerlas, esto depende del segundo parámetro que se le pase en el 
#método, en este caso vamos a utilizar el parámetro cv.RETR_LIST para que no muestre jerarquía en los bordes que encuentre, 
#posteriormente se le debe indicar en el tercer parámetro la forma en la que se va a guardar la información recabada, ya que 
#puede guardar todos los puntos del contorno identificado o solo guardar los puntos de las esquinas que conforman el contorno, 
#para que guarde todos los puntos de los contornos se le indica con el atributo cv.CHAIN_APPROX_NONE, para guardar solo las 
#esquinas se usa el atributo cv.CHAIN_APPROX_SIMPLE.
Contornos, _ = cv.findContours(img_umbral, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
for objeto in Contornos:
    #cv.boundingRect(): Lo que hace este método es pintar un cuadro alrededor de un objeto, indicando cúanto mide el cuadro de 
    #alto, de ancho y las coordenadas izquierda superior del recuadro que rodea los objetos identificados en la imagen, para ello 
    #se debe analizar los contornos previamente identificados con el filtro de Canny o el método cv.findContours().
    x, y , ancho, alto = cv.boundingRect(objeto)
    #Como se quiere dibujar una flecha a la mitad del objeto, debemos encontrar la mitad de la altura para pintar la flecha ahí 
    #con el método cv.arrowedLine().
    x_extremo1 = x + ancho + flecha 
    y_extremo1 = y + int(alto/2) - flecha
    x_extremo2 = x + ancho
    y_extremo2 = y + int(alto/2)
    #arrowedLine(): Método que crea una flechita en la imagen que le indique en su primer parámetro, luego debo indicar el punto 
    #de inicio, punto final, color y grosor de la flechita. El color se indica en formato BGR y si la imagen fue obtenida en 
    #formato de grises, este color no se respetará y aparecerá en formato de grises también. Este se debe poner antes de la 
    #instrucción imshow().
    cv.arrowedLine(imgu1, (x_extremo1, y_extremo1), (x_extremo2, y_extremo2), color, grosor)

cv.imshow("Imagen 1", imgu1) #Mostrar una ventana que tenga como título el 1er parametro y muestre la imagen del 2do
cv.imshow("Imagen 2", imgu2) #Mostrar una ventana que tenga como título el 1er parametro y muestre la imagen del 2do
#NO DEJAR QUE SE CIERREN LAS VENTANAS: Las siguientes dos líneas de código sirven para que no se cierre la ventana.
cv.waitKey(0) #Mostrar la ventana hasta que se presione la tecla X
cv.destroyAllWindows() #Destruir todas las ventanas después de cerrarlas con el comando