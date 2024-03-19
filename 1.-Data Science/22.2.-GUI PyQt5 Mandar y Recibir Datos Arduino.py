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
#   Panel de la librería PyQt5.
#           - Widget: Es un contenedor que puede almacenar widgets directamente, proporcionando funcionalidades 
#             para mostrar, ocultar, establecer posición, tamaño, manejar eventos, etc. de los diferentes 
#             botones, checkboxes, áreas de texto, comboboxes, radiobuttons, listboxes, etc.
# - Ventana: Es la ventana principal de la GUI, que a su vez contiene todos los contenedores con los widgets que 
#   conforman la GUI, se declara a través de la clase QMainWindow de la librería pyQt5 y es el equivalente al 
#   Frame de PyQt5.
from PyQt5 import QtWidgets
#PyQt5 - QtCore: Clase que incluye métodos para trabajar con temporizadores, tamaño de elementos, fechas, 
#archivos, directorios, señales, hilos, subprocesos, etc.
from PyQt5 import QtCore
#PyQt5 - QtGui: Clase que incluye clases y métodos para trabajar con gráficos, fuentes, colores, imágenes, 
#íconos y otros elementos visuales utilizados en una interfaz gráfica (GUI) de PyQt5.
from PyQt5 import QtGui
#matplotlib - Figure: La clase Figure es la base para crear y organizar los elementos gráficos en Matplotlib, 
#que es una librería de graficación matemática.
from matplotlib.figure import Figure
#matplotlib - FigureCanvasQTAgg: La clase FigureCanvasQTAgg proporcionada por la biblioteca Matplotlib en el 
#módulo matplotlib.backends.backend_qt5agg se utiliza para mostrar y manejar gráficos generados por Matplotlib 
#dentro de una ventana o contenedor de pyQt5. En este caso se utiliza para mostrar una gráfica que podría 
#actualizar sus datos en tiempo real o no, en este caso se mantendrá estática.
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
import numpy as np #numpy: Librería que realiza operaciones matemáticas complejas (matriciales).
import serial #serial: Librería que establece una comunicación serial con  microcontroladores, módems, etc.
import sys #sys: Librería que permite interactuar directamente con el sistema operativo y consola del ordenador.
import glob #glob: Librería que sirve para buscar archivos o directorios.
#pyfirmata: Librería que permite la comunicación bidireccional entre Python y Arduino, brindando control y 
#monitoreo de sus pines digitales y analógicos, envío de señales PWM, lectura y escritura de datos y establecer
#una comunicación a través de los protocolos I2C y Serial. La comunicación entre Arduino y Python se realiza 
#utilizando el protocolo Firmata, el cual permite controlar y monitorear dispositivos conectados a una placa 
#Arduino desde un software de computadora, para habilitarlo, primero se debe subir el programa:
#21.-Stardard_Firmata_Mandar_Datos_Arduino.ino a la placa de desarrollo a través del IDE de Arduino.
import pyfirmata

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
    # - width: El ancho del lienzo en píxeles o pulgadas.
    # - height: La altura del lienzo en píxeles o pulgadas.
    # - dpi: La resolución del lienzo en puntos por pulgada. Por defecto, se establece en 80 y puede afectar al 
    #   tamaño de la gráfica.
    # - bgcolor: Indica el color de fondo del lienzo. Puede ser especificado a través de las siguientes formas:
    #       - Nombre color: Por medio de un string se pueden declarar valores que reconoce Matplotlib como por 
    #         ejemplo, white', 'red', 'blue', etc.
    #       - Tupla RGB: Por medio de una tupla se especifican los tonos de color RGB (Rojo, Verde Azul) con 
    #         valores que van de 0 a 1, como por ejemplo, (1, 1, 1) para blanco.
    def __init__(self, parent = None, width = None, height = None, dpi = 100, bgcolor = (0.077, 0.025, 0.024)):
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
        # - labelpad: Especifica el espaciado entre la etiqueta del eje x y el eje en sí
        # - color: Indica el color del texto colocado en el eje x, para ello es válido usar colores: 
        #       - Básicos CSS: como "red", "blue", "green", etc. 
        #       - Colores hexadecimales: "#FF0000", "#00FF00", etc. 
        #       - Colores RGB: "rgb(255,255,255)" para el color blanco y "rgb(0,0,0)" para el negro.
        self.axes.set_xlabel(xlabel = "Time [s]", fontname = "Consolas", fontsize = 8, color = "white")
        #matplotlib.Figure.add_subplot().set_ylabel(): Método para indicar el texto que aparece en el eje y.
        self.axes.set_ylabel(ylabel = "Voltage [V]", fontname = "Consolas", fontsize = 8, color = "white")
        #matplotlib.Figure().add_subplot().tick_params(): Método para acceder a las propiedades gráficas de los 
        #números que aparecen en los ejes de la gráfica creada con la librería matplotlib.
        # - axis: Indica el eje que se quiere afectar, ya sea 'x', 'y', 'both' o 'all'.
        # - colors: Indica el color de los números colocados en el eje x o y, para ello es válido usar colores: 
        #       - Básicos CSS: como "red", "blue", "green", etc. 
        #       - Colores hexadecimales: "#FF0000", "#00FF00", etc. 
        #       - Colores RGB: "rgb(255,255,255)" para el color blanco y "rgb(0,0,0)" para el negro.
        # - labelsize: Permite especificar el tamaño de letra en pixeles.
        # - pad: espacio entre las marcas y las etiquetas en puntos.
        self.axes.tick_params(axis = "x", colors = "white", labelsize = 8)
        self.axes.tick_params(axis = "y", colors = "white", labelsize = 8)
        #matplotlib.Figure.add_subplot().set_facecolor(): Método para indicar el color de fondo de la gráfica, 
        #el cual puede ser indicado por los mismos colores previamente mencionados en el método plot() o se 
        #pueden usar los siguientes con el código xkcd:
        # - Colores: xkcd:aqua, xkcd:aquamarine, xkcd:azure, xkcd:beige, etc. Los colores se obtienen de:
        #https://matplotlib.org/stable/tutorials/colors/colors.html
        self.axes.set_facecolor('#180000')
        
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
        self.setWindowTitle("Instrumentación Virtual - PyQt5 y Pyfirmata con Arduino")
        
        #Instancia de la clase GraficaPyQt5 para agregar la gráfica al Window, se le debe pasar como parámetro 
        #al constructor de la clase GraficaPyQt5, los parámetros que se quiera editar para que no se ejecuten 
        #los que vienen declarados por defecto, los que no se editen, se ejecutarán con el valor que fueron 
        #declarados arriba en el constructor.
        self.canvas = GraficaPyQt5(self, width = 5, height = 4, dpi = 120)
        
        #CREACIÓN DE LOS WIDGETS: Botón
        #Instancia de la librería PyQt5 por medio del constructor de la clase QPushButton que hereda de la clase 
        #QtWidgets y sirve para crear un widget de tipo botón, en este se deben indicar como parámetros:
        # - parent: Especifica el objeto padre al que se asociará el botón. Si se proporciona, el botón se 
        #   colocará dentro del widget padre.
        # - text: Con este parámetro se indica el texto que aparecerá sobre el botón.
        # - icon: Establece el ícono que se mostrará junto al texto del botón, debe utilizarse un objeto QIcon 
        #   perteneciente a la librería QtGui para que se pueda agregar un ícono.
        # - checkable: Especifica si el botón funciona como un switch (que mantiene su estado) o como un push 
        #   button (que no mantiene su estado a menos que se mantenga presionado).
        #       - checkable = True:     Botón tipo switch.
        #       - checkable = False:    Botón tipo push button.
        # - autoDefault: Indica si el botón es el predeterminado del diálogo. Si se establece en True, el botón 
        #   responderá automáticamente a la tecla "Enter", sino no lo hará.
        # - flat: Con False se indica que el botón se muestre sin un marco, con True aparece el marco.
        # - menu: Especifica el menú desplegable asociado al botón.
        # - iconSize: Establece el tamaño del ícono del botón, para ello recibe un objeto QSize:
        #       - QtCore.QSize(ancho, alto): Objeto que indica el tamaño del ícono.
        #CREACIÓN DE ÍCONO PARA INCLUIR EN EL BOTÓN:
        #Variable que guarda el directorio y el nombre del archivo creado, se reemplazan los guiones \ por / 
        #para poder leer una imagen o cualquier otro archivo, se usa la dirección relativa o absoluta de un 
        #directorio: 
        # - Dirección relativa: Es una dirección que busca un archivo desde donde se encuentra la carpeta del 
        #   archivo python actualmente, esta se debe colocar entre comillas simples o dobles.
        # - Dirección absoluta: Es una dirección que coloca toda la ruta desde el disco duro C o cualquier otro 
        #   que se esté usando hasta la ubicación del archivo, la cual se debe colocar entre comillas simples o 
        #   dobles.
        #   ..      : Significa que nos debemos salir de la carpeta donde nos encontramos actualmente.
        #   /       : Sirve para introducirnos a alguna carpeta cuyo nombre se coloca después del slash.
        #   .ext    : Se debe colocar siempre el nombre del archivo + su extensión.
        iconPath = "C:/Users/diego/OneDrive/Documents/The_MechaBible/p_Python_ESP/1.-Data Science/0.-Archivos_Ejercicios_Python/Img/LogoBlancoDi_cer0.png"
        #PyQt5.QtGui.QIcon(): Constructor de la clase QIcon que hereda de la clase QtGui y perteneciente a la 
        #librería PyQt5, usado para crear un objeto que ícono que pueda ser añadido a cualquier widget como lo 
        #puede ser un botón, un texto estático, etc. El tamaño de dicha imagen será reducido automáticamente.
        logoDicer0 = QtGui.QIcon(iconPath)
        #Se declaran como self.nombreObjeto los widgets a los que se les vaya a extraer o introducir datos en el 
        #transcurso del funcionamiento de la interfaz gráfica, en este caso se aplica al botón porque este va a 
        #cambiar el texto que tiene escrito cuando sea presionado.
        self.btn_start = QtWidgets.QPushButton(text = "\t\t\t\tStart", icon = logoDicer0, iconSize = QtCore.QSize(30, 30))
        self.btn_stop = QtWidgets.QPushButton(text = "\t\t\t\tStop", icon = logoDicer0, iconSize = QtCore.QSize(30, 30))
        self.btn_save = QtWidgets.QPushButton(text = "\t\t\t\tSave", icon = logoDicer0, iconSize = QtCore.QSize(30, 30))
        #widget.setStyleSheet(): Método que permite aplicar código CSS (la mayoría de métodos, no todos) a los 
        #widgets de una interfaz gráfica de usuario (GUI).
        # - La siguiente línea de código es un método alternativo a usar la herramienta linear-gradient, ya que 
        #   esta no es admitida por PyQt5:
        #   background: qlineargradient(x1:punto_inicial, y1:punto_inicial, x2:punto_final, y2:punto_final, stop:0 rgb(R_inicial,G_inicial,B_inicial), stop:1 rgb(R_final,G_final,B_final));
        self.btn_start.setStyleSheet("background: qlineargradient(x1:0, y1:1, x2:0, y2:0, stop:0 rgb(255,230,181), stop:1 rgb(150,0,0));")
        self.btn_stop.setStyleSheet("background: qlineargradient(x1:0, y1:1, x2:0, y2:0, stop:0 rgb(255,255,255), stop:1 rgb(91,150,242));")
        self.btn_save.setStyleSheet("background: qlineargradient(x1:0, y1:1, x2:0, y2:0, stop:0 rgb(255,255,255), stop:1 rgb(198,132,0));")
        #widget.Hide(): Método que sirve para esconder un widget en la GUI.
        self.btn_stop.hide()            #Esconde inicialmente el botón de STOP
        self.btn_save.hide()            #Esconde inicialmente el botón de SAVE

        #CREACIÓN DE LOS WIDGETS: Texto Estático, clase QLabel
        #Instancia de la librería PyQt5 por medio del constructor de la clase QLabel que hereda de la clase 
        #QtWidgets y sirve para crear un widget que muestre un texto estático o una imagen en una interfaz 
        #gráfica, se le deben indicar los siguientes parámetros cuando se usa para crear texto estático:
        # - parent: Especifica el widget padre del QLabel. Si se proporciona, el texto estático se colocará 
        #   dentro del widget padre.
        # - text: Permite especificar el texto que se mostrará en el widget. Puede ser una cadena de texto en 
        #   formato plano o enriquecido con etiquetas HTML.
        #Para dar estilo al QLabel cuando se utiliza para mostrar texto estático es mejor utilizar etiquetas 
        #HTML que contengan un style que les dé estilo por medio de instrucciones CSS, además es importante 
        #mencionar que para el style se deben usar comillas simples ('') para que no tenga conlficto con las 
        #comillas dobles del parámetro text = "". PyQt5 acepta algunas instrucciones CSS pero no todas.
        lbl_port = QtWidgets.QLabel("<p style='background: qlineargradient(x1:0, y1:1, x2:0, y2:0, stop:0 rgb(150,54,41), stop:1 rgb(64,15,34)); font-size: 15px; font-family: Courier New, monospace; color: white;'>Puerto COM:</p>")
        lbl_samples = QtWidgets.QLabel("<p style='background: qlineargradient(x1:0, y1:1, x2:0, y2:0, stop:0 rgb(150,54,41), stop:1 rgb(64,15,34)); font-size: 15px; font-family: Courier New, monospace; color: white;'>Número de Muestras:</p>")
        lbl_umbral = QtWidgets.QLabel("<p style='background: qlineargradient(x1:0, y1:1, x2:0, y2:0, stop:0 rgb(150,54,41), stop:1 rgb(64,15,34)); font-size: 15px; font-family: Courier New, monospace; color: white;'>Umbral Encendido LED [mV]:</p>") #Label del umbral

        #CREACIÓN DE LOS WIDGETS: Combo Box, Lista Desplegable
        #Instancia de la librería PyQt5 por medio del constructor de la clase QComboBox que hereda de la clase 
        #QtWidgets y sirve para crear un widget que muestre una lista desplegable de elementos seleccionables 
        #en una ventana o layout.
        self.cb_port = QtWidgets.QComboBox()    #Combo box para mostrar todos los puertos detectados
        #widget.setStyleSheet(): Método que permite aplicar código CSS (la mayoría de métodos, no todos) a los 
        #widgets de una interfaz gráfica de usuario (GUI).
        # - La siguiente línea de código es un método alternativo a usar la herramienta linear-gradient, ya que 
        #   esta no es admitida por PyQt5:
        #   background: qlineargradient(x1:punto_inicial, y1:punto_inicial, x2:punto_final, y2:punto_final, stop:0 rgb(R_inicial,G_inicial,B_inicial), stop:1 rgb(R_final,G_final,B_final));
        self.cb_port.setStyleSheet("font-size: 15px; font-family: Courier New, monospace; color: white; background: qlineargradient(x1:0, y1:1, x2:0, y2:0, stop:0 rgb(255,230,181), stop:1 rgb(150,0,0));")
        #QtWidgets.QComboBox.addItems(): Método que se utiliza para agregar una lista de elementos al combo box. 
        #Este puede recibir como parámetro directamente una lista, tupla o diccionario que representen los 
        #elementos que se agregarán al combo box o puede recibir una función propia que cree dicha lista, para 
        #luego añadir dichos elementos creados por la función al QComboBox.
        #Se ejecuta la función propia SerialPorts() declarada fuera del constructor pero dentro de la clase 
        #MainWindow para obtener los puertos disponibles del ordenador actual por medio de la clase serial.
        self.cb_port.addItems(self.SerialPorts())

        #CREACIÓN DE LOS WIDGETS: Spin Box, control numérico
        #Instancia de la librería PyQt5 por medio del constructor de la clase QSpinBox que hereda de la clase 
        #QtWidgets y sirve para crear un widget  que muestre un selector de números en una ventana o layout.
        spb_samples = QtWidgets.QSpinBox()      #Número de muestras.
        spb_umbral = QtWidgets.QSpinBox()       #Umbral de encendido para el led, indicado en milivolts [mV].
        #QtWidgets.QSpinBox.setMinimum(Valor_Mínimo): Método que indica el valor mínimo permitido en el control 
        #numérico SpinBox.
        spb_samples.setMinimum(1)               #Mínimo número de muestras.
        spb_umbral.setMinimum(0)                #Umbral de encendido mínimo para el led.
        #QtWidgets.QSpinBox.setMaximum(Valor_Máximo): Método que indica el valor máximo permitido en el control 
        #numérico SpinBox. El máximo de datos que puede recopilar un archivo de Excel sin fallar son 32,000.
        spb_samples.setMaximum(32000)           #Máximo número de muestras.
        spb_umbral.setMaximum(5000)             #Umbral de encendido máximo para el led.
        #QtWidgets.QSpinBox.setSingleStep(Intervalo): Indica de cuánto en cuanto avanza el valor numérico del 
        #SpinBox.
        spb_samples.setSingleStep(1)            #Intervalo número de muestras.
        spb_umbral.setSingleStep(1)             #Intervalo umbral de encendido del LED.
        #widget.setStyleSheet(): Método que permite aplicar código CSS (la mayoría de métodos, no todos) a los 
        #widgets de una interfaz gráfica de usuario (GUI).
        # - La siguiente línea de código es un método alternativo a usar la herramienta linear-gradient, ya que 
        #   esta no es admitida por PyQt5:
        #   background: qlineargradient(x1:punto_inicial, y1:punto_inicial, x2:punto_final, y2:punto_final, stop:0 rgb(R_inicial,G_inicial,B_inicial), stop:1 rgb(R_final,G_final,B_final));
        spb_samples.setStyleSheet("font-size: 15px; font-family: Courier New, monospace; color: white; background: qlineargradient(x1:0, y1:1, x2:0, y2:0, stop:0 rgb(255,230,181), stop:1 rgb(150,0,0));")
        spb_umbral.setStyleSheet("font-weight: 900; font-size: 16px; font-family: Courier New, monospace; color: aqua; background: qlineargradient(x1:0, y1:1, x2:0, y2:0, stop:0 rgb(255,230,181), stop:1 rgb(150,0,0));")

        #CONTENEDORES DE ELEMENTOS: La biblioteca PyQt5 ofrece varios tipos de contenedores que se pueden 
        #utilizar para organizar los widgets en una interfaz gráfica. Los más comunes son:
        # - QVBoxLayout: Organiza los widgets en una disposición vertical, uno debajo del otro.
        # - QHBoxLayout: Organiza los widgets en una disposición horizontal, uno al lado del otro.
        # - QGridLayout: Organiza los widgets en una cuadrícula bidimensional de filas y columnas.
        # - QFormLayout: Diseñado específicamente para crear formularios, donde los widgets se colocan en pares 
        #   de etiqueta y campo de entrada.
        # - QStackedLayout: Permite apilar varios widgets uno encima del otro y mostrar uno a la vez.
        # - QTabWidget: Permite crear pestañas donde se pueden colocar diferentes conjuntos de widgets en cada 
        #   pestaña.
        # - QScrollArea: Proporciona una vista desplazable para un contenido que puede ser mayor que el área 
        #   visible.
        # - QGroupBox: Crea un grupo que puede contener y organizar otros widgets.
        # - QSplitter: Permite dividir el área de visualización en secciones redimensionables que contienen 
        #   widgets diferentes.
        # - QWidget: Proporciona una ventana o área rectangular en la que se pueden colocar otros widgets para 
        #   crear una interfaz gráfica, un QWidget puede contener otros widgets o contenedores dentro.
        #Cuando se desee ordenar un contenedor de una forma específica dentro de un diseño o establecer ciertas 
        #características como altura, ancho, etc. Es necesario crear un widget que lo contenga, para ello se le 
        #debe pasar dicho widget como parámetro al contenedor, logrando así que el widget se convierta en el 
        #elemento padre del layout.
        # - parent: Si el constructor de esta clase recibe como parámetro un objeto QWidget, ese será el 
        #   contenedor principal del objeto QVBoxLayout que organiza sus elementos verticalmente.
        # - Si no recibe ningún parámetro, este es un contenedor vacío sin widget principal que aceptará 
        #   varios elementos o contenedores y los irá colocando verticalmente, horizontalmente, en forma de 
        #   matriz, o de varias otras formas, uno después del otro.
        main_layout = QtWidgets.QVBoxLayout()
        #PyQt5.QtWidgets.QVBoxLayout.addWidget(): Método usado para añadir un widget de manera secuencial en la 
        #columna de un diseño vertical, como lo puede ser un botón, lista desplegable, texto, imagen, etc. Se 
        #indica el órden en el que se colocarán los elementos dependiendo de cual fue añadido primero y cual 
        #después.
        main_layout.addWidget(self.canvas)
        #Objeto de la clase QGridLayout, el cual se utiliza para organizar los widgets en una en una cuadrícula 
        #bidimensional de filas y columnas.
        # - parent: Si el constructor de esta clase recibe como parámetro un objeto QWidget, ese será el 
        #   contenedor principal del objeto QGridLayout que organiza sus elementos en forma de rejilla.
        # - Si no recibe ningún parámetro, este es un contenedor vacío sin widget principal que aceptará 
        #   varios elementos o contenedores y los irá colocando dependiendo de las coordenadas que se les 
        #   indique al utilizar el método .addWidget().
        control_layout = QtWidgets.QGridLayout()
        #PyQt5.QtWidgets.QGridLayout.addWidget(): Método usado para añadir un widget en una cuadrícula 
        #bidimensional compuesta por filas y columnas, donde la primera coordenada de filas y columnas se 
        #indica desde el número 0:
        # - En su primer parámetro se indica el widget que se quiera aregar.
        # - En su segundo parámetro se indica la fila donde se quiere colocar el elemento, contando desde 0.
        # - En su tercer parámetro se indica la columna donde se quiere colocar el elemento, contando desde 0.
        #Fila 1 = x = 0; Columna 1 = y = 0. 
        control_layout.addWidget(lbl_port, 0, 0)        #Agrega el texto estático que dice COM Ports: en (0,0)
        control_layout.addWidget(self.cb_port, 1, 0)    #Agrega el Combo Box de puertos en (1,0)
        control_layout.addWidget(lbl_samples, 0, 1)     #Agrega el texto estático que dice Samples: en (0,1)
        control_layout.addWidget(spb_samples, 1, 1)     #Agrega el Spin Box de muestras en (1,1)
        control_layout.addWidget(self.btn_start, 1, 2)  #Agrega el Botón de Start en (1,2)
        control_layout.addWidget(self.btn_stop, 1, 3)   #Agrega el Botón de Stop en (1,3)
        control_layout.addWidget(self.btn_save, 1, 4)   #Agrega el Botón de Save en (1,4)
        control_layout.addWidget(lbl_umbral, 2, 0)      #Agrega el texto estático que dice Umbral: en (2,0)
        control_layout.addWidget(spb_umbral, 3, 0)      #Agrega el Spin Box del umbral de Led en (3,0)
        #PyQt5.QtWidgets.QVBoxLayout.addLayout(): Método usado para añadir un layout (contenedor) de manera 
        #secuencial en la columna de un diseño vertical, se indica el órden en el que se colocarán los elementos 
        #dependiendo de cual fue añadido primero y cual después.
        main_layout.addLayout(control_layout)
        #Instancia de la clase QWidget, que hereda de la clase QtWidgets y pertenece a la librería PyQt5, dicho 
        #objeto funciona como un contenedor que puede almacenar widgets directamente, proporcionando 
        #funcionalidades para mostrar, ocultar, establecer posición, tamaño, manejar eventos, etc. de los 
        #diferentes botones, checkboxes, áreas de texto, comboboxes, radiobuttons, listboxes, ventanas de 
        #diálogo (ventana que muestra el explorador de archivos), etc. 
        centralWidget = QtWidgets.QWidget()
        #PyQt5.QtWidgets.QVBoxLayout.setLayout(): Método usado para añadir un layout (que es un contenedor más 
        #complejo) a un widget (que es un contenedor más sencillo), esto es útil hacerlo cuando se quiere 
        #colocar el contenedor en una cierta posición (central, arriba, abajo, a la derecha o a la izquierda) 
        #dentro de la ventana de la GUI.
        centralWidget.setLayout(main_layout)
        #ALINEACIÓN DE CONTENIDO EN UN WIDGET O LAYOUT:
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
        self.setCentralWidget(centralWidget)            #Contenedor colocado en el área central de la GUI.
        
        #Instancia_Widget.evento_señal.connect(función_que_reacciona_al_evento): Este método se utiliza para 
        #enlazar un evento a un controlador de eventos, que es una función que se ejecuta cuando ocurra el 
        #evento, para ello se usa el nombre del widget, seguido del evento de tipo señal que detona el método, 
        #la palabra reservdada .connect() y entre paréntesis se coloca el nombre de la función que ejecutará 
        #alguna acción cuando ese evento ocurra. Normalmente las funciones que describen las acciones a 
        #realizar por los widgets de la GUI se encuentran dentro de esta misma clase, pero fuera de su 
        #constructor.
        # - Tipos de Eventos en Python: 
        #       - clicked: Señal emitida cuando se hace clic en un elemento, como un botón.
        #       - doubleClicked: Señal emitida cuando se hace doble clic en un elemento.
        #       - pressed: Señal emitida cuando se presiona un elemento, como un botón.
        #       - released: Señal emitida cuando se suelta un elemento, como un botón.
        #       - textChanged: Señal emitida cuando el texto de un elemento, como un campo de texto, cambia.
        #       - currentIndexChanged: Señal emitida cuando se cambia el índice seleccionado en un elemento, 
        #         como en un menú desplegable.
        #       - activated: Señal emitida cuando se selecciona un elemento, como un elemento de un menú 
        #         desplegable o una opción de una lista.
        #       - keyPressed: Señal emitida cuando se presiona una tecla en el teclado.
        #       - keyReleased: Señal emitida cuando se suelta una tecla en el teclado.
        #       - mousePressEvent: Señal emitida cuando se presiona un botón del mouse.
        #       - mouseReleaseEvent: Señal emitida cuando se suelta un botón del mouse.
        #       - mouseMoveEvent: Señal emitida cuando se mueve el mouse.
        #       - valueChanged: Señal emitida cuando se selecciona un nuevo elemento en un combo box (lista 
        #         desplegable).
        #       - timeout: Señal emitida cuando transcurre cada intervalo de tiempo especificado en un 
        #         temporizador.
        #Es importante mencionar que en  PyQt5, cuando se conecta una función a un evento, la función conectada 
        #puede recibir argumentos adicionales proporcionados por la señal emitida. Estos argumentos son 
        #transmitidos automáticamente por el sistema de señales y slots de PyQt5.
        # - Tipos de argumentos retornados al suceder un evento: 
        #       - *args y **kwargs: Muchas señales en PyQt5 permiten enviar argumentos adicionales a través de 
        #          *args (tupla de argumentos posicionales) y **kwargs (diccionario de argumentos de palabras 
        #          clave). Estos parámetros pueden variar según la señal específica y su contexto de uso.
        #       - checked: Algunas señales, como "clicked" en un botón, pueden enviar el estado de alternancia 
        #         del widget. Este parámetro indica si el widget está marcado y suele ser de tipo booleano.
        #       - text: En widgets de entrada de texto, como QLineEdit o QTextEdit, las señales pueden enviar el 
        #         texto ingresado o modificado como parámetro.
        #       - index: En widgets que tienen índices o selecciones, como QComboBox o QListView, las señales 
        #         pueden enviar el índice seleccionado como parámetro.
        #       - position: En widgets que trabajan con eventos de posición, como QMouseEvent, las señales 
        #         pueden enviar la posición del cursor o del evento como parámetro.
        #Al presionar un botón se ejecutará un método, declarado dentro de la misma clase.
        self.btn_start.clicked.connect(self.OnStartClick)       #Clic en Botón Start = OnStartClick()
        self.cb_port.activated.connect(self.add_port)           #Clic en una opción del Combo box = add_port()
        spb_samples.valueChanged.connect(self.samples_changed)  #Cambio en Spin box samples = samples_changed()
        spb_umbral.valueChanged.connect(self.umbral_changed)    #Cambio en Spin box umbral = umbral_changed()
        self.btn_stop.clicked.connect(self.OnStopClick)         #Clic en Botón Stop  = OnStopClick()
        self.btn_save.clicked.connect(self.OnStartSaving)       #Clic en Botón Save  = OnStartSaving()
        
        #ATRIBUTOS DEL CONSTRUCTOR PERTENECIENTE A LA CLASE BottomPanel:
        self.com_port = ""              #Puerto seleccionado en el ComboBox

        self.period = 500               #Intervalo de muestreo (conteo) del Timer indicado en milisegundos.
        self.time_val = 0               #Variable que cuenta cada 1 segundos el tiempo de ejecución de la GUI.

        self.high_value_board = 5.0     #Valor de tensión Máxima = 5V

        self.count = 0                  #Variable que cuenta los datos recopilados por la GUI.

        #Variable que obtiene los datos de tensión del pin A0 perteneciente al Arduino por medio de una 
        #comunicación serial establecida a través del puerto elegido en el ComboBox.
        self.micro_board = None         #Datos de tensión obtenidos del pin A0 del Arduino.
        
        #QtWidgets.QSpinBox.minimum(): Método que obtiene el valor mínimo en un control numérico SpinBox.
        #La variable que guarda el número de muestras se inicializa con el valor mínimo del SpinBox.
        self.items = spb_samples.minimum()      #Variable que indica el número de muestras.
        self.umbralLed = spb_umbral.minimum()   #Variable que indica la tensión de encendido del led [mV].
    
    
    #función OnStartClick(): Método creado dentro de la clase propia llamada MainWindow que recibe como 
    #parámetro el evento que lo activa, para posteriormente ejecutar cierta acción.
    #En este caso el evento es activado por dar un clic sobre el botón de Start y lo que hace es primero checar 
    #si la comunicación serial está abierta, para poderla cerrar y volverla a abrir, luego checa si se ha 
    #seleccionado un puerto del ComboBox y si esto es cierto, iniciliza el temporizador y establece una 
    #comunicación serial con el puerto seleccionado, si no ha sido elegido ningún puerto del ListBox, muestra 
    #una ventana emergente que indique que no se ha seleccionado ningún puerto, además si es que ha ocurrido un 
    #error al intentar establecer la comunicación serial con el Arduino, mostrará un mensaje de error en una 
    #ventana emergente que indique tal cosa.
    def OnStartClick(self):
        #print(): Método para imprimir un mensaje en consola y después dar un salto de línea (Enter).
        print("\nStart")
        print("Se recopilarán", self.items, "datos.")     #Se indica el número de muestras a recopilar.
        print("Con un umbral inicial de", self.umbralLed, "[mV].")
        self.stp_acq = False            #Variable booleana que indica si se ha presionado el botón STOP.
        #MANEJO DE EXCEPCIONES: Es una parte de código que se conforma de dos partes, try y except: 
        # - Primero se ejecuta el código que haya dentro del try y si es que llegara a ocurrir una excepción 
        #   durante su ejecución, el programa brinca al código del except
        # - En la parte de código donde se encuentra la palabra reservada except, se ejecuta cierta acción 
        #   cuando ocurra el error esperado. 
        #Se utiliza esta arquitectura de código cuando se quiera efectuar una acción donde se espera que pueda 
        #ocurrir un error durante su ejecución.
        try:
            #PYFIRMATA: CONEXIÓN SERIAL, CONTROL Y MONITOREO DE PINES DE UNA TARJETA DE DESARROLLO
            #Instancia de la clase Arduino, que pertenece a la librería pyfirmata, dicho objeto proporciona 
            #métodos para comunicarse con placas Arduino utilizando el protocolo Firmata, permitiendo así el 
            #control y monitoreo de sus pines digitales y analógicos, realizar el envío de señales PWM, lectura 
            #y/o escritura de datos y establecer una comunicación a través de los protocolos I2C y Serial, la 
            #conexión serial con los microcontroladores se realiza utilizando la clase pyfirmata.Arduino(), 
            #independientemente del tipo de microcontrolador que se esté utilizando, ya que la librería 
            #pyfirmata proporciona una interfaz común para comunicarse con diferentes placas de desarrollo, 
            #incluyendo Arduino, Raspberry Pi, Intel Galileo, PyCARD, etc. Para ello su constructor recibe los 
            #siguientes parámetros:
            # - port (obligatorio): Especifica el puerto de comunicación a través del cual se conectará la placa 
            #   Arduino. Puede ser una cadena de texto que representa el nombre del puerto, como por ejemplo 
            #   'COM3' en Windows o '/dev/ttyACM0' en Linux. El nombre del parámetro no se indica 
            #   explícitamente.
            # - timeout (opcional): Especifica el tiempo máximo de espera (en segundos) para establecer la 
            #   conexión con la placa Arduino. Si no se especifica, se utilizará un valor predeterminado.
            # - baudrate: Este parámetro establece la velocidad de comunicación en baudios para la comunicación 
            #   entre la computadora y el microcontrolador. Los baudios representan la cantidad de bits que se 
            #   pueden transmitir por segundo. 
            #       - El valor que utiliza la librería Standard Firmata por default es de 57600, pero también se 
            #         puede usar otros valores como 9600, 115200, etc. Pero esto debería ser cambiado igual en 
            #         el código Arduino de la librería que se sube al Arduino. 
            # - bytesize, parity y stopbits (opcionales): Estos parámetros permiten configurar la transmisión 
            #   serial y se utilizan en conjunto para establecer cómo se transmiten los datos entre la 
            #   computadora y la placa de desarrollo.
            self.micro_board = pyfirmata.Arduino(self.com_port, baudrate = 57600)   #Conexión serial.
            print("La conexión Pyfirmata ha sido exitosa: ", self.micro_board)
            #Instancia de la clase Iterator, que hereda de la clase util y ambas pertenecen a la librería 
            #pyfirmata, dicho objeto permite al programa percibir, capturar y procesar los cambios que ocurran 
            #en los pines de entrada de la placa, para ello su constructor recibe como parámetro un objeto 
            #pyfirmata.Board que ya haya realizado una conexión serial entre la computadora y la tarjeta de 
            #desarrollo.
            self.portListener = pyfirmata.util.Iterator(self.micro_board)           #Monitoreo de pines.
            #pyfirmata.util.Iterator.start(): Método utilizado para iniciar el proceso de lectura de datos 
            #entrantes desde la placa de desarrollo previamente conectada al ordenador de forma serial con el 
            #constructor pyfirmata.Arduino().
            self.portListener.start()
            #SELECCIÓN DE LOS PINES QUE SE QUIERE CONTROLAR Y/O MONITOREAR:
            #pyfirmata.Arduino.get_pin(): Método utilizado para acceder a un pin específico de la placa de 
            #desarrollo con la que ya se ha realizado una conexión serial. Indicando si este es analógico o 
            #digital, su número y si será utilizado como entrada o salida siguiendo la sintaxis descrita a 
            #continuación:
            # - 'analogico_o_digital:   numero_pin:     entrada_o_salida'
            #       - 'analogico:       numero_pin:     entrada'            = 'a: numero_pin: i'
            #       - 'analogico:       numero_pin:     salida'             = 'a: numero_pin: o'
            #       - 'digital:         numero_pin:     entrada'            = 'd: numero_pin: i'
            #       - 'digital:         numero_pin:     salida'             = 'd: numero_pin: o'
            #El número y asignación de pin analógico o digital varía dependiendo de la tarjeta de desarrollo.
            self.analog_0 = self.micro_board.get_pin('a:0:i')                       #Pin A0: Entrada.
            self.analog_1 = self.micro_board.get_pin('a:1:i')                       #Pin A1: Entrada.
            self.digital_13 = self.micro_board.get_pin('d:13:o')                     #Pin 13: Salida.
            self.digital_12 = self.micro_board.get_pin('d:12:o')                     #Pin 12: Salida.
        except:
            #PyQt5.QtWidgets.QMessageBox(): Método de la librería PyQt5 que se utiliza para mostrar una ventana 
            #emergente en la interfaz gráfica. Esta ventana de diálogo muestra un mensaje específico al usuario 
            #y puede contener botones para que el usuario realice una acción, como aceptar, cancelar, etc.
            dlg_board=QtWidgets.QMessageBox()
            #PyQt5.QtWidgets.QMessageBox.setWindowTitle(): Método para colocar un título en la ventana creada 
            #con la librería PyQt5.
            dlg_board.setWindowTitle("Error en Instrumentación con pyfirmata uy no!")
            #PyQt5.QtWidgets.QMessageBox.setText(): Método que se utiliza para establecer el texto principal de 
            #un cuadro de diálogo QMessageBox en PyQt5. Este método recibe el siguiente parámetro:
            # - text: Indica el texto que se mostrará en el cuerpo principal del cuadro de diálogo. Puede ser 
            #   una cadena de texto o admitir el formato HTML para formatear el texto. El nombre del parámetro 
            #   no se menciona explícitamente.
            str_dlg_board = "<h3>No tienes ningún puerto seleccionado!</h3>" 
            str_dlg_board += "<h4>O la placa no se conectó correctamente...</h4>"
            dlg_board.setText(str_dlg_board)
            #PyQt5.QtWidgets.QMessageBox.setStandardButtons(): Método usado para establecer los botones estándar 
            #que se mostrarán en el cuadro de diálogo, esto se realiza a través de los siguientes parámetros:
            # - QtWidgets.QMessageBox.Ok: Botón "Aceptar".
            # - QtWidgets.QMessageBox.Open: Botón "Abrir".
            # - QtWidgets.QMessageBox.Save: Botón "Guardar".
            # - QtWidgets.QMessageBox.Cancel: Botón "Cancelar".
            # - QtWidgets.QMessageBox.Close: Botón "Cerrar".
            # - QtWidgets.QMessageBox.Yes: Botón "Sí".
            # - QtWidgets.QMessageBox.No: Botón "No".
            # - QtWidgets.QMessageBox.Abort: Botón "Abortar".
            # - QtWidgets.QMessageBox.Retry: Botón "Reintentar".
            # - QtWidgets.QMessageBox.Ignore: Botón "Ignorar".
            # - QtWidgets.QMessageBox.Reset: Botón "Restablecer".
            # - QtWidgets.QMessageBox.Help: Botón "Ayuda".
            # - QtWidgets.QMessageBox.Apply: Botón "Aplicar".
            # - QtWidgets.QMessageBox.YesToAll: Botón "Sí a todo".
            # - QtWidgets.QMessageBox.NoToAll: Botón "No a todo".
            # - QtWidgets.QMessageBox.SaveAll: Botón "Guardar todo".
            # - QtWidgets.QMessageBox.Default: Botón "Predeterminado".
            # - QtWidgets.QMessageBox.RestoreDefaults: Botón "Restaurar predeterminados".
            #Puedes combinar varios botones utilizando la compuerta lógica OR (|) para mostrar varios botones en 
            #el cuadro de diálogo.
            dlg_board.setStandardButtons(QtWidgets.QMessageBox.Ok)
            #PyQt5.QtWidgets.QMessageBox.setIcon(): Método que se utiliza para establecer el ícono que se 
            #muestra en un cuadro de diálogo QMessageBox. Recibe un parámetro que especifica el ícono a mostrar. 
            #Los valores posibles para el parámetro son:
            # - QtWidgets.QMessageBox.NoIcon: No se muestra ningún ícono.
            # - QtWidgets.QMessageBox.Information: Muestra un ícono de información.
            # - QtWidgets.QMessageBox.Warning: Muestra un ícono de advertencia.
            # - QtWidgets.QMessageBox.Critical: Muestra un ícono de error/crítico.
            # - QtWidgets.QMessageBox.Question: Muestra un ícono de pregunta.
            dlg_board.setIcon(QtWidgets.QMessageBox.Warning)
            #PyQt5.QtWidgets.QMessageBox.exec_(): Método para que se ejecute en un loop infinito el GUI, 
            #logrando así que no se ejecute una vez y luego cierre por sí solo, sino que solo se cierre 
            #solamente al dar clic en el tache de la ventana emergente.
            dlg_board.exec_()
            #Reinicio de la variable que guarda los datos de tensión obtenidos del pin A0 del Arduino.
            self.micro_board = None
        
        #Condicional if que checa si ya se ha seleccionado algún puerto y además se ha iniciado la conexión 
        #serial, empezado ya a recopilar los datos de tensión del pin A0; si ésta es diferente de None, inicia 
        #el conteo con un temporizador y empieza a almacenar el tiempo transcurrido y los datos de tensión 
        #recabados en una lista que los relacione entre sí.
        if(self.com_port != "" and self.micro_board != None):
            #widget.Hide(): Método que sirve para esconder un widget en la GUI.
            self.btn_start.hide()       #Esconde el botón de START.
            self.btn_save.hide()        #Esconde el botón de SAVE.
            #widget.Show(): Método que sirve para mostrar un widget en la GUI.
            self.btn_stop.show()        #Muestra el botón de STOP.

            #Condicional if que comprueba que el valor de la variable que cuenta los datos recopilados por la 
            #GUI es igual a cero, para que cuando esto sea cierto, se reinicie el valor de todas las variables 
            #antes de comenzar de nuevo una recopilación de datos.
            if(self.count == 0):
                self.x = np.array([])   #Reinicio del numpy array del eje horizontal (x = tiempo [s]).
                self.y0 = np.array([])  #Reinicio del eje vertical perteneciente al pin A0 (y1 = tensión [V]).
                self.y1 = np.array([])  #Reinicio del eje vertical perteneciente al pin A1 (y2 = tensión [V]).
                self.u = np.array([])   #Reinicio del eje vertical perteneciente al umbral (u = tensión [mV]).
                self.values = []        #Reinicio de la lista que guarda los valores de tiempo y tensión.

                self.time_val = 0       #Reinicio de la variable que cuenta cada 1 segundo.

                #CREACIÓN DE WIDGETS: Temporizador
                #Instancia de la librería PyQt5 por medio del constructor de la clase Timer, que hereda de la 
                #clase QtCore y se utiliza para crear un widget de tipo temporizador.
                self.timer = QtCore.QTimer() 
                #INICIACIÓN DEL TEMPORIZADOR:
                #QtCore.QTimer.setInterval(intervalo): Método que indica el intervalo de conteo de un 
                #temporizador en milisegundos.
                self.timer.setInterval(self.period)
                #Instancia_Widget.evento_señal.connect(función_que_reacciona_al_evento): Este método se utiliza 
                #para enlazar un evento a un controlador de eventos, que es una función que se ejecuta cuando 
                #ocurra el evento, para ello se usa el nombre del widget, seguido del evento de tipo señal que 
                #detona el método, la palabra reservdada .connect() y entre paréntesis se coloca el nombre de la 
                #función que ejecutará alguna acción cuando ese evento ocurra. Normalmente las funciones que 
                #describen las acciones a realizar por los widgets de la GUI se encuentran dentro de esta misma 
                #clase, pero fuera de su constructor.
                # - Tipos de Eventos en Python: 
                #       - clicked: Señal emitida cuando se hace clic en un elemento, como un botón.
                #       - doubleClicked: Señal emitida cuando se hace doble clic en un elemento.
                #       - pressed: Señal emitida cuando se presiona un elemento, como un botón.
                #       - released: Señal emitida cuando se suelta un elemento, como un botón.
                #       - textChanged: Señal emitida cuando el texto de un elemento, como un campo de texto, 
                #         cambia.
                #       - currentIndexChanged: Señal emitida cuando se cambia el índice seleccionado en un 
                #         elemento, 
                #         como en un menú desplegable.
                #       - activated: Señal emitida cuando se selecciona un elemento, como un elemento de un menú 
                #         desplegable o una opción de una lista.
                #       - keyPressed: Señal emitida cuando se presiona una tecla en el teclado.
                #       - keyReleased: Señal emitida cuando se suelta una tecla en el teclado.
                #       - mousePressEvent: Señal emitida cuando se presiona un botón del mouse.
                #       - mouseReleaseEvent: Señal emitida cuando se suelta un botón del mouse.
                #       - mouseMoveEvent: Señal emitida cuando se mueve el mouse.
                #       - valueChanged: Señal emitida cuando se selecciona un nuevo elemento en un combo box 
                #         (lista desplegable).
                #       - timeout: Señal emitida cuando transcurre cada intervalo de tiempo especificado en un 
                #         temporizador.
                #Es importante mencionar que en  PyQt5, cuando se conecta una función a un evento, la función 
                #conectada puede recibir argumentos adicionales proporcionados por la señal emitida. Estos 
                #argumentos son transmitidos automáticamente por el sistema de señales y slots de PyQt5.
                # - Tipos de argumentos retornados al suceder un evento: 
                #       - *args y **kwargs: Muchas señales en PyQt5 permiten enviar argumentos adicionales a 
                #         través de *args (tupla de argumentos posicionales) y **kwargs (diccionario de 
                #         argumentos de palabras clave). Estos parámetros pueden variar según la señal 
                #         específica y su contexto de uso.
                #       - checked: Algunas señales, como "clicked" en un botón, pueden enviar el estado de 
                #         alternancia del widget. Este parámetro indica si el widget está marcado y suele ser de 
                #         tipo booleano.
                #       - text: En widgets de entrada de texto, como QLineEdit o QTextEdit, las señales pueden 
                #         enviar el texto ingresado o modificado como parámetro.
                #       - index: En widgets que tienen índices o selecciones, como QComboBox o QListView, las 
                #         señales pueden enviar el índice seleccionado como parámetro.
                #       - position: En widgets que trabajan con eventos de posición, como QMouseEvent, las 
                #         señales pueden enviar la posición del cursor o del evento como parámetro.
                #Cada que transcurra el intervalo de tiempo indicado en el temporizador, se ejecuta una función.
                self.timer.timeout.connect(self.update_plot)    #Intervalo transcurrido  = update_plot()
                #QtCore.QTimer.start(): Método que inicializa el conteo de un temporizador, para ello, 
                #previamente se tuvo que haber usado el método .setInterval() para indicar su intervalo de 
                #conteo en milisegundos.
                self.timer.start()
                print("\nTime [s] \t\tVoltage Pin A0 [V] \t\tVoltage Pin A1 [V] \t\tUmbral [V]")
    

    #función update_plot(): Método creado dentro de la clase propia llamada MainWindow que recibe como 
    #parámetro el evento que lo activa, para posteriormente ejecutar cierta acción. En este caso el método se 
    #ejecuta Cada que transcurra el intervalo de tiempo indicado en el temporizador y lo que hace es actualizar 
    #el estado de la gráfica, para que los datos recopilados se muestren en tiempo real.         
    def update_plot(self):
        #MANEJO DE EXCEPCIONES: Es una parte de código que se conforma de dos partes, try y except: 
        # - Primero se ejecuta el código que haya dentro del try y si es que llegara a ocurrir una excepción 
        #   durante su ejecución, el programa brinca al código del except
        # - En la parte de código donde se encuentra la palabra reservada except, se ejecuta cierta acción 
        #   cuando ocurra el error esperado. 
        #Se utiliza esta arquitectura de código cuando se quiera efectuar una acción donde se espera que pueda 
        #ocurrir un error durante su ejecución.
        try: 
            #pyfirmata.Arduino.get_pin().read(): Método que se utiliza para leer el valor actual de un pin en la 
            #placa. Permite obtener el estado del pin, que puede ser un valor analógico o digital, dependiendo 
            #de cómo esté configurado.
            # - Pin digital de entrada: Devolverá un valor booleano (True o False), que indica si el pin está en 
            #   alto (encendido) o en bajo (apagado) respectivamente.
            # - Pin analógico de entrada: Devolverá un valor numérico que representa la lectura analógica en el 
            #   pin. 
            #       - Placa Arduino: Este valor suele estar en un rango de 0 a 1, donde 0 coresponde al valor 
            #         binario 0 y 1 al valor binario 1023, que hace referencia a la resolución de 10 bits del 
            #         conversor analógico a digital (ADC) en la placa Arduino:
            #               - Resolución de 10 bits del ADC del Arduino: (2^10)-1 = 1023
            #Si se utiliza el método read() en un pin que está configurado como salida, el resultado puede ser 
            #impredecible o no tener sentido.
            tensionBinariaA0 = self.analog_0.read()                                 #Lee el pin analógico A0.
            tensionBinariaA1 = self.analog_1.read()                                 #Lee el pin analógico A1.
            
            #CONVERSIÓN DE NUMEROS BINARIOS NUMÉRICOS DE TENSIÓN A VALORES DE TENSIÓN REALES:
            #float(): Método que convierte un tipo de dato cualquiera en númerico decimal.
            #Se realiza esta operación porque como el ADC del arduino lee de 0 a 5V y como tiene una resolución 
            #de 10 bits permitiendo que en el ADC los valores de tensión se interpreten como valores numéricos 
            #enteros que valen de 0 a (2^10)-1 = 1023, se hace una regla de 3 para que se imprima el valor de la 
            #tensión en consola en vez del valor decimal binario. En esta operación no es necesario dividir el 
            #resultado entre la resolución del ADC porque el valor que retorna el método read ya está 
            #normalizado en el rango de 0 a 1 (correspondiente a los 1024 niveles).
            #Tensión = Tensión_decimal_read*(ValorMáximoTensión) = Tensión_decimal_read*(5)
            VoltsA0 = (float(tensionBinariaA0)*(self.high_value_board))             #Tensión real pin A0.
            VoltsA1 = (float(tensionBinariaA1)*(self.high_value_board))             #Tensión real pin A1.
            umbral = self.umbralLed/1000.0                                          #Tensión de umbral [V].
            
            #VECTOR TIEMPO:
            #Se usa una variable intermedia que va contando el tiempo transcurrido desde que se empezó a recopilar 
            #los valores de tensión del puerto analógico A0 del Arduino hasta que acaba. El intervalo de tiempo con 
            #el que cuenta el temporizador y el tiempo que se detiene el delay que se declarará después del except 
            #debe ser el mismo.
            self.time_val = self.time_val + 0.5         #Variable que cuenta el tiempo de ejecución del programa.
            self.count = self.count + 1                 #Variable que cuenta los datos recopilados por la GUI.

            #IMPRIMIR EN CONSOLA TIEMPO Y TENSIÓN:
            msg_console = str(self.count) + ".- Time: " + str(self.time_val) + " [s]" + "\t" #Tiempo [s].
            msg_console+= "Voltage Pin A0: " + "{0:.5f}".format(VoltsA0)+" [V]\t"          #Tensión real pin A0.
            msg_console+= "Voltage Pin A1: " + "{0:.5f}".format(VoltsA1)+" [V]\t"            #Tensión real pin A1.
            msg_console+= "Umbral: " + "{0:.5f}".format(umbral)+" [V]"                   #Tensión de umbral [V].
            print(msg_console)

            #GUARDAR LOS DATOS RECOPILADOS EN UNA MATRIZ PARA POSTERIORMENTE ALMACENARLOS EN UN ARCHIVO: 
            #append(): Método que sirve para agregar valores a una lista, tupla, numpy array o diccionario.
            #Lista que guarda los valores de tiempo [s] y tensión [V] recopilados.
            self.values.append(str(self.time_val) + ", " + "{0:05f}".format(VoltsA0) + ", " + 
                                                            "{0:05f}".format(VoltsA1) + ", " + 
                                                            "{0:05f}".format(umbral))
            #matplotlib.Figure.add_subplot().cla(): Método cuyo nombre es una abreviatura de "clear axes" y 
            #sirve para restablecer el estado de los ejes pertenecientes a una gráfica creada con la librería 
            #matplotlib.
            self.canvas.axes.cla()
            self.x = np.append(self.x, self.time_val)           #Vector tiempo [segundos].
            self.y0 = np.append(self.y0, VoltsA0)               #Vector tensión A0 [V]. 
            self.y1 = np.append(self.y1, VoltsA1)               #Vector tensión A1 [V].
            self.u = np.append(self.u, umbral)                  #Vector tensión umbral [mV].


            #matplotlib.Figure().add_subplot().set_xlabel(): Método para indicar el texto que aparece en el eje 
            #horizontal de la gráfica, recibe los siguientes parámetros:
            # - xlabel: Especifica el texto que se mostrará en el eje x.
            # - fontname: Indica el estilo de la fuente:
            #       - Nombres de tipos de letra estándar: "Arial", "Times New Roman", "Helvetica", "Courier", 
            #         "Monospaced", "Consolas", etc. Estos nombres deben ser compatibles con los tipos de letra 
            #         instalados en el sistema operativo.
            #       - Nombres de tipos de letra genéricos: "serif", "sans-serif", "monospace", etc.
            #       - Rutas de archivo: Si se tiene un archivo de tipo de letra personalizado, se puede 
            #         especificar la ruta del archivo como el valor de fontname.
            # - fontsize: Indica el tamaño de la fuente.
            # - labelpad: Especifica el espaciado entre la etiqueta del eje x y el eje en sí
            # - color: Indica el color del texto colocado en el eje x, para ello es válido usar colores: 
            #       - Básicos CSS: como "red", "blue", "green", etc. 
            #       - Colores hexadecimales: "#FF0000", "#00FF00", etc. 
            #       - Colores RGB: "rgb(255,255,255)" para el color blanco y "rgb(0,0,0)" para el negro.
            self.canvas.axes.set_xlabel(xlabel = "Time [s]", fontname = "Consolas", fontsize = 8, color = "white")
            #matplotlib.Figure.add_subplot().set_ylabel(): Método para indicar el texto que aparece en el eje y.
            self.canvas.axes.set_ylabel(ylabel = "Voltage [V]", fontname = "Consolas", fontsize = 8, color = "white")
            #matplotlib.Figure.add_subplot().plot(): Método usado para gráficar, indicando como primer parámetro 
            #su eje horizontal, luego su eje vertical y finalmente el estilo de la gráfica:
            # - Colores:             C1: color naranja, r: color rojo, b: color azul, g: verde, c: cyan, 
            #   m: morado, y: amarillo, k: negro, w: blanco.
            # - Tipo de marcadores:  o: círculos, +: símbolos de más, .; puntos, v: Triángulo hacia abajo, 
            #   h: Hexágono, etc.
            # - Tipo de Líneas:      -: sólida, --: punteada (líneas), :: punteada (puntos), -.: línea y punto, 
            #   'or': Nada.
            #Los marcadores se obtienen del siguiente link: https://matplotlib.org/stable/api/markers_api.html
            self.canvas.axes.plot(self.x, self.y0, 'y1:') #'y:' c: color amarillo, 1: tri_down, :: línea punteada.
            self.canvas.axes.plot(self.x, self.y1, 'r2--') #'r.--' c: color rojo, 2: tri_up, --: linea punteada.
            self.canvas.axes.plot(self.x, self.u, 'c,-') #'w,-' c: color cyan, .: pixel, -: línea solida.
            #matplotlib.Figure().add_subplot().legend(): La leyenda de un gráfico es un componente que 
            #proporciona información individualmente sobre los diferentes elementos o series presentes en el 
            #gráfico, el método permite personalizar dicha leyenda a través de los siguientes parámetros:
            # - labels: Se refiere a los nombres que se les puede poner para las leyendas de los distintos 
            #   elementos del gráfico. 
            #           - Las etiquetas se generan automáticamente pero se pueden colocar manualmente de la 
            #             siguiente manera: 
            #               - labels=['Etiqueta 1', 'Etiqueta 2']
            # - loc: Indica la ubicación de la leyenda en el gráfico. Se puede indicar con una cadena de texto o 
            #   un código numérico que represente una posición específica.
            #           - "best": Coloca la leyenda en la mejor ubicación posible, evitando superponerse con 
            #             otros elementos.
            #           - "upper right": Coloca la leyenda en la esquina superior derecha del gráfico.
            #           - "upper left": Coloca la leyenda en la esquina superior izquierda del gráfico.
            #           - "lower right": Coloca la leyenda en la esquina inferior derecha del gráfico.
            #           - "lower left": Coloca la leyenda en la esquina inferior izquierda del gráfico.
            #           - "right": Coloca la leyenda en el lado derecho del gráfico, centrada verticalmente.
            #           - "center left": Coloca la leyenda en el lado izquierdo del gráfico, centrada 
            #             verticalmente.
            #           - "center right": Coloca la leyenda en el lado derecho del gráfico, centrada 
            #             verticalmente.
            #           - "center": Coloca la leyenda en el centro del gráfico.
            self.canvas.axes.legend(labels=['Pin A0', 'Pin A1', 'Umbral Leds 13/12'], loc = "best")
            #matplotlib.FigureCanvas().draw(): Método que actualiza y muestra los datos recopilados en tiempo 
            #real en la gráfica creada con el objeto que instancía la clase FigureCanvasQTAgg.
            self.canvas.draw()
            
            #Si la tensión que ingresa en el pin A0 es mayor al umbral, se enciende un led con el pin 13.
            if(VoltsA0 > umbral):
                #pyfirmata.Arduino.get_pin().write(): Método que se utiliza para escribir un valor en algún pin 
                #digital de la placa, controlando si su estado está en alto (1 o True) o bajo (0 o False).
                # - Encender LED:   write(True)  o write(1).
                # - Apagar LED:     write(False) o write(0).
                #El método write() solamente se puede usar con pines de salida digital, si se quiere controlar 
                #la salida de un pin analógico se debe usa el método analog_write().
                self.digital_13.write(1)                         #Led encendido en el pin 13.
                print("Led en el pin 13 Encendido")
            else:
                self.digital_13.write(0)                         #Led apagado en el pin 13.
            #Si la tensión que ingresa en el pin A1 es mayor al umbral, se enciende un led con el pin 12.
            if(VoltsA1 > umbral):
                self.digital_12.write(True)                      #Led encendido en el pin 12.
                print("Led en el pin 12 Encendido")             
            else:
                self.digital_12.write(False)                     #Led apagado en el pin 12.
        except:
            print("No se pudo actualizar la gráfica")
        
        #Condicional if que checa si se ha llegado al límite impuesto por el número de muestreos indicados en el 
        #Spin Box, además de confirmar que el botón de Stop no ha sido activado, en caso de que cualquiera de 
        #estas dos opciones sean ciertas, se detiene la recopilación de datos.
        if (self.count >= self.items or self.stp_acq == True):
            print("Se ha terminado de recopilar datos.")
            #widget.Hide(): Método que sirve para esconder un widget en la GUI, inicialmente los botones de 
            #STOP y SAVE se encuentran escondidos por esta misma instrucción en el constructor, pero luego 
            #al dar clic en el botón de START, se esconde el botón de START y se muestra el botón de STOP.
            self.btn_stop.hide()        #Esconde el botón de STOP.
            #widget.Show(): Método que sirve para mostrar un widget en la GUI.
            self.btn_start.show()       #Muestra el botón de START.
            self.btn_save.show()        #Muestra el botón de SAVE.

            #QtCore.QTimer.stop(): Método que detiene el conteo de un temporizador previamente empezado con el 
            #método start().
            self.timer.stop()

            self.count = 0              #Reinicio de la variable que cuenta los datos recopilados por la GUI.
            self.stp_acq = False        #Variable booleana que indica si se ha presionado el botón STOP.

            #Condicional if que checa si hay algún puerto serial abierto, esto lo hace al ver el estado de la 
            #variable booeana serialArduino, si esta es diferente de None, termina la comunicación serial, sino 
            #sigue la ejecución del código como si nada.
            if(self.micro_board != None):
                #pyfirmata.Arduino.exit(): Método que cierra la comunicación serial. Es muy importante mencionar 
                #que si no se ejecuta este método, el puerto serial se va a quedar bloqueado y no se podrá usar.
                self.micro_board.exit()
                
    
    #función SerialPorts(): Método creado dentro de la clase propia llamada MainWindow que sirve para rellenar 
    #los elementos del Combo Box que muestran todos los puertos disponibles en el ordenador a donde se podría 
    #conectar la placa de desarrollo Arduino, de estos puertos se debe seleccionar el que haya sido elegido como 
    #puerto de conexión dentro del IDE de Arduino.
    #def nombre_función -> tipo_de_dato: Es una sintaxis llamada anotación que se utiliza para indicar el tipo 
    #de dato que devuelve una función. Es importante tener en cuenta que las anotaciones de tipo en Python son 
    #opcionales y no afectan directamente el comportamiento o la ejecución de la función. Son principalmente 
    #utilizadas para proporcionar información adicional a los desarrolladores.
    def SerialPorts(self) -> list:
        #sys.platform.startswith(): Método utilizado para para comprobar si el sistema operativo (OS) en el que 
        #se está ejecutando este programa de Python coincide con una palabra específica, identificando si es:
        # - win:                Sistema operativo Windows.
        # - Linux o cygwin:     Sistema operativo Linux.
        # - darwin:             Sistema operativo iOS.
        #La variable sys.platform almacena un string que representa el sistema operativo en el que se está 
        #ejecutando este programa de Python. El valor de sys.platform puede variar dependiendo del OS y la 
        #configuración del entorno. 
        #El método startswith() comprueba si una cadena comienza con un string especificado, devolviendo True si 
        #el string original comienza con la cadena especificada y False en caso contrario.
        if (sys.platform.startswith('win')):                                         #OS: Windows.
            #Bucle for en una sola línea: [instrucción      for   variable_local   in   range(inicio, final)]
            #Se ejecuta este bucle for en una sola línea para recopilar todos los puertos COM disponibles en el 
            #ordenador actual, ya que en teoría Windows admite 256 puertos dependiendo del OS y del hardware.
            ports = ["COM%s" %(i+1) for i in range(256)]
            print("El sistema operativo que se está utilizando es: ", sys.platform)
        elif(sys.platform.startswith('Linux') or sys.platform.startswith('cygwin')): #OS: Linux.
            #glob.glob(pathname): Método que devuelve una lista de rutas de archivos o directorios que coinciden 
            #con el patrón especificado en pathname. El pathname puede contener palabras concretas o caracteres 
            #comodín, denotados con asteriscos (*) o signos de interrogación (?), que representan uno o varios 
            #caracteres en un nombre de archivo.
            ports = glob.glob("/dev/tty[A-Za-z]*")
            print("El sistema operativo que se está utilizando es: ", sys.platform)
        elif(sys.platform.startswith('darwin')):                                     #OS: iOS.
            #glob.glob(pathname): Método que devuelve una lista de rutas de archivos o directorios que coinciden 
            #con el patrón especificado en pathname. El pathname puede contener palabras concretas o caracteres 
            #comodín, denotados con asteriscos (*) o signos de interrogación (?), que representan uno o varios 
            #caracteres en un nombre de archivo.
            ports = glob.glob("/dev/tty.*")
            print("El sistema operativo que se está utilizando es: ", sys.platform) 
        else:
            #raise: Instrucción que sirve para crear una excepción, esta a su vez debe ser parte de la clase 
            #Exception para que sea un tipo de excepción correcta y dentro de su paréntesis se indica el mensaje 
            #de error que arroja cuando se genere el error. Esta posible excepción debe ser cachada 
            #posteriormente por una instrucción de manejo de excepciones (try except). 
            raise EnvironmentError('Unsupported platform')
        
        #Variable result donde se guardarán todos los puertos detectados por el programa dependiendo del sistema 
        #operativo
        result = []

        #Bucle for para intentar abrir todos los puertos enlistados y añadirlos a la lista result:
        for port in ports:
            #MANEJO DE EXCEPCIONES: Es una parte de código que se conforma de dos partes, try y except: 
            # - Primero se ejecuta el código que haya dentro del try y si es que llegara a ocurrir una excepción 
            #   durante su ejecución, el programa brinca al código del except
            # - En la parte de código donde se encuentra la palabra reservada except, se ejecuta cierta acción 
            #   cuando ocurra el error. 
            #Se utiliza esta arquitectura de código cuando se quiera efectuar una acción donde se espera que 
            #pueda ocurrir un error durante su ejecución.
            try:
                #Instancia de la librería serial por medio del constructor de la clase Serial para establecer 
                #una comunicación serial por medio de puertos seriales o USB con dispositivos externos como 
                #microcontroladores, módems, teclados, impresoras, etc. Los parámetros que puede recibir el 
                #constructor de la clase Serial son:
                # - port: Especifica el nombre en formato string del puerto serial al que se desea conectar.
                #           - Por ejemplo: "COM1" para sistemas operativos Windows o "/dev/ttyUSB1" para 
                #             sistemas operativos Unix/Linux o iOS.
                # - baudrate: Define la velocidad de transmisión en baudios (bit trasmitido por segundo) para la 
                #   comunicación serial.
                #           - En general, 9600 baudios es una velocidad de transmisión comúnmente utilizada y es 
                #             compatible con la mayoría de los dispositivos y programas. 
                #           - Sin embargo, si se necesita una transferencia de datos más rápida y el 
                #             hardware/software lo admiten, se puede optar por velocidades más altas como 115200 
                #             o 57600 baudios.
                # - bytesize: Especifica el tamaño de los bytes en la comunicación serial. Puede adoptar uno de 
                #   los siguientes valores:  
                #           - serial.FIVEBITS: Tamaño de 5 bits en los paquetes de la transmisión serial.
                #           - serial.SIXBITS: Tamaño de 6 bits en los paquetes de la transmisión serial.
                #           - serial.SEVENBITS: Tamaño de 7 bits en los paquetes de la transmisión serial.
                #           - serial.EIGHTBITS: Tamaño de 8 bits en los paquetes de la transmisión serial.
                # - parity: Indica el tipo de paridad utilizado en la comunicación serial. La paridad es un 
                #   mecanismo utilizado en las comunicaciones seriales para verificar la integridad de los datos 
                #   transmitidos, se basa en la adición de un bit adicional (bit de paridad) en el bit más 
                #   significativo (hasta la izquierda) de cada paquete de datos transmitido. Al seleccionar la 
                #   paridad, nos debemos asegurar de que tanto el dispositivo emisor como el receptor estén 
                #   configurados con la misma paridad para efecutar una comunicación adecuada:
                #           - serial.PARITY_NONE: No se utiliza ningún bit de paridad. Esto implica que no se 
                #             verifica la integridad de los datos mediante la paridad.
                #           - serial.PARITY_EVEN: Se utiliza la paridad par. Para ello se cuentan el número de 
                #             bits en el byte, incluido el bit de paridad:
                #               - Si el número total de bits es impar, se establece el bit de paridad en 1 para 
                #                 que el número total de bits sea par. 
                #               - Si el número total de bits es par, se deja el bit de paridad en 0.
                #                   - Por ejemplo, supongamos que se desea transmitir el byte 11010110. El bit 
                #                     de paridad en la transmisión de la comunicación se calcularía contando el 
                #                     número total de bits, que es 8, el número total de bits es par, por lo que 
                #                     el bit de paridad se establece en 0, Por lo tanto, el byte transmitido 
                #                     sería 011010110, donde el bit más significativo es el bit de paridad. 
                #                     Luego en el extremo receptor de la comunicación, se realizará un cálculo 
                #                     similar para verificar la integridad de los datos. Si el número total de 
                #                     bits, incluido el bit de paridad, no coincide con la paridad esperada (en 
                #                     este caso, par), se puede detectar un error en la transmisión de datos.
                #           - serial.PARITY_ODD: Se utiliza paridad impar. El bit de paridad se establece de 
                #             manera que el número total de bits en el byte transmitido (incluido el bit de 
                #             paridad) sea impar.
                #           - serial.PARITY_MARK: Se utiliza paridad de marca. El bit de paridad se establece en 
                #             1 (marcado) para todos los bytes transmitidos.
                #           - serial.PARITY_SPACE: Se utiliza paridad de espacio. El bit de paridad se establece 
                #             en 0 (espacio) para todos los bytes transmitidos.
                # - stopbits: Define el número de bits de parada en la comunicación serial. El número de bits de 
                #   parada se utiliza para indicar el final de cada byte transmitido en la comunicación serial. 
                #   La elección del número de bits de parada depende de la configuración del dispositivo externo 
                #   con el que se está comunicando. El parámetro uno de los siguientes valores: 
                #           - serial.STOPBITS_ONE: Indica que se utiliza un bit de parada.
                #           - serial.STOPBITS_ONE_POINT_FIVE: Indica que se utiliza un bit y medio de parada. 
                #             Este valor puede ser utilizado en algunas configuraciones especiales.
                #           - serial.STOPBITS_TWO: Indica que se utilizan dos bits de parada.
                # - timeout: Especifica el tiempo de espera en segundos para las operaciones de lectura. Si no 
                #   se recibe ningún dato dentro de este tiempo, la operación de lectura se interrumpe.
                # - xonxoff: Con True o False indica si se utiliza el control de flujo XON/XOFF para la 
                #   comunicación serial.
                # - rtscts: Con True o False indica si se utiliza el control de flujo RTS/CTS para la 
                #   comunicación serial.
                # - dsrdtr: Con True o False indica si se utiliza el control de flujo DSR/DTR para la 
                #   comunicación serial.
                # - write_timeout: Especifica el tiempo de espera en segundos para las operaciones de escritura. 
                #   Si no se puede escribir ningún dato dentro de este tiempo, la operación de escritura se 
                #   interrumpe.
                # - inter_byte_timeout: Define el tiempo de espera en segundos entre la recepción de bytes 
                #   consecutivos durante las operaciones de lectura.
                #str(): Método que convierte un tipo de dato cualquiera en string.
                s = serial.Serial(port)     #Inicio de comunicación serial.
                #serial.Serial.close(): Método que cierra la comunicación serial. Es muy importante mencionar 
                #que si no se ejecuta este método, el puerto serial se va a quedar bloqueado y no se podrá usar.
                s.close()                   #Terminación de la comunicación serial.
                #append(): Método que sirve para agregar valores a una lista, tupla, numpy array o diccionario.
                result.append(port)
            #Para identificar el tipo de excepción que ha ocurrido y utilizarlo en la instrucción except, se 
            #puede utilizar la clase Exception, que es una clase incorporada en Python utilizada para describir 
            #todos los tipos de excepciones, luego de colocar el nombre de la clase Exception se usa la palabra 
            #reservada "as" seguida de un nombre de variable, esto nos permitirá acceder a la instancia de la 
            #excepción y utilizarla dentro del except.
            except Exception as error:
                #type(clase).__name__: Esta instrucción no es un método, sino una expresión que se utiliza para 
                #obtener el nombre de la clase de un objeto en Python, donde type(error) devuelve el tipo de 
                #excepción en este caso ya que error es un objeto de una clase de excepción. 
                # - __name__: Es un atributo especial en Python que se utiliza para obtener el nombre de la 
                #   clase del objeto.
                print("Ocurrió el siguiente tipo de error al intentar conectarse a todos los puertos disponibles: ", type(error).__name__)
                print("Este es el mensaje del error: ", error)
                #Aunque ocurra un error al tratar de encontrar todos los tipos de puertos, esto no significa 
                #que el programa no vaya a funcionar, solo significa que no se ha podido conectar con todos los 
                #puertos seriales que encontró en la computadora, muy seguramente porque puede que estos estén 
                #siendo ya usados en otra cosa.
        
        print("Los puertos encontrados a los que se pudo conectar el programa fueron: \n", result)
        return result

    
    #función add_port(): Método creado dentro de la clase propia llamada MainWindow que recibe como parámetro el 
    #evento que lo activa, para posteriormente ejecutar cierta acción. En este caso el método se ejecuta cada 
    #que se da clic en algún elemento contenido en el ComboBox y lo que hace es asignar su contenido a la 
    #variable cb_port que almacena el puerto que se quiere utilizar.
    def add_port(self):
        #QtWidgets.QComboBox.currentText(): Método que devuelve el texto actualmente seleccionado en un objeto 
        #QComboBox, este no recibe nada como parámetro y devuelve un string.
        self.com_port = self.cb_port.currentText()
        print("El puerto seleccionado fue: \n", self.com_port)


    #función samples_changed(): Método creado dentro de la clase propia llamada MainWindow que recibe como 
    #parámetro el evento que lo activa y el número de muestras del control numérico Spin Box, para 
    #posteriormente ejecutar cierta acción. En este caso el método se ejecuta cada que cambia el valor del 
    #control numérico, por lo que se puede actualizar el número de muestras que se quiere recopilar en tiempo 
    #real y al hacerlo se asigna un nuevo valor a la variable items que almacena el número de muestras a 
    #recopilar.
    def samples_changed(self, val_samples):
        #print(): Método para imprimir un mensaje en consola y después dar un salto de línea (Enter).
        self.items = val_samples
        print("Se recopilarán ", self.items, " datos.")
    
    
    #Método OnStartSaving
    def umbral_changed(self, val_umbral):
        #print(): Método para imprimir un mensaje en consola y después dar un salto de línea (Enter).
        self.umbralLed = val_umbral
        print("Se debe sobrepasar el umbral de ", self.umbralLed, " [mV] = ", 
              self.umbralLed/1000.0,  " [V] para que encienda el led.")
    
    
    #función OnStopClick(): Método creado dentro de la clase propia llamada MainWindow que recibe como 
    #parámetro el evento que lo activa, para posteriormente ejecutar cierta acción.
    #En este caso el evento es activado por dar un clic sobre el botón de Stop y lo que hace es primero esconder
    #el botón de STOP, que previamente tuvo que ser activado y mostrado al dar clic en el botón de START y luego 
    #cambia el valor de la variable booleana stopAcquisition a True, al hacer esto se afectará la función 
    #update_plot(), deteniendo la ejecución del temporizador y logrando así que se detenga la recopilación de 
    #datos.
    def OnStopClick(self):
        print("Stop")
        self.stp_acq = True             #Variable booleana que indica si se ha presionado el botón de STOP.


    #función OnStartSaving(): Método creado dentro de la clase propia llamada MainWindow que recibe como 
    #parámetro el evento que lo activa, para posteriormente ejecutar cierta acción.
    #En este caso el evento es activado por dar un clic sobre el botón de Save y lo que hace es abrir el 
    #explorador de archivos para nombrar el archivo Excel que guardará los datos recabados de tensión y tiempo, 
    #estos datos los tomará del vector self.values, creado en la función update_plot().
    def OnStartSaving(self):
        print("Save Data")
        #Instancia de la librería PyQt5 por medio del constructor de la clase Options, que hereda de las clases 
        #QFileDialog y QtWidgets para ejecutar un método que cree un cuadro de diálogo, el objeto Options se 
        #puede modificar para especificar las opciones de comportamiento del diálogo de archivo, pero para ello 
        #primero se debe crear un objeto y luego usar la compuerta lógica OR (|), ya que el constructor de la 
        #clase Options() no recibe parámetros.
        options = QtWidgets.QFileDialog.Options()
        #Las opciones de configuración disponibles para el objeto Options() son:
        # - DontUseNativeDialog: Indica que no se debe utilizar el explorador de archivos nativo del sistema 
        #   operativo y se debe utilizar el diálogo proporcionado por PyQt, esto significa que tendrá el mismo 
        #   estilo que se indique a la ventana.
        # - ReadOnly: Abre el diálogo en modo de solo lectura, lo que impide al usuario guardar o modificar 
        #   archivos existentes.
        # - HideNameFilterDetails: Oculta los detalles del filtro de nombre en el diálogo.
        # - DontResolveSymlinks: No resuelve los enlaces simbólicos al mostrar el diálogo de archivo.
        # - DontConfirmOverwrite: No muestra un mensaje de confirmación al guardar o sobrescribir un archivo 
        #   existente.
        # - DontUseSheet: No utiliza una hoja de diálogo (específico de macOS).
        # - DontUseCustomDirectoryIcons: No utiliza iconos personalizados para los directorios en el diálogo.
        # - DontUseNativeFileSizeDisplay: No utiliza la representación nativa del tamaño de archivo en el 
        #   diálogo.
        # - DontUseCustomDirectoryIcons: No utiliza iconos personalizados para los directorios en el diálogo.
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        #PyQt5.QtWidgets.QFileDialog.getSaveFileName(): El objeto QtWidgets.QFileDialog proporciona métodos para 
        #mostrar una ventana de selección de archivos. Uno de estos métodos es getSaveFileName(), que se utiliza 
        #para mostrar un diálogo de archivo para guardar un archivo y recibe los siguientes parámetros:
        # - parent: Es el objeto que se utiliza como referencia para mostrar el diálogo de archivo. Puede ser 
        #   una ventana o un widget. Si se proporciona, la ventana se mostrará en la parte superior del objeto.
        # - caption: Es el título que se muestra en la parte superior de la ventana del explorador de archivos.
        # - directory: Es el directorio inicial que se muestra cuando se abre el diálogo de archivo. Se puede 
        #   especificar una ubicación específica  o si no se proporciona solo se mostrará el directorio actual.
        # - filter: Son las opciones de filtro para los tipos de archivos que se mostrarán en la ventana. Se 
        #   pueden especificar diferentes tipos de archivos separados por puntos y coma (;). Por ejemplo, se 
        #   puede indicar un filtro para mostrar solo archivos CSV, PDF o todos los archivos.
        # - initialFilter: Es el filtro que se seleccionará inicialmente cuando se abra el explorador de 
        #   archivos. Si se tiene varios filtros y solo uno se desea que sea seleccionado por defecto, se puede 
        #   especificar en este parámetro.
        # - options: Son opciones adicionales para personalizar el comportamiento del explorador de archivos. Se 
        #   puede usar para ocultar ciertos elementos, permitir la selección de múltiples archivos o mostrar 
        #   miniaturas, modificar el aspecto estético de la ventaba, etc. Para ello se debe asignar el valor 
        #   options al parámetro options y en el método main, usar métodos que afecten a todas las ventanas.
        #   Además se pueden combinar diferentes opciones utilizando operadores especiales.
        #El método .getSaveFileName() devuelve una tupla de dos valores:
        # - filename: Es un string que representa el nombre del archivo seleccionado por el usuario. Si el 
        #   usuario no selecciona ningún archivo o cancela el diálogo, este valor será una cadena vacía. 
        # - filter: Es un string que representa el filtro seleccionado por el usuario en el diálogo de archivo. 
        #   El filtro corresponde al tipo de archivo seleccionado en el diálogo. Por ejemplo, si el usuario 
        #   selecciona el filtro "csv Files (.csv)", este valor será la cadena "csv Files (.csv)". Si el usuario 
        #   cancela el diálogo, este valor también será una cadena vacía.
        #En Python, si queremos almacenar ambos valores en dos variables distintas se usa la siguiente sintaxis:
        #       variable1, variable2 = QtWidgets.QFileDialog.getSaveFileName()
        #Pero si alguno de estos valores no nos interesa que se almacene en una variable, simplemente se coloca 
        #un guión bajo para indicar eso, en este ejemplo el segundo valor de la tupla no se quiere usar:
        #       variable1, _ = QtWidgets.QFileDialog.getSaveFileName()
        nombreArchivo, _= QtWidgets.QFileDialog.getSaveFileName(parent = self,
                                                 caption = "Almacena los datos recopilados del Arduino",
                                                 directory = "",
                                                 filter = "csv Files(*.csv);;All Files (*)",
                                                 options = options)
        #En Python si solo se coloca un if con el nombre de una variable, la condición que se está evaluando 
        #dentro de su paréntesis es que esa variable sea distinta de Null, si es así, se ejecuta la acción que 
        #está dentro del condicional.
        #En este caso se está evaluando que ya se haya seleccionado un nombre de archivo para que se almacenen 
        #los datos recabados del Arduino en él. 
        if(nombreArchivo):
            #open(): Método que sirve para abrir un archivo cualquiera, para ello es necesario indicar dos 
            #parámetros, el primero se refiere a la ruta relativa o absoluta del archivo previamente creado y la 
            #segunda indica qué es lo que se va a realizar con él, el contenido del archivo se asigna a una 
            #variable.
            # - w: Sirve para escribir en un archivo, pero borrará la información que previamente contenía el 
            #   archivo.
            # - a: Sirve para escribir en un archivo sin que se borre la info anterior del archivo, se llama 
            #   append.
            file = open(nombreArchivo, 'w')
            #myFile.write(): Método para colocar un string en un archivo previamente abrierto con el método 
            #open(), en este caso se utiliza para colocar el valor de las dos columnas en el Excel, donde se 
            #acomodan verticalmente los valores de tiempo y tensión recopilados.
            file.write("Library, PyQt5, Pyfirmata" + "\n")
            file.write("Time [s], Voltage Pin A0 [V], Voltage Pin A1 [V], Umbral [V]" + "\n")
            #Del vector values se obtienen los valores de tiempo y tensión recabados y agrupados.
            for i in range(len(self.values)):
                file.write(self.values[i] + "\n")
            #file.close(): Método para cerrar un archivo previamente abrierto con el método open(), es peligroso 
            #olvidar colocar este método, ya que la computadora lo considerará como si nunca hubiera sido 
            #cerrado, por lo cual no podré volver a abrirlo al dar clic sobre él.
            file.close()



#__name__ == __main__: Método main, esta función es super importante ya que sirve para instanciar las clases del 
#programa y ejecutar sus métodos, en python pueden existir varios métodos main en un solo programa, aunque no es 
#una buena práctica.
if (__name__ == "__main__"):
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
    #widget.setStyleSheet(): Método que permite aplicar código CSS (la mayoría de métodos, no todos) a los 
    #widgets de una interfaz gráfica de usuario (GUI).
    # - La siguiente línea de código es un método alternativo a usar la herramienta linear-gradient, ya que 
    #   esta no es admitida por PyQt5:
    #   background: qlineargradient(x1:punto_inicial, y1:punto_inicial, x2:punto_final, y2:punto_final, stop:0 rgb(R_inicial,G_inicial,B_inicial), stop:1 rgb(R_final,G_final,B_final));
    window.setStyleSheet("background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 rgb(24,0,0), stop:1 rgb(150,0,0)); color: white;")
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