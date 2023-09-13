#IMPORTACIÓN DE LIBRERÍAS:
import cv2 #Librería OpenCV: Sirve para todo tipo de operaciones de visión artificial
import numpy as np #Librería numpy: Realiza operaciones matemáticas complejas

class visionArtificial():
    #__dibujarContorno(): Esta función propia se encargará de idenitificar los colores de las figuras que aparezcan 
    #en la cámara para posteriormente rodearlas con un contorno del color BGR (RGB volteado) indicado en su segundo 
    #parámetro.
    def __dibujarContorno(self, mascaraImg, color_contorno, frameContorno):
        #cv2.findContours(): Este método sirve para encontrar los contornos en una imagen, a este se le pasa como 
        #primer parámetro la imagen en escala de grises, después cabe mencionar que en las imágenes existen varios 
        #tipos de contornos y estos pueden tener jerarquías de dentro hacia fuera o pueden no tenerlas, esto depende 
        #del segundo parámetro que se le pase al método, en este caso vamos a utilizar el parámetro cv2.RETR_EXTERNAL 
        #para que muestre solo los bordes externos que encuentre, luego se le debe indicar en el tercer parámetro la 
        #forma en la que se va a guardar la información recabada, ya que puede guardar todos los puntos del contorno 
        #identificado o solo guardar los puntos de las esquinas que conforman el contorno, para que guarde todos los 
        #puntos de los contornos se usa el atributo cv2.CHAIN_APPROX_NONE, pero si se busca guardar solo sus esquinas 
        #se usa el atributo cv2.CHAIN_APPROX_SIMPLE.
        contornos, _ = cv2.findContours(mascaraImg, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        #Bucle for que recorre todas las líneas de los contornos para calcular el área del objeto.
        for lineas in contornos:
            #cv2.contourArea(): Método que permite definir el área de una figura en función se su contorno.
            area = cv2.contourArea(lineas)
            #Con este condicional se filtran las figuras pequeñas que se pueden detectar, para que solo detecte las 
            #grandes.
            if(area > 1500):
                #cv2.convexHull(): Método que filtra un poco el borde de la imagen para reducir su ruido.
                contornoFigGrande = cv2.convexHull(lineas)
                #cv2.drawContours(): Método que sirve para dibujar los contornos recabados con el método 
                #cv2.findContours(), para ello primero se debe indicar en qué imagen o frame se va a dibujar el 
                #contorno, no debe ser el mismo de donde se obtuvieron los contornos, después se indica en el 
                #segundo parámetro la variable en donde están almacenados los contornos, en el tercer parámero se 
                #establece si se quiere que el contorno sea hueco o sólido, como se busca que sea sólido se pone -1, 
                #si fuera hueco, en esta parte se indicarían los pixeles del perímetro (borde) del contorno, 
                #posteriormente se indica el color y finalmente los contornos que quiero que muestre.
                cv2.drawContours(frameContorno, [contornoFigGrande], 0, color_contorno, 3)
                #cv.moments(): Método que permite obtener el centroide de la figura rodeada por un contorno.
                momentoCentroide = cv2.moments(lineas)
                if (momentoCentroide["m00"] == 0):
                    momentoCentroide["m00"] == 1
                centroide_x = int(momentoCentroide["m10"]/momentoCentroide["m00"])
                centroide_y = int(momentoCentroide["m01"]/momentoCentroide["m00"])
                tipoLetra = cv2.FONT_HERSHEY_COMPLEX    #Tipo de letra sans-serif del texto que indica el color.
                if (color_contorno == [0, 255, 255]):
                    #cv2.putText(): Método utilizado para agregar texto a una imagen o un fotograma de video, para 
                    #ello recibe como parámetros la imagen donde se quiere colocar, el texto, las coordenadas donde 
                    #se posicionará, el tipo de letra, la escala de su tamaño, su color, grosor, y tipo de línea para 
                    #dibujar las letras, que usualmente es el cv2.LINE_AA.
                    cv2.putText(frameContorno, "Amarillo", (centroide_x + 10, centroide_y), tipoLetra, 0.75, (0, 255, 255), 1, cv2.LINE_AA)
                elif (color_contorno == [0, 0, 255]):
                    cv2.putText(frameContorno, "Rojo", (centroide_x + 10, centroide_y), tipoLetra, 0.75, (0, 0, 255), 1, cv2.LINE_AA)
                elif (color_contorno == [255, 0, 0]):
                    cv2.putText(frameContorno, "Azul", (centroide_x + 10, centroide_y), tipoLetra, 0.75, (0, 0, 255), 1, cv2.LINE_AA)
                elif (color_contorno == [0, 255, 0]):
                    cv2.putText(frameContorno, "Verde", (centroide_x + 10, centroide_y), tipoLetra, 0.75, (0, 0, 255), 1, cv2.LINE_AA)


    #reconocerColoresVideo(): Esta función utiliza el método __dibujarContorno() para que por medio de ciertas 
    #máscaras que identifican ciertos colores en el video con formato HSV se rodee las figuras que detecten dicho 
    #color en la cámara.
    def reconocerColoresVideo(self):
        #DECLARACIÓN DE COLORES CON GAMA HSV:
        #La mejor manera de detectar los colores en una imagen o video es a través del código de color HSV (Hue, 
        #Saturation y View), ya que este no solo considera el color sino su intensidad, luz, etc.
        # -	Hue = Matiz: Representa todos los tonos de colores y abarca valores de 0 a 180.
        # -	Saturation = Saturación: Representa la intensidad del color y abarca valores de 0 a 255.
        # -	View = Valor: Representa la luz y abarca valores también de 0 a 255.
        #En la gráfica incluida en el documento 9.-Asistente Virtual - SpeechRecognition, Whisper y LangChain se 
        #muestra los colores que se pueden abarcar variando el Matiz (Hue) corresponde al eje x y la Saturación 
        #(Saturation) correspodiente al eje y, el cual aumenta su valor de arriba hacia abajo.
        amarillo_Obscuro = np.array([20, 190, 20], np.uint8)
        amarillo_Claro = np.array([30, 255, 255], np.uint8)

        rojo_Obscuro_Izq = np.array([0, 100, 20], np.uint8)
        rojo_Claro_Izq = np.array([5, 255, 255], np.uint8)
        rojo_Obscuro_Der = np.array([175, 100, 20], np.uint8)
        rojo_Claro_Der = np.array([180, 255, 255], np.uint8)

        azul_Obscuro = np.array([85, 200, 20], np.uint8)
        azul_Claro = np.array([125, 255, 255], np.uint8)

        verde_Obscuro = np.array([45, 100, 20], np.uint8)
        verde_Claro = np.array([75, 255, 255], np.uint8)

        #cv2.VideoCapture(): Método de python para acceder a la webcam, como parámetro solo se enlista el número de 
        #webcams a las que se quiere acceder, empezando a contar desde el índice 0, 1, 2, etc. O se le puede pasar 
        #entre comillas la ruta de un video para que lo reproduzca.
        camara = cv2.VideoCapture(0)

        #.isOpened(): Método que se aplica a un objeto de OpenCV que haya abierto una webcam, este identifica si la 
        #ventana de la webcam está abierta o no, para que se realice el análisis de la imagen en el video.
        if not camara.isOpened():
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
            ret, frame = camara.read()
            #Condicional que se ejecuta cuando no se pudo obtener un fotograma.
            if not ret:
                print("No es posible obtener la imagen")
                break
            else:
                #OBTENCIÓN DE COLORES HSV:
                #cvtColor(): Método de la librería OpenCV que recibe como primer parámetro una imagen RGB y en su 
                #segundo parámetro recibe un atributo de OpenCV llamado cv2.COLOR_BGR2HSV para convertir una imagen 
                #RGB a su formato de colores HSV.
                frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
                #cv2.inRange(): Este método sirve para umbralizar una imagen hsv, en ella se le pasa como primer 
                #parámetro la imagen en colores hsv que se va a umbralizar, a continuación se indica el valor mínimo 
                #y máximo que puede alcanzar el umbral.
                mascaraAmarilla = cv2.inRange(frameHSV, amarillo_Obscuro, amarillo_Claro)

                mascaraRojaIzq = cv2.inRange(frameHSV, rojo_Obscuro_Izq, rojo_Claro_Izq)
                mascaraRojaDer = cv2.inRange(frameHSV, rojo_Obscuro_Der, rojo_Claro_Der)
                mascaraRoja = cv2.add(mascaraRojaIzq, mascaraRojaDer)

                mascaraAzul = cv2.inRange(frameHSV, azul_Obscuro, azul_Claro)

                mascaraVerde = cv2.inRange(frameHSV, verde_Obscuro, verde_Claro)

                #__dibujarContorno(): Esta función propia recibe dos parámetros, el primero es la máscara del color 
                #que identificará y el segundo es un array que representa un color BGR para que pinte el contorno de 
                #ese color, BGR es lo mismo que RGB pero al revés. 
                self.__dibujarContorno(mascaraAmarilla, [0, 255, 255], frame)
                self.__dibujarContorno(mascaraRoja, [0, 0, 255], frame)
                self.__dibujarContorno(mascaraAzul, [255, 0, 0], frame)
                self.__dibujarContorno(mascaraVerde, [0, 255, 0], frame)

                #imshow(): Con el método se puede mostrar una ventana con una imagen o video, el primer parámetro es 
                #el nombre de la ventana donde aparecerá la imagen o video y el segundo parámetro es la imagen 
                #recopilada con el método cv2.imread() o el video recopilado con el método .read() aplicado a un 
                #video con el método cv2.VideoCapture().
                cv2.imshow('Reconocimiento colores', frame)

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
                if cv2.waitKey(1) == ord('c'): #Se cierra el programa cuando se presione la letra q
                    #cv2.VideoCapture().release(): Con este método se libera la webcam, tanto en software como en 
                    #hardware.
                    camara.release()
                    #destroyAllWindows(): Función que permite a los usuarios destruir todas las ventanas en 
                    #cualquier momento. No toma ningún parámetro y no devuelve nada, esto se incluye para que al 
                    #cerrar la ventana después del método waitKey() se destruyan para poder utilizarse en otra cosa.
                    cv2.destroyAllWindows()
                    break