# -*- coding: utf-8 -*-
#Comentario de una sola linea con el simbolo #, en Python para nada se deben poner acentos sino el programa
#puede fallar o imprimir raro en consola, la primera línea de código es para que no tenga error, pero aún
#así al poner un ángulo saldrá raro en consola, la línea debe ponerse tal cual como aparece y justo al inicio.

#IMPORTACIÓN DE LIBRERÍAS:
import cv2 as cv #Librería OpenCV: Sirve para todo tipo de operaciones de visión artificial
import scipy.ndimage #Librería scipy: Se utiliza para aplicar filtros de máximos y mínimos a una imagen




#FILTRO DE MÁXIMOS, MÍNIMOS Y MEDIA: El filtro de máximos y mínimos se utiliza para el manejo de ruido en una imagen, para ello 
#se instala la librería Scipy, los filtros de máximos y mínimos son más utilizados en imagenes de escala de grises con tonos muy 
#obscuros o binarias ya que se utilizan para obtener mayor definición en los tonos negros o blancos de una imagen, por ejemplo, es 
#utilizado en radiografías para determinar de mejor manera las formas de los huesos en la imagen de blanco y negro, mientras que 
#los filtros de media son utilizados en imagenes con escala de grises normales ya que estos ayudan a recuperar una imagen con 
#escala de grises, quitando su ruido y manteniendo en mayor medida su color y forma original.

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
img1 = cv.imread('0.-Img/Lena_Ruido.jpg', 1)
#imshow(): Con el método se puede mostrar una imagen, el primer parámetro es el nombre de la ventana donde aparecerá la imagen 
#y el segundo parámetro es la imagen recopilada con el método imread()
cv.imshow('Imagen con ruido', img1) #Mostrar una ventana que tenga como título el 1er parametro y muestre la imagen del 2do

#SCIPY NDIMAGE: Es una parte de la librería scipy que sirve para aplicar filtros multidimensionales de todo tipo, su 
#documentación se encuentra en el siguiente link:
#https://docs.scipy.org/doc/scipy/reference/generated/scipy.ndimage.maximum_filter.html#scipy.ndimage.maximum_filter
#scipy.ndimage.maximum_filter(): Es el método perteneciente al paquete ndimage de la librería scipy que sirve para aplicar 
#filtros máximos, este recibe como primer parámetro la imagen que quiere analizar, obtenida con el método imread() y como segundo 
#parámetro el tamaño del filtro que se quiere aplicar, este tamaño afectará a la modificación de la imagen original, tanto en el 
#filtro máximo como en el mínimo.

#FILTRO DE MÁXIMOS: Vuelve todo el ruido en tonos blancos, obteniendo así mayor definición en los tonos blancos de la imagen 
#original, quitando negros y maximizando blancos, en función del tamaño del filtro. Recordemos que el tamaño del filtro se refiere 
#al tamaño de la vecindad que rodea cada píxel de analisis en la imagen, mientras más pequeño sea el tamaño del vecindario, es 
#aplicado de manera más fina el filtro. El tamaño del filtro puede ser decimal.
mask = 3.1416 #Al tamaño del filtro se le puede llamar máscara, este puede ser entero o decimal.
img2 = scipy.ndimage.maximum_filter(img1, size = mask)
#FILTRO DE MÍNIMOS: Vuelve todo el ruido en tonos negros, obteniendo así mayor definición en los tonos negros de la imagen 
#original, quitando blancos y maximizando negros, en función del tamaño de la máscara del filtro. El tamaño del filtro puede ser 
#decimal.
img3 = scipy.ndimage.minimum_filter(img1, size = mask)
#FILTRO DE MEDIA: Este filtro como los dos pasados, analiza los tonos de los pixeles incluidos en la vecindad de cada píxel 
#analizado, luego hace un promedio con el tono de gris de estos pixeles y deja pasar ese tono, en específico este filtro trata de 
#remover el ruido de una imagen con escala de grises, conservando su forma y color original, el problema con este filtro es que 
#difumina más la imagen mientras sea mayor el tamaño de la vecindad, a esto se le llama suavizado de imagen. El tamaño del filtro 
#NO puede ser decimal.
img4 = scipy.ndimage.median_filter(img1, size = 6)
#imshow(): Se diferencía las ventanas que van a aparecer dependiendo del título que tengan, las que tengan en mismo título 
#reemplazarán a la imstrucción anterior de imshow().
cv.imshow('Imagen sin ruido - Filtro maximo', img2)
cv.imshow('Imagen sin ruido - Filtro minimo', img3)
#arrowedLine(): Método que crea una flechita en la imagen que le indique en su primer parámetro, luego debo indicar el punto de 
#inicio, punto final, color y grosor de la flechita. El color se indica en formato BGR y si la imagen fue obtenida en formato de 
#grises, este color no se respetará y aparecerá en formato de grises también. Este se debe poner antes de la instrucción imshow()
cv.arrowedLine(img4, (300, 100), (200, 150), (0, 255, 255), 2)
cv.imshow('Imagen sin ruido - Filtro medio', img4)

