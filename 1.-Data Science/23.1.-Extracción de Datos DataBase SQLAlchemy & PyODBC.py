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

#PyODBC: La librería pyodbc permite trabajar con bases de datos utilizando el estándar ODBC (Open DataBase 
#Connectivity), el cual es una API que permite a las aplicaciones conectarse a una amplia variedad de bases de 
#datos que tienen controladores ODBC disponibles, como Microsoft SQL Server, MySQL, PostgreSQL, Oracle, etc.
#Permitiendo a los desarrolladores enviar consultas SQL directamente a la base de datos, sin necesidad de 
#establecer una conexión ODBC de forma manual.
#No es que exista una mejor librería de manejo de datos, sino que dependiendo de la base de datos a la que nos 
#queramos conectar, conviene utilizar una biblioteca en vez de otra.
# - SQLAlchemy: Conviene usarse cuando se utilizan bases de datos como MySQL Workbench, PostgreSQL y SQLite.
# - PyODBC: Conviene usarse cuando se utilizan bases de datos como Microsoft SQL Server.
# - Psycopg2: Es conveniente usar esta librería cuando se utiliza una base de datos PostgreSQL.

# - Entidad: Se refiere a una tabla que almacena datos sobre un tipo de objeto o elemento del mundo real. Cada 
#   fila en la tabla representa una instancia individual de esa entidad, y cada columna representa un atributo o 
#   característica de esa entidad.
# - Atributo: Son las columnas de una tabla que representan las características o propiedades de la entidad que 
#   está siendo modelada, todas ellas tienen un nombre y tipo de dato asociado.
# - Registro: También conocido como "fila" o "tupla", representa una instancia individual de una entidad en la 
#   tabla. Cada registro contiene los valores de los atributos correspondientes a esa instancia específica de la 
#   entidad.

#SQLAlchemy - create_engine: El método create_engine sirve para configurar la conexión a la base de datos.
from sqlalchemy import create_engine
#SQLAlchemy - text: El método text se utiliza para crear un objeto de expresión textual que recibe como 
#parámetro el código de una consulta SQL en forma de String.
from sqlalchemy import text
#pandas: Librería que proporciona estructuras de datos y herramientas de manipulación y análisis de datos. 
import pandas

