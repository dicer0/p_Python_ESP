#IMPORTACIÓN DE LIBRERÍAS:
import cv2 as cv #Librería OpenCV: Sirve para todo tipo de operaciones de visión artificial

#IDENTIFICAR LAS FIGURAS Y MOSTRAR UN TEXTO QUE INDIQUE CADA FIGURA QUE HAYA IDENTIFICADO
umbral = 240 #El umbral se debe cambiar para que identifique de manera correcta las líneas de las figuras.
color = (0,0,0) #Color del borde
grosor = 3 #Grosor del borde
texto = "" #Variable que almacena el texto que queremos mostrar
fuente = cv.FONT_HERSHEY_SIMPLEX #Fuente de la letra a utilizarse

#IDENTIFICACIÓN DE FIGURAS - PARAMETRIZACIÓN DE PASOS:
#1.- Recopilación de imágenes.
Img = cv.imread('0.-Img/Figuras_3.png')

#2.- Conversión a escala de grises: Porque es más sencillo analizar una matriz a analizar 3 sobrepuestas.
#cvtColor(): Método de la librería OpenCV que recibe como primer parámetro una imagen RGB y en su segundo parámetro recibe un
#atributo de OpenCV llamado cv.COLOR_BGR2GRAY para convertir una imagen RGB a su escala de grises.
img_gray = cv.cvtColor(Img, cv.COLOR_BGR2GRAY)

#3.- Umbralización de la imagen: Creación de imagen binaria para separar el objeto del fondo.
#cv.threshold(): Este método sirve para umbralizar una imagen, en ella se le pasa como primer parámetro la imagen en escala de 
#grises que va a umbralizar, a continuación se indica el valor del umbral, el valor máximo que puede alcanzar el umbral y se 
#especifica que el resultado debe ser una imagen binaria con un atributo de OpenCV llamado cv.THRESH_BINARY o si se quiere el 
#inverso se puede usar cv.THRESH_BINARY_INV, en este caso se usa un guión bajo antes del nombre de la variable, porque esta es 
#una variable interna.
#El guión bajo también usa para ignorar valores específicos, si no se necesita algún valor en específico del método, o no usa 
#estos valores, simplemente se asignan estos valores a la "variable" representada con un guión bajo, en python el orden del 
#guión importa, ya que indica qué variable es la que será interna.
_, img_umbral = cv.threshold(img_gray, umbral, 255, cv.THRESH_BINARY)

#4.- Identifiación de contornos en la imagen: Para obtener los bordes de los objetos que se busca identificar.
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
#debe indicar en qué imagen se va a dibujar el contorno, después se indica en el segundo parámetro la variable en donde están 
#almacenados los contornos, en el tercer parámero se establece si se quiere que sea hueco o sólido el contorno, como se busca que 
#sea sólido se pone -1, si fuera hueco, en esta parte se indicaría los pixeles del perímetro (borde) del contorno, posteriormente 
#se indica el color y finalmente los contornos que quiero que muestre.
cv.drawContours(Img, contornos, -1, color, grosor)

#Análisis de contornos individualmente
for contorno in contornos:
    #cv.boundingRect(): Lo que hace este método es pintar un cuadro alrededor de un objeto, indicando cúanto mide el cuadro de 
    #alto, de ancho y las coordenadas izquierda superior del recuadro que rodea los objetos identificados en la imagen, para ello 
    #se debe analizar los contornos previamente identificados con el filtro de Canny o el método cv.findContours().
    x, y, ancho, alto = cv.boundingRect(contorno)
    #arcLength(): Método que calcula un perímetro de contorno o una longitud de curva, se debe haber utilizado el método de 
    #cv.findContours() praviamente y un bucle for para que se le pase los contornos identificados, posteriormente se indica por 
    #medio de una variable booleana si queremos que se nos indique si la curva analizada está cerrada o no, con True se indica, 
    #con False no se indica.
    # - En este caso se multiplica por 0.01 para que por medio del algoritmo de Douglas-Pecker los contornos de las figuras, por 
    #   medio de un margen de error de 0.1 por la longitud del contorno.
    margen_error = 0.01 * cv.arcLength(contorno, True)
    #Algoritmo de Douglas Pecker: Identificación de líneas en forma de vector, se hace a través del método cv.approxPolyDP().
    #cv.approxPolyDP(): Método que identifica líneas en forma de vector, como primer parámetro recibe el contorno obtenido del 
    #método cv.findContours(), luego se le pasa el margen de error, descrito para el algoritmod e Douglas Pecker y finalmente si 
    #la curva aproximada se cerrará. Si es True la curva aproximada se cierra, de lo contrario, la curva se queda abierta.
    Contorno_dim = cv.approxPolyDP(contorno, margen_error, True)
    if (len(Contorno_dim) == 3): #Si el método cv.approxPolyDP() identificó 3 líneas lo clasifica como triángulo
        texto = "Triangulo"
    elif (len(Contorno_dim) == 4): #Si el método cv.approxPolyDP() identificó 4 líneas lo clasifica como cuadrado
        texto = "Cuadrado"
    elif (len(Contorno_dim) == 5): #Si el método cv.approxPolyDP() identificó 5 líneas lo clasifica como pentágono
        texto = "Pentagono"
    #cv.getTextSize(): El método calcula y devuelve el tamaño de un cuadro que contiene el texto especificado. Es decir, el 
    #siguiente código representa algo de texto, el cuadro estrecho que lo rodea y la línea de base, este recibe como parámetro el 
    #texto que quiere analizar, su fuente, escala y grosor.
    #ancho_texto, alto_texto = cv.getTextSize(texto, fuente, 1, grosor)
    #Ahora se va a hacer un cálculo para que aparezca encima del objeto la figura que representa.
    pos_x = int(x)
    pos_y = int(y + (alto)/2)
    #cv.putText(): Permite colocar texto en cualquier imagen, como primer parámetro se le indica la imagen en donde se pondrá el 
    #texto, luego el texto que se quiere colocar, después se indica la posición donde se colocará el texto, la fuente, escala, el 
    #color y el grosor del texto.
    cv.putText(Img, texto, (pos_x,pos_y), fuente, 1, grosor)

cv.imshow("Figuras",Img) #Mostrar una ventana que tenga como título el 1er parametro y muestre la imagen del 2do
#NO DEJAR QUE SE CIERREN LAS VENTANAS: Las siguientes dos líneas de código sirven para que no se cierre la ventana.
cv.waitKey(0) #Mostrar la ventana hasta que se presione la tecla X
cv.destroyAllWindows() #Destruir todas las ventanas después de cerrarlas con el comando