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
#SQLAlchemy - Column: La clase Column de la biblioteca SQLAlchemy se utiliza para definir las columnas 
#(atributos) en las tablas (entidades) de la base de datos utilizando el mapeo de objeto-relacional (ORM).
from sqlalchemy import Column
#SQLAlchemy - Integer, String, CHAR: Son los tipos de datos que pueden adoptar los objetos Column.
from sqlalchemy import Integer, String, CHAR
#SQLAlchemy.ext.declarative - declarative_base: El método declarative_base perteneciente al paquete orm permite 
#definir clases de modelo en Python, las cuales definen la estructura de los datos que se busca crear o manipular 
#en una database. Luego estas se mapean automáticamente a una tabla (entidad) en una base de datos relacional.
from sqlalchemy.orm import declarative_base
#SQLAlchemy.orm - sessionmaker: Una vez que se hayan definido las clases de modelo (si es que se quiere ingresar 
#datos a la DB) y se haya configurado la conexión a la base de datos con el método create_engine, es necesario 
#crear sesiones para poder realizar operaciones del CRUD (Create-Read-Update-Delete) como agregar, modificar o 
#eliminar filas (registros) en las tablas (entidades) de la base de datos.
from sqlalchemy.orm import sessionmaker
#pandas: Librería que proporciona estructuras de datos y herramientas de manipulación y análisis de datos. 
import pandas

#En este caso lo que se hará es extraer datos de la base de datos, los cuales serán comparados con algunos valores 
#de la siguiente lista de diccionarios y si algunos de ellos son iguales, se tomará algunos datos de la database 
#(DB), se extraerán algunos otros de la lista de diccionarios y se agregarán unos nuevos para crear una nueva 
#estructura de datos, que pueda ser agregada a un reporte y posteriormente mostrada a su vez en una GUI de PyQt5.
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
    #create_engine().connect(): El método .connect() sirve para establecer la conexión con la base de datos.
    connection1 = mysql_engine.connect()
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
    print(finalDataFrame)

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
    objetoExcel = pandas.ExcelWriter(path = pathExcel, engine = 'xlsxwriter', mode = "w", datetime_format = "%d-%m-%Y %H:%M:%S")
    #pandas.DataFrame().to_excel(): Método para escribir el contenido de un DataFrame en un archivo de Excel.
    # - excel_writer: Recibe el objeto pandas.ExcelWriter que especifica ciertos aspectos del Excel.
    # - index: Es un booleano que especifica si se quiere incluir el índice del DataFrame en el archivo de Excel.
    #   Si se establece en False, el índice no se incluirá en el Excel. El valor predeterminado es True.
    # - index_label: Especifica el nombre que se le dará a la columna de índice en el archivo de Excel. Si se 
    #   establece en None, no se asignará un nombre a la columna de índice. El valor predeterminado es 'index'.
    # - sheet_name: Especifica el nombre de la hoja en el archivo de Excel donde se escribirán los datos. El valor 
    #   predeterminado es 'Sheet1'.
    # - startrow: Especifica la fila inicial donde se comenzará a escribir los datos del DataFrame. Esto es útil 
    #   si se desea agregar los datos en una ubicación específica. El valor predeterminado es 0.
    # - startcol: Especifica la columna inicial donde se comenzará a escribir los datos del DataFrame. Esto es útil 
    #   si se desea agregar los datos en una ubicación específica. El valor predeterminado es 0.
    # - header: Es un booleano que especifica si se debe incluir o no el encabezado (nombres de columna) del 
    #   DataFrame en el archivo de Excel. El valor predeterminado es True.
    # - merge_cells: Es un booleano que especifica si se deben fusionar las celdas que tengan columnas con encabezados 
    #   duplicados. El valor predeterminado es True.
    # - engine: Especifica el motor de escritura de Excel que se utilizará para escribir los datos, sus valores son los 
    #   mismos que se indicaban en el objeto pandas.ExcelWriter. Si no se especifica, se utilizará el motor 'xlsxwriter'.
    finalDataFrame.to_excel(excel_writer = objetoExcel, index = False, index_label = None, sheet_name = 'Sheet1', startrow = 0, startcol = 0, header = True, engine = 'xlsxwriter')
    workbook = objetoExcel.book
    worksheet = objetoExcel.sheets['Sheet1']
    for j, col in enumerate(finalDataFrame.columns):
        worksheet.write(0, j, col, workbook.add_format({'bg_color': 'blue', 'bold': True}))
    for i in range(finalDataFrame.shape[0] + 1):
        for j in range(finalDataFrame.shape[1]):
            cell_format = workbook.add_format()
            if j == 0:
                cell_format.set_bg_color('green')
            elif j == 1:
                cell_format.set_bg_color('gray')
            elif i == finalDataFrame.shape[0]:
                cell_format.set_bg_color('yellow')
            else:
                cell_format.set_bg_color('yellow')
            worksheet.write(i + 1, j, finalDataFrame.iloc[i - 1, j], cell_format)
    date_format = workbook.add_format({'num_format': 'yyyy-mm-dd', 'bg_color': 'yellow'})
    for i in range(finalDataFrame.shape[0]):
        worksheet.write(i + 1, finalDataFrame.columns.get_loc('fecha_publicacion'), pandas.to_datetime(finalDataFrame.iloc[i]['fecha_publicacion']).date(), date_format)
    for idx, col in enumerate(finalDataFrame):
        max_len = max(finalDataFrame[col].astype(str).map(len).max(), len(str(col))) + 1
        worksheet.set_column(idx, idx, max_len)
    objetoExcel.save()

