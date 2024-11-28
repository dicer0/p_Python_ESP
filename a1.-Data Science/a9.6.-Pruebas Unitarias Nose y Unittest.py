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

#PRUEBAS UNITARIAS:
import unittest #unittest: Librería orientada a objetos para ejecutar y analizar pruebas unitarias.
import nose #nose: Extensión de la librería unittest, simplificando su código, entre otras mejoras adicionales.
#Usar dos librerías distintas para realizar pruebas unitarias en un mismo programa puede resultar complicado y 
#propenso a errores, ya que los frameworks de pruebas están diseñados para proporcionar una estructura 
#coherente y consistente para las pruebas, por lo que mezclar dos o más frameworks puede generar inconsistencias 
#y conflictos. Si se desea utilizar librerías distintas para diferentes pruebas en un mismo programa, es 
#recomendable separar las pruebas en módulos o archivos diferentes, asignando a cada módulo a un framework 
#específico con su propio conjunto de configuraciones y variables, para que no se vean afectadas las pruebas 
#del otro módulo.
#Se realizará un programa que utilice dos de las librerías de testing más famosas en Python, una es la librería 
#nose y la otra es la librería unittest, identificando el error generado al usar ambas.

#ERROR AL USAR DOS FRAMEWORKS EN EL MISMO ARCHIVO: En el siguiente archivo se verifica el resultado obtenido al 
#sumar dos valores distintos:
# - Prueba unittest: Se suman dos valores numéricos y se comprueba que su suma sea igual a 12.
#       - El error causado por utilizar las dos librerías unittest y nose en el mismo archivo es que al forzar 
#         un error en la prueba unittest, se lanzará una excepción tanto para nose como para unittest, cuando en 
#         realidad solo se debería lanzar para unittest, no para nose.
# - Prueba nose: Se concatenan dos valores string y se comprueba el resultado diga "HolaMundo".
#       - Al forzar un error en la prueba nose, si se generará una excepción correcta en nose, y no se generará 
#         una para unittest, así es como debería ejecutarse el archivo.
#Por lo tanto, el error es obtenido cuando falla la prueba de unittest, ya que erróneamente arroja una excepción 
#para nose también.



#CONDICIÓN DE LAS PRUEBAS UNITTEST Y NOSE:
#mi_funcion(): Función propia que realiza una suma de dos variables distintas, definiendo así la operación que 
#quieren comprobar las pruebas unitarias unittest y nose.
def mi_funcion(a, b):
    return a + b



#PRUEBAS UNITARIAS AUTOMÁTICAS CON LA LIBRERÍA UNITTEST: La librería unittest está muy enfocada a la 
#programación orientada a objetos (POO), por lo cual, para utilizarla es necesario crear una clase propia que 
#herede de la clase TestCase, perteneciente a la librería unittest.
class MyTestCase(unittest.TestCase):
    #setUp(): Método que pertenece a las herramientas incluídas con la librería unittest, este sirve para 
    #indicar los atributos que se utilizan al realizar las pruebas unitarias y se ejecuta antes de cada prueba 
    #para configurar su estado inicial.
    def setUp(self):
        #ATRIBUTOS DE LA CLASE: Palabra reservada self.
        #Configuración inicial para cada prueba unittest, con la palabra reservada self se está accediendo a la 
        #instancia de la clase actual, osea la clase MyTestCase, para así asignar como atributo los siguientes 
        #valores:
        self.parametro3 = 10
        self.parametro4 = 2     #Si la variable es diferente a 2, ocurre un error en unittest y nose.
    #tearDown(): Método que pertenece a las herramientas incluídas con la librería unittest, este sirve para 
    #limpiar o reiniciar el valor de los atributos utilizados al realizar pruebas unitarias.
    def tearDown(self):
        #ATRIBUTOS DE LA CLASE: Palabra reservada self.
        #Limpieza después de cada prueba unittest, con la palabra reservada self se está accediendo a la 
        #instancia de la clase actual, osea la clase MyTestCase, para así asignar como atributo los siguientes 
        #valores:
        self.parametro3 = None
        self.parametro4 = None
    #PRUEBA UNITARIA PERSONALIZADA UNITTEST:
    #test_algo(): Las funciones que realizan pruebas unitarias a través de la librería unittest se deben 
    #encontrar dentro de una clase propia que herede de TestCase. Dentro de la función se declaran los métodos 
    #que realizarán pruebas unitarias personalizadas. Es muy importante mencionar que el nombre de todas las 
    #funciones que se creen con este fin deben empezar con la palabra "test", para que todas puedan ser 
    #ejecutadas automáticamente cuando en el método main se corran las pruebas unitarias unittest.
    def test_algo(self):
        # Acceder a los parámetros configurados en setUp()
        print("Test Unittest")
        resultado = mi_funcion(self.parametro3, self.parametro4)
        self.assertEqual(resultado, 12)



