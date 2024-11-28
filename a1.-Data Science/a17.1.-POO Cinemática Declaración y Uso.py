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

#POO: La programación orientada a objetos es una forma de estructurar programas y aplicaciones de tal forma que 
#los datos y las operaciones con estos se agrupan en clases para que se puedan acceder a estos por medio de 
#objetos.
#1.-Y: Clase que utiliza la fórmula cinemática de Movimiento Rectilíneo Uniformemente Acelerado para calcular 
#la posición de una partícula.

#DECLARACIÓN DE LA CLASE Y:
class Y:
    #CONSTRUCTOR O INICIALIZADOR DE LA CLASE: En él se declaran los atributos que se reutilizarán en los demás 
    #métodos y que además, deben a fuerza de tener un valor.
    def __init__(self, y0, v0): #Los argumentos o parámetros del constructor de la clase Y son y0 y v0.
        #self lo que hace es referenciar métodos o datos de la clase donde nos encontramos, es una referencia 
        #a lo que sea que pertenezca a esta clase
        self.y0 = y0    #Atributo 1 de la clase Y = y0 = Posición inicial (Altura inicial)
        self.v0 = v0    #Atributo 2 de la clase Y = v0 = Velocidad inicial
        self.g = 9.81   #Atributo 3 de la clase Y = g = Aceleración de gravedad [m/s^2]
        #El operador self lo que hace es referenciar no a la variable local del constructor, sino a la variable
        #de instancia declarada dentro de la clase, de esta manera indicamos que a la variable de instancia y0 
        #se le asigna el valor del parámetro y0 del cosntructor. En python las variables de instancia no se 
        #declaran de forma explícita en la clase, pero de esta manera se indica que el parámetro de la función
        #hace referencia a dicha variable de instancia que pertenece a esta clase en específico.


    #MÉTODO RESULTADO: Recibe como parámetros los mismos que el constructor (y0 y v0), pero además la variable t.
    #Evaluación de la fórmula a través de un método llamado resultado, este hace lo mismo que el método __call__ 
    #lo que tiene de especial este método es la forma en la que se manda a llamar fuera de la clase, pero en sí 
    #podemos hacer que realice la operación que sea y solo puede existir un método __call__ por cada clase.
    def resultado(self, t):
        #Fórmula de la Caída Libre (Movimiento Rectilíneo Uniformemente Acelerado o MRUA):
        #y = y0 + v0*t +1/2(g*t^2); El exponente en Python se denota poniendo 2 signos de multiplicación; ^ = **
        #y = Altura, y0 = Altura inicial
        #v0 = Velocidad inicial
        #t = Tiempo
        #g = Gravedad
        return self.y0 + self.v0*t + 0.5*self.g*t**2


    #MÉTODO CALL: Este método es propio del lenguaje de programación Python y para utilizarze se declarar el 
    #nombre del objeto y sus parámetros, a diferencia de los demás donde se declara el nombre del objeto más el 
    #nombre del método:
    # - ObjetoClase(parámetro1, parámetro2, ..., parámetro_n)                       Método call
    # - ObjetoClase.NombreMétodo(parámetro1, parámetro2, ..., parámetro_n)          Método cualquiera
    #Solo puede existir un método call por clase y este trabaja con los atributos del constructor y puede 
    #incluir otros.
    def __call__(self, t):
        return self.y0 + self.v0*t + 0.5*self.g*t**2 


    #MÉTODO FÓRMULA: Método de la clase para imprimir en pantalla el resultado de la operación.
    def formula(self):
        #print(): Imprimir un mensaje en consola.
        print("y = %g + %g*t + 0.5*%g*t^2"%(self.y0, self.v0, self.g))



#USO DE LA CLASE Y:
#Operaciones con la clase y, creando un objeto que la instancíe.
y0 = 10
v0 = 5
objeto_y = Y(y0, v0)    #Creación del objeto o instancia de la clase Y
t = 10                  #Evaluar en el tiempo t = 100 segundos en el método resultado
#Utilización del método llamado resultado perteneciente a la clase Y para resolver la ecuación de MRUA: Realiza 
#la operación de la ecuación de Movimiento Rectilíneo Uniformemente Acelerado (MRUA).
y_resultado = objeto_y.resultado(t)
print("Método resultado = ", y_resultado)
#Utilización del método call de la clase Y, como es especial no se debe indicar su nombre: Realiza la operación.
y_call = objeto_y(t)
print("Método __call__ = ", y_call)
#Utilización del método formula de la clase Y: Este sirve para imprimir en consola el resultado de la operación.
objeto_y.formula() 
#De esta manera se puede acceder al atributo y0 del constructor perteneciente a la clase Y:
objeto_y.y0 = 0
print(objeto_y(t))
objeto_y.formula()