#En este caso lo que se hará es extraer datos de la base de datos, los cuales serán comparados con algunos 
#valores de la siguiente lista de diccionarios y si algunos de ellos son iguales, se tomará algunos datos de la 
#database (DB), se extraerán algunos otros de la lista de diccionarios y se agregarán unos nuevos para crear una 
#nueva estructura de datos, que pueda ser agregada a un reporte y posteriormente mostrada a su vez en una GUI de 
#PyQt5.
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
# - Por último, cuando no ocurra una excepción durante la ejecución del gestor de excepciones, se ejecutará el 
#   código que esté incluido dentro del finally después de haber terminado de ejecutar lo que haya en el try, 
#   pero si ocurre una excepción, la ejecución terminará cuando se llegue al except.
#Se utiliza esta arquitectura de código cuando se quiera efectuar una acción donde se espera que pueda ocurrir un 
#error durante su ejecución.
#1.- MySQL: create_engine('mysql+pymysql://username:password@hostname:port/database_name')
#instalation: pip install mysqlclient
#instalation: pip install pymysql
try:
    #create_engine: Método que sirve para configurar la conexión a un tipo de base de datos en específico.
    mysql_engine = create_engine('mysql+pymysql://root:Diego1234@localhost:3306/1_platziblog_db')
    #CONTEXTO DE EJECUCIÓN: Es un concepto de programación que se utiliza cuando se quiere trabajar con recursos 
    #que necesitan ser gestionados de forma prioritaria, como una apertura de archivos, conexiones de red o 
    #conexiones a bases de datos. Su sintaxis básica es la siguiente: 
    #       with expresion as variable:
    # - expresion: Este parámetro recibe un método que devuelva un objeto, ya que este se comportará como el 
    #   "contexto de ejecución", osea el recurso que debe ser gestionado, un ejemplo es open('archivo.txt', 'r').
    # - variable: Es el nombre de la variable que se asigna al objeto de contexto dentro del bloque with.
    #Utilizar el operador with es igual a asignar una variable, la única diferencia es que al utilizar el 
    #operador with nos aseguramos que el objeto que devuelva el método utilizado sea gestionado por un entorno 
    #temporal y complete sus tareas correctamente, como cerrar un archivo, incluso si ocurren errores: 
    #   nombreVariable = método() 
    #   with método() as nombreVariable
    #De igual manera, el operador with se asegura que no debamos guardar el archivo al terminar la acción, o 
    #cerrar una conexión a la base de datos, ya que esta se maneja de forma automática por el operador.
    #create_engine().connect(): El método .connect() sirve para establecer la conexión con la base de datos.
    with mysql_engine.connect() as connection1:
        print("1.- MySQL Connection successful!!!")
        #OBTENCIÓN DE DATOS DE LA BASE DE DATOS: Ya que estemos seguros que la conexión a la base de datos se ha 
        #realizado de forma exitosa, podremos utilizar comandos SQL para filtrar y obtener cierta información, 
        #esto se realiza a través de la variable que haya utilizado el método .connect(), el método .execute() y 
        #.text().  
        SQL_Query_string =  """SELECT 	  * 
                                FROM 	    posts
                                ORDER BY  titulo DESC;"""
        SQL_TextObject = text(SQL_Query_string)
        #.create_engine().connect().execute(): Ya que se haya realizado la conexión con la base de datos, a 
        #través de un objeto de variable textual (text) se puede realizar una consulta a la base de datos a 
        #través de SQL y lo que devuelve es un objeto llamado ResultProxy, el cual en algunas cosas se maneja 
        #como un diccionario.
        resultProxy = connection1.execute(SQL_TextObject)
        print("Tipo de Dato ResultProxy: ", type(resultProxy))
        #pandas.DataFrame: La clase DataFrame de la librería pandas representa una estructura de datos matricial 
        #en forma de tablas que pueden contener datos de diferentes tipos y se pueden manipular de manera 
        #eficiente para realizar diversas operaciones de análisis de datos, su constructor recibe los siguientes 
        #parámetros:
        # - data: Este es el parámetro principal que especifica los datos que se utilizarán para crear el 
        #   DataFrame.
        #   Puede ser un diccionario, una lista de listas, un numpyArray, otra estructura de datos de Pandas 
        #   (como otro DataFrame o una Serie), etc.
        # - index (opcional): Este parámetro especifica las etiquetas de índice para las filas del DataFrame. 
        #   Puede ser una lista, una matriz, una Serie, etc. Si no se especifica, se utilizarán índices enteros.
        # - columns (opcional): Este parámetro opcional especifica los nombres de las columnas del DataFrame. Si 
        #   no se especifica, se utilizarán nombres de columnas predeterminados (0, 1, 2, ...).
        #       - .keys(): Como los objetos ResultProxy se manejan como diccionarios, se puede obtener el nombre 
        #         de sus etiquetas (keys) para de esa manera asignar los nombres de las columnas de un DataFrame, 
        #         pero si se quisiera obtener sus valores, no existe un método .values(), se debe acceder de 
        #         otra forma. 
        # - dtype (opcional): Este parámetro especifica el tipo de datos para cada columna del DataFrame.
        dataFramePandas = pandas.DataFrame(data = resultProxy, columns = resultProxy.keys())    
        print(dataFramePandas, "\n")
        #pandas.to_datetime(): Este método se utiliza para convertir un objeto iterable como una lista, tupla, 
        #DataFrame, Serie de Pandas, etc. que contiene fechas o marcas de tiempo en un objeto de tipo DateTime.
        #pandas.to_datetime().dt: El atributo .dt proporciona acceso a una serie de métodos para obtener o 
        #manipular las fechas/horas de su objeto DateTime. Algunas de las cosas que se pueden hacer con el 
        #atributo .dt son:
        # - Fechas/horas individuales: Se puede acceder al año, mes, día, hora, minuto, segundo, etc.
        #       - Obtener el año:               pandas.DataFrame['key_ObjetoDateTime'].dt.year 
        #       - Obtener el mes:               pandas.DataFrame['key_ObjetoDateTime'].dt.month
        #       - Obtener el día:               pandas.DataFrame['key_ObjetoDateTime'].dt.day
        #       - Obtener la hora:              pandas.DataFrame['key_ObjetoDateTime'].dt.hour
        #       - Obtener el día de la semana:  pandas.DataFrame['key_ObjetoDateTime'].dt.dayofweek
        # - Convertir el formato de fecha/hora: Especifica el formato de fecha y hora que se utilizará para 
        #   mostrar el objeto DateTime, para ello se debe proporcionar un código que indique algún formato 
        #   compatible con la sintaxis de strftime de Python:
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
        # - Calcular diferencias de tiempo: Se pueden calcular diferencias de tiempo entre fechas y horas.
        #       - pandas.DataFrame['DateTime_fecha_fin'] - pandas.DataFrame['DateTime_fecha_inicio']
        # - Agregar o restar intervalos de tiempo: Se puede sumar o restar tiempo a las fechas y horas.
        #       - pandas.DataFrame['DateTime_fecha'] + pandas.Timedelta(days = 1)
        dataFramePandas['fecha_publicacion'] = pandas.to_datetime(dataFramePandas['fecha_publicacion']).dt.strftime('%d-%m-%Y')

    #CREAR UN NUEVO ARRAY QUE COMBINE DATOS DE LA DATABASE CON OTROS A TRAVÉS DE UN DICCIONARIO DE FILTRADO:
    #bucle for each: Es un bucle que recorre la lista de diccionarios compareDicc, por lo que la variable indDicc 
    #lleva contenidos todos los diccionarios en cada iteración, uno por uno.
    for indDicc in compareDicc:
        #Indexación booleana: Es una técnica que se realiza con estructuras de datos de la librería pandas para 
        #filtrar las filas de un DataFrame basándose en el uso de operadores lógicos simples como & (and), | (or) 
        #y ~ (not). La operación solo devolverá las filas del DataFrame que cumplan con las condiciones descritas 
        #dentro de su corchete (osea que devuelvan un True):
        #resultadoFiltrado = pandas.DataFrame()[~(operacionLogica_1 & operacionLogica_2 | operacionLogica_n)]
        #En este punto con el contenido de las filas del DataFrame y la variable indDicc que recorre la lista de 
        #diccionarios es donde se pueden realizar las comparaciones para filtrar los datos.
        filtered = dataFramePandas[(dataFramePandas['estatus'] == indDicc['estatusFilter']) &
                                (dataFramePandas['usuarios_id'] == indDicc['userIdFilter']) &
                                (dataFramePandas['categorias_id'] == indDicc['categoryIdFilter'])]
        #pandas.DataFrame().empty: El atributo .empty devuelve un valor True cuando su DataFrame está vacío y 
        #False cuando el DataFrame si cuenta con filas y columnas.
        #El operador not simplemente es una negación (~), osea que cuando algo sea True, lo volverá False y 
        #viceversa, esto se utiliza porque los if se ejecutan cuando su condición vale True.
        if (not(filtered.empty)):
            #pandas.DataFrame().iterrows(): El método iterrows() se debe aplicar a algun objeto de la clase 
            #DataFrame y siempre se encontrará como parámetro de un bucle for, ya que este recorre todos los 
            #datos de su DataFrame, devolviendo una tupla que indica el índice de cada fila y su contenido.
            for (index, row) in (filtered.iterrows()):
                #Una vez obtenido el índice y contenido de los elementos del DataFrame, se pueden agregar un 
                #valor u otro a la lista final dependiendo de si se cumple o no una condición, para ello se 
                #utilizan condicionales de una sola línea que llevan la siguiente sintaxis:
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
                #En este caso la condición evalúa si en la columna contenido de la base de datos filtrada 
                #contiene específicamente el valor de "Phasellus laoreet eros nec vestibulum varius..." y si es 
                #así, coloca un valor que se llama "standard", sino coloca "not conventional".
                contentStatus = "standard" if (standardContent in row["contenido"]) else "not conventional"
                #Dentro del bucle, la variable indDicc representa cada diccionario de la lista de diccionarios 
                #que realiza el filtrado y la variable row representa cada fila de la base de datos filtrada.
                finalData.append({
                    "Titulo Static": indDicc["tituloStatic"],
                    "Content Status": contentStatus,
                    "Dato Static": indDicc["datoStatic"],
                    "Titulo": row["titulo"],
                    "Fecha de Publicacion": row["fecha_publicacion"]
                })
        #Dentro del else se consideran los datos que no cumplan con las condiciones del filtro, para que estos 
        #no sean despreciados, sino clasificados.
        else:
            #Una vez teniendo almacenados todos los datos de la base de datos que cumplan las condiciones del 
            #filtro, se añaden y organizan los datos del DataFrame final que queramos recopilar dentro de la 
            #lista vacía finalData que no lo hayan hecho.
            finalData.append({
                "Titulo Static": "Not categorized",
                "Content Status": "Not categorized",
                "Dato Static": "Not categorized",
                "Titulo": row["titulo"],
                "Fecha de Publicacion": row["fecha_publicacion"]
            })
    #Cuando se crea un DataFrame a partir de un diccionario, no es necesario indicar explícitamente las columnas 
    #en su constructor, se pasa directamente a su parámetro data.
    finalDataFrame = pandas.DataFrame(data = finalData)
    print(finalDataFrame, "\n")
