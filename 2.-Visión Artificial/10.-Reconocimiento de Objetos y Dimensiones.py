# -*- coding: utf-8 -*-
#Comentario de una sola linea con el simbolo #, en Python para nada se deben poner acentos sino el programa
#puede fallar o imprimir raro en consola, la primera línea de código es para que no tenga error, pero aún
#así al poner un ángulo saldrá raro en consola, la línea debe ponerse tal cual como aparece y justo al inicio.
#CERVANTES RODRÍGUEZ DIEGO; SISTEMAS DE VISIÓN ARTIFICIAL; 4MM6; ENRIQUE GAYTAN JESÚS

#IMPORTACIÓN DE LIBRERÍAS:
import cv2 as cv #Librería OpenCV: Sirve para todo tipo de operaciones de visión artificial


#RECONOCIMIENTO DE OBJETOS Y DIMENSIONES: En el programa se realiza la identificación de objetos por medio de su geometría, para 
#ello se puede recortar la imagen original para reconocer un objeto en específico o seleccionar una sección de la imagen para que 
#reconozca todos los objetos que se encuentran en esa sección o recorte.


#SELECCIÓN DE OBJETO A ANALIZAR:
#RECORTE DE REGIONES: Esta operación se realiza para hacer un recorte de una imagen de cierta región que se quiere analizar, ya 
#sea para analizar ojos, formas específicas, objetos de cierto color, etc.
#Para mostrar la parte que se va a recortar de la imagen con el mouse se debe mostrar un rectangulo rojo, en este primero que nada 
#se debe indicar sus propiedades guardadas en unas variables.
color_rectangulo = (0, 0, 255) #El color se guarda en una lista, recordemos que el color se maneja como BGR en OpenCV
grosor_rectangulo = 2 #Grosor del rectángulo en píxeles
ancho_min = 100 #Ancho mínimo en píxeles del rectángulo que extraerá la imagen

#imread(): Sirve para leer la imagen de un directorio especificado, si en el segundo parámetro se pone un 1, la imagen se 
#obtendrá en forma de matriz 3D RGB y si se pone un 0 se obtendrá en escala de grises, obteniendo una matriz 2D.
imagen1 = cv.imread('0.-Img/Objetos_flashV3.jpeg', 1)
#img.copy(): Se crea una copia de la imagen original para que cuando se modifique la imagen, de donde se obtendrá la región que se 
#quiere extraer, y no se quiera ver esa modificación en la ventana original, exista una imagen que refresque la ventana y muestre 
#la imagen original sin ningún cambio. Por eso es que se creó esta copia, además servirá para realizar la sintonización de la 
#geometría de la figura posteriormente.
imagen1_copia = imagen1.copy()

#imshow(): Con el método se puede mostrar una imagen, el primer parámetro es el nombre de la ventana donde aparecerá la imagen 
#y el segundo parámetro es la imagen recopilada con el método imread()
cv.imshow('Interfaz para recorte de imagen RGB', imagen1)

