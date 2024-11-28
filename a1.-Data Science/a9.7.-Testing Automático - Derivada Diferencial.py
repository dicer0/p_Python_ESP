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

import numpy as np #numpy: Librería que realiza operaciones matemáticas complejas (matriciales).
import tabulate #tabulate: Librería que permite crear tablas con varios formatos conocidos.
import nose.tools #nose: Extensión de la librería unittest, brindando características y mejoras adicionales.
#Usar dos librerías distintas para realizar pruebas unitarias en un mismo programa puede resultar complicado y 
#propenso a errores, ya que los frameworks de pruebas están diseñados para proporcionar una estructura 
#coherente y consistente para las pruebas, por lo que mezclar dos o más frameworks puede generar inconsistencias 
#y conflictos. Si se desea utilizar librerías distintas para diferentes pruebas en un mismo programa, es 
#recomendable separar las pruebas en módulos o archivos diferentes, asignando a cada módulo a un framework 
#específico con su propio conjunto de configuraciones y variables, para que no se vean afectadas las pruebas 
#del otro módulo.

#6.- DIFERENCIACIÓN NUMÉRICA: Derivada con la fórmula diferencial - Assertion, Unittesting y Nose Testing. 
#La fórmula general puede utilizarse para hallar una derivada aproximada de una función matemática f(x) 
#si h es lo suficientemente pequeña:
#f'(x) ≈ (f(x+h)-f(x-h))/2*h

#a)	Escribe una función diff(f, x, h = 1e-5) que devuelva una aproximación de la derivada de una función 
#matemática representada por una función f(x).
def diff(f, x, h = 1e-5):
    #El 2 del numerador se expresa con un valor decimal para que se entienda que el valor que devuelve df es 
    #float, osea un número decimal.
    df = (f(x+h) - f(x-h))/(2.0*h) #f'(x) ≈ (f(x+h)-f(x-h))/2*h
    return df



#b) Aplica la función diff() para diferenciar las siguientes ecuaciones, que están declaradas por medio de 
#funciones anónimas dentro del código Python, luego resta el resultado obtenido en la diferencial menos el 
#que se debió haber obtenido al realizar la derivada de la función al ser evaluada en el punto de x indicado 
#debajo, con esta operación se calcula el error manualmente:
# 1.- f(x) = e^x;           x = 0;              f'(0) = 1*e^x = 1*e^0 = 1
# 2.- f(x) = e^(-2x^2);     x = 0;              f'(0) = -4x*e^(-2x^2) = -4(0)*e^(-2(0)^2) = 0*e^(0) = 0
# 3.- f(x) = cos⁡x;          x = 2π;             f'(0) = -sin(x) = -sin(0) = -sin(0) = 0
# 4.- f(x) = ln⁡x;           x = 1;              f'(0) = 1/x = 1/1 = 1

#Función Anónima: En este tipo de funciones se utiliza la palabra reservada "lambda" para crear funciones 
#sin nombre, mejor conocidas como "funciones lambda" o "expresiones lambda", estas son declaradas por medio 
#de la siguiente sintaxis:
#   variable = lambda       parámetros:     operación_función
#numpy.exp(x) = e^x = e**x: Método que devuelve el valor exponencial de un número con base "e".
#numpy.cos(x): Calcula la función coseno aplicada a una variable x, esperando que su valor esté en radianes.
#numpy.log(x): Calcula el logaritmo natural (logaritmo en base e) ln de un valor o una matriz de valores.
f1 = lambda x: np.exp(x)                   #1.- f(x) = e^x
f2 = lambda x: np.exp(-2.0*(x**2))         #2.- f(x) = e^(-2x^2)
f3 = lambda x: np.cos(x)                   #3.- f(x) = cos⁡x
f4 = lambda x: np.log(x)                   #4.- f(x) = ln⁡x