except Exception as error:
    print("1.- Ups an Error ocurred while Opening the MySQL DataBase:\n" + str(error) + "\n")

#2.- PostgreSQL: create_engine('postgresql://username:password@hostname:port/database_name')
#instalation: pip install psycopg2 
try:
    #with: Con este operador de contexto de ejecución se maneja la apertura y cierre de la conexión a la base de 
    #datos de forma automática, por lo que esta no se debe abrir ni cerrar de forma manual, solo se llama al 
    #método y se le asigna una variable para poderla utilizar.  
    postgresql_engine = create_engine('postgresql://username:password@hostname:port/database_name')
    with postgresql_engine.connect() as connection2:
        print("2.- PostgresSQL Connection successful!!!")
except Exception as error:
    print("2.- Ups an Error ocurred while Opening the PostgresSQL DataBase:\n" + str(error) + "\n")

#3.- SQLite (path relativo): create_engine('sqlite:///mydatabase.db')
#No additional installation is needed.
try:
    #Pero si no se utiliza el operador with, la conexión se debe abrir de forma manual con el método connect() 
    #y luego cerrarse con el método .close(), pero el problema de hacer esto es que si se quiere rellenar un 
    #reporte o algo del estilo, podrá haber problemas al momento de la extracción de datos.
    sqlite_engine_relative = create_engine('sqlite:///mydatabase.db')
    connection3 = sqlite_engine_relative.connect()
    print("5.- Microsoft SQL Server Connection successful with Windows authentication!!!")
