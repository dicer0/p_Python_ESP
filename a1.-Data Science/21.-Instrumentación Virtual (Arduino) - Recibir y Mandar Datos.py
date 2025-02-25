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

#INSTRUMENTACIÓN VIRTUAL CON PYFIRMATA Y ARDUINO:
#Para que se pueda realizar la instrumentación virtual con una tarjeta de desarrollo Arduino, primero se debe 
#correr en su IDE (editor de código) el programa 21.-Instrumentacion_Virtual_Mandar_Recibir_Datos_Arduino.ino, 
#donde se encuentra la librería Standard Firmata, además se indica de esta manera cuál es el puerto de conexión 
#serial entre la placa de desarrollo Arduino y el ordenador. 
#La función de la biblioteca Standard Firmata de Arduino y la librería pyfirmata es permitir el intercambio 
#bidireccional entre la placa de desarrollo y el ordenador, permitiendo así su control y monitoreo. Para ello,
#el pin de salida donde se hará parpadear un led y el pin de entrada analógico con el cual se reciben y grafican 
#sus niveles de tensión son los siguientes:
#   - Puerto de salida digital donde parpadea un led = 13.
#   - Puerto de entrada analógico que recibe niveles de tensión = A0.
#Si la tarjeta de desarrollo Arduino no se encuentra conectada al ordenador, el programa arrojará un error.
#El código completo de Arduino se incluye comentado en la parte de abajo de este programa.

import matplotlib.pyplot as plt #matplotlib: Librería de graficación matemática.
import drawnow #drawnow: Librería para generar gráficos que se actualizan continuamente en tiempo real.
import time #time: Librería del manejo de tiempos, como retardos, contadores, etc.
#pyfirmata: Librería que permite la comunicación bidireccional entre Python y Arduino, brindando control y 
#monitoreo de sus pines digitales y analógicos, envío de señales PWM, lectura y escritura de datos y establecer
#una comunicación a través de los protocolos I2C y Serial. La comunicación entre Arduino y Python se realiza 
#utilizando el protocolo Firmata, el cual permite controlar y monitorear dispositivos conectados a una placa 
#Arduino desde un software de computadora, para habilitarlo, primero se debe subir el programa:
#21.-Stardard_Firmata_Mandar_Datos_Arduino.ino a la placa de desarrollo a través del IDE de Arduino.
import pyfirmata

#VARIABLES:
t = []                #Lista que almacena los datos del eje horizontal (x = tiempo [s]) de la gráfica.
data = []             #Lista que almacena los datos del eje vertical (y = tensión [V]) de la gráfica.
temp_t = 0            #Variable que cuenta cada 0.5 segundos el tiempo de ejecución del programa.
samplingTime = 0.5    #Intervalo del conteo del objeto Time indicado en segundos.

serial_port = "COM7"  #Variable tipo string con el mismo puerto al que está conectado el Arduino en su IDE.

