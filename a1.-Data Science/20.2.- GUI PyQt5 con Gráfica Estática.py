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

#LIBRERÍAS:
#PyQt5 - QtWidgets: La clase QtWidgets proporciona todos los elementos que conforman las interfaces gráficas 
#(GUI) hechas con la librería PyQt5, entre dichas herramientas se incluyen: 
# - Widgets: Elementos gráficos básicos de los que se conforma una GUI como lo son botones (QPushButton), cajas 
#   de texto (QLineEdit), texto estático (QLabel), listas desplegables (QComboBox), barras de progreso 
#   (QProgressBar), casillas de verificación (QCheckBox), imágenes (QLabel), etc.
#   - Diálogos: Los diálogos son elementos gráficos que  facilitan la interacción con el usuario, incluyen 
#     widgets como cuadros de diálogo de mensajes (QMessageBox), cuadros de diálogo para seleccionar archivos o 
#     directorios (QFileDialog), cuadros de diálogo de entrada de texto (QInputDialog), etc.
# - Layouts: Es un contenedor de PyQt5 que permite almacenar y organizar varios widgets, es el equivalente al 
#   Panel de la librería wxPython.
#           - Widget: Es un contenedor que puede almacenar widgets directamente, proporcionando funcionalidades 
#             para mostrar, ocultar, establecer posición, tamaño, manejar eventos, etc. de los diferentes 
#             botones, checkboxes, áreas de texto, comboboxes, radiobuttons, listboxes, etc.
# - Ventana: Es la ventana principal de la GUI, que a su vez contiene todos los contenedores con los widgets que 
#   conforman la GUI, se declara a través de la clase QMainWindow de la librería pyQt5 y es el equivalente al 
#   Frame de wxPython.
from PyQt5 import QtWidgets
#matplotlib - Figure: La clase Figure es la base para crear y organizar los elementos gráficos en Matplotlib, 
#que es una librería de graficación matemática.
from matplotlib.figure import Figure
#matplotlib - FigureCanvasQTAgg: La clase FigureCanvasQTAgg proporcionada por la biblioteca Matplotlib en el 
#módulo matplotlib.backends.backend_qt5agg se utiliza para mostrar y manejar gráficos generados por Matplotlib 
#dentro de una ventana o contenedor de pyQt5. En este caso se utiliza para mostrar una gráfica que podría 
#actualizar sus datos en tiempo real o no, en este caso se mantendrá estática.
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
import sys #sys: Librería que permite interactuar directamente con el sistema operativo y consola del ordenador.

#GUI (Graphical User Interface): Es una ventana con elementos como botones, áreas de texto, desplegables, 
#imágenes, etc. que sirven para realizar alguna acción de forma gráfica para el usuario. A continuación, veremos 
#como se crean este tipo de elementos en Python utilizando la librería wxPython o PyQt5.
#La librería PyQt5 es una muy utilizada y versátil, su programación es mas sencilla y reducida en comparación 
#con la librería wxPython, pero su principal desventaja y diferencia es que PyQt5 está disponible bajo dos 
#licencias: una licencia comercial y una licencia GPL de código abierto, esto significa que si se desea 
#desarrollar aplicaciones comerciales con PyQt5, se deberá adquirir una licencia comercial. Por otro lado, 
#wxPython se distribuye bajo una licencia de código abierto y permite su uso tanto en aplicaciones comerciales 
#como en proyectos de código abierto. 

