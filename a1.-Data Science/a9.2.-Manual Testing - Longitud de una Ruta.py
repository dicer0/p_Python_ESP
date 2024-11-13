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
#a) FUNCIÓN PATHLENGTH: Calcula la longitud de una ruta según la fórmula L.
#Un objeto se mueve a lo largo de una trayectoria en el plano. En n + 1 puntos de tiempo se han registrado las 
#correspondientes posiciones (x, y) del objeto: (x0, y0), (x1, y1), ..., (xn, yn). La longitud total L del 
#camino de (x0, y0) a (xn, yn) es la suma de todos los segmentos de línea individuales
#((xi-1, yi-1) a (xi, yi), donde i = 1, ..., n):
#L = Σ√(x(i) - x(i-1))^2 + (y(i) - y(i-1))^2; donde i = 1,..., n.
def longitudRuta(x, y):
    Longitud = 0    #Longitud inicial = 0

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

#input(): Método que sirve para imprimir en consola un mensaje y que luego se permita al usuario ingresar un 
#valor, que será de tipo String y podrá ser almacenado en una variable.
#int(): Método que convierte un tipo de dato cualquiera en numérico entero.
num_coordenadas = int(input('Indique el número de coordenadas del camino (igual o mayor que 2)\n'))

#Declaración de dos listas vacías donde se almacenarán todos los puntos de las coordenadas de la ruta 
x_total = []        #Puntos horizontales (x1), …, (xn) de las coordenadas.
y_total = []        #Puntos verticales (y1), …, (yn) de las coordenadas.
coordenadas = []    #Lista que almacenará todas las coordenadas ingresadas para imprimirlas en consola.

#CONDICIONAL IF: En Python no se utilizan llaves de apertura o cierre al utilizar condiconales, solamente se 
#utilizan dos puntos para indicar el inicio del condicional y tabuladores para ver qué es lo que está dentro o 
#fuera de él, ya sea para el condicional if, else if (elif) o else.
if num_coordenadas < 2:
    print('Un camino no puede tener solo una coordenada, debe ser mínimo de 2 o más')
else:
    #Dependiendo del número de coordenadas que haya introducido el usuario, se ejecutará varias veces el bucle 
    #for para que el usuario las introduzca todas: 
    for i in range(0, num_coordenadas):
        #input(): Método que sirve para imprimir en consola un mensaje y que luego se permita al usuario 
        #ingresar un valor, que será de tipo String y podrá ser almacenado en una variable.
        #int(): Método que convierte un tipo de dato cualquiera en numérico entero.
        x_nuevo = int(input(f'Ingrese la coordenada horizontal del punto x{i}: \t'))
        y_nuevo = int(input(f'Ingrese la coordenada vertical del punto y{i}: \t'))

        #print(): Método para imprimir un mensaje en consola y después dar un salto de línea (Enter).
        print("La coordenada ", i, " es:\n", "(", x_nuevo, ", ", y_nuevo, ")")
        
        #append(): Método que sirve para agregar valores a una lista, tupla, numpy array o diccionario.
        x_total.append(x_nuevo)
        y_total.append(y_nuevo)
        #LISTAS ANIDADAS: Cuando dentro de la posición de una lista se encuentra otra lista interna, se le 
        #llama lista anidada, esto se realiza por ejemplo para categorizar datos, realizar operaciones 
        #matriciales, etc.
        #AGREGAR LISTAS ANIDADAS CON EL MÉTODO lista.append(): Esto se debe realizar usualmente dentro de un 
        #bucle for, en este caso para ello primero se extraen los valores de "x_nuevo" y "y_nuevo" y luego se 
        #agregan a la lista de coordenadas como una lista anidada [x_nuevo, x_nuevo] con el método append().
        coordenadas.append([x_nuevo, y_nuevo])
    
    #USO DE LA FUNCIÓN longitudRuta(): Terminando el bucle for pero dentro del condicional if se utiliza la 
    #función que realiza el cálculo de la distancia total de una ruta con todos los puntos de sus coordenadas.
    Longitud_total = longitudRuta(x_total, y_total)

    #print(): Método para imprimir un mensaje en consola y después dar un salto de línea (Enter), además si se 
    #quiere concatenar un mensaje (mostrar resultados de variables junto con texto estático), este se debe 
    #separar entre comillas, declarando los mensajes estáticos entre comillas y los nombres de variables sin 
    #comillas.
    print("Las coordenadas ingresadas fueron: ", coordenadas)
    print('La distancia total de la ruta con', num_coordenadas, 'coordenadas tiene una longitud de:', Longitud_total)




#TESTING: Acción realizada cuando a través de una función se comprueba el funcionamiento de otra.
#b) FUNCIÓN TEST_PATHLENGTH: Función que ejecuta la función PATHLENGTH para comprobar que se ejecuta 
#correctamente, a esta acción se le llama testing.
def test_pathLenght():
    coordenada_1 = (0, 0)
    coordenada_2 = (1, 0)
    coordenada_3 = (2, 0)

    #nombreLista[index]: Para acceder a la posición de una lista se debe indicar su nombre seguido de unos 
    #corchetes que indiquen la coordenada a la que se quiere acceder.Se debe tomar en cuenta que las coordenadas 
    #se empiezan a contar desde 0, aunque el tamaño de la lista se cuenta desde 1.
    x_total = (coordenada_1[0], coordenada_2[0], coordenada_3[0])
    y_total = (coordenada_1[1], coordenada_2[1], coordenada_3[1])

    Longitud_total = longitudRuta(x_total, y_total)

    print('Testing: La distancia total de la ruta con', len(x_total), 'coordenadas tiene una longitud de:', Longitud_total)

#USO DE LA FUNCIÓN test_pathLenght().
test_pathLenght()