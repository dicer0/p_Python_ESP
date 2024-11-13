# -*- coding: utf-8 -*-

#En Python se introducen comentarios de una sola linea con el simbolo #.
#La primera línea de código incluida en este programa se conoce como declaración de codificación o codificación 
#de caracteres. Al especificar utf-8 (caracteres Unicode) como la codificación, nos aseguramos de que el archivo 
#pueda contener caracteres especiales, letras acentuadas y otros caracteres no ASCII sin problemas, garantizando 
#que Python interprete correctamente esos caracteres y evite posibles errores de codificación.
#Se puede detener una ejecución con el comando [CTRL] + C puesto en consola, con el comando "cls" se borra su 
#historial y en Visual Studio Code con el botón superior derecho de Play se corre el programa.
#Para comentar en Visual Studio Code varias líneas de código se debe pulsar:
#[CTRL] + K (VSCode queda a la espera). Después pulsa [CTRL] + C para comentar y [CTRL] + U para descomentar.

#GRAFICACIÓN MÚLTIPLE MATRICIAL CON MATPLOTLIB:
import matplotlib.pyplot as plt #matplotlib: Librería de graficación matemática.
import numpy as np #numpy: Librería que realiza operaciones matemáticas complejas (matriciales).

#ABRIR y LEER UN ARCHIVO:
#Para leer una imagen o cualquier otro archivo se usa la dirección relativa o absoluta de un directorio: 
# - Dirección relativa: Es una dirección que busca un archivo desde donde se encuentra la carpeta del 
#   archivo python actualmente, esta se debe colocar entre comillas simples o dobles.
# - Dirección absoluta: Es una dirección que coloca toda la ruta desde el disco duro C o cualquier otro 
#   que se esté usando hasta la ubicación del archivo, la cual se debe colocar entre comillas simples o 
#   dobles.
#   ..      : Significa que nos debemos salir de la carpeta donde nos encontramos actualmente.
#   /       : Sirve para introducirnos a alguna carpeta cuyo nombre se coloca después del slash.
#   .ext    : Se debe colocar siempre el nombre del archivo + su extensión.
#Es un archivo de Excel el que se va a crear, por eso tiene extensión .csv
filename = "C:/Users/diego/OneDrive/Documents/The_MechaBible/p_Python_ESP/a1.-Data Science/0.-Archivos_Ejercicios_Python/a16.-Graficación Matricial Múltiple/Datos2.csv"#Nombre del archivo a abrir
#open(): Método que sirve para abrir un archivo cualquiera, para ello es necesario indicar dos parámetros, 
#el primero se refiere a la ruta relativa o absoluta del archivo previamente creado y la segunda indica qué 
#es lo que se va a realizar con él, el contenido del archivo se asigna a una variable.
#   - w: Sirve para escribir en un archivo, pero borrará la información que previamente contenía el archivo.
#   - a: Sirve para escribir en un archivo sin que se borre la info anterior del archivo, se llama append.
#   - r: Sirve para leer el contenido de un archivo.
new_file = open(filename, 'r') #Variable que guarda los datos que lea en el archivo de Excel.
#Los datos que están relacionados entre sí, se encuentran acomodados en forma de columna, pero el programa 
#lo que hará es leer todas las filas de una en una para así crear una matriz de datos, esta matriz se irá 
#guardando en la variable text.
text = ''
#Cada que se termine de leer una fila del archivo, se añadirá un valor a la variable rowsNumber, ya que esta 
#indica cuántas filas existen en la matriz, para así después acomodar y relacionar todos los datos de una 
#columna entre sí.
rowsNumber = 0
#La variable mat1 es una lista (array de python) vacía para guardar temporalmente todos los datos 
#correspondientes a las distintas filas de la matriz creada con los datos de la matriz new_file extraída del 
#archivo Excel, para así poder después transponer esta matriz y relacionar los datos entre sus columnas, para 
#de esta forma exponer varias gráficas a través de una sola matriz en un solo figure.
#La primera columna de la matriz mat1 corresponde al eje x de todas las demás columnas.
mat1 = []

#Bucle for each para ir guardando temporalmente en la variable mat1 los datos de las columnas pertenecientes 
#a la matriz de la variable new_file, extraídos del archivo de Excel.
for line in new_file:
    #De esta forma se agrega a la variable text de tipo String el contenido de la fila de datos.
    text += line
    #replace(): Método que reemplaza un caracter que se encuentra en un string por otro declarado por nosotros, 
    #esto se ejecutará todas las veces que dicho caracter aparezca en el string.
    line = line.replace("\n", "") #Va a reemplazar los saltos de línea por un string vacío.
    line = line.replace(" ", "") #Quita los espacios por un string vacío.
    
    #find(): El método find devuelve el índice de la lista en donde se encuentre solamente el que primer caracter 
    #indicado como su parámetro y si este no se encuentra en ningún lado, devuelve un -1.
    if(line.find(',')!=-1):
        #append(): Lo que hace es agregar un elemento a la lista (array de python).
        #split(): Método que crea una lista interna nueva en el index de la lista actual donde nos encontramos, 
        #esto sucederá cuando se encuentre el caracter indicado como parámetro, creando así una lista interna 
        #en cada una de las posiciones de la lista principal con los elementos que estén separados entre comas.
        mat1.append(line.split(',')) #Al encontrar una coma que separe los datos, se agrega una lista interna.
    if(line.find('\t')!=-1):
        mat1.append(line.split('\t')) #Al encontrar un tabulador que separe los datos, se agrega una lista interna.
    
    rowsNumber+=1 #Al terminar de analizar la fila de datos, se agrega un número a la variable rowsNumber.
    #print(): Imprimir un mensaje en consola.
    print("Fila número", rowsNumber, "extraída del archivo de Excel: ", "\n", line)

