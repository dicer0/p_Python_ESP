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


#ABRIR, ESCRIBIR y LEER UN ARCHIVO: Genere un programa que escriba un mensaje y lo guarde en un archivo, 
#posteriormente, ábralo y lea su contenido. Para probar el programa, escriba la frase: ¡Hola mundo, cruel!, 
#en consola, luego guarde el mensaje en un archivo, después recupérela y finalmente imprímala en la pantalla.
#Con las siguientes líneas de código se abre un archivo, se escribe sobre él, se lee su contenido y se imprime 
#en consola.

#INTRODUCIR UN MENSAJE EN CONSOLA:
#input(): Método que sirve para introducir un mensaje en consola, que en el programa se interpreta como un dato 
#de tipo String.
stMessage = input("Ingresa el mensaje en consola: \n") #Variable que guarda un mensaje introducido en consola


#ABRIR y ESCRIBIR EN UN ARCHIVO:
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
filename = "0.-Archivos_Ejercicios_Python/12.-Abrir, Escribir y Leer un Archivo/Mensaje.txt"
#open(): Método que sirve para abrir un archivo cualquiera, para ello es necesario indicar dos parámetros, 
#el primero se refiere a la ruta relativa o absoluta del archivo previamente creado y la segunda indica qué 
#es lo que se va a realizar con él, el contenido del archivo se asigna a una variable.
#   - w: Sirve para escribir en un archivo, pero borrará la información que previamente contenía el archivo.
#   - a: Sirve para escribir en un archivo sin que se borre la info anterior del archivo, se llama append.
new_file = open(filename, 'w')
#var_file_open.write(): Método para colocar un string en un archivo previamente abrierto con el método open().
new_file.write(stMessage) #Sirve para escribir el mensaje que ingresó el usuario en consola.
#var_file_open.close(): Método para cerrar un archivo previamente abrierto con el método open(), es peligroso 
#olvidar colocar este método, ya que la computadora lo considerará como si nunca hubiera sido cerrado, por lo 
#cual no podré volver a abrirlo al dar clic sobre él.
new_file.close() #Sirve para cerrar el archivo que crea el archivo en el directorio indicado.


#ABRIR y LEER UN ARCHIVO:
#open(): Método que sirve para abrir un archivo cualquiera, para ello es necesario indicar dos parámetros, 
#el primero se refiere a la ruta relativa o absoluta del archivo previamente creado y la segunda indica qué 
#es lo que se va a realizar con él, el contenido del archivo se asigna a una variable.
#   - r: Sirve para leer el contenido de un archivo.
#Es importante mencionar que no se podrá abrir el archivo si este se encuentra abierto por otro programa.
my_file = open(filename, 'r') 
#var_file_open.readline(): Método para leer la primera línea del contenido de un archivo previamente abrierto 
#con el método open().
stRecoveredMessage = my_file.readline() #Sirve para leer y guardar el mensaje que ingresó el usuario en consola.
#var_file_open.close(): Método para cerrar un archivo previamente abrierto con el método open(), es peligroso 
#olvidar colocar este método, ya que la computadora lo considerará como si nunca hubiera sido cerrado, por lo 
#cual no podré volver a abrirlo al dar clic sobre él.
my_file.close() #Sirve para cerrar el archivo que crea el archivo en el directorio indicado.
#print(): Imprimir un mensaje en consola.
print(stRecoveredMessage)