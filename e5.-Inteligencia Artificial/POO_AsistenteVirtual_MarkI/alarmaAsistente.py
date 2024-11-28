#ESTABLECER ALARMA:
import datetime #datetime: Librería que proporciona método para trabajar con fechas y horas en Python.
#re: Librería que identifica patrones en expresiones regulares. Una expresión regular es un patrón de texto que se 
#puede utilizar para buscar, reemplazar o extraer texto de una cadena.
import re       #re: Librería que permite utilizar expresiones regulares para detectar patrones.
import keyboard #keyboard: Librería que permite detectar pulsaciones de teclas en el teclado.
import pygame   #pygame: librería de multimedia que permite mostrar gráficos, reproducir sonido, etc.

class widgetAlarma:
    def programarAlarma(self, preguntaUsuario):
        #.replace().lower(): Lo que hace el método replace() es reemplazar todas las palabras que aparezcan en un 
        #string en otra cadena específica y el método lower() sirve para convertir todas las letras de una cadena en 
        #minúsculas, esto es importante hacerlo porque al reproducir una canción o mandar una búsqueda a internet, 
        #siempre es mejor tener puras minúsculas.
        instruccionHora = preguntaUsuario.replace(' alarma', '').lower()
        #strip(): Método utilizado para eliminar los caracteres especificados en una cadena, como espacios saltos de 
        #línea (\n), tabuladores (\t), etc. Si no se le pasa ningún parámetro, eliminará los espacios del string.
        instruccionHora = instruccionHora.strip()
        print(instruccionHora)
        #re.findall(r): El método findall() utilizado para encontrar todas las ocurrencias de una expresión regular en 
        #una cadena de texto (string) recibe 3 parámetros, la expresión regular que se quiere encontrar, la cadena de 
        #caracteres donde se buscará y modificadores opcionales que se pueden utilizar para personalizar el 
        #comportamiento de la búsqueda.
        # - pattern: Parámetro que indica la expresión regular utilizada para extraer partes específicas del string.
        #   Las expresiones regulares más comunes son:
        #   - Búsqueda de números en un string:
        #       - \d: Expresión regular que busca un dígito del 0 al 9 en un string.
        #       - \d+: Expresión regular que coincide con uno o más dígitos del 0 al 9.
        #       - \d{2,4}: Expresión regular que coincide con una secuencia de dígitos de 2 al 4 específicamente, 
        #         osea 234.
        #   - Búsqueda de letras en un string:
        #       - \w: Expresión regular que busca una letra mayúscula o minúscula, un dígito del 0 al 9 o un guión 
        #         bajo.
        #       - \w+: Expresión regular que coincide con uno o más caracteres de los descritos anteriormente.
        #       - [A-Za-z]: Expresión regular que busca solo una letra mayúscula o minúscula.
        #       - \b: Expresión regular que representa el inicio o final de una palabra en un string, usualmente se 
        #         incluyen dos para indicar que se debe buscar un patrón en cada palabra. Por ejemplo, si se declara la 
        #         expresión regular \bHola\b, esto extraerá todas las palabras Hola dentro de un string.
        #   - Búsqueda de palabras en un string (grupos de captura):
        #       - (patrón1|patrón2): Expresión regular que crea un grupo de captura para identificar uno o varios 
        #         patrones específicos.
        #       - |: Compuerta OR utilizada para reconocer uno o varios patrones dentro de un grupo de captura.
        #   - Búsqueda de espacios en blanco, puntos y paréntesis en un string:
        #       - \s: Expresión regular que coincide con un carácter de espacio vacío, como un espacio, tabulador (\t), 
        #         salto de línea (\n), etc.
        #       - \.: Expresión regular que encuentra un punto en un string.
        #       - \(: Expresión regular que encuentra un paréntesis de apertura en un string.
        #       - \): Expresión regular que encuentra un paréntesis de cierre en un string.
        #   - Búsqueda de repeticiones en un string:
        #       - *: Encuentra cero o más repeticiones de la expresión regular que tenga a la izquierda.
        #       - +: Encuentra una o más repeticiones de la expresión regular que tenga a la izquierda.
        #       - ?: Encuentra cero o una repetición de la expresión regular que tenga a la izquierda. Esto significa 
        #         que la expresión regular que la precede es opcional y puede aparecer una vez o no aparecer en 
        #         absoluto en la cadena que se está buscando.
        #       - {2,4}: Coincide con 2, 3 o 4 repeticiones de la expresión regular que tenga a la izquierda.
        #   - Anclaje de patrones:
        #       - ^: Cuando se coloca al principio de un patrón indica que la coincidencia debe encontrarse al comienzo 
        #         de la línea de texto. Por ejemplo, si se declara la expresión regular ^Hola, esto será cierto solo 
        #         cuando la palabra Hola se encuentre al inicio del string.
        #       - $: Cuando se coloca al final de un patrón indica que la coincidencia debe encontrarse al final de la 
        #         línea de texto. Por ejemplo, si se declara la expresión regular $mundo, esto será cierto solo cuando 
        #         la palabra mundo se encuentre al final del string.
        #       - ?: : Cuando se coloca un signo de interrogación seguido de dos puntos se está indicando que es un 
        #         grupo no capturador, esto significa que se tomará en cuenta para hacer coincidencias, pero no será 
        #         incluido dentro de la lista de tuplas.
        # - string: Palabra en la que se desea buscar patrones a través de la expresión regular especificada.
        # - flags: Modificadores opcionales que personalizan el comportamiento de la búsqueda.
        #   - re.IGNORECASE: Realiza la búsqueda sin distinción entre mayúsculas y minúsculas.
        #   - re.MULTILINE: Permite que el patrón coincida con múltiples líneas en la cadena.
        #   - re.DOTALL: Hace que el carácter . en el patrón coincida también con el carácter de nueva línea \n.
        #Esta expresión regular busca números en un string.
        numeroshora = re.findall(r"\d+", instruccionHora)
        print(numeroshora)
        #join(): Este método toma una lista de strings como argumento y los concatena, juntando cada string con el 
        #carácter especificado.
        hora = ":".join(numeroshora)
        print(hora)
        
        #Para que el string que representa la hora pueda ser convertido a un objeto datetime con formato de 12 
        #horas, se debe indicar si la hora de este es pm o am, pero para que esto sea entendido por el método 
        #strptime(), se debe indicar en mayúsculas.
        if("pm" in instruccionHora):
            hora += " PM"
        else:
            hora += " AM"
        #datetime.datetime.strptime(): Método de la clase datetime que toma una cadena que representa una fecha y 
        #hora en un formato específico y la convierte a un objeto datetime, para ello recibe las siguientes 
        #instrucciones en su segundo parámetro:
        # - %H: Hora en formato de 24 horas (00-23).
        # - %I: Hora en formato de 12 horas (01-12). Para esto se debe indicar si la hora es AM o PM.
        # - %p: AM o PM (funciona con %I para indicar la parte de la tarde o la mañana).
        # - %M: Minutos (00-59).
        # - %S: Segundos (00-59).
        # - %f: Microsegundos (000000-999999).
        # - %z: Desplazamiento de la zona horaria UTC en formato ±HHMM o ±HH:MM.
        hora = datetime.datetime.strptime(hora, "%I:%M %p")  #Se indica "%I" para usar el formato de 12 horas.
        #Conversión de objeto datetime con formato de 12 horas en formato de 24 horas. Esto se hace para que sea 
        #compatible con la hora actual retornada por medio del método datetime.datetime.now().strftime("%H:%M").
        horaAlarma = hora.strftime("%H:%M")
        print(horaAlarma)
        #datetime.datetime.now().strftime(): Método que devuelve la  fecha y hora actual en el formato 
        #YYYY-MM-DD HH:MM:SS, al cual se accede con el string "%Y-%m-%d %H:%M:%S".
        print(datetime.datetime.now().strftime("%H:%M"))
        return horaAlarma

    def sonarAlarma(self, horaAlarma):
        respuestaAlarma = ""
        if (datetime.datetime.now().strftime("%H:%M") == horaAlarma):
            while True:
                print("---------Hola di_cer0, ya es la hora en la que me pediste que estableciera una alarma---------")
                #pygame.mixer.init(): El método init() inicializa el objeto mixer de la librería pygame 
                #que sirve para reproducir sonidos con Python.
                pygame.mixer.init()
                #pygame.mixer.music.load(): El método load() carga un archivo de música con formato wav, 
                #mp3 u ogg en la memoria para que pueda ser reproducido al ejecutar el método play().
                pygame.mixer.music.load("C:/Users/diego/OneDrive/Documents/The_MechaBible/p_Python_ESP/5.-Inteligencia Artificial/0.-Archivos_Ejercicios_Python/Till I Collapse - Eminem.mp3")
                pygame.mixer.music.play()
                #keyboard.read_key(): Método que devuelve la tecla presionada por el usuario.
                if(keyboard.read_key() == "space"):
                    #pygame.mixer.music.stop(): Método que detiene la música que se haya reproducido 
                    #anteriormente con la función play().
                    pygame.mixer.music.stop()
                    break
            horaAlarma = None
            respuestaAlarma = "Hola di0, alarma detenida"
        return respuestaAlarma