#GraficaPyQt5: Esta clase propia hereda de la clase FigureCanvasQTAgg, que pertenece a la librería PyQt5 y 
#permite mostrar gráficos generados por Matplotlib en un Widget de PyQt5, permitiendo manejar eventos de 
#interacción del usuario, como hacer zoom, seleccionar puntos en el gráfico, etc.
class GraficaPyQt5(FigureCanvasQTAgg):
    #CONSTRUCTOR O INICIALIZADOR DE LA CLASE: En él se declaran los atributos que se reutilizarán en los demás 
    #métodos y que además, deben a fuerza de tener un valor. Los parámetros que puede recibir el constructor de 
    #la clase son los siguientes:
    # - figure: La instancia de la clase Figure que se va a asociar con el lienzo. Por defecto, se establece en 
    #   None. Este parámetro es el primero y no usa la sintaxis: figure = valor, solamente se pone.
    # - parent: El widget padre al que se asocia el lienzo. Por defecto, se establece en None.
    # - width: El ancho del lienzo en píxeles o pulgadas. En este caso solo se indica un valor inicial pero el 
    #   ancho real será asignado cuando se cree una instancia de la clase.
    # - height: La altura del lienzo en píxeles o pulgadas. En este caso solo se indica un valor inicial pero el 
    #   ancho real será asignado cuando se cree una instancia de la clase.
    # - dpi: La resolución del lienzo en puntos por pulgada. Por defecto, se establece en 80 y puede afectar al 
    #   tamaño de la gráfica.
    # - bgcolor: Indica el color de fondo del lienzo. Puede ser especificado a través de las siguientes formas:
    #       - Nombre color: Por medio de un string se pueden declarar valores que reconoce Matplotlib como por 
    #         ejemplo, white', 'red', 'blue', etc.
    #       - Tupla RGB: Por medio de una tupla se especifican los tonos de color RGB (Rojo, Verde Azul) con 
    #         valores que van de 0 a 1, como por ejemplo, (1, 1, 1) para blanco.
    def __init__(self, parent = None, width = None, height = None, dpi = 120, bgcolor = (0.8, 0, 0)):
        #Figure(): Constructor de la clase Figure perteneciente a la librería Matplotlib, usado para crear un 
        #lienzo en el que se puedan dibujar gráficos, actúando como un contenedor para los subgráficos.
        #A este objeto se le pueden asignar los parámetros indicados en el constructor de la clase 
        #FigureCanvasQTAgg.
        fig = Figure(figsize = (width, height), dpi = dpi)
        #matplotlib.Figure().set_facecolor(): Método que sirve para establecer el color de fondo de una gráfica. 
        #A este objeto se le puede asignar el parámetros bgcolor indicado en el constructor de la clase 
        #FigureCanvasQTAgg.
        fig.set_facecolor(bgcolor)
        #matplotlib.Figure().add_subplot(): Método aplicado a un objeto de la clase Figure, perteneciente a la 
        #librería Matplotlib, lo que hace es agregar un subgráfico al lienzo vacío, los números de su parámetro 
        #lo que indican es:
        # - Primer Número:  Indica el número de filas de las subgráficas.
        # - Segundo Número: Indica el número de columnas de las subgráficas.
        # - Tercer Número:  Indica el índice de la subgráfica que se está creando en específico.
        #El parámetro 111 crea una sola gráfica de una columna con un solo espacio para mostrar una gráfica.
        #Se declaran como self.nombreObjeto los widgets a los que se les vaya a extraer o introducir datos en el 
        #transcurso del funcionamiento de la interfaz gráfica.
        self.axes = fig.add_subplot(111)
        #super(Llamada al constructor heredado).__init__(Parámetros que se le asignan): Lo que hace el método 
        #super() es llamar al constructor de la clase padre de la clase actual (si es que no se le indica ningún 
        #parámetro) o a cualquier clase que se le indique en su parámetro, después la instrucción .__init__() 
        #asigna valores default a los parámetros del constructor de la clase padre (si es que no se indica 
        #ningún parámetro), aunque de igual manera se pueden asignar parámetros adicionales, cualquier parámetro 
        #incluido en el método init, será considerado como adicional. En conclusión, lo que está realizando la 
        #línea de código es primero llamar al constructor de la superclase para realizar las tareas de 
        #inicialización requeridas antes de indicar parámetros adicionales a la instancia de la clase actual.
        super(GraficaPyQt5, self).__init__(fig) #Asigna el objeto fig al constructor de la clase GraficaPyQt5.



