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

import math #math: Librería que proporciona funciones y constantes matemáticas como seno, π, logaritmo, etc.

#FUNCIONES EN PYTHON: Las funciones en python se indican a través de la palabra reservada def, seguida del 
#nombre de la función, un paréntesis que contiene sus distintos parámetros y dos puntos para denotar su inicio,
#en Python no se utilizan llaves de apertura o cierre para su sintaxis, solamente se utilizan dos puntos para 
#indicar su inicio y tabuladores para diferenciar qué es lo que está dentro o fuera de ella.
#   - Las funciones son muy utilizadas en Python ya que sirven para volver modular el código, logrando así que 
#     se pueda ejecutar varias veces una misma acción sin necesidad de escribirla varias veces.
#   - Los distintos métodos que se utilizan en todos los lenguajes de programación para ejecutar acciones 
#     diferentes como por ejemplo lo es el método print(), son en realidad funciones, pero que utilizan una 
#     arquitectura de programación orientada a objetos (POO).
#   - Los parámetros que recibe una función son las variables con las que interactúa para realizar su acción, 
#     una función cualquiera puede o no recibir parámetros para ejecutarse. 
#   - Una función puede o no devolver una variable que almacene su valor resultante, esto se realiza a través 
#     de la palabra reservada "return".
#   - Para utilizar una función en Python se debe declarar su nombre seguido de un paréntesis en donde se le 
#     pase sus parámetros, si es que recibe algunos, además su resultado puede o no guardarse en una variable 
#     dependiendo de si retorna un valor o no.

#2.- LONGITUD DE UNA RUTA: Cálculo con sus coordenadas (x1, y1), …, (xn, yn)
#FUNCIÓN PATHLENGTH: Calcula la longitud de una ruta según la fórmula L.
#Un objeto se mueve a lo largo de una trayectoria en el plano. En n + 1 puntos de tiempo se han registrado las 
#correspondientes posiciones (x, y) del objeto: (x0, y0), (x1, y1), ..., (xn, yn). La longitud total L del 
#camino de (x0, y0) a (xn, yn) es la suma de todos los segmentos de línea individuales
#((xi-1, yi-1) a (xi, yi), donde i = 1, ..., n):
#L = Σ√(x(i) - x(i-1))^2 + (y(i) - y(i-1))^2; donde i = 1,..., n.

#3.- APROXIMACIÓN DE π: Utilizando el programa de Cálculo de Longitud de Ruta.
#El valor de π es igual a la circunferencia de un círculo de radio r = 1/2. Supongamos que aproximamos la forma 
#de una circunferencia mediante un polígono que pasa por n + 1 puntos del círculo, la longitud de este polígono 
#se puede hallar usando la función de Cálculo de Longitud de Ruta del ejercicio 2, calculando la ruta de n + 1 
#puntos consecutivos con coordenadas (xi, yi) a lo largo de una circunferencia de radio r = 1/2 según las 
#siguientes fórmulas, considerando que n = 2^k, donde k determina la precisión de la aproximación del polígono. 
#A medida que la variable k aumente, el número de puntos utilizados y la cantidad de segmentos rectos aumenta, 
#lo que resulta en una aproximación más precisa de la circunferencia, reduciendo exponencialmente el error entre 
#el valor real de π y la aproximación obtenida:
#xi = 1/2*cos(2*π*i/n) = 1/2*cos(2*π*i/(2^k)); i = n+1 = (2^k)+1
def longitudRuta(x, y):
    Longitud = 0                    #Longitud inicial = 0

    #BUCLE FOR: En Python no se utilizan llaves de apertura o cierre para la sintaxis de un bucle, solamente se 
    #utilizan dos puntos para indicar su inicio y tabuladores para diferenciar qué es lo que está dentro o fuera 
    #de él. Además, después de la palabra reservada "for" se declara una variable local numérica entera que solo 
    #existirá dentro del bucle y será la que cuente desde 0 por default o desde el primer número indicado dentro 
    #del paréntesis hasta el extremo indicado en el segundo parámetro que se encuentra dentro del paréntesis de 
    #la palabra reservada range() para terminar el bucle. En otras palabras, dentro del paréntesis de la palabra 
    #reservada "range()" se coloca el inicio y final del conteo para indicar cuantas veces se ejecutará el 
    #bucle.
    #Es importante mencionar que los bucles for se pueden utilizar para realizar sumatorias en operaciones 
    #matemáticas:
    #L = Σ√(x(i)-x(i-1))^2+(y(i)-y(i-1))^2; donde i = 1,..., n.
    #len(): Este método sirve para ver el tamaño de una lista, tupla, diccionario o numpy array.
    for i in range(1, len(x)):
        #float(): Método que convierte un tipo de dato cualquiera en numérico decimal.
        #numero ** potencia = numero ^ potencia = número elevado a cierta potencia.
        #numero ** 1/2 = numero ^ 1/2 = Σnúmero.
        L = (((float(x[i]) - float(x[i-1]))**(2)) + ((float(y[i]) - float(y[i-1]))**(2)))**(1/2)
        #Se utiliza una variable intermedia llamada L para calcular cada una de las longitudes y luego sumarlas 
        #a la variable Longitud que almacenará el valor de la longitud total.
        Longitud += L
    return Longitud