except Exception as error:
    print("1.- Ups an Error ocurred while Opening the MySQL DataBase:\n" + str(error) + "\n")
finally:
    #CERRAR LA CONEXIÓN CON LA BASE DE DATOS:
    #locals(): Es un método de Python que devuelve un diccionario que contiene las variables locales activas, ya 
    #sea las que se encuentran dentro de una función o en un bloque de código definido, como una clase. Es útil 
    #en situaciones donde se necesita inspeccionar el ámbito local para verificar la presencia de una variable 
    #específica antes de tomar una acción en consecuencia.
    if ('resultProxy' in locals()):
        #.create_engine().connect().execute().close(): El cerrar la conexión con la consulta hecha con el método 
        #.execute() asegura que se liberen los recursos asociados con ese objeto una vez que se haya terminado el 
        #query. Aunque no es estrictamente necesario hacer esto, es una buena práctica para limpiar y liberar 
        #cualquier recurso adicional que pueda estar asociado con él.
        resultProxy.close()
    if ('connection1' in locals()):
        print("1.- Connection 1 closed\n")
        #create_engine().close(): El método .close() sirve para cerrar una conexión previamente configurada y 
        #establecida con el método create_engine().connect().
        connection1.close()
#2.- PostgreSQL: create_engine('postgresql://username:password@hostname:port/database_name')
#instalation: pip install psycopg2 
try:
    postgresql_engine = create_engine('postgresql://username:password@hostname:port/database_name')
    connection2 = postgresql_engine.connect()
    print("2.- PostgresSQL Connection successful!!!")
except Exception as error:
    print("2.- Ups an Error ocurred while Opening the PostgresSQL DataBase:\n" + str(error) + "\n")
finally:
    if ('connection2' in locals()):
        print("2.- Connection 2 closed\n")
        connection2.close()
#3.- SQLite (path relativo): create_engine('sqlite:///mydatabase.db')
#No additional installation is needed.
try:
    sqlite_engine_relative = create_engine('sqlite:///mydatabase.db')
    connection3 = sqlite_engine_relative.connect()
    print("3.- SQLite Connection successful!!!")
except Exception as error:
    print("3.- Ups an Error ocurred while Opening the SQLite DataBase with a Relative Path:\n" + str(error) + "\n")
finally:
    if ('connection3' in locals()):
        print("3.- Connection 3 closed\n")
        connection3.close()
#4.- SQLite (path absoluto): create_engine('sqlite:////absolute/path/to/mydatabase.db')
#No additional installation is needed.
try:
    sqlite_engine_absolute = create_engine('sqlite:////absolute/path/to/mydatabase.db')
    connection4 = sqlite_engine_absolute.connect()
    print("4.- SQLite Connection successful!!!")
except Exception as error:
    print("4.- Ups an Error ocurred while Opening the SQLite DataBase with an Absolute Path:\n" + str(error) + "\n")
finally:
    if ('connection4' in locals()):
        print("4.- Connection 4 closed\n")
        connection4.close()
