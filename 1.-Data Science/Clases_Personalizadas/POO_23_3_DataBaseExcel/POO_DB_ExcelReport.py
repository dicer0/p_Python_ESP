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

#SQLAlchemy: Para instalarlo se debe ejecutar el comando pip install sqlalchemy, y es una biblioteca de Python 
#para SQL ORM (Object-Relacional-Mapping) que proporciona a los desarrolladores un conjunto de herramientas para 
#interactuar con bases de datos utilizando objetos y métodos de Python, en lugar de escribir consultas SQL.
#Entidad: Se refiere a una tabla que almacena datos sobre un tipo de objeto o elemento del mundo real. Cada fila 
#en la tabla representa una instancia individual de esa entidad, y cada columna representa un atributo o 
#característica de esa entidad.
#Atributo: Son las columnas de una tabla que representan las características o propiedades de la entidad que está 
#siendo modelada, todas ellas tienen un nombre y tipo de dato asociado.
#Registro: También conocido como "fila" o "tupla", representa una instancia individual de una entidad en la tabla. 
#Cada registro contiene los valores de los atributos correspondientes a esa instancia específica de la entidad.

#SQLAlchemy - create_engine: El método create_engine sirve para configurar la conexión a la base de datos.
from sqlalchemy import create_engine
#SQLAlchemy - text: El método text se utiliza para crear un objeto de expresión textual que recibe como parámetro 
#el código de una consulta SQL en forma de String.
from sqlalchemy import text
#pandas: Librería que proporciona estructuras de datos y herramientas de manipulación y análisis de datos. 
import pandas