#DIFERENCIACIÓN DE LAS FUNCIONES:
x = [0, 0, 2*np.pi, 1]  #Puntos de x donde se evalúan las diferenciales de las funciones f1, f2, f3 y f4.
resultado_derivada = [1, 0, 0, 1] #Resultados exactos de todas las derivadas evaluadas en los puntos de x.
resultado_diferencial = [] #Lista que guardará el resultado de las derivadas hechas con la diferencial.
#append(): Método que sirve para agregar valores a una lista, tupla, numpy array o diccionario.
#Se aplica la función diferencial a cada función para aproximar su derivada y esto se realiza evaluando cada 
#función en su respectivo valor de x, que es distinto para cada una, además se declara que el valor de 
#dx = h, se cambie al que estaba indicado por default a ser dx = h = 0.01.
dx = 0.01
resultado_diferencial.append(diff(f1, x[0], dx))
resultado_diferencial.append(diff(f2, x[1], dx))
resultado_diferencial.append(diff(f3, x[2], dx))
resultado_diferencial.append(diff(f4, x[3], dx))



#c)	Assertion Testing: Escribe una función assertionTesting() que verifique la implementación de la función 
#diff() aplicada a las funciones del inciso b). En este ejemplo no se está utilizando ninguna biblioteca de 
#pruebas como unittest o nose, en su lugar se está realizando una prueba básica y manual utilizando la 
#declaración assert.
def assertionTesting(umbral_assertion_testing):
    #IMPRIMIR LOS RESULTADOS EN UNA TABLA Y CALCULAR EL ERROR OBTENIDO EN ELLAS CON LA RESTA INDICADA EN C):
    error = [] #Error calculado al restar el resultado de: diferencial_f(x) - derivada_f(x).
    nombre_funciones = ['e^x','e^(-2x^2)','cos(x)','ln(x)'] #Nombre de las columnas en la tabla de funciones.
    #Lista vacía donde se almacenarán el nombre de la función, el valor x con el que se realizó la derivada, su 
    #resultado y el error que se obtuvo al restar ambas para poder mandar la matriz al método tabulate y mostrar 
    #la tabla en consola.
    tabla = []

    #CÁLCULO DEL ERROR PARA CADA UNA DE LAS FUNCIONES: Para ello se resta el valor obtenido de la diferencial 
    #menos el valor que debió haber obtenido al aplicar su derivada, después lo que se hace es sacar el valor
    #absoluto de este valor, ya que no puede existir errores negativos.
    #abs(): Método que saca el valor absoluto de un número, volviéndolo positivo aunque sea originalmente 
    #negativo.
    error.append(abs(resultado_diferencial[0] - resultado_derivada[0]))
    error.append(abs(resultado_diferencial[1] - resultado_derivada[1]))
    error.append(abs(resultado_diferencial[2] - resultado_derivada[2]))
    error.append(abs(resultado_diferencial[3] - resultado_derivada[3]))

    #BUCLE FOR: En Python no se utilizan llaves de apertura o cierre para la sintaxis de un bucle, solamente se 
    #utilizan dos puntos para indicar su inicio y tabuladores para diferenciar qué es lo que está dentro o fuera 
    #de él. Además, después de la palabra reservada "for" se declara una variable local numérica entera que solo 
    #existirá dentro del bucle y será la que cuente desde 0 por default o desde el primer número indicado dentro 
    #del paréntesis hasta el extremo indicado en el segundo parámetro que se encuentra dentro del paréntesis de 
    #la palabra reservada range() para terminar el bucle. En otras palabras, dentro del paréntesis de la palabra 
    #reservada "range()" se coloca el inicio y final del conteo para indicar cuantas veces se ejecutará el 
    #bucle.
    #En específico este bucle for se utiliza para crear la matriz que contenga todos los datos a mostrarse en la 
    #tabla creada con la librería tabulate, otra forma de lograr lo mismo hubiera sido utilizar una variable 
    #intermedia a la que se le haya aplicado el método var_temp.append(i) y luego var_temp.append(j) para crear 
    #una sublista al aplicar finalmente el método matriz.append(var_temp). 
    #Aunque en vez de hacer todo eso se puede aplicar directamente el método matriz.append([i, j]) y así crear 
    #las sublistas.
    for i in range (0, len(nombre_funciones)):
        tabla.append([nombre_funciones[i], x[i], resultado_derivada[i] , resultado_diferencial[i], error[i]])

    #CREAR UNA TABLA CON LA LIBRERÍA TABULATE: La tabla se mostrará hasta que cierre la ventana de la gráfica.
    #tabulate.tabulate(): Método que sirve para crear una lista con los valores de un vector, dicho vector debe 
    #contener listas anidadas en cada una de sus posiciones para que estas sean agrupadas en cada fila de la 
    #lista.
    #Las tablas creadas con el método tabulate aceptan los siguientes parámetros:
    # - tabular_data: Este parámetro especifica los datos a mostrar. Puede ser una lista de listas, una lista de 
    #   diccionarios, una lista de tuplas, o una estructura de datos similar.
    # - headers: Es un parámetro opcional que se utiliza para especificar los encabezados de las columnas de la 
    #   tabla. Puede ser una lista de cadenas que representen los nombres de las columnas.
    # - tablefmt: Es un parámetro opcional que indica el formato deseado para la tabla generada. 
    #       - "plain": Sin formato adicional.
    #       - "simple": Formato simple con líneas horizontales.
    #       - "grid": Formato con bordes de cuadrícula.
    #       - "pipe": Formato con delimitadores de tubería.
    #       - "orgtbl": Formato de tabla org.
    # - numalign: Este parámetro se utiliza para alinear los números en las columnas de la tabla. Puede tener 
    #   los siguientes valores:
    #       - "left": Alinea los números a la izquierda.
    #       - "center": Centra los números en la columna.
    #       - "right": Alinea los números a la derecha.
    # - stralign: Este parámetro se utiliza para alinear las cadenas de texto en las columnas de la tabla. Puede 
    #   tener los siguientes valores:
    #       - "left": Alinea las cadenas de texto a la izquierda.
    #       - "center": Centra las cadenas de texto en la columna.
    #       - "right": Alinea las cadenas de texto a la derecha.
    # - missingval: Este parámetro se utiliza para establecer el valor a mostrar cuando los datos son nulos o no 
    #   están disponibles. Puede ser cualquier valor válido, como una cadena de texto, un número, etc. Cuando se 
    #   encuentre un valor nulo en los datos, se mostrará el valor especificado en missingval.
    print(tabulate.tabulate(tabla, headers = ['f(x)','Valor de x','Derivada evaluada en x','Diferencial evaluada en x','Error'], tablefmt = "grid", numalign = "center"))

    #PRUEBAS UNITARIAS AUTOMÁTICAS CON LA DECLARACIÓN ASSERT (ASSERTION TESTING):
    #{index:formato}.format(variable): El método format() permite asignar un formato a un string, para ello 
    #primero se debe usar un especificador de formato, que sigue la siguiente sintaxis: 
    # - {caracteres_que_se_quieren_afectar:formato} 
    #       - {index:}: Para indicar los caracteres que se quieren afectar tenemos que tener en cuenta que las 
    #         posiciones de un string se manejan igual que las de una lista, tupla o diccionario, por lo cual se 
    #         empiezan a contar desde 0 si es que solamente se quiere afectar un solo string, si es que se 
    #         quieren afectar todos, no se pone nada.
    #       - {:formato}: Se pueden agregar modificadores de formato para controlar la precisión decimal, el 
    #         relleno, la alineación y otros aspectos del formato. Algunos modificadores comunes incluyen:
    #           - {:.0e}: El número se mostrará en notación científica con 0 dígitos después del punto decimal, 
    #             para ello primero se debe convertir a entero con el método float().
    #           - {.5f}: El número se mostrará en formato decimal con 5 dígitos después del punto, para ello 
    #             primero se debe convertir a entero con el método float().
    #           - {:b}: El número se mostrará en formato binario, para ello primero se debe convertir a entero 
    #             con el método int().
    #           - {:d}: El número se mostrará en formato de número decimal, para ello primero se debe convertir 
    #             a entero con el método int().
    #           - {:b}: El número se mostrará en formato octal, para ello primero se debe convertir a entero con 
    #             el método int().
    #           - {:x}: El número se mostrará en formato hexadecimal con minúsculas, para ello primero se debe 
    #             convertir a entero con el método int().
    #           - {:X}: El número se mostrará en formato hexadecimal con mayúsculas, para ello primero se debe 
    #             convertir a entero con el método int().
    notacion_cientifica = "{:.1e}".format(umbral_assertion_testing)
    print("\n\n--------------------------------------------Assertion Testing--------------------------------------------")
    print("Para pasar las pruebas de Assertion Testing el error debe ser menor o igual a: ", umbral_assertion_testing, " = ", notacion_cientifica)
    #assert: La palabra reservada assert en Python se utiliza como una declaración de aserción. Su propósito es 
    #verificar si una condición dada es verdadera. Si la condición es falsa, se genera una excepción llamada 
    #AssertionError, la sintaxis de la operación de aserción o afirmación es la siguiente:
    # - assert      condición,      mensaje_de_error
    #       - condición: Es una expresión que se evalúa como verdadera o falsa.
    #       - mensaje_de_error: Es un string opcional que se mostrará si la condición es falsa, si se llegara a 
    #         mostrar este mensaje cuando la condición es falsa, el programa terminaría su ejecución en esa 
    #         línea de código.
    #         Este mensaje puede proporcionar información sobre el error o la aserción que falló.
    assert (error[0] <= umbral_assertion_testing), "Error muy grande al aproximar la derivada de e^x por medio de su diferencial"
    assert (error[1] <= umbral_assertion_testing), "Error muy grande al aproximar la derivada de e^(-2x^2) por medio de su diferencial"
    assert (error[2] <= umbral_assertion_testing), "Error muy grande al aproximar la derivada de cos(x) por medio de su diferencial"
    assert (error[3] <= umbral_assertion_testing), "Error muy grande al aproximar la derivada de ln(x) por medio de su diferencial"
    print("Todas las pruebas pasaron correctamente.")

