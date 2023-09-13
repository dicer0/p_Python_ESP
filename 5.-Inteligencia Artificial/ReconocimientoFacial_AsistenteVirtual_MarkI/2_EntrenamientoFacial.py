#IMPORTACIÓN DE LIBRERÍAS:
import cv2      #Librería OpenCV: Sirve para todo tipo de operaciones de visión artificial
import os       #os: Librería que permite acceder a funciones y métodos relacionados con el sistema operativo.
import numpy as np #numpy: Librería que realiza operaciones matemáticas complejas.

#Este programa lo que hará es recibir el video de alguna persona que se quiera reconocer, luego de este video 
#extraerá varias fotos pequeñas de su rostro en distintos ángulos y así después se entrenará al programa para
#reconocer la cara de cada persona, ya que se haya llevado a cabo el reconocimiento facial se creará una 
#carpeta con su nombre, si se busca reconocer una persona nueva, solo se debe cargar otro video y cambiar el 
#nombre de la variable usuario para que cree una nueva carpeta de datos faciales.

#Creación de la ruta donde guardará el programa los datos faciales del usuario para que lo reconozca.
rutaUsuarios = "C:/Users/diego/OneDrive/Documents/The_MechaBible/p_Python_ESP/5.-Inteligencia Artificial/UsuariosReconocimientoFacial"
#os.listdir(): Método que extrae todos los nombres de los archivos y carpetas contenidos en un directorio.
dataUsuarios = os.listdir(rutaUsuarios)
print(dataUsuarios)
carasUsuarios = []
etiquetasCaras = []
etiquetaNumerica = 0

#Bucle for que recorre todas las imágenes de todos los usuarios que se encuentren en la carpeta de
#ReconocimientoFacial_AsistenteVirtual_MarkI, para ello se debió haber ejecutado mínimo una vez el archivo 
#1_DatosFaciales.py.
for persona in dataUsuarios:
    rutaPersona = rutaUsuarios + "/" + persona
    print("Leyendo la carpeta de un usuario")
    for imagenCara in os.listdir(rutaPersona):
        print("Caras: " + persona + "/" + imagenCara)
        #Asignación de un id o etiqueta numérica que después se relacionará a cada imagen de la cara del 
        #usuario. 
        etiquetasCaras.append(etiquetaNumerica)
        #imread(): Sirve para leer la imagen de un directorio especificado, si en el segundo parámetro se pone 
        #un 1, la imagen se obtendrá en forma de matriz 3D RGB y si se pone un 0 se obtendrá en escala de 
        #grises, obteniendo una matriz 2D.
        imgCara = cv2.imread(rutaPersona + "/" + imagenCara, 0)
        carasUsuarios.append(imgCara)
    etiquetaNumerica += 1

#cv2.face.LBPHFaceRecognizer_create(): Este método crea un objeto de reconocimiento de rostros utilizando el 
#algoritmo de reconocimiento de patrones basado en histogramas locales de patrones binarios (Local Binary 
#Patterns Histograms, LBPH) de OpenCV que se utiliza para reconocer caras en imágenes y luego crear un 
#histograma de patrones binarios, el cual será utilizado para identificar cada rostro una vez que haya sido 
#entrenado con un conjunto de imágenes etiquetadas de una cara en específico.
reconocimientoUsuario = cv2.face.LBPHFaceRecognizer_create()
print("Ingresando nuevo usuario al reconocimiento facial... bip bup...")
#cv2.face.LBPHFaceRecognizer_create().train(): Este método se utiliza para entrenar el objeto LBPH con un 
#conjunto de datos de entrenamiento que consiste en imágenes de rostros etiquetadas con un id correspondiente 
#a cada usuario. En su primer parámetro recibe una lista con los datos de las imágenes del entrenamiento y en
#el segundo un numpy array que contenga una lista de las etiquetas correspondientes a cada imagen.
reconocimientoUsuario.train(carasUsuarios, np.array(etiquetasCaras))

#cv2.face.LBPHFaceRecognizer_create().write(): Método que se utiliza para guardar un modelo de reconocimiento 
#de rostros previamente entrenado en un archivo con extensión XML, cuyo nombre y extensión se debe indicar 
#como su parámetro.
rutaModeloEntrenado = "C:/Users/diego/OneDrive/Documents/The_MechaBible/p_Python_ESP/5.-Inteligencia Artificial/ReconocimientoFacial_AsistenteVirtual_MarkI/modeloReconocimientoFacial.xml"
reconocimientoUsuario.write(rutaModeloEntrenado)
print("Modelo de reconocimiento facial entrenado y almacenado en un archivo xml...")