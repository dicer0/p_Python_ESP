#ESTE CÓDIGO POR EL MOMENTO NO SIRVE YA QUE USA UNA API KEY DE UNA CUENTA MEXICANA, Y POR EL MOMENTO LA API 
#SOLO ESTÁ DISPONIBLE PARA CUENTAS DE USA O REINO UNIDO, POR LO QUE SE ARROJA UN ERROR INDICANDO QUE ÉSTA ES 
#INVÁLIDA.

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

#IMPORTACIÓN DE LIBRERÍAS:
import os #os: Librería que permite acceder a funciones y métodos relacionados con el sistema operativo.
from bardapi import Bard #bardapi: Librería que permite utilizar el LLM (Large Language Model) de Google Bard.

#IMPORTACIÓN DE LLAVE: Cuando se quiera utilizar una API que utiliza un key, por seguridad es de buenas prácticas 
#declararla en un archivo externo, además cabe mencionar que el nombre de dicho archivo y constante no pueden empezar 
#con un número, sino cuando la quiera importar obtendré un error y se va accediendo a las carpetas por medio de puntos:
# - Directorio normal:      carpeta1/carpeta2/carpeta3
# - Directorio paquetes:    carpeta1.carpeta2.carpeta3
#La parte del directorio se coloca después de la palabra reservada from y la llave a importar después de import.
from API_Keys.Llaves_ChatGPT_Bard_etc import LlaveBard

#os.environ: El método environ proveniente de la librería os permite acceder a las variables de entorno del sistema 
#operativo, estas están organizadas en una forma de key:value, por lo que serán datos tipo diccionario o JSON, y su 
#objetivo es proveer cierta información de configuración que afecte a múltiples programas o aplicaciones, evitando 
#así que cada uno deba ser configurado por separado, pudiendo adaptarse automáticamente a diferentes entornos al leer 
#las variables de entorno relevantes, que usualmente almacenan información sensible, como contraseñas o API keys.
#Para crear una nueva variable de entorno se utiliza la siguiente sintaxis, indicando su nombre en mayúsculas:
#   os.environ['NOMBRE_VARIABLE'] = 'valorVariableDeEntorno'
#Para almacenar una variable de entorno en una variable se utiliza la siguiente sintaxis:
#   variable = os.environ.get('NOMBRE_VARIABLE')
os.environ["BARD_API_KEY"] = LlaveBard
APIkey = os.environ.get("BARD_API_KEY")
#bardapi.Bard(): El constructor de Bard como mínimo recibe la API key.
googleBard = Bard(token = APIkey)
#bardapi.Bard().get_answer(): El método get_answer() sirve para mandar una pregunta de forma directa a Google Bard.
result = googleBard.get_answer("Cuéntame un chiste muy gracioso")
print(result)