#namedWindow(): Método de la librería OpenCV que recibe como primer parámetro el título de alguna ventana mostrada con el método 
#cv.imshow() y en su segundo parámetro recibe un atributo de OpenCV llamado WINDOW_NORMAL para hacer que la ventana tenga un 
#tamaño pequeño.
cv.namedWindow('Imagen sin ruido - Filtro maximo', cv.WINDOW_NORMAL)
#moveWindow(): Método de la librería OpenCV que recibe como primer parámetro el título de alguna ventana mostrada con el método 
#cv.imshow() y en su segundo y tercer parámetro recibe la posición en la pantalla donde queremos que se muestre esa ventana, las 
#posiciones xy se indican en pixeles y parten de la esquina superior izquierda.
cv.moveWindow('Imagen con ruido', 0, 0) #Posición izquierda superior
cv.moveWindow('Imagen sin ruido - Filtro maximo', 0, 300) #Posición izquierda inferior
cv.moveWindow('Imagen sin ruido - Filtro minimo', 800, 0) #Posición derecha superior
cv.moveWindow('Imagen sin ruido - Filtro medio', 800, 300) #Posición derecha inferior

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




#OBTENCIÓN Y MUESTRA DEL COLOR DE UNA IMAGEN DONDE SE DÉ CLIC CON EL MOUSE: En esta parte se va a crear una función que obtenga 
#el color de la parte donde se dé clic con el mouse y pinte un círculo con el color del pixel al que se le dió clic, esto solo 
#pasará mientras se esté dando clic sobre la imagen, al soltar el mouse, desaparecerá el círculo.
img5 = cv.imread('0.-Img/Iron Man Bullet.jpg', 1) #Imagen RGB obtenida con el método imread()
#copy(): Este método se debe aplicar a un objeto de la librería OpenCV y sirve para crear una copia del objeto al que se esté 
#aplicando para poder guardarse en una variable extra.
#Se crea una copia de la imagen original para que cuando se modifique la imagen original, de donde se obtendrá el resultado del 
#color, y cuando ya no quiera que se vea esa modificación, debe haber una imagen que refresque la interfaz y muestre la imagen 
#original, por eso es que se creó esta copia.
img_copy = img5.copy()
cv.imshow('Color imagen - RGB', img_copy) #Ventana que tenga como título el 1er parametro y muestre la imagen del 2do

