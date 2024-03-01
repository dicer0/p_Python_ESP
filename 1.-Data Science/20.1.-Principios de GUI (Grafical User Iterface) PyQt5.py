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
#PyQt5 - QtCore: Clase que incluye métodos para trabajar con temporizadores, tamaño de elementos, fechas, 
#archivos, directorios, señales, hilos, subprocesos, etc.
from PyQt5 import QtCore 
#PyQt5 - QtGui: Clase que incluye clases y métodos para trabajar con gráficos, fuentes, colores, imágenes, 
#íconos y otros elementos visuales utilizados en una interfaz gráfica (GUI) de PyQt5.
from PyQt5 import QtGui
import sys #sys: Librería que permite interactuar directamente con el sistema operativo y consola del ordenador.

#GUI (Graphical User Interface): Es una ventana con elementos como botones, áreas de texto, desplegables, 
#imágenes, etc. que sirven para realizar alguna acción de forma gráfica para el usuario. A continuación, veremos 
#como se crean este tipo de elementos en Python utilizando la librería wxPython o PyQt5.
#La librería PyQt5 es una muy utilizada y versátil, su programación es más sencilla y reducida en comparación 
#con la librería wxPython, pero su principal desventaja y diferencia es que PyQt5 está disponible bajo dos 
#licencias: una licencia comercial y una licencia GPL de código abierto, esto significa que si se desea 
#desarrollar aplicaciones comerciales con PyQt5, se deberá adquirir una licencia comercial. Por otro lado, 
#wxPython se distribuye bajo una licencia de código abierto y permite su uso tanto en aplicaciones comerciales 
#como en proyectos de código abierto. 