#Función para que cada que se de clic sobre la imagen, se obtenga las coordenadas de la parte en donde se dio clic, para ello se 
#debe recibir como parámetros: 
# - El evento del mouse: Este evento forma parte de los eventos descritos por la librería OpenCV.
# - Las coordenadas en x y y de la parte de la imagen donde se dió clic: Obtenidas de la imagen ya que esta es una matriz.
# - Bandera: Indica cuando ya se realizó el evento del mouse
# - Los parámetros: No se hace nada con ellos en esta función
def region(evento, x, y, bandera, parametro):
    #Se declara dos variables x1 y y1 que almacenen las coordenadas de la imagen donde se dió clic y una variable que se llame 
    #igual a la imagen original que almacena la imagen para que se pueda ver o alcanzar desde cualquier parte del código.
    global x1, y1, imagen1
    #El primer if reacciona cuando se presione el mouse, para que en conjunto los tres condicionales identifiquen cuando se deje 
    #presionado el mouse y se arrastre para seleccionar una parte de la imagen y de esta manera se seleccione lo que se quiere 
    #recortar de la imagen:
    # - EVENT_LBUTTONDOWN: Evento que indica que el botón izquierdo del ratón está presionado.
    if (evento == cv.EVENT_LBUTTONDOWN):
        #Se asigna el valor de la parte donde se dió clic en la imagen a las variables globales x1 y y1
        x1, y1 = x, y
    #El condicional else if lo que hará es ver cuando el mouse esté presionado y moviéndose, esto se realiza analizando el evento 
    #de la función y la bandera, ambas indican el estado del mouse y con ambas se pone la condición de refrescar la imagen.
    #El condicional else if lo que hará es refrescar varias veces la imagen y a su vez pintar el cuadrado que indica la parte que 
    #se quiere recortar de la imagen, para ello primero que nada se asigna a la variable de la imagen original una copia de la 
    #copia de la imagen para que se refresque lo que muestra la ventana y luego se crea el rectángulo.
    # -  EVENT_MOUSEMOVE: Evento que indica que el puntero del ratón se ha movido sobre la ventana.
    # -  EVENT_FLAG_LBUTTON: Bandera que indica que el botón izquierdo del ratón está presionado.
    elif ((evento == cv.EVENT_MOUSEMOVE) and (bandera == cv.EVENT_FLAG_LBUTTON)):
        #Si no se crea una copia de la copia de la imagen original y se va pintando sobre la imagen, se dibujarán varios cuadrados 
        #sobre la imagen que mancharán la parte seleccionada.
        imagen1 = imagen1_copia.copy() #Copia de la copia de la imagen original
        #cv.rectangle(): Con este método perteneciente a la librería OpenCV se puede crear un rectángulo, en él se indica primero 
        #en que imagen obtenida con el método imread() se va a dibujar la figura, luego las coordenadas iniciales x,y de la imagen 
        #en donde se va a dibujar la esquina superior izquierda del rectángulo, que en este caso son las coordenadas x1 y y1 en 
        #donde primero se presionó el mouse, seguido de las coordenadas x,y que son las actuales donde se está dando dejando 
        #presionado el clic y arrastrando el mouse, su color y si se quiere que sea hueco o sólido el rectángulo, si se buscara 
        #que fuera sólido se pondría un -1, si fuera hueco, en esta parte se indicaría el los pixeles del grosor del borde del 
        #rectángulo.
        cv.rectangle(imagen1, (x1, y1), (x, y), color_rectangulo, grosor_rectangulo)
    #Cuando se deje de presionar el mouse, simplemente se refresca la imagen, mostrando una copia de la copia de la imagen 
    #original, para que esto pase debemos checar si las coordenadas actuales x,y son mayores que las coordenadas x1,y1 donde se 
    #dió clic por primera vez al mouse, si esto es así y además se cumple la condición de que el ancho del rectángulo es mayor o 
    #igual que el ancho mínimo, se hace el recorte de la imagen, si no es el caso, simplemente se refresca la ventana, mostrando 
    #la imagen original.
    #Los eventos que se van a manejar son parte de la librería OpenCV:
    # - EVENT_LBUTTONDOWN: Indica que el botón izquierdo del ratón está presionado.
    elif (evento == cv.EVENT_LBUTTONUP):
        if((x > x1) and (y > y1) and (x-x1 >= ancho_min)):
            #Recordemos que la imagen es una matriz, entonces para acceder a solo una parte de ella, se indica que de la matriz, 
            #osea del numpy array, solo tome un rango de valores que vayan desde x1 hasta x en la parte horizontal de las 3 capas 
            #y de las coordenadas y1 hasta y en la parte vertical de las 3 capas que conforman la imagen digital. 
            obj1_recorte = imagen1_copia[y1:y, x1:x]
            cv.imshow('Recorte imagen', obj1_recorte) #Ventana que tenga como título el 1er parametro y muestre la imagen del 2do
            #imwrite(): Método de la librería OpenCV que sirve para guardar una imagen, como primer parámetro tengo que poner el 
            #nombre con el que se guardará la imagen con todo y extensión y en el segundo debo poner la variable de la que extrae 
            #la imagen.
            cv.imwrite('0.-Img/Reconocimiento_obj_1.jpg', obj1_recorte)
    #imshow(): Se diferencía las ventanas que van a aparecer dependiendo del título que tengan, las que tengan en mismo título 
    #reemplazarán a la imstrucción anterior de imshow().
    cv.imshow('Interfaz para recorte de imagen RGB', imagen1) #Ventana que tenga como título el 1er parametro y muestre la imagen del 2do

#CONFIGURACIÓN DE LA OPERACIÓN CON EL MOUSE:
#setMouseCallback(): Se utiliza esta función para que el mouse pueda interactuar con una ventana en específico, se manda a llamar 
#esta ventana poniendo el mismo nombre que usa en el título del método imshow() para mostrarla, además se indica la función que se 
#va a ejecutar con el mouse dentro de la ventana y si es necesario al final se indica dónde se almacena la data proveniente.
cv.setMouseCallback('Interfaz para recorte de imagen RGB', region)
cv.waitKey(0) #Mostrar la ventana hasta que se presione la tecla X
cv.destroyAllWindows() #Destruir todas las ventanas después de cerrarlas con el comando