#Función para que cada que se de clic sobre la imagen, se obtenga el color de la parte en donde se dio clic, para ello se 
#debe recibir como parámetros: 
# - El evento del mouse: Este evento forma parte de los eventos descritos por la librería OpenCV.
# - Las coordenadas en x y y de la parte de la imagen donde se dió clic: Obtenidas de la imagen ya que esta es una matriz.
# - Bandera: Indica cuando ya se realizó el evento del mouse
# - Los parámetros: 
def color(evento, x, y, bandera, parametros):
    #Se debe declarar una variable llamada igual que la variable que almacena la imagen original obtenida con el método imread(), 
    #sea declara como tipo global para que se pueda ver o alcanzar desde cualquier parte del código.
    global img5
    #El primer if lo que hará es mostrar un círculo pintado con el color del pixel al que se le dió clic en la imagen.
    #Los eventos que se van a manejar son parte de la librería OpenCV:
    # - EVENT_LBUTTONDOWN: Indica que el botón izquierdo del ratón está presionado.
    if (evento == cv.EVENT_LBUTTONDOWN):
        #Recordemos que la imagen es tal cual una matriz y esta se puede manejar como tal, de esta manera cuando se realice el 
        #evento de clic en la imagen, podemos obtener las coordenadas xy de la parte donde se dió clic de la imagen.
        #.toList(): Este método se aplica a una variable de tipo array para convertirla en una lista, específicamente en visión 
        #artificial esto se usa para poder acceder a las coordenadas x,y de las 3 capas o dimensiones RGB y guardarlas en una 
        #serie de valores BGR, ya que en un inicio cuando son de tipo numpy array (osea un array proveniente de la librería numpy), 
        #solo vienen uno tras otro pero no organizados, como se muestra en el siguiente ejemplo y recordando que en python se 
        #accede a los colores RGB en el orden BGR:
        # - color = img[x, y].toList()
        # - azul  = img[x, y][0]
        # - rojo  = img[x, y][1]
        # - verde = img[x, y][2]
        array = img5[x,y]
        #print(): Imprime en consola el mensaje que se incluya dentro de su paréntesis en forma de string
        print("Tipo primitivo: " + str(type(array)))
        print("Valor array: ", array)
        color_lista = img5[x,y].tolist()
        print("Tipo primitivo: " + str(type(color_lista)))
        print("Valor lista: ", color_lista)
        #cv.circle(): Con este método perteneciente a la librería OpenCV se puede crear un círculo, en él se indica primero en 
        #que imagen obtenida con el método imread() se va a dibujar la figura, luego la coordenada x,y de la imagen en donde se 
        #va a mostrar, el radio en pixeles del círculo, su color y si se quiere que sea hueco o sólido el círculo, como se busca 
        #que sea sólido se pone -1, si fuera hueco, en esta parte se indicaría los pixeles del perímetro (borde) del círculo.
        #En la interfaz se mostrará un círculo para mostrar de dónde se está obteniendo el color de la imagen.
        cv.circle(img5, (x, y), 10, color_lista, -1)
    #El condicional else if lo que hará es remover el círculo pintado con el color del pixel al que se le dió clic en la imagen, 
    #esto pasa cuando se deja de dar clic, para ello se asigna a la variable de la imagen original una copia de la copia de la 
    #imagen original para que se refresque lo que muestra en la ventana. En simples términos, cuando se deje de presionar el mouse, 
    #simplemente se refresca la imagen, mostrando una copia de la copia de la imagen original.
    #Los eventos que se van a manejar son parte de la librería OpenCV:
    # - EVENT_LBUTTONDOWN: Indica que el botón izquierdo del ratón está presionado.
    elif (evento == cv.EVENT_LBUTTONUP):
        img5 = img_copy.copy() #Copia de la copia de la imagen original.
    #imshow(): Se diferencía las ventanas que van a aparecer dependiendo del título que tengan, las que tengan en mismo título 
    #reemplazarán a la imstrucción anterior de imshow().
    cv.imshow('Color imagen - RGB', img5) #Ventana que tenga como título el 1er parametro y muestre la imagen del 2do

#CONFIGURACIÓN DE LA OPERACIÓN CON EL MOUSE:
#setMouseCallback(): Se utiliza esta función para que el mouse pueda interactuar con una ventana en específico, se manda a llamar 
#esta ventana poniendo el mismo nombre que usa en el título del método imshow() para mostrarla, además se indica la función que se 
#va a ejecutar con el mouse dentro de la ventana y si es necesario al final se indica dónde se almacena la data proveniente.
cv.setMouseCallback('Color imagen - RGB', color)
#NO DEJAR QUE SE CIERREN LAS VENTANAS: Las siguientes dos líneas de código sirven para que no se cierre la ventana.
cv.waitKey(0) #Mostrar la ventana hasta que se presione la tecla X
cv.destroyAllWindows() #Destruir todas las ventanas después de cerrarlas con el comando




#RECORTE DE REGIONES: Esta operación se realiza para hacer un recorte de una imagen de cierta región que se quiere analizar, ya 
#sea para analizar ojos, formas específicas, objetos de cierto color, etc.
#Para mostrar la parte que se va a recortar de la imagen con el mouse se debe mostrar un rectangulo rojo, en este primero que nada 
#se debe indicar sus propiedades guardadas en unas variables.
color_rectangulo = (0, 0, 255) #El color se guarda en una lista, recordemos que se maneja como BGR en OpenCV
grosor_rectangulo = 2 #Grosor del rectángulo en píxeles
ancho_min = 100 #Ancho mínimo en píxeles

img6 = cv.imread('0.-Img/Iron Man 3.jpg', 1) #Imagen RGB obtenida con el método imread()
#Se crea una copia de la imagen original para que cuando se modifique la imagen original, de donde se obtendrá la región que se 
#quiere extraer, y cuando ya no quiera que se vea esa modificación, debe haber una imagen que refresque la ventana y muestre la 
#imagen original, por eso es que se creó esta copia.
img_copy2 = img6.copy()