#PYFIRMATA: CONEXIÓN SERIAL, CONTROL Y MONITOREO DE PINES DE UNA TARJETA DE DESARROLLO
#Instancia de la clase Arduino, que pertenece a la librería pyfirmata, dicho objeto proporciona métodos para 
#comunicarse con placas Arduino utilizando el protocolo Firmata, permitiendo así el control y monitoreo de sus 
#pines digitales y analógicos, realizar el envío de señales PWM, lectura y/o escritura de datos y establecer una 
#comunicación a través de los protocolos I2C y Serial, la conexión serial con los microcontroladores se realiza 
#utilizando la clase pyfirmata.Arduino(), independientemente del tipo de microcontrolador que se esté 
#utilizando, ya que la librería pyfirmata proporciona una interfaz común para comunicarse con diferentes placas 
#de desarrollo, incluyendo Arduino, Raspberry Pi, Intel Galileo, PyCARD, etc. Para ello su constructor recibe 
#los siguientes parámetros:
# - port (obligatorio): Especifica el puerto de comunicación a través del cual se conectará la placa Arduino. 
#   Puede ser una cadena de texto que representa el nombre del puerto, como por ejemplo 'COM3' en Windows 
#   o '/dev/ttyACM0' en Linux. El nombre del parámetro no se indica explícitamente.
# - timeout (opcional): Especifica el tiempo máximo de espera (en segundos) para establecer la conexión con la 
#   placa Arduino. Si no se especifica, se utilizará un valor predeterminado.
# - baudrate: Este parámetro establece la velocidad de comunicación en baudios para la comunicación entre la 
#   computadora y el microcontrolador. Los baudios representan la cantidad de bits que se pueden transmitir por 
#   segundo. 
#       - El valor que utiliza la librería Standard Firmata por default es de 57600, pero también se puede usar 
#         otros valores como 9600, 115200, etc. Pero esto debería ser cambiado igual en el código Arduino de la 
#         librería que se sube al Arduino. 
# - bytesize, parity y stopbits (opcionales): Estos parámetros permiten configurar la transmisión serial y se 
#   utilizan en conjunto para establecer cómo se transmiten los datos entre la computadora y la placa de 
#   desarrollo.
board = pyfirmata.Arduino(serial_port, baudrate = 57600)   #Conexión serial.
#Instancia de la clase Iterator, que hereda de la clase util y ambas pertenecen a la librería pyfirmata, dicho 
#objeto permite al programa percibir, capturar y procesar los cambios que ocurran en los pines de entrada de la 
#placa, para ello su constructor recibe como parámetro un objeto pyfirmata.Board que ya haya realizado una 
#conexión serial entre la computadora y la tarjeta de desarrollo.
it = pyfirmata.util.Iterator(board)
#pyfirmata.util.Iterator.start(): Método utilizado para iniciar el proceso de lectura de datos entrantes desde 
#la placa de desarrollo previamente conectada al ordenador de forma serial con el constructor:
#pyfirmata.Arduino().
it.start()
#SELECCIÓN DE LOS PINES QUE SE QUIERE CONTROLAR Y/O MONITOREAR:
#Opción 1: 
#pyfirmata.Arduino.digital[númeroPin].mode = pin_de_entrada_o_salida: Método utilizado para acceder a un pin 
#digital específico, perteneciente a la placa de desarrollo con la que ya se ha realizado una conexión serial. 
#Indicando después del signo igual si este es utilizado como entrada o salida por medio de las constantes OUTPUT 
#o INPUT de la librería pyfirmata.
#pyfirmata.Arduino.analog[númeroPin].mode = pin_de_entrada_o_salida: Método utilizado para acceder a un pin 
#analógico específico, perteneciente a la placa de desarrollo con la que ya se ha realizado una conexión serial. 
#Indicando después del signo igual si este es utilizado como entrada o salida por medio de las constantes OUTPUT 
#o INPUT de la librería pyfirmata.
#Opción 2: 
#pyfirmata.Arduino.get_pin(): Método utilizado para acceder a un pin específico de la placa de desarrollo con la 
#que ya se ha realizado una conexión serial. Indicando si este es analógico o digital, su número y si será 
#utilizado como entrada o salida siguiendo la sintaxis descrita a continuación:
# - 'analogico_o_digital:   numero_pin:     entrada_o_salida'
#       - 'analogico:       numero_pin:     entrada'            = 'a: numero_pin: i'
#       - 'analogico:       numero_pin:     salida'             = 'a: numero_pin: o'
#       - 'digital:         numero_pin:     entrada'            = 'd: numero_pin: i'
#       - 'digital:         numero_pin:     salida'             = 'd: numero_pin: o'
#El número y asignación de pin analógico o digital varía dependiendo de la tarjeta de desarrollo.
board.digital[13].mode = pyfirmata.OUTPUT
board.analog[0].mode = pyfirmata.INPUT

#time.sleep(): Método que se utiliza para suspender la ejecución de un programa durante un intervalo de tiempo 
#específico dado en segundos. 
time.sleep(2)         #Delay de 2 segundos

#pyfirmata.Arduino.analog[númeroPin].enable_reporting(): Método utilizado para para habilitar el monitoreo y 
#lectura de valores analógicos en un pin analógico específico de la placa Arduino.
board.analog[0].enable_reporting()


#GRÁFICA ÚNICA TIPO MATPLOTLIB: 
#make_figure(): Función para graficar los datos recabados del Arduino, se declara dentro de una función propia
#la graficación de los datos ya que para que estos puedan ser actualizados en tiempo real, se utiliza el método 
#drawnow(), perteneciente a la librería drawnow, que debe recibir esta función como su parámetro.
def make_figure():
    #matplotlib.title(): Método que indica indica el título de la ventana que muestra la gráfica dinámica.
    plt.title("Instrumentación Virtual Arduino - Pyfirmata")
    plt.ylim(-0.1, 6) #matplotlib.ylim(): Método que indica el rango del eje vertical en la gráfica.
    #matplotlib.grid(): Método que recibe un valor booleano para indicar si aparece una rejilla o no en la 
    #gráfica, por default está en valor False.
    plt.grid(True)
    plt.xlabel("Tiempo (s)") #matplotlib.xlabel(): Método que indica el texto que aparece en el eje horizontal.
    plt.ylabel("Tensión (V))") #matplotlib.ylabel(): Método que indica el texto que aparece en el eje vertical.
    #matplotlib.plot(): Método usado para crear la gráfica, indicando como primer parámetro su eje horizontal, 
    #luego su eje vertical y finalmente el estilo de la gráfica.
    # - Colores:             C1: color naranja, r: color rojo, b: color azul, g: verde, c: cyan, m: morado, 
    #   y: amarillo, k: negro, w: blanco.
    # - Tipo de marcadores:  o: círculos, +: símbolos de más, .; puntos, v: Triángulo hacia abajo, h: Hexágono, 
    #   s: cuadrados, etc.
    # - Tipo de Líneas:      -: sólida, --: punteada (líneas), :: punteada (puntos), -.: línea y punto, 
    #   'or': Nada.
    plt.plot(t,data,'ch--')
