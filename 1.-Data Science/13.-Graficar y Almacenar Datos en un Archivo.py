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


#VECTOR X^2 HECHO CON DOS BUCLES FOR Y UNA FUNCIÓN (LISTAS DE COMPRENSIÓN):
#Función f(x) = x^2
def f(x):
    return x**2
#Las listas en Python pueden ser usadas como vector.
#Declaración de un vector que represente los valores del eje x, de 0 a 10, el último valor del bucle no es 
#alcanzado.
x_l_c = [i for i in range (11)]
#Declaración de un vector que represente los valores del eje y, usando los valores del eje x, yendo igual de 
#0 a 10 pero elevando dichos valores al cuadrado.
y_l_c = [f(x_l_c[i]) for i in range (11)]
#LISTAS DE COMPRENSIÓN: Las listas de comprensión son listas que se crean por medio de ciclos for pero que se 
#declaran dentro de la misma lista, el problema de usar este método es que si no sabemos si los datos están bien 
#organizados o si pueden venir de varios tipos de datos, algunos numéricos, algunos strings y así, puede ocurrir 
#un error en la recopilación de datos, por lo que es mejor entonces usar el método tradicional en esos casos.
print("El vector horizontal creado con lista es: \n", x_l_c)
print("El vector vertical creado con lista es: \n", y_l_c)



#VECTOR X^2 HECHO CON UNA FUNCIÓN Y UN BUCLE FOR (MÉTODO TRADICIONAL):
#Función f(x) = x^2
def f(x):
    return x**2
#Método tradicional (listas)
x_lista = []
y_lista = []
for i in range(11):
    x_lista.append(i)
    y_lista.append(f(i))
#Arreglo hecho con método tradicional, que es más útil para cuando no sabemos la estructura en la que se reciben 
#los datos.
print("El vector horizontal creado con método tradicional es: \n", x_lista)
print("El vector vertical creado con el método tradicional es: \n", y_lista)



#VECTOR X^2 HECHO CON ARREGLOS PERTENECIENTES A LA LIBRERÍA NUMPY:
import numpy as np #numpy: Librería que realiza operaciones matemáticas complejas (matriciales).
#arange(inicio, final, paso): Método que sirve para indicarle al vector de donde empieza, de cuanto en cuanto 
#avanza y en donde termina:
x_np = np.arange(0, 11, 1) #El dato se llama numpy array, es distinto a las listas
y_np_v1 = f(x_np)
y_np_v2 = (x_np)**2 #Vectorizado: No utiliza bucles sino que se hace operación directa con vectores
#Arreglo hecho con el objeto numpy array, que es perteneciente a la librería numpy.
print("El vector horizontal creado con numpy es: \n", x_np)
print("El vector vertical creado con numpy versión 1 es: \n", y_np_v1)
print("El vector vertical creado con numpy versión 2 es: \n", y_np_v2)



#ABRIR y ESCRIBIR EN UN ARCHIVO:
#Variable que guarda el directorio y nombre del archivo deseado, se deben reemplazar los guiones\ por /
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
nombreArchivo = "0.-Archivos_Ejercicios_Python/13.-Graficar y Almacenar Datos en un Archivo/DatosXY.csv"
#open(): Método que sirve para abrir un archivo cualquiera, para ello es necesario indicar dos parámetros, 
#el primero se refiere a la ruta relativa o absoluta del archivo previamente creado y la segunda indica qué 
#es lo que se va a realizar con él, el contenido del archivo se asigna a una variable.
#   - w: Sirve para escribir en un archivo, pero borrará la información que previamente contenía el archivo.
#   - a: Sirve para escribir en un archivo sin que se borre la info anterior del archivo, se llama append.
nuevo_archivo = open(nombreArchivo, 'w')
#var_file_open.write(): Método para colocar un string en un archivo previamente abrierto con el método open().
#str(): Lo que hace el método es convertir cada elemento de la lista a un string, esto es porque el método
#write no permite escribir datos de otro tipo en un archivo.
#Se concatenan los datos de un string por medio del símbolo + y poniendo los strings concatenados entre comillas.
for i in range(len(x_lista)):
    nuevo_archivo.write(str(x_lista[i])+","+str(y_lista[i])+"\n")
#var_file_open.close(): Método para cerrar un archivo previamente abrierto con el método open(), es peligroso 
#olvidar colocar este método, ya que la computadora lo considerará como si nunca hubiera sido cerrado, por lo 
#cual no podré volver a abrirlo al dar clic sobre él.
nuevo_archivo.close()