#PRUEBAS UNITARIAS AUTOMÁTICAS CON LA LIBRERÍA NOSE: Una de las mejoras de la librería nose en comparación con 
#unittest, es que su programación es más sencilla, ya que no se debe utilizar una clase para su ejecución, sus 
#funciones se declaran de forma normal y se ejecutan de forma manual.
#configInicialNose(): Función propia que indica los atributos a utilizar en las pruebas unitarias nose, este se 
#ejecuta antes de cada prueba para configurar su estado inicial, así como lo hacía el método setUp() de la 
#librería unittest, pero a diferencia de ese método, todo este proceso se ejecuta de forma manual.
def configInicialNose():
    #MODIFICADORES DE ACCESO: Palabra reservada global.
    #Configuración inicial para cada prueba nose, con la palabra reservada global se está accediendo al 
    #modificador de acceso de una variable, para así lograr que se pueda acceder a ella desde fuera de la 
    #función o método:
    global parametro1, parametro2
    parametro1 = "Hola"
    parametro2 = "Mundo"        #Si la variable es diferente a "Mundo", ocurre un error en nose.
#limpiezaVariables(): Función propia que limpia o reinicia el valor de los atributos utilizados al realizar 
#pruebas unitarias nose, este se ejecuta después de cada prueba para limpiar los valores asignados previamente 
#en su estado inicial, así como lo hacía el método tearDown() de la librería unittest, pero a diferencia de ese 
#método, todo este proceso se ejecuta de forma manual.
def limpiezaVariables():
    #MODIFICADORES DE ACCESO: Palabra reservada global.
    #Limpieza después de cada prueba nose, con la palabra reservada global se está accediendo al modificador de 
    #acceso de una variable, para así lograr que se pueda acceder a ella desde fuera de la función o método:
    global parametro1, parametro2
    parametro1 = None
    parametro2 = None

#PRUEBA UNITARIA PERSONALIZADA NOSE:
#test_algo(): Las funciones que realizan pruebas unitarias a través de la librería nose deben declarar los 
#métodos que realizan sus pruebas unitarias personalizadas. Es muy importante mencionar que el nombre de todas 
#las funciones que se creen con este fin deben empezar con la palabra "test", para que todas puedan ser 
#ejecutadas automáticamente cuando en el método main se corran las pruebas unitarias nose, de la misma forma 
#como se declaran las funciones que realizan pruebas unitarias unittest.
def test_otra_cosa():
    configInicialNose()         #Configuración inicial para cada prueba nose.
    resultado = mi_funcion(parametro1, parametro2)
    assert resultado == "HolaMundo"
    limpiezaVariables()         #Limpieza de variables para las pruebas nose.