#matplotlib.show(): Método para mostrar la gráfica creada.
plt.show()


#EJECUCIÓN DE LA GRÁFICA:
N = 50        #Variable que indica el límite de datos recopilados, el límite de Excel es de 32,000 datos.
print("El programa recopilará ", N, " datos.")
for i in range(N):
    #La operación % significa módulo y lo que hace esta es dividir un número y ver el resultado de su residuo.
    #En la operación 3%2 == 0, lo que está haciendo es dividir 3/2 y ver si su residuo es cero, que en este caso 
    #no lo sería, ya que residuo = 1.
    # - n%2 == 0: La operación verifica si el valor de n es divisible por 2 sin dejar residuo. En otras 
    #   palabras, verifica si n es un número par.
    if (i%2 == 0):
        #pyfirmata.Arduino.digital[númeroPin].write(): Método que se utiliza para escribir un valor en algún pin 
        #digital de la placa, controlando si su estado está en alto (1 o True) o bajo (0 o False).
        # - Encender LED:   write(True)  o write(1).
        # - Apagar LED:     write(False) o write(0).
        #El método write() solamente se puede usar con pines de salida digital, si se quiere controlar la salida 
        #de un pin analógico se debe usa el método analog_write().
        board.digital[13].write(1)
    else:
        board.digital[13].write(0)
    if (i == 0):
        print("Tiempo [s]\tTensión [V]")
    #MANEJO DE EXCEPCIONES: Es una parte de código que se conforma de dos partes, try y except: 
    # - Primero se ejecuta el código que haya dentro del try y si es que llegara a ocurrir una excepción durante 
    #   su ejecución, el programa brinca al código del except
    # - En la parte de código donde se encuentra la palabra reservada except, se ejecuta cierta acción cuando 
    #   ocurra el error. 
    #Se utiliza esta arquitectura de código cuando se quiera efectuar una acción donde se espera que pueda 
    #ocurrir un error durante su ejecución.
    try:
        #pyfirmata.Arduino.analog[númeroPin].read(): Método que se utiliza para leer el valor actual de un pin 
        #en la placa. Permite obtener el estado del pin, que puede ser un valor analógico o digital, dependiendo 
        #de cómo esté configurado.
        # - Pin digital de entrada: Devolverá un valor booleano (True o False), que indica si el pin está en 
        #   alto (encendido) o en bajo (apagado) respectivamente.
        # - Pin analógico de entrada: Devolverá un valor numérico que representa la lectura analógica en el 
        #   pin. 
        #       - Placa Arduino: Este valor suele estar en un rango de 0 a 1, donde 0 coresponde al valor 
        #         binario 0 y 1 al valor binario 1023, que hace referencia a la resolución de 10 bits del 
        #         conversor analógico a digital (ADC) en la placa Arduino:
        #               - Resolución de 10 bits del ADC del Arduino: (2^10)-1 = 1023
        #Si se utiliza el método read() en un pin que está configurado como salida, el resultado puede ser 
        #impredecible o no tener sentido.
        tensionBinariaA0 = board.analog[0].read()
        print("Valor decimal obtenido del ADC de 10 bits del Arduino:       ", tensionBinariaA0)

        #CONVERSIÓN DE NUMEROS BINARIOS NUMÉRICOS DE TENSIÓN A VALORES DE TENSIÓN REALES:
        #float(): Método que convierte un tipo de dato cualquiera en númerico decimal.
        #Se realiza esta operación porque como el ADC del arduino lee de 0 a 5V y como tiene una resolución de 
        #10 bits permitiendo que en el ADC los valores de tensión se interpreten como valores numéricos enteros 
        #que valen de 0 a (2^10)-1 = 1023, se hace una regla de 3 para que se imprima el valor de la tensión en 
        #consola en vez del valor decimal binario. En esta operación no es necesario dividir el resultado entre 
        #la resolución del ADC porque el valor que retorna el método read ya está normalizado en el rango de 0 a
        #1 (correspondiente a los 1024 niveles).
        #Tensión = Tensión_decimal_read*(ValorMáximoTensión) = Tensión_decimal_read*(5)
        highValueBoard = 5.0            #Valor de tensión Máxima = 5V.
        VoltsA0 = float(tensionBinariaA0)*highValueBoard
        print(i, "-. Valor real de tensión:                                 ", VoltsA0, "[V]")
        #append(): Método que sirve para agregar valores a una lista, tupla, numpy array o diccionario.
        data.append(VoltsA0)            #Creación del vector tensión (voltaje).

        #VECTOR TIEMPO:
        #Se usa una variable intermedia que va contando el tiempo transcurrido desde que se empezó a recopilar 
        #los valores de tensión del puerto analógico A0 del Arduino hasta que acaba. El intervalo de tiempo con 
        #el que cuenta el temporizador y el tiempo que se detiene delay que se declarará después del except debe
        #ser el mismo.
        temp_t = temp_t + samplingTime  #Variable intermedia que cuenta el tiempo de ejecución del programa.
        #append(): Método que sirve para agregar valores a una lista, tupla, numpy array o diccionario.
        t.append(temp_t)                #Creación del vector tiempo.
        print("%.1f \t %g"%(temp_t, VoltsA0))

        #drawnow.drawnow(): Método que permite actualizar y redibujar una figura o gráfico en tiempo real. Se 
        #utiliza comúnmente junto con la librería matplotlib para crear visualizaciones interactivas que se 
        #actualizan dinámicamente y se utiliza en conjunto con una función de graficación personalizada. 
        #Esta función de trazado define cómo se representan los datos en el gráfico.
        drawnow.drawnow(make_figure)    #Actualización dinámica de la gráfica.
    except:
        #print(): Método para imprimir un mensaje en consola y después dar un salto de línea (Enter).
        print("Chafeó la medida")

    #time.sleep(): Método que se utiliza para suspender la ejecución de un programa durante un intervalo de 
    #tiempo específico dado en segundos. 
    time.sleep(samplingTime)            #Delay de 0.5 segundos