cv.imshow('Interfaz para recorte de imagen RGB', img6) #Ventana que tenga como título el 1er parametro y muestre la imagen del 2do

#Función para que cada que se de clic sobre la imagen, se obtenga el color de la parte en donde se dio clic, para ello se 
#debe recibir como parámetros: 
# - El evento del mouse: Este evento forma parte de los eventos descritos por la librería OpenCV.
# - Las coordenadas en x y y de la parte de la imagen donde se dió clic: Obtenidas de la imagen ya que esta es una matriz.
# - Bandera: Indica cuando ya se realizó el evento del mouse
# - Los parámetros: 
def region(evento, x, y, bandera, parametro):
    #Se declara dos variables x1 y y1 que almacenen las coordenadas de la imagen sean globales y una variable que se llame igual 
    #a la que almacena la imagen para que se pueda ver o alcanzar desde cualquier parte del código.
    global x1, y1, img6
    #El primer if reacciona cuando se presione el mouse, para que en conjunto los tres condicionales identifiquen cuando se deje 
    #presionado el mouse y se arrastre para seleccionar una parte de la imagen y de esta manera se seleccione lo que se quiere 
    #recortar de la imagen:
    # - EVENT_LBUTTONDOWN: Indica que el botón izquierdo del ratón está presionado.
    if (evento == cv.EVENT_LBUTTONDOWN):
        #Se asigna el valor de la parte donde se dió clic en la imagen a las variables globales x1 y y1
        x1, y1 = x, y
    #El condicional else if lo que hará es ver cuando el mouse esté presionado y moviéndose, esto se realiza analizando el evento 
    #de la función y la bandera, ambas indican algún evento del mouse y con ambas se pone la condición de refrescar la imagen.
    #El condicional else if lo que hará es refrescar varias veces la imagen y a su vez pintar el cuadrado que indica la parte que 
    #se quiere recortar de la imagen, para ello primero que nada se asigna a la variable de la imagen original una copia de la 
    #copia de la imagen para que se refresque lo que muestra la ventana y luego se crea el rectángulo.
    # -  EVENT_MOUSEMOVE: Evento que indica que el puntero del ratón se ha movido sobre la ventana.
    # -  EVENT_FLAG_LBUTTON: Bandera que indica que el botón izquierdo del ratón está presionado.
    elif ((evento == cv.EVENT_MOUSEMOVE) and (bandera == cv.EVENT_FLAG_LBUTTON)):
        img6 = img_copy2.copy() #Copia de la copia de la imagen original
        #cv.rectangle(): Con este método perteneciente a la librería OpenCV se puede crear un rectángulo, en él se indica primero 
        #en que imagen obtenida con el método imread() se va a dibujar la figura, luego las coordenadas iniciales x,y de la imagen 
        #en donde se va a dibujar la esquina superior izquierda del rectángulo, que en este caso son las coordenadas x1 y y1 en 
        #donde primero se presionó el mouse, seguido de las coordenadas x,y que son las actuales donde se está dando dejando 
        #presionado el clic y arrastrando el mouse, su color y si se quiere que sea hueco o sólido el rectángulo, si se buscara 
        #que fuera sólido se pondría un -1, si fuera hueco, en esta parte se indicaría el los pixeles del grosor del borde del 
        #rectángulo.
        cv.rectangle(img6, (x1, y1), (x, y), color_rectangulo, grosor_rectangulo)
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
            img_recorte = img_copy2[y1:y, x1:x]
            cv.imshow('Recorte imagen', img_recorte) #Ventana que tenga como título el 1er parametro y muestre la imagen del 2do
            #imwrite(): Método de la librería OpenCV que sirve para guardar una imagen, como primer parámetro tengo que poner el 
            #nombre con el que se guardará la imagen con todo y extensión y en el segundo debo poner la variable de la que extrae 
            #la imagen.
            cv.imwrite('Recorte_imagen.png', img_recorte)
    #imshow(): Se diferencía las ventanas que van a aparecer dependiendo del título que tengan, las que tengan en mismo título 
    #reemplazarán a la imstrucción anterior de imshow().
    cv.imshow('Interfaz para recorte de imagen RGB', img6) #Ventana que tenga como título el 1er parametro y muestre la imagen del 2do

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