#La documentación para realizar todas las operaciones de este ejercicio son las siguientes:
#MÉTODOS PARA CONTROLAR LOS EVENTOS DEL MOUSE: Para ver cuando se haya dado clic, se suelte el clic del mouse, etc.
#https://docs.opencv.org/3.4/d0/d90/group__highgui__window__flags.html#gga927593befdddc7e7013602bca9b079b0ad3419100fc2d7688c6dbe3da030fbfd9




#OBTENCIÓN DE LA GEOMETRÍA DE OBJETOS POR MEDIO DE UMBRALIZACIÓN Y SINTONIZACIÓN CON BARRA DE VALOR VARIABLE:
#imread(): Sirve para leer la imagen de un directorio especificado, si en el segundo parámetro se pone un 1, la imagen se 
#obtendrá en forma de matriz 3D RGB y si se pone un 0 se obtendrá en escala de grises, obteniendo una matriz 2D.
objeto1_recorte = cv.imread('0.-Img/Reconocimiento_obj_1.jpg', 1) #Imagen RGB obtenida con el método imread()
#shape: Atributo extraído de una variable obtenida con el método cv.imread(), indica distintas características de la imagen y 
#las guarda en 3 distintas variables, guardándo primero el ancho, luego el alto y finalmente el número de canales, 
#específicamente en ese órden.
alto, ancho, canales = objeto1_recorte.shape
#Se analizó el tamaño de la imagen para ver si es necesario utilizar el método resize que cambia el tamaño de la imagen, esto se 
#hace porque si la imagen es demasiado pequeña, no podrá aparecer la barra que varía el valor del umbral correctamente, por lo 
#cual no se podrá sintonizar la imagen correctamente, específicamente se realiza esto cuando el alto y ancho de la imagen es menor
#a 200 pixeles correspondientemente.
if((alto < 200) or (ancho < 200)):
    #resize(): Lo que hace este método es cambiar el tamaño de una imagen obtenida con el método imread(), para ello recibe como 
    #primer parámetro la variable que almacena la imagen y como segundo parámetro indica la magnitud de la nueva imagen. 
    #Si el ancho o alto de la imagen es menor a 200 pixeles, se le da un nuevo tamaño de 500x500 pixeles.
    objeto1_recorte_bigger = cv.resize(objeto1_recorte, (500, 500))
    objeto1_recorte_modificada = objeto1_recorte_bigger
else:
    #Si el ancho o alto de la imagen no es menor a 200 pixeles en cualquiera de las dos magnitudes, se deja el tamaño tal cual está
    objeto1_recorte_modificada = objeto1_recorte
#copy(): Este método se debe aplicar a un objeto de la librería OpenCV y sirve para crear una copia del objeto al que se esté 
#aplicando para poder guardarse en una variable extra.
#Se crea una copia de la imagen original para que cuando se modifique la imagen original, de donde se obtendrá el resultado del 
#color, y cuando ya no quiera que se vea esa modificación, debe haber una imagen que refresque la interfaz y muestre la imagen 
#original, por eso es que se creó esta copia.
img_copy = objeto1_recorte_modificada.copy()
#cvtColor(): Método de la librería OpenCV que recibe como primer parámetro una imagen RGB y en su segundo parámetro recibe un
#atributo de OpenCV llamado cv.COLOR_BGR2GRAY para convertir una imagen RGB a su escala de grises, este método debe recibir la 
#imagen original, no importando el tamaño de la imagen que se quiere mostrar con el navbar porque sino se modificará toda la 
#identificación de la geometría de los objetos en la imagen.
img_gray = cv.cvtColor(objeto1_recorte, cv.COLOR_BGR2GRAY)

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
#valores obtenidos, se puede analizar la imagen para identificar solo ciertas figuras por su geometría.
"""
Sintonización de la imagen - Identificación de monedas - Valores obtenidos:
Umbral óptimo: 125
Martillo        = 15787.0
Metro           = 44851.5
Pasta de soldar = 20668.0
Pinzas          = 29355.5
Cutter          = 101925.0, 110908.0


Umbral óptimo: 140
Martillo        = 17470.5
Metro           = 51815.5
Pasta de soldar = 21439.5
Pinzas          = 166116.5, 187590.0
Cutter          = 9958.5, 101925.0, 110898.0


Umbral óptimo: 146
Martillo        = 18066.0
Metro           = 53366.5, 52897.0
Pasta de soldar = 21698.0
Pinzas          = 162268.0, 178001.5
Cutter          = 7369.0, 8069.5, 9993.0, 26949.0, 26942.0
"""
umbral = 146
#Se va a escribir en la imagen, por lo que se debe especificar las características del texto:
grosor = 1 #Grosor de las letras, dado en pixeles
fuente = cv.FONT_HERSHEY_SIMPLEX #Fuente de la letra a utilizarse
posicion_texto_1 = (20, 20) #Posición donde se mostrará el texto cuando se identifique la moneda 1
posicion_texto_2 = (20, 40) #Posición donde se mostrará el texto cuando se identifique la moneda 2
posicion_texto_3 = (20, 60) #Posición donde se mostrará el texto cuando se identifique la moneda 3
posicion_texto_4 = (20, 80) #Posición donde se mostrará el texto cuando se identifique la moneda 3
posicion_texto_5 = (20, 100) #Posición donde se mostrará el texto cuando se identifique la moneda 3
#Colores de los textos que indican la identificación de monedas, recordemos que se indica en formato BGR:
color_texto1 = (0, 255, 255)    #Color amarillo
color_texto2 = (255, 255, 255)  #Color negro
color_texto3 = (255, 0, 0)      #Color azul
color_texto4 = (0, 0, 255)      #Color rojo
color_texto5 = (0, 255, 0)      #Color verde
#Tamaño del texto
tamanoTexto = 0.6
#Se declaran como variables las áreas obtenidas en la sintonización, se pone un valor un poco menor para que identifique la 
#moneda considerando un margen de error:
martilloMax = 18200
martilloMin = 17900     #Matrillo sí; Umbral = 146
metroMax = 53500
metroMin = 52700        #Metro sí; Umbral = 146
pastaSoldarMax = 21800
pastaSoldarMin = 21400  #Pasta de soldar sí; Umbral = 146
#PinzasMax = 5300
PinzasMin = 162000      #Pinzas sí; Umbral = 146
CutterMax = 9993.0
CutterMin = 7525.0      #Cutter sí; Umbral = 146
#Variable que indica el objeto captado en la imagen, en un inicio tienen valor cero
Martillo = 0
Metro = 0
PastaSoldar = 0
Pinzas = 0
Cutter = 0

