# -*- coding: utf-8 -*-

#En Python se introducen comentarios de una sola linea con el simbolo #.
#La primera línea de código incluida en este programa se conoce como declaración de codificación o codificación 
#de caracteres. Al especificar utf-8 (caracteres Unicode) como la codificación, nos aseguramos de que el archivo 
#pueda contener caracteres especiales, letras acentuadas y otros caracteres no ASCII sin problemas, garantizando 
#que Python interprete correctamente esos caracteres y evite posibles errores de codificación.
#Se puede detener una ejecución con el comando [CTRL] + C puesto en consola, con el comando "cls" se borra su 
#historial y en Visual Studio Code con el botón superior izquierdo de Play se corre el programa.
#Para comentar en Visual Studio Code varias líneas de código se debe usar las líneas:
#[CTRL] + K (VSCode queda a la espera). Después pulsa [CTRL] + C para comentar y [CTRL] + U para descomentar.

#TIPOS DE ESTRUCTURAS DE DATOS EN PYTHON: La gran diferencia que estos pueden tener es que algunos tienen cierto 
#órden (índice y valor) y otros no, además de que algunos son editables o mutables, donde se les puede agregar, 
#eliminar, o modificar elementos y otros son inmutables, donde sus datos no se pueden cambiar.
# - Listas (list): Una lista es una colección ordenada y mutable (editable) de elementos. Se definen utilizando 
#   corchetes [].
#       Ejemplo: mi_lista = [1, 2, "hola", True].
# - Tuplas (tuple): Una tupla es una colección ordenada e inmutable de elementos. Se definen utilizando 
#   paréntesis ().
#       Ejemplo: mi_tupla = (1, 2, "hola", True).
# - Diccionarios (dict): Un diccionario es una colección desordenada y mutable de pares clave-valor. Se definen 
#   utilizando llaves {} y separando cada par clave-valor por dos puntos :.
#       Ejemplo: mi_diccionario = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}.
# - Conjuntos (set): Un conjunto es una colección desordenada y mutable de elementos únicos. No permite elementos 
#   duplicados y no tiene un orden definido. Se definen utilizando llaves {} o utilizando la función set().
#       Ejemplo: mi_conjunto = {1, 2, 3, 4, 5}.

#LISTAS: Las listas en Python son tipos de datos estructurados, parecido a lo que son los arrays en otros 
#lenguajes de programación, aunque no es el único tipo de dato agrupado que existe en Python, existen además las 
#tuplas, diccionarios y numpy arrays.
lista = [1,2,3,4]

#INTRODUCIR DATOS A UNA LISTA VACÍA:
lista_numeros = []  #Lista vacía
#Bucle for para introducirle 11 datos, que irán de 0 a 10 porque el bucle nunca tocará su último valor y además 
#empezará a contar desde cero.
for i in range(0,11):
    #append(): Método que sirve para agregar valores a una lista, tupla, numpy array o diccionario.
    lista_numeros.append(i)





#LISTAS ANIDADAS: Cuando dentro de la posición de una lista se encuentra otra lista interna, se le llama lista 
#anidada, esto se realiza por ejemplo para categorizar datos, realizar operaciones matriciales, etc.
lista_anidada = [[1,2,3,4],[1,5,6]]
#Además dentro de una lista anidada, se puede incluir otra lista anidada, logrando así que se creen dimensiones 
#dentro de una lista, por ejemplo las imágenes digitales en sus datos brutos están conformadas de 3 capas o 
#dimensiones que describen cada color RGB que conforma una imagen.  
lista_anidada_2 = [[1, [8,9,10], 3], [4,5,6]]
#nombreLista[index_dimension1][index_dimension2]: Para acceder a la posición de una lista se debe indicar su 
#nombre seguido de unos corchetes que indiquen la coordenada a la que se quiere acceder. Se debe tomar en cuenta 
#que las coordenadas se empiezan a contar desde 0, aunque el tamaño de la lista se cuenta desde 1.
#También tomando en cuenta que una lista puede contar con varias dimensiones, para acceder a una posición 
#específica se pueden indicar varios índices que referencíen una posición en cada dimensión.
#Además, en las listas no es necesario que todos los datos sean del mismo tipo.
lista_anidada_2[1][2] = [10,"UPIITA",11,12]

#print(): Método para imprimir un mensaje en consola y después dar un salto de línea (Enter).
print("Los valores de la lista son:", lista)
print("Los valores de la lista rellenada son:", lista_numeros)
print("La lista encontrada de la lista anidada es:", lista_anidada[0])
print("El valor encontrado de la lista anidada de la lista anidada es:", lista_anidada[0][1])
print("El valor encontrado de la lista anidada de la lista anidada de la lista anidada es:", lista_anidada_2[0][1][1])
print("Los valores de la lista anidada rellenada son:", lista_anidada_2)
print("El tipo del valor encontrado en la lista anidada es:", type(lista_anidada_2[1][2][1]))
print("El número de renglones de la lista anidada es:", len(lista_anidada_2))
#   \n: Símbolo que indica un salto de línea.
#   \t: Símbolo que indica un tabulador.
print("El número de columnas de la lista anidada es:", len(lista_anidada_2[0]), "\n")