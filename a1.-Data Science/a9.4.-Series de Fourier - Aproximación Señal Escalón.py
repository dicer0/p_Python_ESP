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

#4.- SERIES DE FOURIER: Aproximar una Función Escalonada con una suma de Senos/Cosenos.
#A la suma de las funciones seno y/o coseno para obtener una aproximación de otra señal, se le denomina Serie de 
#Fourier (F.S.). La aproximación de una función mediante una serie de Fourier es una técnica muy importante en 
#el arte de la ciencia y tecnología.
#Consideramos la función constante a trozos (escalón) descrita a continuación:
#            1,       0 < t < T/2
#   f(t) = { 0,           t = T/2
#           -1,     T/2 < t < T
#La función abarca desde t = 0 hasta t = T y se vuelve cero cuando t = T/2.
#Se busca aproximar la señal escalón f(t) por medio de la suma:
#   S(t,n) = (4/π)*Σ(1/(2i-1))*sin((2*(2i-1)*π*t)/T); donde i = 1,..., n.
#Mientras mayor sea el número de veces que se realiza la sumatoria de senos, más se aproximará a la función 
#escalón: S(t;n) → f(t) a medida que el número de sumas tiende a infinito: n → ∞.

#a) Escribe una Función Python S(t, n, T) para devolver el valor de la suma de senos S(t;n) que describe la 
#serie de Fourier.
#BUCLE FOR: En Python no se utilizan llaves de apertura o cierre para la sintaxis de un bucle, solamente se 
#utilizan dos puntos para indicar su inicio y tabuladores para diferenciar qué es lo que está dentro o fuera de 
#él. Además, después de la palabra reservada "for" se declara una variable local numérica entera que solo 
#existirá dentro del bucle y será la que cuente desde 0 por default o desde el primer número indicado dentro del 
#paréntesis hasta el extremo indicado en el segundo parámetro que se encuentra dentro del paréntesis de la 
#palabra reservada range() para terminar el bucle. En otras palabras, dentro del paréntesis de la palabra 
#reservada "range()" se coloca el inicio y final del conteo para indicar cuantas veces se ejecutará el bucle.
#Es importante mencionar que los bucles for se pueden utilizar para realizar sumatorias en operaciones 
#matemáticas:
#S(t, n, T) = (4/π)*Σ(1/(2i-1))*sin((2*(2i-1)*π*t)/T); donde i = 1,..., n.
def S(t, n, T):
    serieFourier = 0    #Variable que guarda el valor final de la serie de Fourier S(t,n,T).
    sumatoria = 0       #Variable que guarda el valor temporal de la sumatoria previa a obtener la F.S.
    #Se ejecutó el bucle for hasta n+1 porque ese valor no lo va a tocar, logrando así que la variable i valga:
    #i = 1,..., n.
    for i in range(1, n+1):
        #Dentro del bucle for solo se obtiene el resultado de la sumatoria.
        #sumatoria = Σ(1/(2i-1))*sin((2*(2i-1)*π*t)/T)
        sumatoria = sumatoria + 1.0/(2*i-1)*math.sin((2*((2*i)-1)*math.pi*t)/T)
    #Fuera del bucle for se realiza el resto de la operación, que en este caso es multiplicar la sumatoria 
    #por 4/π.
    #S(t, n, T) = (4/π)*sumatoria = (4/π)*Σ(1/(2i-1))*sin((2*(2i-1)*π*t)/T)
    serieFourier = (4/math.pi)*sumatoria
    return serieFourier