#MainWindow: La clase hereda de la clase QMainWindow, que a su vez hereda de la clase QtWidgets y ambas 
#pertenecen a la librería PyQt5. El elemento representa la ventana del GUI y dentro de ella crea una instancia 
#de alguna clase para agregar cualquier elemento, ya sea un Widget directamente o un Canvas (contenedor).
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
        super().__init__()
        #PyQt5.QtWidgets.QMainWindow.setWindowTitle(): Método para colocar un título al Window creado con PyQt5.
        self.setWindowTitle("My App")

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
        #Variable que guarda el directorio y el nombre del archivo creado, se deben reemplazar los guiones\ por /
        #Para leer una imagen o cualquier otro archivo se usa la dirección relativa o absoluta de un directorio: 
        # - Dirección relativa: Es una dirección que busca un archivo desde donde se encuentra la carpeta del 
        #   archivo python actualmente, esta se debe colocar entre comillas simples o dobles.
        # - Dirección absoluta: Es una dirección que coloca toda la ruta desde el disco duro C o cualquier otro 
        #   que se esté usando hasta la ubicación del archivo, la cual se debe colocar entre comillas simples o 
        #   dobles.
        #   ..      : Significa que nos debemos salir de la carpeta donde nos encontramos actualmente.
        #   /       : Sirve para introducirnos a alguna carpeta cuyo nombre se coloca después del slash.
        #   .ext    : Se debe colocar siempre el nombre del archivo + su extensión.
        iconPath = "C:/Users/diego/OneDrive/Documents/The_MechaBible/p_Python_ESP/1.-Data Science/0.-Archivos_Ejercicios_Python/Img/IconLogoDi_cer0.png"
        #PyQt5.QtGui.QIcon(): Constructor de la clase QIcon que hereda de la clase QtGui y perteneciente a la 
        #librería PyQt5, usado para crear un objeto que ícono que pueda ser añadido a cualquier widget como lo 
        #puede ser un botón, un texto estático, etc. El tamaño de dicha imagen será reducido automáticamente.
        icono = QtGui.QIcon(iconPath)
        #Se declaran como self.nombreObjeto los widgets a los que se les vaya a extraer o introducir datos en el 
        #transcurso del funcionamiento de la interfaz gráfica, en este caso se aplica al botón porque este va a 
        #cambiar el texto que tiene escrito cuando sea presionado.
        self.button = QtWidgets.QPushButton(text = "\t\t\t\tPresionameeee!", icon = icono, iconSize = QtCore.QSize(90, 90), checkable = True)
        #PyQt5.QtWidgets.QPushButton.setStyleSheet(): Método que permite aplicar código CSS (la mayoría de 
        #métodos, no todos) a los widgets de una interfaz gráfica de usuario (GUI).
        # - La siguiente línea de código es un método alternativo a usar la herramienta linear-gradient, ya que 
        #   esta no es admitida por PyQt5:
        #   background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 rgb(255,0,0), stop:1 rgb(0,0,255));
        self.button.setStyleSheet("background: qlineargradient(x1:0, y1:1, x2:0, y2:0, stop:0 rgb(255,255,255), stop:1 rgb(91,150,242));")

        #widget.setFixedSize(): Método que sirve para indicar el tamaño de un elemento en una interfaz gráfica 
        #hecha con la librería PyQt5, para ello recibe un objeto QSize:
        # - QtCore.QSize(ancho, alto): Objeto que indica el tamaño del widget.
        self.button.setFixedSize(QtCore.QSize(250, 150))

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
        self.setCentralWidget(self.button)

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
        #Al presionar el botón se ejecutará el método botonPresionado, declarado dentro de la misma clase.
        self.button.clicked.connect(self.botonPresionado)
        #Al presionar el botón se ejecutará el método the_button_was_toggled, declarado dentro de la misma clase
        self.button.clicked.connect(self.the_button_was_toggled)
    
    #función botonPresionado(): Método creado dentro de la clase propia llamada MainWindow que recibe como 
    #parámetro el evento que lo activa, para posteriormente ejecutar cierta acción.
    #En este caso el evento es activado cuando se presiona el botón y lo que hace es checar que dice el texto 
    #que se encuentra sobre el botón, para alternar lo que este dice cuando sea presionado.
    def botonPresionado(self):
        #PyQt5.QtWidgets.QPushButton.text(): Método que devuelve el texto que esté situado sobre un botón.
        if (self.button.text() == "\t\t\t\tPresionameeee!"):
            #PyQt5.QtWidgets.QPushButton.setText(): Método que coloca el texto indicado en el paréntesis sobre 
            #el botón al que se esté aplicando el método.
            self.button.setText("\t\t\t\tPresionado!")
        else:
            self.button.setText("\t\t\t\tPresionameeee!")
        #print(): Método para imprimir un mensaje en consola y después dar un salto de línea (Enter).
        print("Presionado!")

    #función botonPresionado(): Método creado dentro de la clase propia llamada MainWindow que recibe como 
    #parámetro el evento que lo activa para posteriormente ejecutar cierta acción, además recibe el parámetro 
    #checked que es obtenido a través de la señal clicked, este permite saber si un widget ha sido seleccionado 
    #o no.
    #En este caso el evento es activado cuando se cambia el estado del botón y lo que hace es imprimir un 
    #mensaje en consola donde se indica con True o False si el botón que funciona como Switch está presionado 
    #o no.
    def the_button_was_toggled(self, checked):
        #print(): Método para imprimir un mensaje en consola y después dar un salto de línea (Enter).
        print("¿El switch se encuentra presionado?:", checked)


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
    window.move(300, 300)
    #PyQt5.QtWidgets.QMainWindow.resize(): Método que permite cambiar el tamaño del widget, contenedor o ventana 
    #de una GUI, indicando su ancho y alto en.
    window.resize(500, 500)
    #PyQt5.QtWidgets.QMainWindow.setStyleSheet(): Método que permite aplicar código CSS (la mayoría de métodos, 
    #no todos) a los widgets, contenedores o ventanas de una interfaz gráfica de usuario (GUI).
    window.setStyleSheet("background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 rgb(219,160,32), stop:1 rgb(170,0,0));")
    #PyQt5.QtWidgets.QMainWindow.show() = window.show(): Método aplicado al objeto de la clase QMainWindow, 
    #del que hereda esta clase propia para mostrar la ventana del GUI.
    window.show()
    #PyQt5.QtWidgets.QApplication.exec_(): Método para que se ejecute en un loop infinito el GUI, logrando así 
    #que no se ejecute una vez y luego cierre por sí solo, sino que solo se cierre solamente al dar clic en el 
    #tache del window.
    app.exec_()