#ABRIR y LEER UN ARCHIVO:
#open(): Método que sirve para abrir un archivo cualquiera, para ello es necesario indicar dos parámetros, 
#el primero se refiere a la ruta relativa o absoluta del archivo previamente creado y la segunda indica qué 
#es lo que se va a realizar con él, el contenido del archivo se asigna a una variable.
#   - r: Sirve para leer el contenido de un archivo.
#Es importante mencionar que no se podrá abrir el archivo si este se encuentra abierto por otro programa.
archivo_lectura = open(nombreArchivo, 'r')
data_str = [] #declaración de una lista
for linea in archivo_lectura:
    #replace(): Método que reemplaza un caracter que se encuentra en un string por otro declarado por nosotros, 
    #esto se ejecutará todas las veces que dicho caracter aparezca en el string.
    linea = linea.replace("\n", "") #Reemplaza el salto de línea proveniente del archivo por un espacio.
    #append(): Lo que hace es agregar un elemento a la lista (array de python).
    #split(): Método que crea una lista interna nueva en el index de la lista actual donde nos encontramos, esto 
    #sucederá cuando se encuentre el caracter indicado como parámetro, creando así una lista interna en cada una 
    #de las posiciones de la lista principal con los elementos que estén separados entre comas.
    data_str.append(linea.split(","))
    #Con alguna restricción se le puede decir que solamente cree una lista con ciertos valores y no todos, por 
    #medio de una constante count que se aumente por uno cada vez que el elemento entra en el bucle for y una 
    #condicional que diga de dónde a donde quiero que agarre los elementos del archivo para crear la lista
    print(linea) #Impresión con salto de línea, pero se le quitó con el método replace()
#print(): Imprimir un mensaje en consola.
print("Datos extraídos del archivo: \n", data_str) #Lista creada con los elementos leídos del archivo.
#var_file_open.close(): Método para cerrar un archivo previamente abrierto con el método open(), es peligroso 
#olvidar colocar este método, ya que la computadora lo considerará como si nunca hubiera sido cerrado, por lo 
#cual no podré volver a abrirlo al dar clic sobre él.
archivo_lectura.close()



#MÉTODO TRADICIONAL: Forma tradicional de extraer datos y crear una nueva lista vacía de ceros.
lista_ceros = []
for i in range(len(data_str)):
    lista_temp = []
    for i in range(len(data_str[0])):
        lista_temp.append(0)
    lista_ceros.append(lista_temp)
print("Lista vacía con ceros: \n", lista_ceros) #Lista de ceros con el tamaño de la lista que quiero obtener.



#LISTAS DE COMPRENSIÓN: Las listas de comprensión son listas que se crean por medio de ciclos for pero que se 
#declaran dentro de la misma lista, el problema de usar este método es que si no sabemos si los datos están bien 
#organizados o si pueden venir de varios tipos de datos, algunos numéricos, algunos strings y así, puede ocurrir 
#un error en la recopilación de datos, por lo que es mejor entonces usar el método tradicional en esos casos. 
#Por lo cual las listas de compresión son una forma hardcore de obtener los datos del vector x,y del vector y.
lista_comprension_ceros = [[0 for i in range(len(data_str[0]))] for i in range(len(data_str))] #Lista de ceros.
#Llenado de la lista de ceros
for i in range(len(data_str)):
    for j in range(len(data_str[0])):
        lista_comprension_ceros[i][j] = float(data_str[i][j])
print("Matriz original: \n", lista_comprension_ceros)



#MÉTODO TRADICIONAL: La forma tradicional de extraer datos de un archivo de Excel es buena para cuando no 
#sabemos si los datos están bien organizados o pueden ser de varios tipos de datos, algunos numéricos, algunos 
#strings y así.
x_trad_lista = [] #lista vacía para obtener los datos x de forma tradicional.
y_trad_lista = [] #lista vacía para obtener los datos y de forma tradicional.
for i in range(len(lista_comprension_ceros)):
    x_trad_lista.append(lista_comprension_ceros[i][0])
    y_trad_lista.append(lista_comprension_ceros[i][1])
#print(): Imprimir un mensaje en consola.
print(x_trad_lista)
print(y_trad_lista)