#OBTENCIÓN DE LAS COORDENADAS DE UN POLÍGONO QUE ASEMEJA LA FORMA DE UN CÍRCULO CON RADIO r = 1/2:
#Se declaran las variables n y k para que estos sean los puntos consecutivos con los que se aproxima un polígono 
#para asemejar la forma de un círculo y obtener el valor aproximado de pi, en específico con estas dos variables 
#se tendrán n = 2^k puntos en el polígono para acercarse al valor del perímetro del círculo con diámetro = 1 y 
#radio = 1/2.
#n = 2^k puntos consecutivos que conforman el polígono:
k = (2, 3, 4, 5, 6, 7, 8, 9, 10)    #Lista k: Precisión de la aproximación de un polígono a un círculo.
n = 2                               #Base n: Puntos consecutivos para aproximar un polígono a un círculo.

#Declaración de las listas vacías donde se almacenarán los valores de cada una de las aproximaciones con n = 2^k 
#vértices para obtener el valor de pi con un varios polígonos.
error = []                          #error: Almacena el error para cada una de las aproximaciones.
coordenadas_x = []                  #x: Vector que contiene todas las coordenadas horizontales del polígono.
coordenadas_y = []                  #y: Vector que contiene todas las coordenadas verticales del polígono.
circunferencias = []                #Perímetros: Circunferencias obtenidas con las coordenadas (xi, yi).

#BUCLE FOR EACH: Es un tipo especial de bucle for que sirve para recorrer todos los elementos de una lista, 
#tupla o diccionario, su sintaxis es la siguiente: for i in lista y es lo mismo a poner la instrucción 
#for i in range(0, len(lista)).
#En este caso es lo mismo que poner la instrucción:
# - for i in k = for i in range(0, len(k)): Instrucción que recorre los elementos de la lista k, del número 2 
#   al 10.
#En programación una forma de ejecutar exponentes es por medio de ciclos for anidados: 
# - El bucle for que se encuentre en la parte exterior será el exponente. 
#       En este caso es k.
# - El bucle for interno será la base del exponente. 
#       En este caso es n, para que de esta forma se pueda hacer que n = 2^k.
for i in k: 
    #Declaración de las listas vacías que almacenarán las coordenadas x,y de cada uno de los vértices del 
    #polígono que se aproxima al círculo para obtener así el valor de pi, cuyo valor es igual al perímetro del 
    #círculo con diámetro = 1. 
    xi = []                         #xi: Coordenadas horizontales de i = 0, ..., n.
    yi = []                         #yi: Coordenadas verticales de i = 0, ..., n.
    #El bucle se tiene que ejecutar n+1 veces, pero como n = 2^k, se debe ejecutar (2^k)+1 veces.
    for j in range(0, n**i + 1):
        #Por medio de las siguientes fórmulas se describe la forma en la que se obtendrán las coordenadas
        #del polígono que se aproxima a tener la forma de un círculo.
        #append(): Método que sirve para agregar valores a una lista, tupla, numpy array o diccionario.
        #math.cos(): Método de la librería math que aplica la función coseno a lo que haya en su paréntesis.
        #math.sin(): Método de la librería math que aplica la función seno a lo que haya en su paréntesis.
        #math.pi(): Constante pi (π) de la librería math.
        xi.append(math.cos(2*math.pi*j/n**i)/2) #xi = 1/2*cos(2*π*i/n) = 1/2*cos(2*π*i/(2^k)); i = n+1 = (2^k)+1
        yi.append(math.sin(2*math.pi*j/n**i)/2) #yi = 1/2*sin(2*π*i/n) = 1/2*sin(2*π*i/(2^k)); i = n+1 = (2^k)+1
    
    #Se agregan las coordenadas xi al vector que contiene todas las coordenadas horizontales del polígono
    coordenadas_x.append(xi)
    #Se agregan las coordenadas yi al vector que contiene todas las coordenadas verticales del polígono
    coordenadas_y.append(yi)



#USO DE LA FUNCIÓN longitudRuta(): Se utiliza la función que realiza el cálculo de la distancia total de una 
#ruta con todos los puntos de sus coordenadas, esto se realiza una vez obtenidas todas las coordenadas del 
#polígono que se aproxima a tener la misma forma que un círculo con radio r = 1/2, obteniendo así el valor 
#aproximado de π.
#En el siguiente bucle se analizan cada una de las coordenadas guardadas en las listas "coordenadas_x" y 
#"coordenadas_y" para obtener el perímetro de ese polígono usando cada una de esas coordenadas y así obtener 
#las distintas aproximaciones de pi.
for i in range(0, len(k)):#El bucle for se ejecutará el mismo número de veces que las potencias de precisión k.
    #Se llena la lista de circunferencias con los distintos perímetros obtenidos con las coordenadas (xi, yi) 
    #calculadas en el bucle anterior, esto se realiza utilizando la función longitudRuta().
    circunferencias.append(longitudRuta(coordenadas_x[i], coordenadas_y[i]))

    #Se calcula el error de todas las circunferencias obtenidas restando el valor de pi obtenido de la librería 
    #math menos el valor obtenido con función longitudRuta().
    error.append(math.pi-longitudRuta(coordenadas_x[i],coordenadas_y[i]))
    
    #print(): Método para imprimir un mensaje en consola y después dar un salto de línea (Enter), además si se 
    #quiere concatenar un mensaje (mostrar resultados de variables junto con texto estático), este se debe 
    #separar entre comillas, declarando los mensajes estáticos entre comillas y los nombres de variables sin 
    #comillas.
    print(f'Puntos del Polígono:', n**k[i])          #Impresión en pantalla del número de (2^k)+1 puntos obtenidos del polígono.
    print(f'Circunferencia = Valor de pi obtenido con la aproximación:', circunferencias[i])
    print(f'Error:', error[i])     #Impresión en pantalla del error obtenido con cada circunferencia calculada.