#IMPORTACIÓN DE LIBRERÍAS:
import cv2          #Librería OpenCV: Sirve para todo tipo de operaciones de visión artificial
import os           #os: Librería que permite acceder a métodos relacionados con el sistema operativo (so).
#threading: Librería que permite crear y gestionar los hilos (threads) de un programa. Los hilos son subprocesos 
#que le permiten a un programa realizar múltiples tareas al mismo tiempo, esto se añade debido a la clase de 
#visión artificial, ya que si esto no se añade, el asistente virtual detendrá su ejecución mientras se ejecuta 
#la clase visionArtificialAsistente.
import threading
import pygame       #pygame: librería de multimedia que permite mostrar gráficos, reproducir sonido, etc.
import subprocess   #subprocess: Librería que se usa para interactuar con el so, ejecutar programas externos, etc.
import winsound     #winsound: Biblioteca para reproducir sonidos utilizando el sistema operativo Windows. 

#pygame.mixer.init(): El método init() inicializa el objeto mixer de la librería pygame que sirve para reproducir 
#sonidos con Python.
pygame.mixer.init()
rutaDatosFaciales = "C:/Users/diego/OneDrive/Documents/The_MechaBible/p_Python_ESP/5.-Inteligencia Artificial/UsuariosReconocimientoFacial"
#os.listdir(): Método que extrae todos los nombres de los archivos y carpetas contenidos en un directorio.
dataImagenesUsuarios = os.listdir(rutaDatosFaciales)

#cv2.face.LBPHFaceRecognizer_create(): Este método crea un objeto de reconocimiento de rostros utilizando el 
#algoritmo de reconocimiento de patrones basado en histogramas locales de patrones binarios (Local Binary 
#Patterns Histograms, LBPH) de OpenCV que se utiliza para reconocer caras en imágenes y luego crear un 
#histograma de patrones binarios, el cual será utilizado para identificar cada rostro una vez que haya sido 
#entrenado con un conjunto de imágenes etiquetadas de una cara en específico.
reconocimientoFacial = cv2.face.LBPHFaceRecognizer_create()
#cv2.face.LBPHFaceRecognizer_create().read(): El método read() se utiliza para leer un modelo preentrenado 
#con datos faciales, para así reconocer cierto rostro. Los datos del modelo se obtuvieron al analizar un 
#video del usuario a través del archivo 1_DatosFaciales.py y se entrenó con el programa 2_EntrenamientoFacial.py
reconocimientoFacial.read("C:/Users/diego/OneDrive/Documents/The_MechaBible/p_Python_ESP/5.-Inteligencia Artificial/ReconocimientoFacial_AsistenteVirtual_MarkI/modeloReconocimientoFacial.xml")

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