#MATRIZ TRANSPUESTA: Se debe obtener la transpuesta de los datos extraídos porque siempre de los archivos de 
#Excel, ya que estos son extraídos de forma vertical y los necesitamos de forma horizontal para que puedan ser 
#graficados con Python. 
#MATRIZ TRANSPUESTA (FORMA TRADICIONAL): Obtención de una matriz transpuesta de forma tradicional, en los 
#elementos de las matrices transpuestas, lo que pasa es que se intercambian las coordenadas de sus elementos 
#aij=aji.
def transpuesta(matriz):
    m = len(matriz) #Número de renglones de la matriz.
    n = len(matriz[0]) #Número de columnas de la matriz.
    #x = Eje horizontal de las gráficas.
    #m = Lo que quiero obtener de la matriz transpuesta = filas.
    #n = Lo que quiero introduzco a la matriz transpuesta  = columnas.
    trans = [[0 for x in range(m)] for x in range(n)]
    for i in range(n): #Recorrer lo que introduzco a la matriz transpuesta = columnas
        for j in range(m): #Recorrer lo que quiero obtener de la matriz transpuesta = filas
            trans[i][j] = matriz[j][i]  #La transpuesta contiene el inverso de lo que la matriz original tenía. 
        #for j
    #for i
    return trans
#función transpuesta
matriz_transpuesta = transpuesta(lista_comprension_ceros)
print("Matriz transpuesta: \n", matriz_transpuesta)
x_lista_transpuesta = matriz_transpuesta[0]
y_lista_transpuesta = matriz_transpuesta[1]
print(x_lista_transpuesta)
print(y_lista_transpuesta)



#MATRIZ TRANSPUESTA (NUMPY):Forma rápida de sacar los valores xy con la librería numpy.
#En el primer parámetro se indica la lista que se quiere convertir a un arreglo de numpy y en el segundo 
#parámetro se indica a que tipo de dato primitivo se quiere convertir los datos.
data_numpy = np.array(data_str,dtype=float) 
data_final = data_numpy.T #Transpuesta de la matriz data_numpy
x_numpy = data_final[0]
y_numpy = data_final[1]
print("Matriz original: \n", data_numpy)
print("Matriz transpuesta: \n", data_final)
print("Vector x de la matriz transpuesta: \n",x_numpy)
print("Vector y de la matriz transpuesta: \n",y_numpy)



#GRAFICAR LOS DATOS EN PYTHON:
import matplotlib.pyplot as plt #matplotlib: Librería de graficación matemática.
#matplotlib.figure(): Método usado para crear la ventana de graficación (objeto pyplot).
fig = plt.figure()#Creación del objeto pyplot.
#matplotlib.axes(): Método usado para crear la rejilla en la ventana de graficación.
ax = plt.axes()#Se crea un objeto ax perteneciente de la clase axes().
#axes.plot(): Método usado para crear la gráfica en la rejilla previamente creada en la ventana de graficación, 
#indicando como primer parámetro su eje horizontal, luego su eje vertical y finalmente el estilo de la gráfica:
# - Colores:             C1: color naranja, r: color rojo, b: color azul, g: verde, c: cyan, m: morado, 
#   y: amarillo, k: negro, w: blanco.
# - Tipo de marcadores:  o: círculos, +: símbolos de más, .; puntos, v: Triángulo hacia abajo, h: Hexágono, etc.
# - Tipo de Líneas:      -: sólida, --: punteada (líneas), :: punteada (puntos), -.: línea y punto, 'or': Nada.
ax.plot(x_numpy, y_numpy, 'wo--')#'C1o--' significa C1: color naranja, o: simbolo de círculos --: líneas punteadas.
#axes.set_xlabel(): Método para indicar el texto que aparece en el eje x.
ax.set_xlabel(r'$x$')#Texto que aparece en el eje horizontal
#axes.set_ylabel(): Método para indicar el texto que aparece en el eje y.
ax.set_ylabel(r'$y=x^(2)$')#Texto que aparece en el eje vertical
#axes.set_facecolor(): Método para indicar el color de fondo de la gráfica, el cual puede ser indicado por los 
#mismos colores previamente mencionados en el método plot() o se pueden usar los siguientes con el código xkcd:
# - Colores: xkcd:aqua, xkcd:aquamarine, xkcd:azure, xkcd:beige, etc. Los colores se obtienen de este link:
#https://matplotlib.org/stable/tutorials/colors/colors.html
ax.set_facecolor('xkcd:tomato')
#matplotlib.show(): Método para mostrar la gráfica creada.
plt.show()