print("Matriz de filas extraídas del Archivo de Excel", "\n", mat1)
#var_file_open.close(): Método para cerrar un archivo previamente abrierto con el método open(), es peligroso 
#olvidar colocar este método, ya que la computadora lo considerará como si nunca hubiera sido cerrado, por lo 
#cual no podré volver a abrirlo al dar clic sobre él.
new_file.close()

#El número de columnas será igual al número de elementos en cualquiera de las filas de los datos, recordemos que 
#en cada una de las posiciones (index) de la variable mat1 existe una lista interna con los datos de cada una de 
#las filas de la matriz de datos extraídas del archivo Excel.
#len(): Método que devuelve el número de elementos que tiene una lista (array de python).
columnsNumber = len(mat1[0])



#MATRIZ TRANSPUESTA: Se debe obtener la transpuesta de los datos extraídos porque siempre de los archivos de Excel 
#estos son extraídos de forma vertical y los necesitamos de forma horizontal para que puedan ser graficados con 
#python.
#np.asarray(): Convierte cualquier tipo de dato que pueda ser convertido en un array en un ndarray, que es un 
#tipo de dato perteneciente a la librería numpy de Python.
data = np.asarray(mat1, dtype=float)
#ndarray.T: Método que obtiene el transpuesto de un ndarray, que pudo ser previamente obtenido con el método 
#np.asarray().
data = data.T #Transpuesta de la matriz previamente obtenida en la variable mat1. 
print("Matriz transpuesta de datos extraídos del Archivo de Excel", "\n",data)



#GRAFICAR LOS DATOS EN PYTHON: La primera columna de la data corresponde al eje x de todas las demás columnas.
#matplotlib.figure(): Método usado para crear la ventana de graficación (objeto pyplot).
fig = plt.figure()#Creación del objeto pyplot
#matplotlib.axes(): Método usado para crear la rejilla en la ventana de graficación.
ax = plt.axes()#Se crea un objeto ax perteneciente de la clase axes() 
#Bucle for para graficar las distintas gráficas descritas por una matriz.
for i in range(1, columnsNumber):
    #axes.plot(): Método usado para crear la gráfica en la rejilla previamente creada en la ventana de graficación, 
    #indicando como primer parámetro su eje horizontal, luego su eje vertical y finalmente el estilo de la gráfica:
    # - Colores:                C1: color naranja, r: color rojo, b: color azul, g: verde, c: cyan, m: morado, 
    #   y: amarillo, k: negro, w: blanco.
    # - Colores: xkcd:aqua, xkcd:aquamarine, xkcd:azure, xkcd:beige, etc. Los colores se pueden obtener de este link:
        #https://matplotlib.org/stable/tutorials/colors/colors.html
    # - Tipo de marcadores:     o: círculos, +: símbolos de más, .; puntos, v: Triángulo hacia abajo, h: Hexágono, 
    #   etc.
    # - Tipo de Líneas:         -: sólida, --: punteada (líneas), :: punteada (puntos), -.: línea y punto, 
    #   'or': Nada.
    ax.plot(data[0], data[i], 'r.-')#'c.-' significa C1: color cyan, .: simbolo de punto -: línea sólida.
     #Si se quiere, se puede indicar un estilo específico para alguno de los gráficos con un if, en este caso se 
     #está dando un estilo diferente a la primera gráfica, la de en medio y la última.
    if(i == 1):                     #Primera gráfica, que no es i = 0, porque esa posición corresponde al eje x.
        ax.plot(data[0], data[i], 'bv:')#'bv:' significa b: color azul, v: simbolo de triángulos hacia abajo :: línea punteada.
    if(i == round(len(data)/2)):    #Gráfica de en medio
        ax.plot(data[0], data[i], 'gh-.')#'bv:' significa b: color azul, v: simbolo de triángulos hacia abajo :: línea punteada.
    if(i == len(data)-1):           #Última gráfica
        ax.plot(data[0], data[i], 'cs--')#'bv:' significa b: color azul, v: simbolo de triángulos hacia abajo :: línea punteada.
    #axes.set_xlabel(): Método para indicar el texto que aparece en el eje x.
    ax.set_xlabel(r'$tiempo (segundos)$') #Texto que aparece en el eje horizontal
    #axes.set_ylabel(): Método para indicar el texto que aparece en el eje y.
    ax.set_ylabel(r'$Amplitud (unidades arbitrarias)$') #Texto que aparece en el eje vertical
#matplotlib.show(): Método para mostrar la gráfica creada.
plt.show()