#DatabaseExcelHandler: La clase representa la acción de conectarse a la base de datos a través de una URL, 
#procesar los datos y finalmente crear un reporte en Excel, para ello al constructor se le debe pasar dos 
#parámetros, la URL de conexión a la base de datos y la dirección donde quiero que se guarden mis reportes.
class DatabaseExcelHandler:
    #def __init__(self): Es el constructor o inicializador de la clase, este se llama automáticamente cuando se 
    #crea un objeto que instancíe la clase y en él se declaran los atributos que se reutilizarán en los demás 
    #métodos. En Python, el primer parámetro de cualquier método constructor debe ser self, los demás pueden 
    #servir para cualquier cosa, pero si se declaran en el constructor, estos a fuerza deben tener un valor.
    #self: Se refiere al objeto futuro que se cree a partir de esta clase, es similar al concepto de this en 
    #otros lenguajes de programación.
    def __init__(self, db_url):
        #De esta manera se asigna al atributo self.db_url el valor de la URL que recibe el constructor de la 
        #clase como parámetro.
        self.db_url = db_url    #URL de conexión para la base de datos.

    #En este caso lo que se hará es extraer datos de la base de datos, los cuales serán comparados con algunos 
    #valores de la siguiente lista de diccionarios y si algunos de ellos son iguales, se tomará algunos datos de 
    #la database (DB), se extraerán algunos otros de la lista de diccionarios y se agregarán unos nuevos para 
    #crear una nueva estructura de datos, que pueda ser agregada a un reporte y posteriormente mostrada a su vez 
    #en una GUI de PyQt5.
    finalData = []  #Array que almacenará lo que trae el ORM de la base de datos.
    compareDicc = [{
        "tituloStatic": "Grupo de Datos 1",     #Datos que así se pasan al diccionario final.
        "datoStatic": "Dato grupo 1",         
        "estatusFilter": "activo",              #Datos de filtrado.
        "userIdFilter": 1,
        "categoryIdFilter": 2
    },
    {
        "tituloStatic": "Grupo de Datos 2",     #Datos que así se pasan al diccionario final.
        "datoStatic": "Dato grupo 2",         
        "estatusFilter": "inactivo",            #Datos de filtrado.
        "userIdFilter": 2,
        "categoryIdFilter": 3
    }]
    #CONFIGURAR LA CONEXIÓN A DISTINTOS TIPOS DE BASES DE DATOS: Para ello de igual manera se debe realizar la
    #instalación de diferentes librerías.
    #MANEJO DE EXCEPCIONES: Es una parte de código que se conforma de 2 o3 partes, try, except y finally: 
    # - Primero se ejecuta el código que haya dentro del try, y si es que llegara a ocurrir una excepción durante su 
    #   ejecución, el programa brinca al código del except.
    # - En la parte de código donde se encuentra la palabra reservada except, se ejecuta cierta acción cuando ocurra 
    #   el error esperado.
    # - Po último, cuando no ocurra una excepción durante la ejecución del gestor de excepciones, se ejecutará el 
    #   código que esté incluido dentro del finally después de haber terminado de ejecutar lo que haya en el try, pero
    #   si ocurre una excepción, la ejecución terminará cuando se llegue al except.
    #Se utiliza esta arquitectura de código cuando se quiera efectuar una acción donde se espera que pueda ocurrir un 
    #error durante su ejecución.
    #1.- MySQL: create_engine('mysql+pymysql://username:password@hostname:port/database_name')
    #instalation: pip install mysqlclient
    #instalation: pip install pymysql
    try:
        mysql_engine = create_engine('mysql+pymysql://root:PincheTonto!123@localhost:3306/1_platziblog_db')
        #CONTEXTO DE EJECUCIÓN: Es un concepto de programación que se utiliza cuando se quiere trabajar con recursos 
        #que necesitan ser gestionados de forma prioritaria, como una apertura de archivos, conexiones de red o 
        #conexiones a bases de datos. Su sintaxis básica es la siguiente: 
        #       with expresion as variable:
        # - expresion: Este parámetro recibe un método que devuelva un objeto, ya que este se comportará como el 
        #   "contexto de ejecución", osea el recurso que debe ser gestionado, un ejemplo es open('archivo.txt', 'r').
        # - variable: Es el nombre de la variable que se asigna al objeto de contexto dentro del bloque with.
        #Utilizar el operador with es igual a asignar una variable, la única diferencia es que al utilizar el operador
        #with nos aseguramos que el objeto que devuelva el método utilizado sea gestionado por un entorno temporal y 
        #complete sus tareas correctamente, como cerrar un archivo, incluso si ocurren errores: 
        #   nombreVariable = método() 
        #   with método() as nombreVariable
        #De igual manera, el operador with se asegura que no debamos guardar el archivo al terminar la acción, o cerrar 
        #una conexión a la base de datos, ya que esta se maneja de forma automática por el operador.
        #create_engine().connect(): El método .connect() sirve para establecer la conexión con la base de datos.
        with mysql_engine.connect() as connection1:
            print("1.- MySQL Connection successful!!!")
            #OBTENCIÓN DE DATOS DE LA BASE DE DATOS: Ya que estemos seguros que la conexión a la base de datos se ha 
            #realizado de forma exitosa, podremos utilizar comandos SQL para filtrar y obtener cierta información, esto se 
            #realiza a través de la variable que haya utilizado el método .connect(), el método .execute() y .text().  
            SQL_Query_string =  """SELECT 	  * 
                                    FROM 	    posts
                                    ORDER BY  titulo DESC;"""
            SQL_TextObject = text(SQL_Query_string)
            #.create_engine().connect().execute(): Ya que se haya realizado la conexión con la base de datos, a través de 
            #un objeto de variable textual (text) se puede realizar una consulta a la base de datos a través de SQL y lo 
            #que devuelve es un objeto llamado ResultProxy, el cual en algunas cosas se maneja como un diccionario.
            resultProxy = connection1.execute(SQL_TextObject)
            print("Tipo de Dato ResultProxy: ", type(resultProxy))
            #pandas.DataFrame: La clase DataFrame de la librería pandas representa una estructura de datos matricial en 
            #forma de tablas que pueden contener datos de diferentes tipos y se pueden manipular de manera eficiente para 
            #realizar diversas operaciones de análisis de datos, su constructor recibe los siguientes parámetros:
            # - data: Este es el parámetro principal que especifica los datos que se utilizarán para crear el DataFrame.
            #   Puede ser un diccionario, una lista de listas, un numpyArray, otra estructura de datos de Pandas (como 
            #   otro DataFrame o una Serie), etc.
            # - index (opcional): Este parámetro especifica las etiquetas de índice para las filas del DataFrame. 
            #   Puede ser una lista, una matriz, una Serie, etc. Si no se especifica, se utilizarán índices enteros.
            # - columns (opcional): Este parámetro opcional especifica los nombres de las columnas del DataFrame. Si no 
            #   se especifica, se utilizarán nombres de columnas predeterminados (0, 1, 2, ...).
            #       - .keys(): Como los objetos ResultProxy se manejan como diccionarios, se puede obtener el nombre de 
            #         sus etiquetas (keys) para de esa manera asignar los nombres de las columnas de un DataFrame, pero 
            #         si se quisiera obtener sus valores, no existe un método .values(), se debe acceder de otra forma. 
            # - dtype (opcional): Este parámetro especifica el tipo de datos para cada columna del DataFrame.
            dataFramePandas = pandas.DataFrame(data = resultProxy, columns = resultProxy.keys())    
            print(dataFramePandas, "\n")
            #pandas.to_datetime(): Convertir la columna de fecha_publicacion a formato de fecha------------------------
            dataFramePandas['fecha_publicacion'] = pandas.to_datetime(dataFramePandas['fecha_publicacion']).dt.strftime('%d-%m-%Y')

        #CREAR UN NUEVO ARRAY QUE COMBINE DATOS DE LA DATABASE CON OTROS A TRAVÉS DE UN DICCIONARIO DE FILTRADO:
        #bucle for each: Es un bucle que recorre la lista de diccionarios compareDicc, por lo que la variable 
        #filter_item lleva contenidos todos los diccionarios en cada iteración, uno por uno.
        for indDicc in compareDicc:
            filtered_rows = []  #Lista vacía para almacenar los elementos extraídos de la base de datos.
            #pandas.DataFrame().iterrows(): El método iterrows() se debe aplicar a algun objeto de la clase 
            #DataFrame y siempre se encontrar como parámetro de un bucle for ya que este recorre todos los datos 
            #de su DataFrame, devolviendo una tupla que indica el índice de cada fila y su contenido.  
            for (index, row) in (dataFramePandas.iterrows()):
                #En este punto con el contenido de las filas del DataFrame y la variable que recorre la lista de 
                #diccionarios es donde se pueden realizar las comparaciones para filtrar los datos.
                if (row['estatus'] == indDicc['estatusFilter'] and
                    row['usuarios_id'] == indDicc['userIdFilter'] and
                    row['categorias_id'] == indDicc['categoryIdFilter']):
                    #Los datos que cumplan las condiciones, se agregan a la lista vacía filtered_rows.
                    filtered_rows.append(row)

            #Una vez teniendo almacenados todos los datos de la base de datos que cumplan las condiciones del filtro, 
            #se añaden y organizan los datos del DataFrame final que queremos obtener.
            for filtered_dataBase in filtered_rows:
                #De igual manera se pueden agregar valores solo cuando se cumpla una condición en la variable
                #filtered_dataBase, para ello se utilizan condicionales de una sola línea que llevan la siguiente 
                #sintaxis:
                #variable =   valor_si_verdadero        if      condicion       else        valor_si_falso
                #Si se quiere utilizar una estructura else-if, lo que se hace es agregar un paréntesis y varias 
                #condiciones de una línea dentro.
                #variable =   (
                #               valor_si_verdadero1     if      condicion1      else        valor_si_falso1
                #               valor_si_verdadero2     if      condicion2      else        valor_si_falso2
                #               ...
                #               valor_si_verdadero_n    if      condicion_n     else        valor_si_falso_n
                #               valor_por_defecto
                #             )
                standardContent = """Phasellus laoreet eros nec vestibulum varius. Nunc id efficitur lacus, non imperdiet quam. Aliquam porta, tellus at porta semper, felis velit congue mauris, eu pharetra felis sem vitae tortor. Curabitur bibendum vehicula dolor, nec accumsan tortor ultrices ac. Vivamus nec tristique orci. Nullam fringilla eros magna, vitae imperdiet nisl mattis et. Ut quis malesuada felis. Proin at dictum eros, eget sodales libero. Sed egestas tristique nisi et tempor. Ut cursus sapien eu pellentesque posuere. Etiam eleifend varius cursus.\n\nNullam viverra quam porta orci efficitur imperdiet. Quisque magna erat, dignissim nec velit sit amet, hendrerit mollis mauris. Mauris sapien magna, consectetur et vulputate a, iaculis eget nisi. Nunc est diam, aliquam quis turpis ac, porta mattis neque. Quisque consequat dolor sit amet velit commodo sagittis. Donec commodo pulvinar odio, ut gravida velit pellentesque vitae. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos.\n\nMorbi vulputate ante quis elit pretium, ut blandit felis aliquet. Aenean a massa a leo tristique malesuada. Curabitur posuere, elit sed consectetur blandit, massa mauris tristique ante, in faucibus elit justo quis nisi. Ut viverra est et arcu egestas fringilla. Mauris condimentum, lorem id viverra placerat, libero lacus ultricies est, id volutpat metus sapien non justo. Nulla facilisis, sapien ut vehicula tristique, mauris lectus porta massa, sit amet malesuada dolor justo id lectus. Suspendisse sit amet tempor ligula. Nam sit amet nisl non magna lacinia finibus eget nec augue. Aliquam ornare cursus dapibus. Lorem ipsum dolor sit amet, consectetur adipiscing elit.\n\nDonec ornare sem eget massa pharetra rhoncus. Donec tempor sapien at posuere porttitor. Morbi sodales efficitur felis eu scelerisque. Quisque ultrices nunc ut dignissim vehicula. Donec id imperdiet orci, sed porttitor turpis. Etiam volutpat elit sed justo lobortis, tincidunt imperdiet velit pretium. Ut convallis elit sapien, ac egestas ipsum finibus a. Morbi sed odio et dui tincidunt rhoncus tempor id turpis.\n\nProin fringilla consequat imperdiet. Ut accumsan velit ac augue sollicitudin porta. Phasellus finibus porttitor felis, a feugiat purus tempus vel. Etiam vitae vehicula ex. Praesent ut tellus tellus. Fusce felis nunc, congue ac leo in, elementum vulputate nisi. Duis diam nulla, consequat ac mauris quis, viverra gravida urna."""
                #En este caso la condición evalúa si en la columna contenido de la base de datos filtrada contiene 
                #específicamente el valor de "Phasellus laoreet eros nec vestibulum varius..." y si es así, coloca un 
                #valor que se llama "standard", sino coloca "not conventional".
                contentStatus = "standard" if (standardContent in filtered_dataBase["contenido"]) else "not conventional"
                #Dentro del bucle, la variable indDicc representa cada diccionario de la lista de diccionarios y la 
                #variable filtered_dataBase representa cada fila de la base de datos filtrada.
                finalData.append({
                    "tituloStatic": indDicc["tituloStatic"],
                    "contentStatus": contentStatus,             #Columna agregada con condicionales.
                    "datoStatic": indDicc["datoStatic"],
                    "titulo": filtered_dataBase["titulo"],
                    "fecha_publicacion": filtered_dataBase["fecha_publicacion"]
                })
        #Cuando se crea un DataFrame a partir de un diccionario, no es necesario indicar explícitamente las columnas 
        #en su constructor. 
        finalDataFrame = pandas.DataFrame(data = finalData)
        print(finalDataFrame, "\n")

        #GUARDAR UN DATAFRAME EN UN ARCHIVO DE EXCEL, INDICANDO SU FORMATO ESTÁTICO, NO UNO QUE DEPENDA DE LOS DATOS:
        #pandas.ExcelWriter: La clase ExcelWriter de la librería pandas permite crear un objeto específicamente creado 
        #para escribir datos en un archivo de Excel, dándole formato y organizándolo en sheets, su constructor recibe 
        #los siguientes parámetros:
        # - path: Especifica la ruta y el nombre de archivo del archivo de Excel que se va a crear.
        # - engine: Especifica el motor de escritura de Excel que se utilizará. Los valores comunes son 'xlsxwriter', 
        #   'openpyxl' y 'xlwt'.
        #       - 'xlsxwriter': Motor de escritura predeterminado para Excel, ofreciendo el formateo de celdas, la 
        #         creación de gráficos y la adición de comentarios a las celdas.
        #       - 'openpyxl': Motor de escritura compatible con formatos de archivos más modernos en Excel como .xlsx,
        #         Proporciona funciones más avanzadas como la capacidad de cargar y modificar archivos existentes.
        #       - 'xlwt': Motor de escritura compatible con formatos de archivos más antiguos en Excel como .xls,
        #         Es útil para escribir en archivos con versiones más viejas de Excel.
        # - options: Un diccionario que contiene opciones adicionales para el motor de escritura de Excel.
        # - mode: Controla cómo se manejarán los datos cuando se escriban en el archivo de Excel. 
        #       - 'w': Se utiliza para sobrescribir los datos del archivo.
        #       - 'a': Se usa para agregar datos al final del archivo.
        # - options: Un diccionario que contiene opciones adicionales para el motor de escritura de Excel.
        # - datetime_format: Especifica el formato de fecha y hora que se utilizará para escribir en el Excel.
        #   Se debe proporcionar un código que indique un formato compatible con la sintaxis de strftime de Python:
        #       - %Y: Año con cuatro dígitos (ejemplo: 2022).
        #       - %y: Año con dos dígitos (ejemplo: 22).
        #       - %m: Mes como número decimal (01-12).
        #       - %d: Día del mes como número decimal (01-31).
        #       - %H: Hora (00-23).
        #       - %I: Hora (01-12).
        #       - %p: AM o PM.
        #       - %M: Minuto (00-59).
        #       - %S: Segundo (00-59).
        #       - %f: Microsegundos (000000-999999).
        #       - %j: Día del año (001-366).
        #       - %U: Número de semana del año, comenzando por el domingo (00-53).
        #       - %W: Número de semana del año, comenzando por el lunes (00-53).
        #       - %a: Nombre corto del día de la semana (Sun, Mon, etc.).
        #       - %A: Nombre completo del día de la semana (Sunday, Monday, etc.).
        #       - %b: Nombre corto del mes (Jan, Feb, etc.).
        #       - %B: Nombre completo del mes (January, February, etc.).
        #       - %c: Representación de la fecha y hora local.
        #       - %x: Representación de la fecha local.
        #       - %X: Representación de la hora local.
        # - date_format: Especifica el formato de solo fecha que se utilizará para escribir en el Excel.
        #   Se debe proporcionar un código de formato strftime, igual que como se hacía con el parámetro anterior.
        # - float_format: Especifica el formato de punto decimal (flotante) que se utilizará al escribir números.
        #       - {:.2f}: Formatea el número con dos decimales.
        #       - {:.4f}: Formatea el número con cuatro decimales.
        #       - {:.0f}: Formatea el número sin decimales.
        #       - {:+.2f}: Formatea el número con dos decimales e incluye el signo "+" para valores positivos.
        #       - {:.2%}: Formatea el número como porcentaje con dos decimales.
        #       - {:.2e}: Formatea el número en notación científica con dos decimales.
        #       - {:<10.2f}: Formatea el número con dos decimales y lo alinea a la izquierda en un espacio de 10 
        #         caracteres.
        #       - {:^10.2f}: Formatea el número con dos decimales y lo centra en un espacio de 10 caracteres.
        #       - {:0>10.2f}: Formatea el número con dos decimales y lo rellena con ceros a la izquierda en un 
        #         espacio de 10 caracteres.
        #       - {:,}: Formatea el número con separadores de miles.
        pathExcel = "C:/Users/diego/OneDrive/Documents/The_MechaBible/p_Python_ESP/1.-Data Science/0.-Archivos_Ejercicios_Python/23.-GUI PyQt5 Conexion DataBase/23.-Reporte Analisis de Datos.xlsx"
        with pandas.ExcelWriter(path = pathExcel, engine = 'xlsxwriter', mode = "w") as objetoExcel:
            #pandas.DataFrame().to_excel(): Método para escribir el contenido de un DataFrame en un archivo de Excel.
            # - excel_writer: Recibe el objeto pandas.ExcelWriter que especifica ciertos aspectos del Excel.
            # - index: Es un booleano que especifica si se quiere incluir el índice del DataFrame en el Excel.
            #   Si se establece en False, el índice no se incluirá en el Excel. El valor predeterminado es True.
            # - index_label: Especifica el nombre que se le dará a la columna de índice en el archivo de Excel. Si se 
            #   establece en None, no se asignará un nombre a la columna de índice. El valor predeterminado es 'index'.
            # - sheet_name: Especifica el nombre de la hoja en el archivo de Excel donde se escribirán los datos. El 
            #   valor predeterminado es 'Sheet1'.
            # - startrow: Especifica la fila inicial donde se comenzará a escribir los datos del DataFrame. Esto es 
            #   útil si se desea agregar los datos en una ubicación específica. El valor predeterminado es 0.
            # - startcol: Especifica la columna inicial donde se comenzará a escribir los datos del DataFrame. Esto es 
            #   útil si se desea agregar los datos en una ubicación específica. El valor predeterminado es 0.
            # - header: Es un booleano que especifica si se debe incluir o no el encabezado (nombres de columna) del 
            #   DataFrame en el archivo de Excel. El valor predeterminado es True.
            # - merge_cells: Es un booleano que especifica si se deben fusionar las celdas que tengan columnas con 
            #   encabezados duplicados. El valor predeterminado es True.
            # - engine: Especifica el motor de escritura de Excel que se utilizará para escribir los datos, sus valores 
            #   son los mismos que se indicaban en el objeto pandas.ExcelWriter. Si no se especifica, se utilizará el 
            #   motor 'xlsxwriter'.
            finalDataFrame.to_excel(excel_writer = objetoExcel, index = False, index_label = None, sheet_name = 'Sheet1', startrow = 0, startcol = 0, header = True, engine = 'xlsxwriter')
            #Después de haber creado el objeto pandas.ExcelWriter y haber convertido el DataFrame a un excel con el 
            #método .to_excel(), se debe extraer el book (archivo excel) y sheet (página dentro del book) del Excel 
            #para darle formato al archivo, ambas cosas se deben almacenar en variables distintas y acceder a ellas a 
            #través del objeto ExcelWriter. 
            #pandas.ExcelWriter().book: Atributo que obtiene el libro del Excel.
            workbook = objetoExcel.book
            #pandas.ExcelWriter().sheets["nombreSheet"]: Atributo para obtener una página del Excel.
            worksheet = objetoExcel.sheets['Sheet1']
            #Una vez que se haya accedido al book y sheet deseado y guardado ambos en variables, se debe indicar los 
            #formatos estáticos de sus celdas, guardando todos en variables y asignándolos al book a través del método 
            #.add_format().
            #pandas.ExcelWriter().book.add_format({}): Este método sirve para guardar en una variable un formato de 
            #celda, el cual se indica en un diccionario porque se pueden encapsular varias propiedades:
            # - bg_color: Define el color de fondo de la celda.
            # - font_color: Define el color de la fuente de la celda.
            # - font_name: Define el nombre de la fuente de la celda.
            # - font_size: Define el tamaño de la fuente de la celda.
            # - bold: Define si el texto de la celda está en negrita (True) o no (False).
            # - font_italic: Define si el texto de la celda está en cursiva (True) o no (False).
            # - font_underline: Define si el texto de la celda está subrayado (True) o no (False).
            # - align: Define la alineación del texto dentro de la celda ('left', 'center', 'right', 'justify', etc.).
            # - valign: Define la alineación vertical del texto dentro de la celda ('top', 'vcenter', 'bottom', 
            #   'vjustify', etc.).
            # - num_format: Define el formato numérico de la celda (por ejemplo, '0.00' para dos decimales).
            # - border: Define los bordes de la celda (puedes especificar si quieres bordes en la parte superior, 
            #   inferior, izquierda, derecha, etc.).
            # - text_wrap: Define si el texto debe envolverse dentro de la celda (True) o no (False).
            blue_format = workbook.add_format({'bg_color': '#0000FF'})
            green_format = workbook.add_format({'bg_color': '#00FF00'})
            grey_format = workbook.add_format({'bg_color': '#D3D3D3'})
            yellow_format = workbook.add_format({'bg_color': '#FFFF00'})
            #Luego de haber definido todos los formatos que se quiere utilizar en el Excel, se deberá extraer el 
            #tamaño del DataFrame, esto se hará a través de su atributo pandas.DataFrame().shape, el cual devuelve una 
            #tupla que indica su número de filas y columnas: (filas, columnas) = pandas.DataFrame().shape
            (filasDataFrame, columnasDataFrame) = finalDataFrame.shape
            #Finalmente se añadirán los formatos previamente guardados en el sheet extraído del objeto ExcelWriter() a
            #través del método conditional_format().
            #pandas.ExcelWriter().sheets["nombreSheet"].conditional_format(): Método que se utiliza para aplicar un 
            #formato a un rango de celdas en una hoja de cálculo específica (sheet) en un archivo Excel (book), para 
            #ello cabe mencionar que las posiciones de las filas y columnas se empiezan a contar desde 0 pero su 
            #tamaño se considera desde 1.
            # - first_row: Es un número o variable que indica la celda inicial de las filas en la tabla.
            # - first_col: Es un número o variable que indica la celda inicial de las columnas en la tabla.
            # - last_row: Es un número o variable que indica la celda final de las filas en la tabla. Aquí es donde se 
            #   usa la variable filasDataFrame obtenida del atributo pandas.DataFrame().shape.
            # - last_col: Es un número o variable que indica la celda final de las columnas en la tabla. Aquí es donde 
            #   se usa la variable columnasDataFrame obtenida del atributo pandas.DataFrame().shape.
            # - type: Este parámetro indica la condición que se debe cumplir para que se aplique un formato en una 
            #   celda.
            #       - 'cell_value': Aplica el formato si el valor de la celda cumple con cierta condición.
            #       - 'no_blanks': Aplica el formato si la celda no está en blanco.
            #       - 'formula': Aplica el formato si la fórmula en la celda devuelve verdadero.
            #       - 'time_period': Aplica el formato si la fecha en la celda cae dentro de un cierto período de 
            #         tiempo.
            #       - 'text': Aplica el formato basado en el contenido de texto de la celda.
            #       - 'average': Aplica el formato si el valor de la celda es un promedio de un rango específico.
            #       - 'duplicate': Aplica el formato si el valor de la celda es duplicado de un rango específico.
            #       - 'unique': Aplica el formato si el valor de la celda es único dentro de un rango específico.
            #       - '3_color_scale': Aplica un formato de escala de 3 colores basado en los valores de las celdas.
            #       - '2_color_scale': Aplica un formato de escala de 2 colores basado en los valores de las celdas.
            #       - 'icon_set': Aplica un conjunto de iconos basado en los valores de las celdas.
            # - format: Este parámetro recibe una variable de formato pandas.ExcelWriter().book.add_format({}).
            #worksheet.conditional_format(first_row, first_col, last_row, last_col, {'type': 'condition', 'format': formato})
            worksheet.conditional_format(0, 0, 0, columnasDataFrame - 1, {'type': 'no_blanks', 'format': blue_format})
            worksheet.conditional_format(1, 0, filasDataFrame, 0, {'type': 'no_blanks', 'format': green_format})
            worksheet.conditional_format(1, 1, filasDataFrame, 1, {'type': 'no_blanks', 'format': grey_format})
            for col in range(2, columnasDataFrame):
                worksheet.conditional_format(1, col, filasDataFrame, col, {'type': 'no_blanks', 'format': yellow_format})

    except Exception as error:
        print("1.- Ups an Error ocurred while Opening the MySQL DataBase:\n" + str(error) + "\n")