except Exception as error:
    print("5.- Ups an Error ocurred while Opening the Microsoft SQL Server DataBase with Windows authentication:\n" + str(error) + "\n")
finally:
    if ('connection3' in locals()):
        print("5.- Connection 5 closed manually\n")
        connection3.close()

#4.- SQLite (path absoluto): create_engine('sqlite:////absolute/path/to/mydatabase.db')
#No additional installation is needed.
try:
    sqlite_engine_absolute = create_engine('sqlite:////absolute/path/to/mydatabase.db')
    with postgresql_engine.connect() as connection4:
        print("4.- PostgresSQL Connection successful!!!")
except Exception as error:
    print("4.- Ups an Error ocurred while Opening the SQLite DataBase with an Absolute Path:\n" + str(error) + "\n")

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
#Cabe mencionar que para este tipo de bases de datos, conviene más utilizar la librería pyodbc de forma directa.
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

#6.1.- Microsoft SQL Server (SQL Server authentication): create_engine('mssql+pyodbc://username:password@mydsn')
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
#Cabe mencionar que para este tipo de bases de datos, conviene más utilizar la librería pyodbc de forma directa.
try:
    mssql_engine_sql_auth = create_engine('mssql+pyodbc://username:password@mydsn')
    connection6 = mssql_engine_sql_auth.connect()
    print("6.1.- Microsoft SQL Server Connection successful with Server authentication!!!")
except Exception as error:
    print("6.1.- Ups an Error ocurred while Opening the Microsoft SQL Server DataBase with Server authentication:\n" + str(error) + "\n")