#Llamada a la función assertionTesting().
#Si la tolerancia se vuelve igual o menor a 1e-5, la prueba unitaria falla y se lanza una excepción. 
umbralAssertion = 1e-4        #Tolerancia de comparación del Assertion Testing
assertionTesting(umbralAssertion)



#d)	Nose Testing: Siguiendo las convenciones de la librería de pruebas nose, que extiende y mejora las 
#capacidades de la librería unittest, realiza y ejecuta pruebas automatizadas a través de la función 
#test_nose_application(). La librería unittest está muy enfocada a la programación orientada a objetos (POO), 
#mientras que la librería nose no, por lo cuál es más sencilla de utilizar, esa es una de sus grandes ventajas.
#Si la tolerancia se vuelve igual o menor a 1e-4, la prueba unitaria falla y se lanza una excepción.

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
    global umbral_nose_testing
    umbral_nose_testing = 1e-4                 #Tolerancia de comparación del Nose Testing
#limpiezaVariables(): Función propia que limpia o reinicia el valor de los atributos utilizados al realizar 
#pruebas unitarias nose, este se ejecuta después de cada prueba para limpiar los valores asignados previamente 
#en su estado inicial, así como lo hacía el método tearDown() de la librería unittest, pero a diferencia de ese 
#método, todo este proceso se ejecuta de forma manual.
def limpiezaVariables():
    #MODIFICADORES DE ACCESO: Palabra reservada global.
    #Limpieza después de cada prueba nose, con la palabra reservada global se está accediendo al modificador de 
    #acceso de una variable, para así lograr que se pueda acceder a ella desde fuera de la función o método:
    global umbral_nose_testing
    umbral_nose_testing = None                 #Limpieza de la variable que almacena la tolerancia.