class machineLearning():
    def reconocimientoFacial(self, estado):
        #cv2.VideoCapture(): Método de python para acceder a la webcam, como parámetro solo se enlista el número 
        #de webcams a las que se quiere acceder, empezando a contar desde el índice 0, 1, 2, etc. O se le puede 
        #pasar entre comillas la ruta de un video para que lo reproduzca.
        camara = cv2.VideoCapture(0)

        while True:
            #.isOpened(): Método que se aplica a un objeto de OpenCV que haya abierto una webcam, este identifica 
            #si la ventana de la webcam está abierta o no, para que se realice el análisis de la imagen en el 
            #video.
            if not camara.isOpened():
                #Mensaje que se imprimirá en consola cuando no se pueda abrir la webcam del ordenador.
                print("No es posible abrir la cámara")
                exit()
            #Bucle while: Cuando se analice un video, se debe realizar dentro de un bucle while para que se 
            #ejecute hasta que la ventana donde se muestra el video se cierre.
            while True:
                #.read(): Método que se aplica a un objeto de OpenCV que haya abierto una webcam, este método 
                #obtiene dos resultados: 
                # - ret: Variable booleana que puede ser true si hay un video (fotograma) capturado y false si no 
                #   hay fotograma que leer, este se usa más que nada para crear un if cuando se quiere leer un 
                #   video ya existente en vez de grabar y mostrar uno nuevo o si se quiere asegurar que la webcam 
                #   está grabando.
                # - frame: La variable frame devuelve todas las imágenes del video capturado.
                ret, frame = camara.read()
                #Condicional que se ejecuta cuando no se pudo obtener un fotograma.
                if not ret:
                    print("No es posible obtener la imagen")
                    break
                else:
                    #OBTENCIÓN DE COLORES HSV:
                    #cvtColor(): Método de la librería OpenCV que recibe como primer parámetro una imagen RGB y 
                    #en su segundo parámetro recibe un atributo de OpenCV llamado cv2.COLOR_BGR2HSV para 
                    #convertir una imagen RGB a su formato de colores HSV o cv2.COLOR_BGR2GRAY para obtener su 
                    #escala de grises.
                    imgEscalaGrises = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                    #copy(): Método que crea una copia de la imagen.
                    imagenAuxiliar = imgEscalaGrises.copy()

                    #objetoCascadeClassifier.detectMultiScale(): Con este método se accede a la base de datos de 
                    #reconocimiento facial de OpenCV para el reconocimiento de rostros, a este se le pasa como 
                    #parámetro la imagen que se quiere analizar, pero antes se debió haber obtenido la escala de 
                    #grises de la imagen y jalado con el método cv.CascadeClassifier() la base de datos de 
                    #reconocimiento de rostros, después para mejorar la detección de rostros se puede indicar un 
                    #factor de escala que se encargue de reducir el tamaño de la imagen en cada búsqueda durante 
                    #la detección de caras y finalmente el mínimo número de vecinos para que una región sea 
                    #considerada una detección válida, donde un valor más alto requiere que más comprobaciones 
                    #correctas para ser tomada en cuenta como una detección correcta. Esto ayuda a eliminar 
                    #detecciones falsas.
                    caras = clasificacionFacial.detectMultiScale(imgEscalaGrises, 1.3, 5)

                    #Bucle for que dibuja un rectángulo alrededor del rostro identificado, para ello debe 
                    #reconocer el ancho y alto del rostro.
                    color_rectangulo = (176, 224, 17) #El vector de color BGR se guarda en una lista.
                    grosor_rectangulo = 2 #Grosor del rectángulo en píxeles
                    for (x, y, ancho, altura) in caras:
                        #Recordemos que la imagen en realidad es una matriz, entonces para acceder a solo una 
                        #parte de ella, se indica que de la matriz, osea del numpy array, solo se tome un rango 
                        #de valores que vayan desde x hasta ancho en la parte horizontal de las 3 capas y de las 
                        #coordenadas y hasta altura en la parte vertical de las 3 capas que conforman la imagen 
                        #digital. 
                        cara = imagenAuxiliar[y:y + altura, x:x + ancho]
                        #resize(): Lo que hace este método es cambiar el tamaño de una imagen, para ello recibe 
                        #como primer parámetro la variable que almacena la imagen y como segundo parámetro indica 
                        #la magnitud de la nueva imagen, como segundo parámetro se le da un nuevo tamaño de 
                        #150x150 pixeles y finalmente el parámetro opcional interpolation sirve para ajustar los 
                        #valores de píxeles en la matriz de la nueva imagen para que no se pierda su calidad y 
                        #esencia.
                        cara = cv2.resize(cara, (150, 150), interpolation = cv2.INTER_CUBIC)
                        #cv2.face.LBPHFaceRecognizer_create().read().predict(): El método predict() que se aplica 
                        #al objeto de reconocimiento facial LBPH (Local Binary Patterns Histograms) y previamente 
                        #ha sido alimentado con el modelo de reconocimiento facial de un archivo xml propio, 
                        #sirve para analizar el fotograma (imagen del video) captado y de esta forma identificar 
                        #si el rostro es el del usuario a través de un rango que puede adoptar valores de 0 a 80 
                        #cuando si se reconozca el rostro del usuario, si no se reconoce el valor será mayor a 80.
                        resultadoFacial = reconocimientoFacial.predict(cara)
                        print("Resultado de reconocimiento facial:\n" + str(resultadoFacial))
                        
                        #cv2.putText(): Método utilizado para agregar texto a una imagen o un fotograma de video, 
                        #para ello recibe como parámetros la imagen donde se quiere colocar, el texto, las 
                        #coordenadas donde se posicionará, el tipo de letra, la escala de su tamaño, su color, 
                        #grosor, y tipo de línea para dibujar las letras, que usualmente es el cv2.LINE_AA.
                        tipoLetra = cv2.FONT_HERSHEY_PLAIN    #Tipo de letra que indica el nombre del usuario.
                        cv2.putText(frame, f"{resultadoFacial}", (x, y-5), tipoLetra, 1.1, (0, 0, 200), 1, cv2.LINE_AA)

                        #Si el resultado del reconocimiento facial se encuentra entre 0 y 80 el rostro fue 
                        #identificado, pero si su resultado es mayor a 80, significa que el rostro no fue 
                        #reconocido.
                        if (resultadoFacial[1] < 85):
                            #Para extraer el nombre del usuario se recorrerá el directorio que contiene las 
                            #imágenes de reconocimiento facial, ya que al crear esas carpetas, a través de la 
                            #variable usuario se indicó su nombre y este se reconoce con el valor del 
                            #identificador del resultadoFacial porque está asociado de igual manera a los id de 
                            #sus datos.
                            cv2.putText(frame, f"{dataImagenesUsuarios[resultadoFacial[0]]}", (x, y-25), tipoLetra, 2, (200, 200, 200), 1, cv2.LINE_AA)
                            #cv.rectangle(): Con este método perteneciente a la librería OpenCV se puede crear un 
                            #rectángulo, en él se indica primero en que imagen se va a dibujar la figura, luego 
                            #las coordenadas iniciales x,y de la imagen en donde se va a dibujar la esquina 
                            #superior izquierda del rectángulo, seguido de las coordenadas x2,y2 que consideran 
                            #el tamaño de la imagen, su color y si se quiere que sea hueco o sólido el rectángulo, 
                            #si se buscara que fuera sólido se pondría un -1, si fuera hueco, en esta parte se 
                            #indicaría el grosor del borde del rectángulo en pixeles.
                            cv2.rectangle(frame, (x, y), (x + ancho, y + altura), color_rectangulo, grosor_rectangulo)
                        else:
                            #Si no se reconoció al usuario, se hará sonar una alarma y se pondrá el texto de 
                            #usuario desconocido en la imagen del video, además de que se pintará de igual manera 
                            #un rectángulo que rodee su rostro. 
                            cv2.putText(frame, "Usuario desconocido", (x, y-20), tipoLetra, 1.1, (0, 0, 255), 1, cv2.LINE_AA)
                            cv2.rectangle(frame, (x, y), (x + ancho, y + altura), (0, 0, 255), 4)
                    
                    #imshow(): Con el método se puede mostrar una imagen, el primer parámetro es el nombre de la 
                    #ventana donde aparecerá la imagen y el segundo parámetro es la imagen recopilada.
                    cv2.imshow('Reconocimiento facial', frame)
                    #waitKey(): Método que permite a los usuarios mostrar una ventana durante un número de 
                    #milisegundos determinados si su parámetro es un número mayor a 1 o hasta que se presione 
                    #cualquier tecla. Toma un tiempo en milisegundos como parámetro y espera el tiempo dado para 
                    #destruir la ventana: 
                    # - Si se pasa 0 como argumento, espera hasta que se presiona cualquier tecla.
                    # - Si se pasa 1 como argumento, espera hasta que se presione una tecla específica para 
                    #   cerrar la ventana.
                    #El método waitKey() está monitoreando si se presiona una tecla o no, este modo se activa si 
                    #se le pasa como parámetro un número 1, de esta manera:
                    # - Si no se presiona una tecla retorna un valor -1 (False). 
                    # - Si se presiona una tecla, retorna un valor ASCII correspondiente a la tecla que se 
                    #   oprimió, con el método ord() podemos indicar el código ASCII de la letra del teclado que 
                    #   indiquemos en su parámetro o simplemente en un condicional un valor diferente a -1 o 0 
                    #   se considera como True.
                    #Se cierra el programa cuando se presione cualquier tecla y el valor de estado sea 1.
                    if (cv2.waitKey(1) == ord('r')) or (estado == 1):
                        #cv2.VideoCapture().release(): Con este método se libera la webcam, tanto en software 
                        #como en hardware.
                        camara.release()
                        #destroyAllWindows(): Función que permite a los usuarios destruir todas las ventanas en 
                        #cualquier momento. No toma ningún parámetro y no devuelve nada, esto se incluye para que 
                        #al cerrar la ventana después del método waitKey() se destruyan para poder utilizarse en 
                        #otra cosa.
                        cv2.destroyAllWindows()
                        break

olis = machineLearning()
olis.reconocimientoFacial(0)