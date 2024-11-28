#ABRIR Y GUARDAR NOTAS EN UN ARCHIVO TXT:
import os       #os: Librería que permite acceder a funciones del sistema operativo, como abrir archivos. 

class widgetEscribirNotas:
    def escribirNotaTxt(self, respuestaAsistenteVirtual):
        respuestaNotas = ""
        filename = "C:/Users/diego/OneDrive/Documents/The_MechaBible/p_Python_ESP/5.-Inteligencia Artificial/NotasTimmy.txt"
        #MANEJO DE EXCEPCIONES: Es una parte de código que se conforma de dos partes, try y except: 
        # - Primero se ejecuta el código que haya dentro del try y si es que llegara a ocurrir una excepción 
        #   durante su ejecución, el programa brinca al código del except.
        # - En la parte de código donde se encuentra la palabra reservada except, se ejecuta cierta acción 
        #   cuando ocurra el error esperado. 
        #Se utiliza esta arquitectura de código cuando se quiera efectuar una acción donde se espera que pueda 
        #ocurrir un error durante su ejecución.
        try:
            #with as source: La instrucción with se utiliza para definir una variable que tiene asignada un 
            #método o recurso específico, el cual puede ser un archivo, una conexión a una base de datos, la 
            #cámara, micrófono o cualquier otro objeto que requiera ser cerrado. La palabra clave as se utiliza 
            #para asignar dicho recurso a una variable que puede utilizarse para acceder al recurso dentro del 
            #bloque with. 
            #Dentro del manejo de excepciones la instrucción with as source: asegura que se cierre el recurso, 
            #incluso si se produce un error dentro del bloque try.
            #open(): Método que sirve para abrir un archivo cualquiera y manejarlo por medio de Python.
            with open(filename, "w", encoding="utf-8") as f:
                f.write(respuestaAsistenteVirtual)
                #var_file_open.close(): Método para cerrar un archivo previamente abrierto con el 
                #método open(), es peligroso olvidar colocar este método, ya que la computadora lo 
                #considerará como si nunca hubiera sido cerrado, por lo cual no podré volver a 
                #abrirlo al dar clic sobre él.
                f.close()
                #os.system(): Método que permite ejecutar comandos del sistema operativo desde 
                #Python.
                # - ls: Mostrar todas las carpetas del directorio.
                # - cd: Command directory sirve para moverme de directorio.
                # - start: Abrir o ejecutar un archivo.
                # - ejecutable + archivo: Con este comando que incluye un ejecutable y un archivo 
                #   se indica al sistema operativo que abra cierto archivo usando un programa en 
                #   específico. 
                programa_para_abrir = "notepad.exe"
                os.system(f'{programa_para_abrir} "{filename}"')
        except FileNotFoundError as errorArchivo:
            #open(): Método que sirve para abrir un archivo cualquiera, para ello es necesario 
            #indicar dos parámetros, el primero se refiere a la ruta relativa o absoluta del archivo 
            #previamente creado y la segunda indica qué es lo que se va a realizar con él, el 
            #contenido del archivo se asigna a una variable.
            # - w: Sirve para escribir en un archivo, pero borrará la información que previamente 
            #   contenía el archivo.
            # - a: Sirve para escribir en un archivo sin que se borre la info anterior del archivo, 
            #   se llama append.
            file = open(filename, "w", encoding="utf-8")
            file.write(respuestaAsistenteVirtual)
            file.close()
            #os.system(): Método que permite ejecutar comandos del sistema operativo desde Python.
            # - ls: Mostrar todas las carpetas del directorio.
            # - cd: Command directory sirve para moverme de directorio.
            # - start: Abrir o ejecutar un archivo.
            # - ejecutable + archivo: Con este comando que incluye un ejecutable y un archivo se 
            #   indica al sistema operativo que abra cierto archivo usando un programa en 
            #   específico. 
            programa_para_abrir = "notepad.exe"
            os.system(f'{programa_para_abrir} "{filename}"')
        print("---------Hola di_cer0, ya respondí tu pregunta y guardé la respuesta en mis notas...----------")
        respuestaNotas = "Hola di0, ya escribí la respuesta que te dí en mi archivo de notas y luego te lo mostré."
        return respuestaNotas