#MainWindow: La clase hereda de la clase QMainWindow, que a su vez hereda de la clase QtWidgets y ambas 
#pertenecen a la librería PyQt5. El elemento representa la ventana del GUI y crea una instancia de la clase 
#GraficaPyQt5 para agregar dentro de la ventana una gráfica.
class MainWindow(QtWidgets.QMainWindow):
    #CONSTRUCTOR O INICIALIZADOR DE LA CLASE: En él se declaran los atributos que se reutilizarán en los demás 
    #métodos y que además, deben a fuerza de tener un valor.
    def __init__(self):
        #super(Llamada al constructor heredado).__init__(Parámetros que se le asignan): Lo que hace el método 
        #super() es llamar al constructor de la clase padre de la clase actual (si es que no se le indica ningún 
        #parámetro) o a cualquier clase que se le indique en su parámetro, después la instrucción .__init__() 
        #asigna valores default a los parámetros del constructor de la clase padre (si es que no se indica 
        #ningún parámetro), aunque de igual manera se pueden asignar parámetros adicionales, cualquier parámetro 
        #incluido en el método init, será considerado como adicional. En conclusión, lo que está realizando la 
        #línea de código es primero llamar al constructor de la superclase para realizar las tareas de 
        #inicialización requeridas antes de indicar parámetros adicionales a la instancia de la clase actual.
        super(MainWindow, self).__init__() #Asigna parámetros estándar al constructor de la clase MainWindow.
        #PyQt5.QtWidgets.QMainWindow.setWindowTitle(): Método para colocar un título al Window creado con PyQt5.
        self.setWindowTitle("Mi GUI con PyQt5")

        #Instancia de la clase GraficaPyQt5 para agregar la gráfica al Window, se le debe pasar como parámetro 
        #al constructor de la clase GraficaPyQt5, los parámetros que se quiera editar para que no se ejecuten 
        #los que vienen declarados por defecto, los que no se editen, se ejecutarán con el valor que fueron 
        #declarados arriba en el constructor.
        sc = GraficaPyQt5(self, width = 7, height = 6, dpi = 100)
        
        #matplotlib.Figure.add_subplot().plot(): Método usado para gráficar, indicando como primer parámetro su 
        #eje horizontal, luego su eje vertical y finalmente el estilo de la gráfica:
        # - Colores:             C1: color naranja, r: color rojo, b: color azul, g: verde, c: cyan, m: morado, 
        #   y: amarillo, k: negro, w: blanco.
        # - Tipo de marcadores:  o: círculos, +: símbolos de más, .; puntos, v: Triángulo hacia abajo, h: 
        #   Hexágono, etc.
        # - Tipo de Líneas:      -: sólida, --: punteada (líneas), :: punteada (puntos), -.: línea y punto, 
        #   'or': Nada.
        #Los marcadores se pueden obtener del siguiente link: https://matplotlib.org/stable/api/markers_api.html
        sc.axes.plot([0, 1, 2, 3, 4], [10, 1, 20, 3, 40], 'r1:') #'r1:' r: color rojo, 1: tri_down, :: línea punteada
        #matplotlib.Figure().add_subplot().set_xlabel(): Método para indicar el texto que aparece en el eje 
        #horizontal de la gráfica, recibe los siguientes parámetros:
        # - xlabel: Especifica el texto que se mostrará en el eje x.
        # - fontname: Indica el estilo de la fuente:
        #       - Nombres de tipos de letra estándar: "Arial", "Times New Roman", "Helvetica", "Courier", 
        #         "Monospaced", "Consolas", etc. Estos nombres deben ser compatibles con los tipos de letra 
        #         instalados en el sistema operativo.
        #       - Nombres de tipos de letra genéricos: "serif", "sans-serif", "monospace", etc.
        #       - Rutas de archivo: Si se tiene un archivo de tipo de letra personalizado, se puede especificar 
        #         la ruta del archivo como el valor de fontname.
        # - fontsize: Indica el tamaño de la fuente.
        # - labelpad: Especifica el espaciado entre la etiqueta del eje x y el eje en sí.
        sc.axes.set_xlabel(xlabel = "x", fontname = "Consolas", fontsize = 15)
        #matplotlib.Figure.add_subplot().set_ylabel(): Método para indicar el texto que aparece en el eje y.
        sc.axes.set_ylabel(ylabel = "y", fontname = "Consolas", fontsize = 15)
        #matplotlib.Figure.add_subplot().set_facecolor(): Método para indicar el color de fondo de la gráfica, 
        #el cual puede ser indicado por los mismos colores previamente mencionados en el método plot() o se 
        #pueden usar los siguientes con el código xkcd:
        # - Colores: xkcd:aqua, xkcd:aquamarine, xkcd:azure, xkcd:beige, etc. Los colores se obtienen de:
        #https://matplotlib.org/stable/tutorials/colors/colors.html
        sc.axes.set_facecolor('xkcd:black')
        
        #PyQt5.QtWidgets.QMainWindow.setCentralWidget() = self.setCentralWidget(): Método aplicado al objeto de 
        #la clase QMainWindow, del que hereda esta clase propia para establecer el widget central de la ventana 
        #principal, ya que en PyQt5 las ventanas generalmente se dividen en diferentes áreas:
        # - Una barra de menú en la parte superior, para ello se debe indicar que objeto es el menu bar.
        #       - widget.setMenuBar(widget, QMenuBar)
        # - Una barra de herramientas opcional en la parte superior o inferior.
        #       - widget.setStatusBar(widget, QStatusBar)
        # - Un área central donde se coloca el contenido principal de la ventana. 
        #       - widget.setCentralWidget(widget)
        #El método setCentralWidget() se utiliza para especificar qué widget se debe colocar en el área central
        #de la ventana creada con esta clase propia.
        self.setCentralWidget(sc)