_, img_umbral = cv.threshold(img_gray, umbral, 255, cv.THRESH_BINARY) #Binarización de la imagen.
Contornos, _ = cv.findContours(img_umbral, cv.RETR_LIST, cv.CHAIN_APPROX_NONE) #Identificación de bordes por figura.

for borde_moneda in Contornos:
    #abs(): Obtiene el valor absoluto de un valor, se usa el método abs() porque a veces los resultados de área vienen en valor 
    #negativo
    #contourArea(): Función que sirve para medir áreas, para ello se debe haber obtenido el contorno de una figura en una imagen, 
    #esta se obtiene en área de pixeles, por lo que no se considera como un área tal cual del mundo real.
    area = abs(cv.contourArea(borde_moneda))
    if (martilloMax>= area >= martilloMin):
        Martillo += 1
    elif (metroMax>= area >= metroMin):
        Metro += 1
    elif (pastaSoldarMax >= area >= pastaSoldarMin):
        PastaSoldar += 1
    elif (area >= PinzasMin):
        Pinzas += 1
    elif (CutterMax >= area >= CutterMin):
        Cutter += 1
    
#cv.putText(): Permite colocar texto en cualquier imagen, como primer parámetro se le indica la imagen en donde se pondrá el 
#texto, luego el texto que se quiere colocar, después se indica la posición donde se colocará el texto, la fuente, escala, el 
#color y el grosor del texto.  
cv.putText(objeto1_recorte_modificada, "Martillo: " + str(Martillo), posicion_texto_1, fuente, tamanoTexto, color_texto1, grosor)
cv.putText(objeto1_recorte_modificada, "Metro: " + str(Metro), posicion_texto_2, fuente, tamanoTexto, color_texto2, grosor)
cv.putText(objeto1_recorte_modificada, "Pasta de soldar: " + str(PastaSoldar), posicion_texto_3, fuente, tamanoTexto, color_texto3, grosor)
cv.putText(objeto1_recorte_modificada, "Pinzas: " + str(Pinzas), posicion_texto_4, fuente, tamanoTexto, color_texto4, grosor)
cv.putText(objeto1_recorte_modificada, "Cutter: " + str(Cutter), posicion_texto_5, fuente, tamanoTexto, color_texto5, grosor)

cv.imshow('Imagen contornos', objeto1_recorte_modificada) #Mostrar una ventana que tenga como título el 1er parametro y muestre la imagen del 2do
#NO DEJAR QUE SE CIERREN LAS VENTANAS: Las siguientes dos líneas de código sirven para que no se cierre la ventana.
cv.waitKey(0) #Mostrar la ventana hasta que se presione la tecla X
cv.destroyAllWindows() #Destruir todas las ventanas después de cerrarlas con el comando