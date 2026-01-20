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

#CÓDIGO PARA MULTIPLICAR DOS MATRICES:
#El producto AB de la matriz A por la matriz B está definido sólo cuando el número de columnas de A son iguales 
#al número de renglones de B.
#   • En multiplicación de matrices el orden del producto si altera el resultado, AB ≠ BA.
#   • El producto de la matriz A y la matriz B produce la matriz C = A*B, cuyos elementos son el resultado de la 
#     multiplicación de los vectores fila de A por los vectores columna de B. 
#       Si ai denota el i−ésimovector vector (fila) de A y bj el j−ésimovector vector (columna) de B; entonces 
#       los elementos resultantes de la multiplicación cij de C = A*B están dados por:
#           cij = ai*bj = Σai*bj

#LISTAS:
#Declaración e iniciación de las matrices en un tipo de dato de Python llamado lista, siguiendo la nomenclatura 
#descrita a continuación, tomando en cuenta que el número de elementos de las filas debe ser el mismo:
#Matriz_lista = [[fila1],[fila2],...,[fila_n]],     FILA X COLUMNA
#vector_renglon = [1,2,3],          1X3
#vector_columna = [[1],[2],[3]],    3X1
A = [[1,3],[2,4]] #Matriz A (tipo de dato lista),   2X2
B = [[2,3],[0,4]] #Matriz B (tipo de dato lista),   2X2
#Se debe declarar la matriz vacía que almacenará el resultado de la multiplicación:
C = [[0,0],[0,0]] #Matriz C = A*B, 2X2

#Obtención de las dimensiones de la matriz para acceder a las posiciones de sus elementos y realizar la 
#multiplicación, ya que debe coincidir el tamaño de las columnas de la matriz A con el tamaño de las filas de la
#matriz B para que se pueda hacer su producto.
#len(): Este método sirve para ver el tamaño de una matriz, que en Python a ese tipo de dato se le llama lista.
m = len(A) #Número de filas o renglones de la matriz A
#Si una lista tiene posiciones con listas internas, como lo es en el caso de las matrices, lo que se hace para 
#saber el tamaño de las listas internas es que se indica que se quiere saber el tamaño de la posición de una 
#matriz, como todas las filas deben tener el mismo número de elementos, no importa que posición se elija, el 
#tamaño de todas será iguales. Es importante mencionar que las posiciones o index de las listas se empieza a 
#contar desde cero, pero el tamaño de una lista se empieza a contar desde 1.
n = len(B[0]) #Número de las columnas de la matriz B
#El número de columnas de la matriz A debe ser igual al número de filas de la mariz B
l = len(A[0]) #l = len(A[0]) = len(B)

#BUCLE FOR: En Python no se utilizan llaves de apertura o cierre para la sintaxis de un bucle, solamente se 
#utilizan dos puntos para indicar su inicio y tabuladores para diferenciar qué es lo que está dentro o fuera 
#de él. Además, después de la palabra reservada "for" se declara una variable local numérica entera que solo 
#existirá dentro del bucle y será la que cuente desde 0 por default o desde el primer número indicado dentro 
#del paréntesis hasta el extremo indicado en el segundo parámetro que se encuentra dentro del paréntesis de la 
#palabra reservada range() para terminar el bucle. En otras palabras, dentro del paréntesis de la palabra 
#reservada "range()" se coloca el inicio y final del conteo para indicar cuantas veces se ejecutará el bucle.
#Es importante mencionar que los bucles for se pueden utilizar para realizar sumatorias en operaciones 
#matemáticas:
#cij = ai*bj = Σai*bj
for i in range(0, m): #Lectura de filas de la matriz A.
    for j in range(0, n): #Lectura de columnas de la matriz B.
        sum = 0 #Inicialización de la variable que almacenará el valor de cada elemento de la matriz resultante.
        for k in range(0, l): #Lectura de las columnas de la matriz A, que es igual a las filas de la matriz B.
            sum = sum +  A[i][k]*B[k][j] #Llenado de los elementos de la matriz C: cij = ai*bj = Σai*bj
        #for k
        C[i][j] = sum #Asignación del valor de cada elemento de la matriz resultante C.
    #for j
#for i
    
#Impresión de la matriz C:
#print(): Método para imprimir un mensaje en consola y después dar un salto de línea (Enter), además si se quiere 
#concatenar un mensaje (mostrar resultados de variables junto con texto estático), este se debe separar entre 
#comillas, declarando los mensajes estáticos entre comillas y los nombres de variables sin comillas.
print("El resultado de la multiplicación de las matrices A: ", A, " y B: ", B, " es igual a: ", C)


#NUMPY ARRAY:
#BIBLIOTECA NUMPY: Esta librería de Python importa mucho material para poder hacer operaciones entre matrices 
#sin necesidad de hacerlo con bucles, además de permitir realizar matemática más compleja.
#Para importar librerías primero esta se debe descargar con la consola de Windows CMD, Powershell o GitBash, 
#luego se usa la palabra reservada import, el nombre de la librería, la palabra reservada "as" y el nuevo 
#nombre con el que se quiere usar los métodos de la librería dentro del código.
import numpy as np

#Ejemplo de multiplicación de matrices con 3 filas y 3 columnas, osea FXC = 3X3
#Las matrices declaradas con el método array de la librería numpy no son listas, son totalmente otro tipo de 
#valor perteneciente a la librería numpy, llamado numpy array y para declarar arrays de este tipo de dato se usa 
#la siguiente nomenclatura:
#Matriz_numpy_array = numpy.array([[fila1],[fila2],...,[fila_n]]), FILA X COLUMNA
#La diferencia con la matriz declarada en forma de lista es la siguiente:
#Matriz_lista = [[fila1],[fila2],...,[fila_n]], FILA X COLUMNA
D = np.array([[1,2,3],[4,5,6],[7,8,9]]) #Matriz D (tipo de dato numpy array), 3X3
E = np.array([[1],[2],[3]]) #Matriz E (tipo de dato numpy array), 3X1
#Recordemos que para que se pueda realizar la multiplicación entre matrices, el número de columnas de la primera 
#matriz y el número de filas de la segunda matriz debe ser el mismo y el resultado será del tamaño que sobre de 
#las matrices originales, cuando se está usando la librería numpy no es necesario declarar la matriz vacía que 
#almacenará el resultado de la multiplicación.

#numpy.dot(): Este método de la librería numpy sirve para realizar el producto de dos matrices sin necesidad de 
#usar un bucle, en su primer parámetro se pone la primera matriz que se quiere multiplicar y en el segundo la 
#segunda matriz, recordemos que en matrices el orden de los elementos si afecta al resultado del producto.
F = np.dot(D,E)

#Impresión de la matriz F, cuando se imprima el resultado de matrices hechas con la librería numpy se debe dar 
#saltos de línea entre el texto y donde se muestre el valor de las matrices porque por default estas dan un 
#salto de línea.
print("El resultado de la multiplicación de las matrices D: \n", D, "\nY E: \n", E, "\nEs igual a: \n", F)