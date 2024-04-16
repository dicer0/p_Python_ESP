# -*- coding: utf-8 -*-

#openpyxl: Es una biblioteca que permite automatizar tareas en Excel, como leer y escribir datos en hojas de 
#cálculo, manipular gráficos, ejecutar macros y más, todo desde Python.
import xlwings
#time: Librería para el manejo de tiempos, como retardos, contadores, etc.
import time
#PyQt5 - QtCore: Clase que incluye métodos para trabajar con temporizadores, tamaño de elementos, fechas, 
#archivos, directorios, señales, hilos, subprocesos, etc.
from PyQt5 import QtCore

#ExcelDataCopier: Clase propia para copiar la tabla de un archivo de Excel y guardarla temporalmente en memoria, 
#para posteriormente poderla pegar en donde queramos de forma automática. Esta clase hereda de QtCore.QThread, 
#porque el archivo de Excel solo se podrá pegar con todo y su formato mientras el archivo de Excel se mantenga 
#abierto por la librería xlwings, esto solo ocurrirá durante el tiempo indicado por el temporizador creado con 
#la librería time. QtCore.QThread lo que hace es mostrar dicho contador en la GUI de PyQt5.
class ExcelDataCopier(QtCore.QThread):
    #QtCore.pyqtSignal(): El método .pyqtSignal() de la clase PyQt5.QtCore se utiliza para declarar señales que 
    #se comuniquen durante la ejecución de una GUI de PyQt5. Las señales son una forma de comunicación entre 
    #objetos en PyQt5, permitiendo que un objeto emita una señal y otros la reciban y respondan en consecuencia.
    #Su constructor recibe como parámetro el tipo de dato que la señal va a transportar, como int, str, float, 
    #list, dict, etc. La señal se utilizará como si fuera un tipo de evento en PyQt5.
    # - Definición de la señal: Esto se hace creando un objeto de señal QtCore.pyqtSignal().
    #       - signal = QtCore.pyqtSignal()
    # - Emisión de la señal: En algún lugar de la clase, se puede llamar al método emit() a través del operador 
    #   self (ya que este cambia su valor durante la ejecución del código) y el objeto QtCore.pyqtSignal() para 
    #   enviar la variable que transporta la señal a las clases que la quieran usar.
    #       - self.signal.emit(variable)
    # - Conexión de la señal: En otras clases del programa, se pueden conectar funciones o métodos que hagan 
    #   algo con lo que devuelve la señal utilizando el método updated.connect() a través de un objeto de la 
    #   clase que creó la señal.
    #       - objectoClaseSeñal.signal.connect(funcion_Que_Hace_Algo_Con_Lo_Que_Devuelve_La_Señal)
    signal = QtCore.pyqtSignal(str)    #La señal transportará el conteo de cuando está abierto el Excel.

    #Bucle que cierra todas las aplicaciones o instancias abiertas por el programa de Excel al ejecutar este 
    #programa. Esto se debe hacer antes y después de haber abierto el archivo de Excel.
    #xlwings.apps: El atributo apps extraído directamente de la librería xlwings que contiene todas las 
    #aplicaciones de Microsoft Excel que están siendo controladas por xlwings durante la ejecución del programa.
    for app in xlwings.apps:
        #xlwings.apps.quit(): Este método se utiliza para cerrar las aplicaciones de Excel asociadas a un 
        #objeto Book previamente abiertas con el método constructor xlwings.Book(). 
        app.quit()

    #def __init__(self): Es el constructor o inicializador de la clase, este se llama automáticamente cuando se 
    #crea un objeto que instancíe la clase y en él se declaran los atributos que se reutilizarán en los demás 
    #métodos. En Python, el primer parámetro de cualquier método constructor debe ser self, los demás pueden 
    #servir para cualquier cosa, pero si se declaran en el constructor, estos a fuerza deben tener un valor.
    #self: Se refiere al objeto futuro que se cree a partir de esta clase, es similar al concepto de this en 
    #otros lenguajes de programación.
    def __init__(self, file_path, delay_segs):
        #super(Llamada al constructor heredado).__init__(Parámetros que se le asignan): Lo que hace el método 
        #super() es llamar al constructor de la clase padre de la clase actual (si es que no se le indica ningún 
        #parámetro) o a cualquier clase que se le indique en su parámetro, después la instrucción .__init__() 
        #asigna valores default a los parámetros del constructor de la clase padre (si es que no se indica 
        #ningún parámetro), aunque de igual manera se pueden asignar parámetros adicionales, cualquier parámetro 
        #incluido en el método init, será considerado como adicional. En conclusión, lo que está realizando la 
        #línea de código es primero llamar al constructor de la superclase para realizar las tareas de 
        #inicialización requeridas antes de indicar parámetros adicionales a la instancia de la clase actual.
        super().__init__()          #Herencia del constructor de la clase QtCore.QThread.
        self.file_path = file_path  #Directorio del archivo de Excel del cual queremos obtener su tabla.
        self.workBook = None        #Valor inicial del libro (workBook) del Excel.
        self.delay = delay_segs     #Temporizador que me permite mantener abierto el archivo de Excel.
        self.countdown_message = "Bienvenido"   #Mensaje de bienvenida inicial.

    #run(): Cuando se quiere crear una señal de PyQt5, la clase que la contenga debe heredar de la clase 
    #QtCore.QThread, luego se creará la señal (que se debe llamar signal) a través de un objeto 
    #QtCore.pyqtSignal() y después se debe añadir un método que se llame run(), este contendrá el código que se 
    #correrá en un hilo (Thread) el cual se ejecutará por separado cuando en una clase distinta se incialice 
    #por medio de un método que se debe llamar start().
    # - signal = QtCore.pyqtSignal()
    # - run(): Código que se ejecuta en un hilo por separado cuando se quiera utilizar la señal.
    # - start(): Método que inicializa la ejecución del hilo donde se corre el método run().
    #run(): Método que obtiene toda la tabla de una hoja de un libro de Excel y nos permite copiarla al 
    #portapapeles con todo y su formato de celdas durante cierto tiempo dado por un temporizador donde se 
    #encuentra abierto el archivo de Excel, cuando se termina dicho conteo, solo se podrán copiar los datos de 
    #la tabla, pero ya no contendrá su formato de celdas.
    def run(self):
        #xlwings.Book(): Método para abrir o crear (si es que este no existe) un archivo (libro) de Excel para 
        #acceder a sus hojas de cálculo. Este método devuelve un objeto que representa el libro de Excel 
        #abierto.
        self.workBook = xlwings.Book(self.file_path)
        
        #xlwings.Book: Los atributos del objeto Book que devuelven propiedades específicas del Excel son:
        # - xlwings.Book.sheets:        Este atributo devuelve una lista de objetos xlwings.Sheet, que 
        #   representan las hojas de cálculo en el libro.
        # - xlwings.Book.names:         Devuelve una lista de objetos xlwings.Name que representan los nombres 
        #   definidos en el libro, osea rangos de celdas definidos para aplicar fórmulas o macros. 
        # - xlwings.Book.charts:        Devuelve una lista de objetos xlwings.Chart que representan los gráficos 
        #   en el libro.
        # - xlwings.Book.app:           Devuelve el objeto xlwings.App que representa la aplicación de Excel 
        #   asociada al libro. La aplicación es la instancia de Excel que se está ejecutando en el sistema y 
        #   representa todo el programa de Excel, incluyendo todas las hojas de cálculo, libros abiertos, 
        #   configuraciones de aplicación, etc.
        #       - xlwings.Book.app.visible:         Es un atributo booleano que indica si la ventana de Excel es 
        #         visible (True) o no (False).
        #       - xlwings.Book.app.display_alerts:  Es un atributo booleano que indica si el programa de Excel 
        #         puede mostrar (True) o no (False) mensajes de alerta, como advertencias o confirmaciones 
        #         durante la ejecución del programa. El evitar la aparición de ventanas emergentes nos 
        #         aseguramos que el programa no se vea detenido o estorbado por ellas.
        #       - xlwings.Book.app.version:         Devuelve la versión de Excel con la que estás trabajando.
        #       - xlwings.Book.app.screen_updating: Es un atributo booleano que controla si las actualizaciones 
        #         de pantalla están habilitadas (True) o deshabilitadas (False). Deshabilitar las 
        #         actualizaciones de pantalla puede mejorar el rendimiento al ejecutar operaciones de 
        #         manipulación de celdas y rangos.
        #       - xlwings.Book.app.calculation:     Controla el modo de cálculo de Excel. Puede ser "manual", 
        #         "automatic" o "semiautomatic", determinando si Excel recalcula automáticamente las fórmulas al 
        #         cambiar los datos o si espera hasta que se le indique explícitamente que lo haga.
        #       - xlwings.Book.app.status_bar:      Permite establecer un mensaje en la barra de estado de 
        #         Excel.
        #       - xlwings.Book.app.books:           Devuelve una lista de todos los libros abiertos en la 
        #         instancia de Excel.
        # - xlwings.Book.fullname:      Devuelve la ruta completa del archivo del libro de Excel.
        # - xlwings.Book.name:          Devuelve el nombre del archivo del libro de Excel.
        # - xlwings.Book.path:          Devuelve la ruta del directorio en el que se encuentra el libro de 
        #   Excel.
        # - xlwings.Book.selection:     Devuelve el rango de celdas seleccionado actualmente en el libro.
        # - xlwings.Book.active_sheet:  Devuelve el objeto xlwings.Sheet que representa la hoja de cálculo 
        #   activa en el libro.
        # - xlwings.Book.colors:        Devuelve una lista de colores definidos en el libro.
        print("Libro de Excel abierto:\t\t", self.workBook.app.books)   #Nombre del libro de Excel abierto.
        print("Hojas del Excel abierto:\t", self.workBook.sheets)       #Nombre de las hojas del Excel abierto.
        self.workBook.app.visible = False                               #Visualización del Excel = False.
        self.workBook.app.display_alerts = False                        #Ventanas emergentes del Excel = False.
        #Bucle for que recorre la lista de objetos Sheet devueltos del atributo xlwings.Book.sheets, que 
        #representan todas las hojas de cálculo del libro del Excel abierto.
        for sheet in self.workBook.sheets:
            #xlwings.Book: Los atributos del objeto Book que devuelven propiedades específicas del Excel son:
            # - xlwings.Book.sheets: Este atributo devuelve una lista de objetos xlwings.Sheet, que representan 
            #   las hojas de cálculo en el libro.
            #       - xlwings.Book.sheets.add():            Agrega una nueva hoja de cálculo al libro de Excel.
            #       - xlwings.Book.sheets.select():         Selecciona la hoja de cálculo especificada por su 
            #         nombre, su índice o simplemente devuelve todo el contenido (tablas) de todas las páginas.
            #       - xlwings.Book.sheets.__getitem__():    Permite acceder a una hoja de cálculo específica 
            #         utilizando tanto el índice numérico (contando desde 0) como el nombre de la hoja de 
            #         cálculo para acceder a la hoja deseada.
            #       - xlwings.Book.sheets.__len__():        Devuelve el número de hojas de cálculo en el libro.
            #       - xlwings.Book.sheets.names:            Devuelve una lista de los nombres de todas las hojas 
            #         de cálculo en el libro.
            #       - xlwings.Book.sheets.__iter__():       Permite iterar (ir una por una) sobre todas las 
            #         hojas de cálculo del libro.
            #       - xlwings.Book.sheets.range():          Devuelve un objeto Range que representa un rango de 
            #         celdas en la hoja de cálculo.
            sheet.select()              #Selecciona todo el contenido (todas las tablas) del objeto Sheet.
            #xlwings.Book.sheets.api.UsedRange.Copy(): Este método permite acceder a la API de Excel para poder 
            #interactuar con su hoja desde Python (Sheets.api), con ella podremos copiar el rango de celdas que 
            #esté siendo utilizado en el Sheet del workBook, osea que contenga datos o formatos aplicados en la 
            #hoja de cálculo de Excel y copiar ese contenido al portapapeles (Sheets.api.UsedRange.Copy()).
            # - Portapapeles: También conocido como "clipboard", es una memoria temporal en los sistemas 
            #   operativos que se utiliza para copiar y almacenar datos temporalmente (texto, imágenes, etc.) 
            #   mientras estos se transfieren entre diferentes aplicaciones. Los datos en el portapapeles se 
            #   sobrescriben cuando se copian nuevos datos en él.
            sheet.api.UsedRange.Copy()  #Copiar el contenido del Sheet del Excel en el portapapeles.
        
        #Solamente se puede pegar la tabla con sus datos y formato mientras se encuentra abierto el archivo de 
        #Excel al cerrarse, se copian solamente los datos, pero ya no el formato, para solucionar esto se creará
        #un temporizador.
        #BUCLE FOR: La sintaxis de este se conforma de una variable temporal que corresponde a cada iteración del 
        #bucle in range(num_Inicio, num_Final, intervalo_De_Conteo). 
        for remaining in range(self.delay, 0, -1):
            #self.countdown_message: Se actulizará el atributo para mostrar un mensaje cambiante en la GUI de 
            #PyQt5.
            self.countdown_message = f"Countdown: {remaining} seconds"      #Actualiza el mensaje de conteo.
            # - Emisión de la señal: En algún lugar de la clase, se puede llamar al método emit() a través del 
            #   operador self (ya que la señal cambia su valor durante la ejecución del código) y el objeto 
            #   QtCore.pyqtSignal() para enviar la variable que transporta la señal a las clases que la quieran 
            #   usar.
            #       - self.QtCore.pyqtSignal().emit(variable)
            self.signal.emit(self.countdown_message)        #Mandar variable por medio de señal.
            #print(): Método para imprimir un mensaje en consola y después dar un salto de línea (Enter). Este 
            #método puede recibir además los siguientes parámetros adicionales:
            # - sep:    Especifica el separador entre los objetos que se imprimen. Por defecto, es un espacio en 
            #   blanco.
            # - end:    Especifica el carácter o cadena que se imprimirá al final. Por defecto, es un salto de 
            #   línea (\n), pero puede ser un tabulador (\t), un delete de toda la línea (\r).
            # - file:   En este se indica un objeto de archivo abierto o un objeto similar a un archivo que se 
            #   utilizará como destino de salida. Por defecto, es sys.stdout.
            # - flush:  Un valor booleano que indica si se debe forzar el vaciado del búfer. Por defecto, es 
            #   False. Un buffer es una región de memoria temporal utilizada para almacenar datos mientras se 
            #   transfieren entre dos dispositivos o procesos que operan a diferentes velocidades o de manera 
            #   asincrónica. 
            print(self.countdown_message, end = "\r")
            #time.sleep(): Método que se utiliza para suspender la ejecución de un programa durante un intervalo 
            #de tiempo específico dado en segundos. 
            time.sleep(1)
        #Al terminar de ejecutar el conteo, se actualiza el mensaje mostrado en consola y la GUI.
        self.countdown_message = "Countdown finished. Closing Excel..."
        print(self.countdown_message)
        #Y se vuelve a emitir este mensaje a través de la señal personalizada creada en esta clase.
        self.signal.emit(self.countdown_message)
        
        #MANEJO DE EXCEPCIONES: Es una parte de código que se conforma de 2 o3 partes, try, except y finally: 
        # - Primero se ejecuta el código que haya dentro del try, y si es que llegara a ocurrir una excepción 
        #   durante su ejecución, el programa brinca al código del except.
        # - En la parte de código donde se encuentra la palabra reservada except, se ejecuta cierta acción 
        #   cuando ocurra el error esperado.
        # - Por último, cuando no ocurra una excepción durante la ejecución del gestor de excepciones, se 
        #   ejecutará el código que esté incluido dentro del finally después de haber terminado de ejecutar lo 
        #   que haya en el try, pero si ocurre una excepción, la ejecución terminará cuando se llegue al except.
        try:
            #xlwings.Book.close(): Este método se utiliza para cerrar el libro de Excel asociado a un objeto 
            #Book previamente abierto con el método constructor xlwings.Book(). 
            self.workBook.close()
        except Exception as e:
            print(f"An error occurred while closing the Excel file: {e}")
        
        #Bucle que cierra todas las aplicaciones o instancias abiertas por el programa de Excel al ejecutar este 
        #programa. Esto se debe hacer antes y después de haber abierto el archivo de Excel.
        #xlwings.apps: El atributo apps extraído directamente de la librería xlwings que contiene todas las 
        #aplicaciones de Microsoft Excel que están siendo controladas por xlwings durante la ejecución del 
        #programa.
        for app in xlwings.apps:
            #xlwings.apps.quit(): Este método se utiliza para cerrar las aplicaciones de Excel asociadas a un 
            #objeto Book previamente abiertas con el método constructor xlwings.Book(). 
            app.quit()