#VentanaImagen: La clase hereda de la clase QMainWindow, que a su vez hereda de la clase QtWidgets y ambas 
#pertenecen a la librería PyQt5. El elemento representa la ventana del GUI y crea una instancia de la clase 
#GraficaPyQt5 para agregar dentro de la ventana una gráfica.
class VentanaImagen(QtWidgets.QMainWindow):
    #CONSTRUCTOR O INICIALIZADOR DE LA CLASE: En él se declaran los atributos que se reutilizarán en los demás 
    #métodos y que además, deben a fuerza de tener un valor. A través de este constructor se recibe el ancho y 
    #alto de la imagen, que se ajusta al tamaño de la interfaz gráfica.
    def __init__(self, widthImagen, heightImagen):
        #super(Llamada al constructor heredado).__init__(Parámetros que se le asignan): Lo que hace el método 
        #super() es llamar al constructor de la clase padre de la clase actual (si es que no se le indica ningún 
        #parámetro) o a cualquier clase que se le indique en su parámetro, después la instrucción .__init__() 
        #asigna valores default a los parámetros del constructor de la clase padre (si es que no se indica 
        #ningún parámetro), aunque de igual manera se pueden asignar parámetros adicionales, cualquier parámetro 
        #incluido en el método init, será considerado como adicional. En conclusión, lo que está realizando la 
        #línea de código es primero llamar al constructor de la superclase para realizar las tareas de 
        #inicialización requeridas antes de indicar parámetros adicionales a la instancia de la clase actual.
        super().__init__()
        #PyQt5.QtWidgets.QMainWindow.setWindowTitle(): Método para colocar un título al Window creado con PyQt5.
        self.setWindowTitle("GUI Imagen y texto estáticos")
        
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
        text_label = QtWidgets.QLabel(text = "<p style='background-color: black; font-size: 30px; font-family: Consolas, monospace; color: white;'>di_cer0 Logo</p>")
        
        #CREACIÓN DE LOS WIDGETS: Imágen, clase QLabel
        #Las clases PyQt5.QtGui.QPixmap y PyQt5.QtWidgets.QLabel están relacionadas y se utilizan en conjunto 
        #para trabajar con imágenes en la interfaz gráfica.
        #   PyQt5.QtGui.QPixmap: Representa una imagen en memoria creada con datos en bruto, osea un formato 
        #   matricial 3D conformado 3 capas o dimensiones RGB que contienen valores de 0 a 255. Esta clase 
        #   proporciona métodos para cargar, manipular y transformar imágenes.
        #  
        #   PyQt5.QtWidgets.QLabel: Es una representación de imagen que puede ser utilizada directamente en los 
        #   controles y widgets de la interfaz gráfica de PyQt5.
        #Variable que guarda el directorio y el nombre del archivo creado, se reemplazan los guiones\ por / para 
        #leer una imagen o cualquier otro archivo se usa la dirección relativa o absoluta de un directorio: 
        # - Dirección relativa: Es una dirección que busca un archivo desde donde se encuentra la carpeta del 
        #   archivo python actualmente, esta se debe colocar entre comillas simples o dobles.
        # - Dirección absoluta: Es una dirección que coloca toda la ruta desde el disco duro C o cualquier otro 
        #   que se esté usando hasta la ubicación del archivo, la cual se debe colocar entre comillas simples o 
        #   dobles.
        #   ..      : Significa que nos debemos salir de la carpeta donde nos encontramos actualmente.
        #   /       : Sirve para introducirnos a alguna carpeta cuyo nombre se coloca después del slash.
        #   .ext    : Se debe colocar siempre el nombre del archivo + su extensión.
        path = "C:/Users/diego/OneDrive/Documents/The_MechaBible/p_Python_ESP/1.-Data Science/0.-Archivos_Ejercicios_Python/Img/IconLogoDi_cer0.png"
        #Cargar una Imagen: Se crea una instancia de la librería PyQt5 por medio del constructor de la clase 
        #QPixmap para cargar una imagen en memoria con datos en bruto.
        # - filepath: En este atributo se indica el nombre de archivo junto con la ruta completa de donde se 
        #   encuentra la imagen que se va a cargar, la cual debe estar indicada en forma de string, con este 
        #   atributo no se sigue la nomenclatura de poner el nombre del atributo seguido de su valor 
        #   (filepath = valor), solamente se pone el path entre comillas.
        # - format: El formato de imagen deseado. Puede ser una cadena como "PNG", "JPEG", "BMP", etc. Si no se 
        #   especifica, se intentará detectar automáticamente el formato.
        rawImage = QtGui.QPixmap(path, format = "PNG")
        #PyQt5.QtGui.QPixmap.scaled(): Método utilizado para redimensionar una imagen conformada por datos 
        #brutos, representada por un objeto QPixmap, se realiza a través de la siguiente sintaxis:
        #scaledImage = originalImage.scaled(width, height, aspectRatioMode)
        # - originalImage: Es el objeto QPixmap original que se desea redimensionar.
        # - width: Es el nuevo ancho de la imagen redimensionada.
        # - height: Es la nueva altura de la imagen redimensionada.
        # - aspectRatioMode: Es una constante de la clase QtCore.Qt.AspectRatioMode que especifica cómo se debe 
        #   ajustar la imagen para mantener la proporción.
        #           - QtCore.Qt.AspectRatioMode.IgnoreAspectRatio: La imagen se ajusta exactamente al tamaño 
        #             especificado, sin mantener la proporción original. Esto puede dar lugar a una distorsión 
        #             de la imagen.
        #           - QtCore.Qt.AspectRatioMode.KeepAspectRatio: La imagen se redimensiona manteniendo la 
        #             proporción original y ajustándose dentro del tamaño especificado para que quepa 
        #             completamente sin recortarla. Esto puede generar márgenes en blanco si la relación de 
        #             aspecto difiere del tamaño especificado.
        #           - QtCore.Qt.AspectRatioMode.KeepAspectRatioByExpanding: La imagen se redimensiona 
        #             manteniendo la proporción original y ocupando todo el tamaño especificado. Esto puede 
        #             provocar que parte de la imagen quede fuera de los límites del tamaño especificado.
        #En todos los parámetos mencionados para este método, no se indica explícitamente su nombre, solo se 
        #asigna un valor y el método identifica cuál es por su orden.
        #Todas las operaciones donde se afecta a una imagen se deben realizar a la imagen representada en 
        #datos brutos, para luego asignarse al widget de la GUI.
        scaledImage = rawImage.scaled(widthImagen, heightImagen, QtCore.Qt.AspectRatioMode.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        #Mostrar la imagen en un widget: Para mostrar la imagen de tipo Bitmap en un widget gráfico de se usa 
        #una instancia de la clase PyQt5.QtWidgets.QLabel, que es parte de la biblioteca PyQt5 y se utiliza para 
        #crear un widget que muestre un texto estático o una imagen en una interfaz gráfica, se le deben indicar 
        #los siguientes parámetros cuando se usa para crear una imagen estática:
        # - parent: Este parámetro es opcional y especifica el widget padre del QLabel. Indica a qué widget 
        #   pertenece el QLabel.
        # - pixmap (QPixmap): La imagen que se mostrará en la etiqueta.
        #Para dar estilo al QLabel cuando se utiliza para mostrar texto estático es mejor utilizar etiquetas 
        #HTML que contengan un style que les dé estilo por medio de instrucciones CSS, además es importante 
        #mencionar que para el style se deben usar comillas simples ('') para que no tenga conlficto con las 
        #comillas dobles del parámetro text = "". PyQt5 acepta algunas instrucciones CSS pero no todas.
        image_label = QtWidgets.QLabel(pixmap = scaledImage)    #Imagen redimensionada.

        #ALINEACIÓN DEL CONTENIDO EN LOS LABELS (IMÁGENES O TEXTO ESTÁTICOS):
        #PyQt5.QtWidgets.QLabel.setAlignment(): Método utilizado para establecer la alineación del contenido 
        #dentro de un objeto QLabel. Permite controlar cómo se posiciona y alinea el texto o la imagen dentro 
        #del espacio disponible en la etiqueta. Los valores que recibe el método son:
        # - QtCore.Qt.AlignLeft: Alinea el contenido a la izquierda.
        # - QtCore.Qt.AlignRight: Alinea el contenido a la derecha.
        # - QtCore.Qt.AlignHCenter: Alinea el contenido en el centro horizontal.
        # - QtCore.Qt.AlignJustify: Justifica el contenido.
        # - QtCore.Qt.AlignJustify: Justifica el contenido.
        # - QtCore.Qt.AlignBottom: Alinea el contenido en la parte inferior.
        # - QtCore.Qt.AlignVCenter: Alinea el contenido en el centro vertical.
        # - QtCore.Qt.AlignCenter: Alinea el contenido en el centro tanto horizontal como vertical.
        #Estos valores se pueden combinar utilizando el operador OR (|) para lograr una alineación específica.
        text_label.setAlignment(QtCore.Qt.AlignCenter)          #QLabel texto colocado en medio.
        image_label.setAlignment(QtCore.Qt.AlignCenter)         #QLabel imagen colocado en medio.

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
        #Instancia de la clase QWidget, que hereda de la clase QtWidgets y pertenece a la librería PyQt5, dicho 
        #objeto funciona como un contenedor que puede almacenar widgets directamente, proporcionando 
        #funcionalidades para mostrar, ocultar, establecer posición, tamaño, manejar eventos, etc. de los 
        #diferentes botones, checkboxes, áreas de texto, comboboxes, radiobuttons, listboxes, ventanas de 
        #diálogo (ventana que muestra el explorador de archivos), etc. 
        central_widget = QtWidgets.QWidget()                    #Contenedor de una imagen y un texto estáticos.
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
        self.setCentralWidget(central_widget)                   #Contenedor colocado en el área central.

        #Objeto de la clase QVBoxLayout, el cual se utiliza para organizar los widgets en una disposición 
        #vertical, proporcionando una forma conveniente de colocar los widgets uno debajo del otro en una 
        #ventana o en otro contenedor. 
        # - parent: Si el constructor de esta clase recibe como parámetro un objeto QWidget, ese será el 
        #   contenedor principal del objeto QVBoxLayout que organiza sus elementos verticalmente.
        # - Si no recibe ningún parámetro, este es un contenedor vacío sin widget principal que aceptará 
        #   varios elementos o contenedores y los irá colocando verticalmente uno después del otro.
        layout = QtWidgets.QVBoxLayout(central_widget) #Alineación vertical de contenedores.
        #PyQt5.QtWidgets.QVBoxLayout.addWidget(): Método usado para añadir un widget de manera secuencial en la 
        #columna de un diseño vertical, como lo puede ser un botón, lista desplegable, texto, imagen, etc. Se 
        #indica el órden en el que se colocarán los elementos dependiendo de cual fue añadido primero y cual 
        #después. 
        layout.addWidget(image_label)                           #Al contenedor primero se coloca la imagen.
        #PyQt5.QtWidgets.QVBoxLayout.addWidget(): Método que permite agregar un espacio vacío indicado en 
        #pixeles entre los widgets de un contenedor QVBoxLayout, este se debe colocar exactamente entre los 
        #elementos que se desea separar, antes de siquiera agregarlo al contenedor con el método .addWidget()
        layout.addSpacing(30)                                   #Luego un espacio de separación de 30px.
        layout.addWidget(text_label)                            #Y finalmente se coloca el texto.
        

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
    appImg = QtWidgets.QApplication(sys.argv)
    #Instancia de nuestra clase propia llamada MainWindow que fue creada en este mismo programa (window se 
    #refiere a la ventana del GUI en PyQt5) e incluye una instancia de la clase GraficaPyQt5 para agregar un 
    #widget que crea una gráfica dentro, el constructor vacío lo que hace es indicar que se cree y muestre la 
    #ventana. Además en este caso se le pasa como parámetro el ancho y alto de la ventana e imagen al 
    #constructor de la clase. 
    ancho = 500                                                 #Ancho de la ventana e imagen de 500px.
    alto = 500                                                  #Alto de la ventana e imagen de 500px.
    #Debido a que la imagen se redimensionó manteniendo su proporción original y ajustándose dentro del tamaño 
    #especificado para que quepa completamente sin recortarla, solamente hará caso al ancho de la ventana, no a 
    #su altura, ya que sino esta se vería deformada.
    windowImg = VentanaImagen(ancho, alto)
    #PyQt5.QtWidgets.QMainWindow.setStyleSheet(): Método que permite aplicar código CSS (la mayoría de métodos, 
    #no todos) a los widgets, contenedores o ventanas de una interfaz gráfica de usuario (GUI).
    windowImg.setStyleSheet("background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 rgb(20,20,20), stop:1 rgb(150,0,0));")
    #PyQt5.QtWidgets.QMainWindow.show() = window.show(): Método aplicado al objeto de la clase QMainWindow, 
    #del que hereda esta clase propia para mostrar la ventana del GUI.
    windowImg.show()
    #PyQt5.QtWidgets.QApplication.exec_(): Método para que se ejecute en un loop infinito el GUI, logrando así 
    #que no se ejecute una vez y luego cierre por sí solo, sino que solo se cierre solamente al dar clic en el 
    #tache del window.
    appImg.exec_()