#__name__ == __main__: Método main, esta función es super importante ya que sirve para instanciar las clases del 
#programa y ejecutar sus métodos, en python pueden existir varios métodos main en un solo programa, aunque no es 
#una buena práctica.
if(__name__ == "__main__"):
    #Instancia de la librería PyQt5 por medio del constructor de la clase QApplication, que hereda de la clase 
    #QtWidgets para crear un objeto que funcione como la base de una GUI.
    # - sys.argv: Se refiere a un vector llamado "argument vector" que puede ser accedido desde la librería sys, 
    #   este incluye en su contenido el nombre del archivo que se quiere ejecutar y los argumentos necesarios 
    #   que se le deben pasar para que efectúe su ejecución. Se le debe pasar como parámetro al constructor de 
    #   la clase QApplication para que se pueda crear la base de la GUI.
    #       - Por ejemplo, si se ejecutara el siguiente comando en consola:
    #           python mi_script.py arg1 arg2 arg3
    #         El contenido de sys.argv sería:
    #           ['mi_script.py', 'arg1', 'arg2', 'arg3']
    app = QtWidgets.QApplication(sys.argv)
    #Instancia de nuestra clase propia llamada MainWindow que fue creada en este mismo programa (window se 
    #refiere a la ventana del GUI en PyQt5) e incluye una instancia de la clase GraficaPyQt5 para agregar un 
    #widget que crea una gráfica dentro, el constructor vacío lo que hace es indicar que se cree y muestre la 
    #ventana.
    window = MainWindow()
    #PyQt5.QtWidgets.QMainWindow.move() = window.move(): Método utilizado para indicar la posición inicial de 
    #la ventana dentro de la pantalla del ordenaror, este método recibe como parámetro una tupla que indica la 
    #posición:
    # - (x, y): Con este atributo se indica la posición inicial del Frame en pixeles, siendo la posición 0,0 la 
    #   esquina superior izquierda, donde las "y" positivas indican que se mueva el botón hacia abajo y las "x" 
    #   positivas hacia la derecha.
    window.move(100, 100)
    #PyQt5.QtWidgets.QMainWindow.show() = window.show(): Método aplicado al objeto de la clase QMainWindow, 
    #del que hereda esta clase propia para mostrar la ventana del GUI.
    window.show()
    #PyQt5.QtWidgets.QApplication.exec_(): Método para que se ejecute en un loop infinito el GUI, logrando así 
    #que no se ejecute una vez y luego cierre por sí solo, sino que solo se cierre solamente al dar clic en el 
    #tache del window.
    app.exec_()