#__name__ == __main__: Método main, esta función es super importante ya que sirve para instanciar las clases del 
#programa y ejecutar sus métodos, en python pueden existir varios métodos main en un solo programa, aunque no es 
#una buena práctica.
#Ejecutar las pruebas dentro del método main permite ejecutarlas automáticamente cuando el archivo se ejecute 
#como archivo principal, mientras que ejecutar las pruebas fuera del método main proporciona más control sobre 
#cuándo y cómo se ejecutan las pruebas, lo que puede ser útil en escenarios más complejos o personalizados.
if __name__ == "__main__":
    #MANEJO DE EXCEPCIONES: Es una parte de código que se conforma de dos partes, try y except: 
    # - Primero se ejecuta el código que haya dentro del try y si es que llegara a ocurrir una excepción durante 
    #   su ejecución, el programa brinca al código del except
    # - En la parte de código donde se encuentra la palabra reservada except, se ejecuta cierta acción cuando 
    #   ocurra el error. 
    #Se utiliza esta arquitectura de código cuando se quiera efectuar una acción donde se espera que pueda 
    #ocurrir un error durante su ejecución y en este caso se usa para intentar manejar de forma separada las 
    #excepciones causadas en las pruebas unittest y nose, aunque solo funciona parcialmente.
    #Ejecutar pruebas unittest:
    print("--------------------------------------------Unit Test Testing--------------------------------------------")
    try:
        #EJECUCIÓN DE PRUEBAS UNITARIAS UNITTEST DE FORMA AUTOMATIZADA: 
        #Creación de objeto o instancia de la clase TestSuite(), perteneciente a la librería unittest.
        suite = unittest.TestSuite()
        #TestSuite es un objeto que permite agrupar y organizar todas las pruebas unitarias creadas a partir de 
        #la librería unittest. Proporcionando varios métodos que permiten construir el conjunto de pruebas de 
        #manera flexible y escalable:
        # - addTest(test): Agrega una prueba individual al conjunto de pruebas.
        #           - 
        # - addTests(tests): Agrega varias pruebas al conjunto de pruebas.
        #           - 
        # - addTestSuite(test_suite): Agrega otro objeto TestSuite al conjunto de pruebas.
        #           - 
        # - countTestCases(): Retorna el número total de casos de prueba en el conjunto.
        # - tests(): Retorna una lista de todas las pruebas en el conjunto, en el orden en que fueron agregadas.
        # - debug(): Ejecuta las pruebas en el conjunto en modo de depuración.
        # - getTestCaseNames(testcase_class): Retorna una lista de los nombres de los casos de prueba en una 
        #   clase de caso de prueba dada.
        # - __iter__(): Retorna un iterador para recorrer todas las pruebas en el conjunto.
        # - __str__(): Retorna una representación de cadena legible del conjunto de pruebas.
        suite.addTest(MyTestCase('test_algo'))
        #Creación de objeto o instancia de la clase TextTestRunner(), perteneciente a la librería unittest.
        #TestSuite es un objeto que se utiliza para ejecutar pruebas unitarias y generar un informe de 
        #resultados en formato de texto que se muestre en consola:
        # - run(result): Ejecuta las pruebas del conjunto result y genera informes que indican si cada prueba ha 
        #   tenido éxito o ha fallado, además de mostrar en cuánto tiempo fue ejecutada cada prueba. Dichos 
        #   informes se presentan en un formato legible para los humanos en consola o en un archivo de texto y 
        #   se conforman de la siguiente estructura:
        #           - Nombre de la prueba: Se muestra información sobre cada prueba individual ejecutada, como 
        #             el nombre de la prueba y la clase que la está ejecutando, normalmente esto se muestra 
        #             solamente cuando ocurre una excepción.
        #                   test_nombre_de_prueba           (clase_de_prueba)
        #                   ----------------------------------------------------------------------
        #                   Mensaje de la excepción.
        #                   ----------------------------------------------------------------------
        #           - Estado de la prueba: Muestra si la prueba ha pasado correctamente o ha fallado. Si una 
        #             prueba falla, se mostrará un mensaje de error específico para cada prueba.
        #                   OK:    La prueba fue aprobada.
        #                   F o E: La prueba ha fallado y arrojado una excepción.
        #           - Tiempo de ejecución: Indica la cantidad total de pruebas que se ejecutaron y el tiempo que 
        #             tomó en ejecutarse.
        #                   ----------------------------------------------------------------------
        #                   Ran       "numero_pruebas"      tests in    "tiempo"  s
        #           - Estadísticas globales: Después de mostrar los detalles de cada prueba, se presenta un 
        #             resumen general de los resultados, mostrando la misma información de arriba pero ahora 
        #             para la suma de todas las pruebas. 
        # - runTest(test): Ejecuta una prueba individual especificada dentro del conjunto.
        unittest.TextTestRunner().run(suite)
    #Para identificar el tipo de excepción que ha ocurrido y utilizarlo en la instrucción except, se puede 
    #utilizar la clase Exception, que es una clase incorporada en Python utilizada para describir todos los 
    #tipos de excepciones, luego de colocar el nombre de la clase Exception se usa la palabra reservada "as" 
    #seguida de un nombre de variable, esto nos permitirá acceder a la instancia de la excepción y 
    #utilizarla dentro del except, aunque esto al ejecutar pruebas unitarias no funciona de nada, ya que estas 
    #líneas de código son ignoradas y el error es mostrado siu¿guiendo las convenciones de las librerías de 
    #pruebas unittest y/o nose.
    except Exception as e:
        print("Ocurrió el siguiente tipo de error: ", type(e).__name__)
        print("Error en unittest:", e)
    
    #Ejecutar pruebas nose con métodos de configuración inicial y limpieza implementados:
    print("\n\n----------------------------------------------Nose Testing-----------------------------------------------")
    try:
        #nose.runmodule(): Método que busca y ejecuta automáticamente todas las pruebas unitarias que utilicen 
        #la librería de pruebas nose de Python, para ello el nombre de todas las funciones que ejecuten pruebas 
        #unitarias con nose deben empezar con la palabra "test", además genera un informe de resultados en la 
        #salida estándar, ya sea en consola o en un archivo de texto. Dichos informes se presentan en un formato 
        #legible para los humanos en consola o en un archivo de texto y se conforman de la siguiente estructura:
        # - Nombre de la prueba: Indica el nombre de la prueba unitaria que se está ejecutando.
        #       test_nombre_de_prueba           (clase_de_prueba)
        #       ----------------------------------------------------------------------
        #       Mensaje de la excepción.
        #       ----------------------------------------------------------------------
        # - Estado de la prueba: Muestra si la prueba ha pasado correctamente o ha fallado. Si una prueba falla, 
        #   se mostrará un mensaje de error específico para cada prueba.
        #       OK:    La prueba fue aprobada.
        #       F o E: La prueba ha fallado y arrojado una excepción.
        #           - Tiempo de ejecución: Indica la cantidad total de pruebas que se ejecutaron y el tiempo que 
        #             tomó en ejecutarse.
        #       ----------------------------------------------------------------------
        #       Ran       "numero_pruebas"      tests in    "tiempo"  s
        # - Estadísticas globales: Después de mostrar los detalles de cada prueba, se presenta un resumen 
        #   general de los resultados, mostrando la misma información de arriba pero ahora para la suma de todas 
        #   las pruebas.
        nose.runmodule()
    except Exception as e:
        print("Error en nose:", e)