finally:
    if ('connection6' in locals()):
        print("6.1.- Connection 6.1 closed\n")
        connection6.close()

#6.2.- PyODBC: La librería pyodbc permite trabajar con bases de datos utilizando el estándar ODBC (Open Database 
#Connectivity), el cual es una API que permite a las aplicaciones conectarse a una amplia variedad de bases de 
#datos que tienen controladores ODBC disponibles, como Microsoft SQL Server, MySQL, PostgreSQL, Oracle, etc.
#Permitiendo a los desarrolladores enviar consultas SQL directamente a la base de datos, sin necesidad de establecer 
#una conexión ODBC.
#No es que exista una manera mejor de manejar los datos, sino que dependiendo de la base de datos que se quiera 
#utilizar, a veces conviene utilizar una librería en vez de otra.
# - SQLAlchemy: Conviene usarse cuando se utilizan bases de datos como MySQL Workbench, PostgreSQL y SQLite.
# - PyODBC: Conviene usarse cuando se utilizan bases de datos como Microsoft SQL Server.
import pyodbc
#7.- Microsoft SQL Server (SQL Server authentication): create_engine('mssql+pyodbc://username:password@mydsn')
#instalation: pip install pyodbc
#pyodbc.connect(stringConnection): El método pyodbc.connect() se utiliza para establecer una conexión a una base 
#de datos, usualmente de tipo Microsoft SQL Server. Este toma un string de conexión como argumento que contiene 
#información necesaria para la conexión establecida:
# - DRIVER: Este parámetro especifica el nombre del controlador que se utilizará para la conexión, este cambia su 
#   valor dependiendo de a qué base de datos nos queramos conectar.
#       - Microsoft SQL Server: "SQL Server" o "ODBC Driver 17 for SQL Server"
#       - MySQL: "MySQL ODBC 8.0 Unicode Driver" o "MySQL ODBC 5.3 Unicode Driver"
#       - PostgreSQL: "PostgreSQL ANSI" o "PostgreSQL Unicode"
#       - Oracle: "Oracle en OraClient11g_home1"
#       - SQLite: "SQLite3 ODBC Driver"
#       - IBM DB2: "DB2" o "IBM DB2 ODBC DRIVER"
# - SERVER: Nombre o dirección IP del servidor de la base de datos a la que nos queremos conectar.
# - DATABASE: Nombre de la base de datos a la que se desea conectar.
# - UID/Username (opcional): Este parámetro se utiliza para especificar el nombre de usuario que se utilizará para 
#   la autenticación en la base de datos. Si se utiliza la autenticación de Windows, este parámetro no es necesario.
# - PWD/Password (opcional): Contraseña asociada al nombre de usuario especificado.
# - Trusted_Connection: Este parámetro se establece en yes si se desea utilizar la autenticación de Windows para la 
#   conexión (Trusted_Connection=yes). Si se utiliza la autenticación de SQL Server, este parámetro no es necesario.
# - Other Connection Attributes: Además de los parámetros anteriores, puedes especificar otras propiedades de conexión 
#   dependiendo del motor de base de datos específico y las opciones de configuración que permita el controlador ODBC. 
#   Esto puede incluir cosas como el puerto, el nivel de aislamiento de la transacción, el tiempo de espera de la 
#   conexión, etc.
nombreServidor = "localhost"
puertoBaseDeDatos = 3306
nombreBaseDeDatos = "1_platziblog_db"
stringConnection = f"DRIVER={{MySQL ODBC 8.3 Unicode Driver}};SERVER={nombreServidor};PORT={puertoBaseDeDatos};DATABASE={nombreBaseDeDatos};USER=root;PASSWORD=Diego1234;"
try:
    connection7 = pyodbc.connect(stringConnection)
    print("6.2.- Microsoft SQL Server Connection successful with Server authentication using PyODBC!!!")
except Exception as error:
    print("6.2.- Ups an Error ocurred while Opening the Microsoft SQL Server DataBase with Server authentication:\n" + str(error) + "\n")
finally:
    if ('connection7' in locals()):
        print("6.2.- Connection 6.2 closed\n")
        connection7.close()