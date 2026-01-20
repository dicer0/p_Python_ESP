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

#EJERCICIO DICCIONARIO Y FUNCIONES:
#Con la palabra reservada def se declara una función
def char_frequency(st):
    #La declaración de un diccionario se hace con llaves de apertura y cierre {} 
    diccionario = {}
    #Los bucles for-each son muy buenos para recorrer elementos de una lista o diccionario, ya que los strings 
    #son cadenas de caracteres, por lo tanto, en vez de poner for i in range(len(st)), podemos poner for i in st.
    for letra in st:    #Bucle for que recorre cada letra del string que reciba.
        #print(): Imprimir un mensaje en consola.
        print(letra)    #Imprime las letras del string una por una.
        #diccionario.keys(): Con este el método keys() que se aplica a un diccionario obtenemos todas sus keys, 
        #donde la estructura de los diccionarios se asemeja a los JSON: {"key": "value"}, para acceder a los 
        #values de un json, debemos indicar su key, ya que no tenemos indices en este tipo de estructuras.
        llaves = diccionario.keys()
        #Lo que hace aquí el JSON es comparar cada letra del string, con un diccionario que las va recorriendo 
        #una a una, cuando encuentre que existe una vez, le sumará un 1 y lo asignará como su value, indicando 
        #su frecuencia, entonces:
        # - En la iteración 1 donde: letra = g; diccionario = {};  diccionario[letra] = diccionario[g] = None; diccionario = {'g':1}
        # - En la iteración 2 donde: letra = o; diccionario = {'g':1};  diccionario[o] = None; diccionario = {'g':1,'o':1}
        # - En la iteración 3 donde: letra = o; diccionario = {'g':1,'o':1};  diccionario[o] = !None,+=1; diccionario = {'g':1,'o':2}
        # - En la iteración 4 donde: letra = g; diccionario = {'g':1,'o':2};  diccionario[g] = !None,+=1; diccionario = {'g':2,'o':2}
        # - En la iteración 5 donde: letra = l; diccionario = {'g':2,'o':2};  diccionario[l] = None; diccionario = {'g':2,'o':2, 'l':1}
        # - En la iteración 5 donde: letra = e; diccionario = {'g':2,'o':2,'l':1};  diccionario[e] = None; diccionario = {'g':2,'o':2,'l':1,'e':1}
        # - En la iteración 5 donde: letra = .; diccionario = {'g':2,'o':2,'l':1,'e':1};  diccionario[.] = None; diccionario = {'g':2,'o':2,'l':1,'e':1,'.':1}
        # - En la iteración 5 donde: letra = c; diccionario = {'g':2,'o':2,'l':1,'e':1,'.':1};  diccionario[c] = None; diccionario = {'g':2,'o':2,'l':1,'e':1,'.':1,'c':1}
        # - En la iteración 5 donde: letra = o; diccionario = {'g':2,'o':2,'l':1,'e':1,'.':1,'c':1};  diccionario[o] = !None,+=1; diccionario = {'g':2,'o':3,'l':1,'e':1,'.':1,'c':1}
        # - En la iteración 5 donde: letra = m; diccionario = {'g':2,'o':3,'l':1,'e':1,'.':1,'c':1};  diccionario[m] = None; diccionario = {'g':2,'o':3,'l':1,'e':1,'.':1,'c':1,'m':1}
        if(letra in llaves):                    #Si la letra ya está en el JSON existente, le suma un 1 al contador que se encuentra en su value.
            diccionario[letra] += 1
        else:                                   #Si la letra NO está en el JSON existente, la agrega y le asigna un valor de 1.
            #Agregamos letras al diccionario
            diccionario[letra] = 1
    return diccionario                          #El diccionario resultante es: diccionario = {'g':2,'o':3,'l':1,'e':1,'.':1,'c':1,'m':1}.

#Manda a llamar la función char_frequency
print(char_frequency("google.com"))