#b) Escribe una Función Python f(t,T) para describir la función escalón f(t).
#CONDICIONAL ELSE IF: En Python no se utilizan llaves de apertura o cierre para la sintaxis de un condicional, 
#solamente se utilizan dos puntos para indicar su inicio y tabuladores para diferenciar qué es lo que está 
#dentro o fuera de él. 
#Los condicionales else if en Python se indican con la palabra reservada elif y lo que hacen es declarar varias
#condiciones que estén conectadas entre sí, para que de esta manera se puedan evaluar todas sus posibilidades:
#            1,       0 < t < T/2
#   f(t) = { 0,           t = T/2
#           -1,     T/2 < t < T
#La función abarca desde t = 0 hasta t = T y se vuelve cero cuando t = T/2.
#Comparador con y sin Tolerancia: Cuando se compara de forma muy rigida dos valores decimales entre sí, puede 
#existir un error al realizar su comparación, por esta razón es que es recomendable indicar una tolerancia y 
#realizar la comparación respecto a ella, para así evitar errores. 
#La comparación "diferente a" con tolerancia se efectúa al realizar una resta entre los valores comparados, 
#indicando que si el resultado de dicha resta es menor a la tolerancia declarada, los valores son distintos.
def f(t, T):
    if (0 < t < (T/2)):
        senal_escalon = 1       #f(t) = 1, cuando 0 < t < T/2
    #Comparador con tolerancia: En este caso se está dando una tolerancia de 1e-8 = 0.00000001
    #abs(): Método que saca el valor absoluto de un número, volviéndolo positivo aunque sea originalmente 
    #negativo.
    #El método abs() saca el valor absoluto de la comparación para que esta sea más precisa, de esta forma la 
    #tolerancia aplica hacia ambos lados. 
    #Si la comparación da como resultado False es porque t no está ni cerca de ser igual a T/2, osea: t != T/2, 
    #Si da True es porque se encuentra dentro del rango de la tolerancia o es exactamente igual, osea: t == T/2.
    elif (abs(t-(T/2)) < 1e-8):
        senal_escalon = 0       #f(t) = 0, cuando t = T/2
    elif ((T/2) < t < T):
        senal_escalon = -1      #f(t) = -1, cuando T/2 < t < T
    else:
        #Caso de cuando el vector t (tiempo) se sale del rango 0 < t < T:
        print ("El vector t se sale del rango del tiempo, debe estar en el intervalo 0 < t < T, intenta de nuevo")
        senal_escalon = 0
    return senal_escalon

#Número de las sumas de senos que se realizará en la serie de Fourier S(t, n, T) para aproximarse a la función 
#escalón f(t, T).
numSumasFourier = [1, 3, 5, 10, 30, 100]
#Periodo de la función senoidal = 2π
T = 2*math.pi                   #T = 2*π
#Factor alfa de multiplicación para obtener un tiempo en específico respecto al periodo T.
α = [0.01, 0.25, 0.49, 0.5, 0.99]

#Bucle for each de una sola línea para rellenar una lista con una operación específica:
#Bucle for each en una sola línea:  [instrucción      for   variable_local   in   lista_a_recorrer]
#Bucle for en una sola línea:       [instrucción      for   variable_local   in   range(inicio, final)]
tiempo = [alpha*T for alpha in α] #t = α*T

#c) Muestra una tabla en consola que enseñe cómo varía el error f(t) - S(t;n) cuando cambia el valor de las 
#variables n (número de sumas de fourier) y t (tiempo) para los casos en que:
#   n = [1, 3, 5, 10, 30, 100];     t = α*T;     T = 2*π;     α = [0.01, 0.25, 0.49, 0.5, 0.99]
#BUCLE FOR EACH: Es un tipo especial de bucle for que sirve para recorrer todos los elementos de una lista, 
#tupla o diccionario, su sintaxis es la siguiente: 
# - for i in lista: 
#La instrucción del Bucle for each es equivalente a poner la instrucción: 
# - for i in range(0, len(lista)):
#Es importante mencionar que al usar el bucle for each, la variable del Bucle ahora será manejada como si fuera 
#una lista en sí a la cual se le están accediendo todos sus valores, por lo cual ahora usar esta variable 
#corresponde a haber accedido a cada valor de la lista que recorra el bucle:
# - i = lista[i]
for n in numSumasFourier:
    print ("Número de sumas de Fourier: ", n)
    print ("1.- t = ", α[0], "*2π \t\tf(t, T) = ", f(tiempo[0], T), "\t\tS(t, n, T) = ", S(tiempo[0], n, T), "\tError = %", 100*abs(S(tiempo[0], n, T) - f(tiempo[0], T)))
    print ("2.- t = ", α[1], "*2π \t\tf(t, T) = ", f(tiempo[1], T), "\t\tS(t, n, T) = ", S(tiempo[1], n, T), "\tError = %", 100*abs(S(tiempo[1], n, T) - f(tiempo[1], T)))
    print ("3.- t = ", α[2], "*2π \t\tf(t, T) = ", f(tiempo[2], T), "\t\tS(t, n, T) = ", S(tiempo[2], n, T), "\tError = %", 100*abs(S(tiempo[2], n, T) - f(tiempo[2], T)))
    print ("4.- t = ", α[3], "*2π \t\tf(t, T) = ", f(tiempo[3], T), "\t\tS(t, n, T) = ", S(tiempo[3], n, T), "\tError = %", 100*abs(S(tiempo[3], n, T) - f(tiempo[3], T)))
    print ("5.- t = ", α[4], "*2π \t\tf(t, T) = ", f(tiempo[4], T), "\t\tS(t, n, T) = ", S(tiempo[4], n, T), "\tError = %", 100*abs(S(tiempo[4], n, T) - f(tiempo[4], T)))