#pyfirmata.Arduino.analog[númeroPin].disable_reporting(): Método utilizado para para desactivar el monitoreo y 
#lectura de valores analógicos en un pin analógico específico de la placa Arduino.
board.analog[0].disable_reporting()
#pyfirmata.Arduino.digital[númeroPin].write(): Método que se utiliza para escribir un valor en algún pin digital 
#de la placa, controlando si su estado está en alto (1 o True) o bajo (0 o False).
# - Encender LED:   write(True)  o write(1).
# - Apagar LED:     write(False) o write(0).
#El método write() solamente se puede usar con pines de salida digital, si se quiere controlar la salida de un 
#pin analógico se debe usa el método analog_write().
board.digital[13].write(0)
#pyserial.Arduino.exit(): Método que cierra la comunicación serial. Es muy importante mencionar que si no se 
#ejecuta este método, el puerto serial se va a quedar bloqueado y no se podrá usar.
board.exit()
#matplotlib.close(): Método que cierra la gráfica previamente abierta con el método matplotlib.show().
plt.close()
print("Se recopilaron correctamente ", N, " datos.\n")
print(data)


#GUARDAR LOS DATOS RECOPILADOS EN UN ARCHIVO:
filename = "C:/Users/diego/OneDrive/Documents/The_MechaBible/p_Python_ESP/a1.-Data Science/0.-Archivos_Ejercicios_Python/a21.-Instrumentacion_Virtual_Mandar_Recibir_Datos_Arduino/DatosArduinoPyfirmata.csv"
#open(): Método que sirve para abrir un archivo cualquiera, para ello es necesario indicar dos parámetros, el 
#primero se refiere a la ruta relativa o absoluta del archivo previamente creado y la segunda indica qué es lo 
#que se va a realizar con él, el contenido del archivo se asigna a una variable.
# - w: Sirve para escribir en un archivo, pero borrará la información que previamente contenía el archivo.
# - a: Sirve para escribir en un archivo sin que se borre la info anterior del archivo, se llama append.
new_file = open(filename,'w')
#file.write(): Método que sirve para escribir una palabra o string en un archivo.
new_file.write("Library, Pyfirmata" + "\n")
new_file.write("Time [s], Voltage Pin A0 [V]" + "\n")
for i in range(len(data)):
    #Lista que guarda los valores de tiempo [s] y tensión [V] recopilados.    
    new_file.write(str(t[i]) + "," + str(data[i]) + "\n")
#file.close(): Método para cerrar un archivo previamente abrierto con el método open(), es peligroso olvidar 
#colocar este método, ya que la computadora lo considerará como si nunca hubiera sido cerrado, por lo cual no 
#podré volver a abrirlo al dar clic sobre él.
new_file.close()