#GRÁFICACIÓN DEL MOVIMIENTO RECTILÍNEO UNIFORMEMENTE ACELERADO:
import matplotlib.pyplot as plt #matplotlib: Librería de graficación matemática.
import numpy as np #Librería numpy: Realiza operaciones matemáticas complejas (matriciales) y manejar datos.

#Lista vacía para rellenarla con los valores de la distancia y para cada tiempo de t.
y_graph = []
#Bucle for que va de 0 a t-1, ya que el valor de t nunca lo toca
for i in range (0, t):
    #append(): Lo que hace es agregar un elemento a la lista (array de python).
    #Para obtener el resultado de la altura se debe usar una instancia de la clase que use el metodo resultado().
    y_graph.append(objeto_y.resultado(i))

#numpy.linspace(): Método que rellena de números un vector, indicando su número de inicio, número final y número 
#de datos.
t_graph = np.linspace(0, t, t) #Vector que va del número 0 al 15 y se compone de 15 datos.
print("Eje horizontal:\n", t_graph, "\n", "Eje vertical:\n", y_graph)



#MATPLOTLIB: Graficación sin un estilo de Programación Orientada a Objetos
#matplotlib.figure(): Método para ordenar los figures (ventanas) donde se muestran las diferentes gráficas.
plt.figure(1)
#matplotlib.plot(): Método usado para crear la gráfica, indicando como primer parámetro su eje horizontal, luego 
#su eje vertical y finalmente el estilo de la gráfica.
# - Colores:            C1: color naranja, r: color rojo, b: color azul, g: verde, c: cyan, m: morado, 
#   y: amarillo, k: negro, w: blanco.
# - Tipo de marcadores: o: círculos, +: símbolos de más, .; puntos, v: Triángulo hacia abajo, h: Hexágono, 
#   s: cuadrados, 1: tri abajo, 2: tri arriba, 3: tri izquierda, 4: tri derecha, etc.
# - Tipo de Líneas:     -: sólida, --: punteada (líneas), :: punteada (puntos), -.: línea y punto, 'or': Nada.
#numpy.sin(x): Con la librería numpy se pueden crear los datos de amplitud de la gráfica del seno por medio de un 
#vector x que indique los datos del eje horizontal.
plt.plot(t_graph, y_graph, 'm3:') #'m3:' significa m: color magenta, 3: simbolo de tri izquierda, :: línea punteada
#matplotlib.title(): Título del figure.
plt.title(r'MATPLOTLIB: Sin POO')
#matplotlib.xlabel(): Texto que aparece en el eje horizontal.
plt.xlabel(r'$t = tiempo [seg]$')
#matplotlib.ylabel(): Texto que aparece en el eje vertical.
plt.ylabel(r'$y = altura [m]$')
#matplotlib.show(): Método para mostrar la gráfica creada.
plt.show()



#PYPLOT: Graficación con un estilo de Programación Orientada a Objetos, se crea el objeto ax de la clase plt.
fig = plt.figure(2)
#matplotlib.axes(): Método orientado a objetos usado para crear la rejilla en la ventana de graficación.
ax = plt.axes()
#axes.plot(): Método usado para crear la gráfica en la rejilla previamente creada en la ventana de graficación, 
#indicando como primer parámetro su eje horizontal, luego su eje vertical y finalmente el estilo de la gráfica:
# - Colores:            C1: color naranja, r: color rojo, b: color azul, g: verde, c: cyan, m: morado, 
#   y: amarillo, k: negro, w: blanco.
# - Tipo de marcadores: o: círculos, +: símbolos de más, .; puntos, v: Triángulo hacia abajo, h: Hexágono, etc.
# - Tipo de Líneas:     -: sólida, --: punteada (líneas), :: punteada (puntos), -.: línea y punto, 'or': Nada.
ax.plot(t_graph, y_graph, 'r.-') #'r.-' significa r: color rojo, .: simbolo de punto, -: línea sólida
#axes.set_title(): Título del figure.
ax.set_title(r'PYPLOT: Con POO')
#axes.set_xlabel(): Método para indicar el texto que aparece en el eje x.
ax.set_xlabel(r'$t$')
#axes.set_ylabel(): Método para indicar el texto que aparece en el eje y.
ax.set_ylabel(r'$y = y0 + v0*t +(g*t^2)/2$')
#axes.set_facecolor(): Método para indicar el color de fondo de la gráfica, el cual puede ser indicado por los 
#mismos colores previamente mencionados en el método plot() o se pueden usar los siguientes con el código xkcd:
# - Colores: xkcd:aqua, xkcd:aquamarine, xkcd:azure, xkcd:beige, etc. Los colores se obtienen de este link:
#https://matplotlib.org/stable/tutorials/colors/colors.html
ax.set_facecolor('xkcd:black')
#matplotlib.show(): Método para mostrar la gráfica creada.
plt.show()