#5.- Microsoft SQL Server (Windows authentication): create_engine('mssql+pyodbc://@mydsn')
#instalation: pip install pyodbc
#Este tipo de conexión es más compleja que las demás, ya que se debe ejecutar un paso intermedio donde se crea un 
#acceso llamado ODBC (Open DataBase Connectivity), que es una  API estándar de la industria diseñada para permitir 
#que las distintas aplicaciones (código backend Python, Node.js, Java, etc.) puedan acceder a diferentes tipos de 
#bases de datos y/o sistemas de gestión de bases de datos (DBMS) independientemente del sistema operativo o 
#lenguaje de programación que utilicen, proporcionando así una capa intermedia entre ellas.
#Para crear el ODBC se deben seguir los siguientes pasos:
#Panel de Control -> Sistema y Seguridad -> Herramientas Administrativas -> OBDC Data Sources 64 Bit -> Agregar -> 
#SQL Server -> Finalizar -> Nombre: Nombre del OBDC -> Servidor: Servidor al que nos queremos conectar -> 
#Siguiente -> Autentificacion de Windows -> Siguiente -> Establecer la siguiente base de datos como predeterminada: 
#Base de datos a la que nos queremos conectar -> Siguiente -> Finalizar -> Probar Origen de Datos -> Aceptar -> 
#Aceptar.
#Después de haber realizado estos pasos, el nombre del ODBC se deberá añadir en el mydsn del URL de conexión. 
try:
    mssql_engine_windows = create_engine('mssql+pyodbc://@mydsn')
    connection5 = mssql_engine_windows.connect()
    print("5.- Microsoft SQL Server Connection successful with Windows authentication!!!")
except Exception as error:
    print("5.- Ups an Error ocurred while Opening the Microsoft SQL Server DataBase with Windows authentication:\n" + str(error) + "\n")
finally:
    if ('connection5' in locals()):
        print("5.- Connection 5 closed\n")
        connection5.close()
#6.- Microsoft SQL Server (SQL Server authentication): create_engine('mssql+pyodbc://username:password@mydsn')
#instalation: pip install pyodbc
#Este tipo de conexión es la misma a la descrita en el número 5, con la única diferencia que se incluye el nombre 
#de usuario y contraseña para la conexión en vez del puro ODBC, para ello se siguen los siguientes pasos:
#Panel de Control -> Sistema y Seguridad -> Herramientas Administrativas -> OBDC Data Sources 64 Bit -> Agregar -> 
#SQL Server -> Finalizar -> Nombre: Nombre del OBDC -> Servidor: Servidor al que nos queremos conectar -> 
#Siguiente -> SQL Server Authentication -> Login: Nombre de usuario de la DB -> Password: Contraseña de la DB -> 
#Siguiente -> Establecer la siguiente base de datos como predeterminada: Base de datos a la que nos queremos 
#conectar -> Siguiente -> Finalizar -> Probar Origen de Datos -> Aceptar -> Aceptar.
#Después de haber realizado estos pasos, el nombre del ODBC se deberá añadir en el mydsn del URL de conexión y de 
#igual manera se podrán añadir el nombre de usuario y contraseña de forma opcional.
try:
    mssql_engine_sql_auth = create_engine('mssql+pyodbc://username:password@mydsn')
    connection6 = mssql_engine_sql_auth.connect()
    print("6.- Microsoft SQL Server Connection successful with Server authentication!!!")
except Exception as error:
    print("6.- Ups an Error ocurred while Opening the Microsoft SQL Server DataBase with Server authentication:\n" + str(error) + "\n")
finally:
    if ('connection6' in locals()):
        print("6.- Connection 6 closed\n")
        connection6.close()


# #MANDAR DATOS A LA BASE DE DATOS:
# #declarative_base(): Método para definir clases de modelo en python para mandar datos a la DB por medio del ORM.
# Base = declarative_base()
# #Las clases que vayan a mandar datos a la DB deben heredar de la variable que haya usado el método 
# #declarative_base().
# class User(Base):
#     __tablename__ = 'users'
#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#     age = Column(Integer)
#     gender = Column(CHAR)

# #Create a session to interact with the database
# Session = sessionmaker(bind = mysql_engine)
# session = Session()

# #Example: Inserting data into the database
# new_user = User(name = 'John', age = 30, gender = 'm')
# session.add(new_user)
# session.commit()

# #Example: Querying data from the database
# users = session.query(User).all()
# for user in users:
#     print(user.name, user.age)

# #Close the session when done
# session.close()