#test_nose_application(): Las funciones que realizan pruebas unitarias a través de la librería nose no se deben 
#encontrar dentro de una clase, demostrando así su optimización en comparación con el código que utiliza la 
#librería unittest al generar pruebas unitarias personalizadas. Aunque también es muy importante mencionar que 
#el nombre de todas las funciones que se creen con este fin deben empezar con la palabra "test", de igual manera 
#como se realiza al crear pruebas unitarias con la librería unittest.
def test_nose_application():
    #nose.tools.assert_almost_equal(): Método que compara dos valores numéricos y verifica si están "casi" 
    #igualados dentro de una tolerancia dada. Esto es útil cuando se trabaja con cálculos numéricos y se espera 
    #que los resultados sean aproximados debido a errores de redondeo u otras limitaciones, el método recibe 
    #los siguientes parámetros:
    # - nose.tools.assert_almost_equal(valor_real,      valor_esperado,         delta = Tolerancia)
    #       - Si la diferencia entre los valores es menor a la tolerancia, la afirmación se considera verdadera 
    #         y la ejecución continúa sin problemas.
    #       - Si la diferencia es mayor o igual a la tolerancia, se genera una excepción AssertionError, 
    #         indicando que los valores no están "casi" igualados.
    nose.tools.assert_almost_equal(resultado_diferencial[0], resultado_derivada[0], delta = umbral_nose_testing)
    nose.tools.assert_almost_equal(resultado_diferencial[1], resultado_derivada[1], delta = umbral_nose_testing)
    nose.tools.assert_almost_equal(resultado_diferencial[2], resultado_derivada[2], delta = umbral_nose_testing)
    nose.tools.assert_almost_equal(resultado_diferencial[3], resultado_derivada[3], delta = umbral_nose_testing)
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
    #ocurrir un error durante su ejecución.
    #EJECUTAR LAS PRUEBAS UNITARIAS NOSE:
    try:
        configInicialNose()         #Configuración inicial para cada prueba nose.
        #{index:formato}.format(variable): El método format() permite asignar un formato a un string, para ello 
        #primero se debe usar un especificador de formato, que sigue la siguiente sintaxis: 
        # - {caracteres_que_se_quieren_afectar:formato} 
        #       - {index:}: Para indicar los caracteres que se quieren afectar tenemos que tener en cuenta que 
        #         las posiciones de un string se manejan igual que las de una lista, tupla o diccionario, por lo 
        #         cual se empiezan a contar desde 0 si es que solamente se quiere afectar un solo string, si es 
        #         que se quieren afectar todos, no se pone nada.
        #       - {:formato}: Se pueden agregar modificadores de formato para controlar la precisión decimal, el 
        #         relleno, la alineación y otros aspectos del formato. Algunos modificadores comunes incluyen:
        #           - {:.0e}: El número se mostrará en notación científica con 0 dígitos después del punto 
        #             decimal, para ello primero se debe convertir a entero con el método float().
        #           - {.5f}: El número se mostrará en formato decimal con 5 dígitos después del punto, para ello 
        #             primero se debe convertir a entero con el método float().
        #           - {:b}: El número se mostrará en formato binario, para ello primero se debe convertir a 
        #             entero con el método int().
        #           - {:d}: El número se mostrará en formato de número decimal, para ello primero se debe 
        #             convertir a entero con el método int().
        #           - {:b}: El número se mostrará en formato octal, para ello primero se debe convertir a entero 
        #             con el método int().
        #           - {:x}: El número se mostrará en formato hexadecimal con minúsculas, para ello primero se 
        #             debe convertir a entero con el método int().
        #           - {:X}: El número se mostrará en formato hexadecimal con mayúsculas, para ello primero se 
        #             debe convertir a entero con el método int().
        notacion_cientifica_nose = "{:.1e}".format(umbral_nose_testing)
        print("\n\n----------------------------------------------Nose Testing-----------------------------------------------")
        print("Para pasar las pruebas de Nose Testing el error debe ser menor o igual a: ", umbral_nose_testing, " = ", notacion_cientifica_nose)
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
    except Exception as error:
        #type(clase).__name__: Esta instrucción no es un método, sino una expresión que se utiliza para obtener 
        #el nombre de la clase de un objeto en Python, donde type(error) devuelve el tipo de excepción en este 
        #caso ya que error es un objeto de una clase de excepción. 
        # - __name__: Es un atributo especial en Python que se utiliza para obtener el nombre de la clase del 
        #   objeto.
        print("Ocurrió el siguiente tipo de error: ", type(error).__name__)
        print("Error en node:", error)