#IMPORTACIÓN DE LIBRERÍAS:
import datetime #datetime: Librería que proporciona método para trabajar con fechas y horas en Python.
import time     #time: Librería del manejo de tiempos, como retardos, contadores, etc.
import re       #re: Librería que permite utilizar expresiones regulares para detectar patrones.
import locale   #locale: Librería que permite obtener la locación actual del usuario.
import webbrowser   #webbrowser: Librería que permite abrir y utilizar navegadores web en Python.

class widgetGoogleCalendar:
    #CONSTRUCTOR O INICIALIZADOR DE LA CLASE: En él se declaran los parámetros que recibe la clase, que además se 
    #utilizarán en los demás métodos, estos a fuerza deben tener un valor.
    #self: La instrucción self se utiliza para hacer referencia al objeto que se está manipulando cuando se instancía 
    #la clase. Por eso es que a través de la misma nomenclatura de un punto se accede a los distintos atributos y/o 
    #métodos con un objeto desde fuera de la clase.
    def __init__(self, parametro_de_la_clase):
        #ChatGPT API key
        self.servicioAPI = parametro_de_la_clase

    #POO: En Python cuando al nombre de una función se le ponen dos guiones bajos antes de su nombre es porque 
    #se está refiriendo a un método privado, es una buena práctica de sintaxis.
    def __tituloEvento(self, preguntaUsuario):
        #re.findall(r): El método findall() utilizado para encontrar todas las ocurrencias de una expresión 
        #regular en una cadena de texto (string) recibe 3 parámetros, la expresión regular que se quiere encontrar, 
        #la cadena de caracteres donde se buscará y modificadores opcionales que se pueden utilizar para 
        #personalizar el comportamiento de la búsqueda.
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
        #         incluyen dos para indicar que se debe buscar un patrón en cada palabra. Por ejemplo, si se declara 
        #         la expresión regular \bHola\b, esto extraerá todas las palabras Hola dentro de un string.
        #   - Búsqueda de palabras en un string (grupos de captura):
        #       - (patrón1|patrón2): Expresión regular que crea un grupo de captura para identificar uno o varios 
        #         patrones específicos.
        #       - |: Compuerta OR utilizada para reconocer uno o varios patrones dentro de un grupo de captura.
        #   - Búsqueda de espacios en blanco, puntos y paréntesis en un string:
        #       - \s: Expresión regular que coincide con un carácter de espacio vacío, como un espacio, tabulador 
        #         (\t), salto de línea (\n), etc.
        #       - \.: Expresión regular que encuentra un punto en un string.
        #       - \(: Expresión regular que encuentra un paréntesis de apertura en un string.
        #       - \): Expresión regular que encuentra un paréntesis de cierre en un string.
        #   - Búsqueda de repeticiones en un string:
        #       - *: Encuentra cero o más repeticiones de la expresión regular que tenga a la izquierda.
        #       - +: Encuentra una o más repeticiones de la expresión regular que tenga a la izquierda.
        #       - ?: Encuentra cero o una repetición de la expresión regular que tenga a la izquierda. Esto 
        #         significa que la expresión regular que la precede es opcional y puede aparecer una vez o no 
        #         aparecer en absoluto en la cadena que se está buscando.
        #       - {2,4}: Coincide con 2, 3 o 4 repeticiones de la expresión regular que tenga a la izquierda.
        #   - Anclaje de patrones:
        #       - ^: Cuando se coloca al principio de un patrón indica que la coincidencia debe encontrarse al 
        #         comienzo de la línea de texto. Por ejemplo, si se declara la expresión regular ^Hola, esto será 
        #         cierto solo cuando la palabra Hola se encuentre al inicio del string.
        #       - $: Cuando se coloca al final de un patrón indica que la coincidencia debe encontrarse al final de 
        #         la línea de texto. Por ejemplo, si se declara la expresión regular $mundo, esto será cierto solo 
        #         cuando la palabra mundo se encuentre al final del string.
        #       - ?: : Cuando se coloca un signo de interrogación seguido de dos puntos se está indicando que es un 
        #         grupo no capturador, esto significa que se tomará en cuenta para hacer coincidencias, pero no será 
        #         incluido dentro de la lista de tuplas.
        # - string: Palabra en la que se desea buscar patrones a través de la expresión regular especificada.
        # - flags: Modificadores opcionales que personalizan el comportamiento de la búsqueda.
        #   - re.IGNORECASE: Realiza la búsqueda sin distinción entre mayúsculas y minúsculas.
        #   - re.MULTILINE: Permite que el patrón coincida con múltiples líneas en la cadena.
        #   - re.DOTALL: Hace que el carácter . en el patrón coincida también con el carácter de nueva línea \n.
        #Esta expresión regular extrae todas las palabras que se encuentren entre dos conjuntos de palabras clave.
        patronTitulo = re.findall(r"\b(titulo de|título de|se llama|tituladas|titulados|titulo|título|llamado|nombrado|nombrada|nombre)\b\s+(.*?)(?:\s+\b(descripción|descripcion|fecha|hora|inicio|inicial|final|fin)\b|$)", preguntaUsuario, re.IGNORECASE|re.UNICODE)
        #Bucle for each de una sola línea para extraer la posición intermedia de la lista de tuplas.
        tituloLista = [tupla[1] for tupla in patronTitulo]
        #join(): Este método toma una lista de strings como argumento y los concatena, juntando cada string con el 
        #carácter especificado.
        tituloEvento = ', '.join(tituloLista)
        #any():Función que recibe un bucle for que recorrerá un diccionario, lista o tupla para después retornar un 
        #valor booleano True cuando al menos uno de sus elementos sea True o distinto a None.
        #string.endswith(): El método endswith() aplicado a un string verifica si su último caracter es uno en 
        #específico y si es así retorna un valor booleano True.
        if any(tituloEvento.endswith(sufijo) for sufijo in [",", "y", ", ", " y "]):
            #replace(): La función del método replace() es reemplazar todas las veces que una palabra aparezca en 
            #un string por otra cadena específica. 
            tituloEvento = tituloEvento.replace(",", " ")
            tituloEvento = tituloEvento.replace("y", " ")
        #La instrucción not seguida de una variable en un condicional evalúa si esta es un string o lista vacía.
        if not tituloEvento:
            tituloEvento = "Título no detectado, evento sin nombrar."
        return tituloEvento
    
    def __descripcionEvento(self, preguntaUsuario):
        #Esta expresión regular extrae todas las palabras que se encuentren entre dos conjuntos de palabras clave.
        patronDescripcion = re.findall(r"(descripcion de|descripción de|descripcion|descripción)\s+(.*?)(?:\s+\b(titulo|título|fecha|hora|inicio|inicial|final|fin)\b|$)", preguntaUsuario, re.IGNORECASE|re.UNICODE)
        #Bucle for each de una sola línea para extraer la posición intermedia de la lista de tuplas.
        descripcionLista = [tupla[1] for tupla in patronDescripcion]
        #join(): Este método toma una lista de strings como argumento y los concatena, juntando cada string con el 
        #carácter especificado.
        descripcionEvento = ', '.join(descripcionLista)
        #La siguiente instrucción verifica si el último carácter es una "," o una "y" y si es así lo reemplaza por 
        #un espacio vacío.
        if any(descripcionEvento.endswith(sufijo) for sufijo in [",", "y", ", ", " y "]):
            descripcionEvento = descripcionEvento.replace(",", " ")
            descripcionEvento = descripcionEvento.replace("y", " ")
        #La instrucción not seguida de una variable en un condicional evalúa si esta es un string o lista vacía.
        if not descripcionEvento:
            descripcionEvento = "Evento sin descripción."
        return descripcionEvento
    
    #Para establecer un evento en Google Calendar la fecha y hora se debe proporcionar en formato ISO, lo cual es 
    #logrado a través de la librería datetime.
    def __horaInicioEvento(self, preguntaUsuario):
        preguntaUsuario = preguntaUsuario.lower()   #lower(): Transformar todas las letras a minúsculas.
        instruccionHora = preguntaUsuario.strip()   #lower(): Elimina los caracteres en blanco del string.
        numeroshora = ""
        if (":" in instruccionHora):
            #Esta expresión regular extrae todos los números que se encuentren entre dos puntos y antes de las 
            #palabras am o pm, pero como se utiliza la instrucción ?:, las palabras am o pm no serán guardadas en 
            #una tupla dentro de la lista extraída, sino que solo serán extraídos y separados los números.
            numeroshora = re.findall(r"(\d+):(\d+) (?:am|pm)", instruccionHora, re.IGNORECASE|re.UNICODE)
        else:
            #Expresión regular que checa si el número llegó con un punto (.) en vez de dos (:). 
            numeroshora = re.findall(r"(\d+).(\d+) (?:am|pm)", instruccionHora, re.IGNORECASE|re.UNICODE)
        #join(): Este método toma una listao tupla de strings como argumento y los concatena, juntando cada string 
        #con el carácter especificado.
        hora = ":".join(numeroshora[0])
        #Para que el string que representa la hora pueda ser convertido a un objeto datetime con formato de 12 
        #horas, se debe indicar si la hora de este es pm o am, pero para que esto sea entendido por el método 
        #strptime(), se debe indicar en mayúsculas.
        if("pm" in preguntaUsuario):
            hora += " PM"
        else:
            hora += " AM"
        #datetime.datetime.strptime(): Método de la clase datetime que toma una cadena que representa una fecha y 
        #hora en un formato específico y la convierte a un objeto datetime, para ello recibe las siguientes 
        #instrucciones en su segundo parámetro:
        # - %H: Hora en formato de 24 horas (00-23).
        # - %I: Hora en formato de 12 horas (01-12). Para esto se debe indicar si la hora es AM o PM.
        # - %p: AM o PM (funciona con %I para indicar si el formato de la hora es en la tarde o la mañana).
        # - %M: Minutos (00-59).
        # - %S: Segundos (00-59).
        # - %f: Microsegundos (000000-999999).
        # - %z: Desplazamiento de la zona horaria UTC en formato ±HHMM o ±HH:MM.
        hora = datetime.datetime.strptime(hora, "%I:%M %p") #Se indica "%I" para usar el formato de 12 horas.
        #Conversión de objeto datetime con formato de 12 horas en formato de 24 horas. Esto se hace para que sea 
        #compatible con la hora actual retornada por medio del método datetime.datetime.now().strftime("%H:%M").
        horaAlarma = hora.strftime("%H:%M")
        return horaAlarma
        
    def __fechaInicioEvento(self, preguntaUsuario):
        preguntaUsuario = preguntaUsuario.lower()   #lower(): Transformar todas las letras a minúsculas.
        #El diccionario meses realiza la conversión de la palabra de cada mes en su equivalente numérico.
        meses = {
            'enero': '01',
            'febrero': '02',
            'marzo': '03',
            'abril': '04',
            'mayo': '05',
            'junio': '06',
            'julio': '07',
            'agosto': '08',
            'septiembre': '09',
            'octubre': '10',
            'noviembre': '11',
            'diciembre': '12'
        }
        #Esta expresión regular extrae 3 palabras que se encuentren antes y después de ciertas palabras clave.
        #diccionario.keys(): Los diccionarios se componen de llaves y valores, con el método keys() se obtienen 
        #todos sus valores de llave = {'llave': 'valor'}.
        texto_limpio = re.findall(r'((?:\S+\s+){0,3}(?:' + '|'.join(meses.keys()) + r')(?:\s+\S+){0,3})', preguntaUsuario, flags=re.IGNORECASE | re.UNICODE)
        #Si la lista de tuplas que busca 3 palabras antes y después de los meses del año no está vacía, procedemos 
        #a eliminar las palabras que no tienen nada que ver con una fecha, como lo son ciertas palabras clave, 
        #caracteres especiales y espacios en blanco como espacios, tabuladores o saltos de línea.
        if texto_limpio:
            #re.sub(r): El método sub() se utiliza para realizar sustituciones en una cadena de texto (string) 
            #utilizando expresiones regulares. Este recibe 4 parámetros, la expresión regular que se quiere 
            #encontrar, la cadena o caracter que las sustituirá, el texto donde se buscará el patrón y modificadores 
            #opcionales que se pueden utilizar para personalizar el comportamiento de la búsqueda. 
            #En este caso se buscan palabras clave que estorben al encontrar las fechas del evento.
            texto_limpio = re.sub(r'\b(inicio|inicial|titulo|título|tituladas|titulados|fecha|hora|descripcion|descripción|final|fin|como|las|de|del|el|y|a)\b', '', texto_limpio[0].lower(), flags=re.IGNORECASE|re.UNICODE)
            #En este caso se buscan los caracteres especiales que no sean letras o números como !, ?, ., etc.
            texto_limpio = re.sub(r'[^\w\s]', '', texto_limpio)
            #En este caso se buscan espacios en blanco como tabuladores, espacios o saltos de línea.
            texto_limpio = re.sub(r'\s+', ' ', texto_limpio).strip()
            #split(): Método que sirve para separar las palabras en un string en función de todas las veces que 
            #aparezca un caracter en específico.
            componentes = texto_limpio.split(" ")
            mes = componentes[1].lower()            #lower(): Transformar todas las letras a minúsculas.
            #Si el año del evento es None o menor al actual, probablemente se haya captado de forma errónea o no 
            #haya sido proporcionado por el usuario, cuando esto ocurra, por default se indicará que el año es el 
            #actual.
            #datetime.datetime.now().strftime(): Método que devuelve la  fecha y hora actual en el formato 
            #YYYY-MM-DD HH:MM:SS, al cual se accede con el string "%Y-%m-%d %H:%M:%S".
            currentYear = datetime.datetime.now().strftime("%Y")
            if((componentes[2] == None) or (int(componentes[2]) < int(currentYear))):
                componentes[2] = currentYear
                #Reemplaza el contenido de la variable texto_limpio con el nuevo año de la variable componentes.
                texto_limpio = ' '.join(componentes)
            #La variable mes_numerico es donde se almacena temporalmente el valor numérico correspondiente al texto 
            #del mes recibido en la instrucción del usuario, para que después a través del método replace() sea 
            #remplazado y así se pueda convertir dicha fecha a un objeto tipo datetime.
            mes_numerico = meses[mes]
            texto_limpio = texto_limpio.replace(mes, mes_numerico)
            #datetime.datetime.strptime(): Método de la clase datetime que toma una cadena que representa una fecha 
            #y hora en un formato específico y la convierte a un objeto datetime, para ello recibe las siguientes 
            #instrucciones en su segundo parámetro:
            # - %d: Día de la fecha.
            # - %m: Mes de la fecha.
            # - %Y: Año de la fecha.
            # - %z: Desplazamiento de la zona horaria UTC en formato ±HHMM o ±HH:MM.
            #La fecha recibida usualmente indica primero el día, luego el mes y finalmente el año. 
            fecha_objeto = datetime.datetime.strptime(texto_limpio, "%d %m %Y")
            return fecha_objeto
        #Si la fecha no fue recibida en forma de texto, sino de forma numérica, se ejecuta la gestión de errores.
        #MANEJO DE EXCEPCIONES: Es una parte de código que se conforma de dos partes, try y except: 
        # - Primero se ejecuta el código que haya dentro del try y si es que llegara a ocurrir una excepción durante 
        #   su ejecución, el programa brinca al código del except.
        # - En la parte de código donde se encuentra la palabra reservada except, se ejecuta cierta acción cuando 
        #   ocurra el error esperado. 
        #Se utiliza esta arquitectura de código cuando se quiera efectuar una acción donde se espera que pueda 
        #ocurrir un error durante su ejecución.
        try:
            print("La fecha fue proporcionada en forma de número.")
            #Esta expresión regular extrae todos los números que se encuentren entre diagonales (/).
            texto_limpio = re.findall(r"(\d+)/(\d+)/(\d+)", preguntaUsuario, flags=re.IGNORECASE | re.UNICODE)
            #La instrucción not seguida de una variable en un condicional evalúa si esta es un string o lista vacía.
            #Si no se ha podido extraer nada a través de la expresión regular que obtiene la fecha en formato 
            #numérico, se crea una excepción propia llamada fechaFormatoDesconocido, la cual mostrará un mensaje en 
            #consola y le hará saber al usuario que no pudo entender la fecha que dijo en su instrucción y que por 
            #favor la debe repetir de otra forma.
            if not texto_limpio:
                raise fechaFormatoDesconocido("Lo siento, no pude reconocer el formato de la fecha de tu evento.")
            #Reemplaza el contenido de la variable texto_limpio con la nueva fecha en formato numérico.
            texto_limpio = ' '.join(texto_limpio[0])
            #datetime.datetime.strptime(): Método que convierte un string en cierto formato a un objeto datetime.
            fecha_objeto = datetime.datetime.strptime(texto_limpio, "%d %m %Y")
            return fecha_objeto
        #La excepción propia fechaFormatoDesconocido se lanza cuando el programa no puede reconocer la fecha dicha 
        #indicada por el usuario, esta se declara como una clase dentro de este mismo programa. 
        except fechaFormatoDesconocido:
            fecha_objeto = "Lo siento, no pude reconocer la fecha de tu evento, repitemela de otra forma por favor."
            return fecha_objeto
    
    #La hora y fecha inicial del evento se obtiene de forma separada por simplicidad y para mejorar su detección, 
    #pero para que esto pueda ser utilizado con la API de Google Calendar se debe mandar todo junto en una misma 
    #variable y en formato ISO, por dicha razón en esta función se utilizan los métodos declarados anteriormente 
    #para así juntar ambos datos y meterlos en una misma variable.
    def __fechaHoraInicioEvento(self, preguntaUsuario):
        #__horaInicioEvento(): Función propia con modificador de acceso privado que se encarga de obtener la hora 
        #inicial del evento en formato de 12 horas.
        horaInicialEvento = self.__horaInicioEvento(preguntaUsuario)
        #__fechaInicioEvento(): Función propia con modificador de acceso privado que se encarga de obtener la fecha 
        #inicial del evento, no importando si esta viene indicada en forma de texto o en formato numérico.
        fechaEvento = self.__fechaInicioEvento(preguntaUsuario)
        try:
            #datetime.datetime.strptime(): Método que convierte un string en cierto formato a un objeto datetime.
            horaInicialEventoDate = datetime.datetime.strptime(horaInicialEvento, "%H:%M")
            #datetime.replace(): Cuando el método replace() se aplica a un objeto datetime, se puede utilizar para 
            #cambiar la hora, minuto, segundo, etc. de su fecha.
            fechaHora_Inicial = fechaEvento.replace(hour = horaInicialEventoDate.hour, minute = horaInicialEventoDate.minute)
            #dattime.isoformat(): El método isoformat() convierte el formato del objeto datetime a ISO.
            fechaHoraInicial_ISO = fechaHora_Inicial.isoformat()
            return fechaHoraInicial_ISO
        #Si no se pudo identificar el formato de la fecha se lanza la excepción TypeError y se proporciona un 
        #mensaje al usuario.
        except TypeError:
            fechaHoraInicial_ISO = "Lo siento, no pude reconocer la fecha y hora de tu evento, repitemela de otra forma por favor."
            return fechaHoraInicial_ISO
    
    #Una vez que se ha recabado la fecha y hora inicial del evento se analiza si existe alguna otra hora dentro de 
    #la instrucción que se encuentre después de ciertas palabras clave y antes de las palabras am o pm, para que 
    #así se considere la fecha de término del evento dada por el usuario, pero si esta hora no fue dada, por 
    #defecto se declarará que la hora de término sea 1 hora después, ya que la API de Google Calendar lo requiere.
    def __fechaHoraFinalEvento(self, preguntaUsuario):
        preguntaUsuario = preguntaUsuario.lower()   #lower(): Transformar todas las letras a minúsculas.
        instruccionHora = preguntaUsuario.strip()   #lower(): Elimina los caracteres en blanco del string.
        #Esta expresión regular extrae todos los números que se encuentren entre ciertas palabras clave y las 
        #palabras am o pm, pero como se utiliza la instrucción ?:, las palabras am o pm no serán guardadas en una 
        #tupla dentro de la lista extraída ni tampoco las palabras clave, solo serán extraídos y separados los 
        #números.
        fechaHoraFinal = re.findall(r"\b(?:a|termine|hasta\s+las?)\s+(\d+):(\d+) (?:am|pm)?\b", instruccionHora, re.IGNORECASE|re.UNICODE)
        #Condicional que se ejecuta si la hora de finalización del evento fue devuelta por la expresión regular.
        if fechaHoraFinal:
            #join(): Este método toma una listao tupla de strings como argumento y los concatena, juntando cada 
            #string con el carácter especificado.
            horaFinalEvento = ":".join(fechaHoraFinal[0])
            #Para que el string que representa la hora pueda ser convertido a un objeto datetime con formato de 12 
            #horas, se debe indicar si la hora de este es pm o am, pero para que esto sea entendido por el método 
            #strptime(), se debe indicar en mayúsculas.
            if("pm" in preguntaUsuario):
                horaFinalEvento += " PM"
            else:
                horaFinalEvento += " AM"
            #datetime.datetime.strptime(): Método de la clase datetime que toma una cadena que representa una fecha 
            #y hora en un formato específico y la convierte a un objeto datetime, para ello recibe las siguientes 
            #instrucciones en su segundo parámetro:
            # - %H: Hora en formato de 24 horas (00-23).
            # - %I: Hora en formato de 12 horas (01-12). Para esto se debe indicar si la hora es AM o PM.
            # - %p: AM o PM (funciona con %I para indicar si el formato de la hora es en la tarde o la mañana).
            # - %M: Minutos (00-59).
            # - %S: Segundos (00-59).
            # - %f: Microsegundos (000000-999999).
            # - %z: Desplazamiento de la zona horaria UTC en formato ±HHMM o ±HH:MM.
            horaFinalEvento = datetime.datetime.strptime(horaFinalEvento, "%I:%M %p") #Hora en formato de 12 horas.
            #Conversión de objeto datetime con formato de 12 horas en formato de 24 horas. Esto se hace para que sea 
            #compatible con la hora actual retornada por medio del método datetime.datetime.now().strftime("%H:%M").
            horaFinalEvento = horaFinalEvento.strftime("%H:%M")
            #Una vez extraída la hora de finalización, se declara la fecha de finalización, que será la misma a la 
            #inicial.
            fechaEvento = self.__fechaInicioEvento(preguntaUsuario)
        #Después se intentará cambiar el formato de la hora final e incluirla con la fecha final.
        try:
            horaFinalEventoDate = datetime.datetime.strptime(horaFinalEvento, "%H:%M")
            fechaHora_Final = fechaEvento.replace(hour = horaFinalEventoDate.hour, minute = horaFinalEventoDate.minute)
            fechaHoraFinal_ISO = fechaHora_Final.isoformat()
            return fechaHoraFinal_ISO
        #Pero si no se logra realizar esta conversión es porque la fecha final no fue dada por el usuario, por lo 
        #cual se establecerá por default 1 hora después de la dada por la fecha y hora inicial. 
        except UnboundLocalError:
            print("No existe una hora final del evento, pero por default se establecerá 1 hora después.")
            horaInicialEvento = self.__horaInicioEvento(preguntaUsuario)
            fechaEvento = self.__fechaInicioEvento(preguntaUsuario)
            try:
                horaInicialEventoDate = datetime.datetime.strptime(horaInicialEvento, "%H:%M")
                #datetime.timedelta(): Método que se utiliza para representar una duración o un intervalo de tiempo 
                #transcurrido, el cual mayormente es usado para realizar operaciones matemáticas con fechas y horas, 
                #como sumar o restar intervalos de tiempo a objetos datetime.
                horaFinalEventoDate = horaInicialEventoDate + datetime.timedelta(hours = 1)
                fechaHora_Final = fechaEvento.replace(hour = horaFinalEventoDate.hour, minute = horaFinalEventoDate.minute)
                fechaHoraFinal_ISO = fechaHora_Final.isoformat()
                return fechaHoraFinal_ISO
            #Si no se reconoce la hora aún así, se maneja la excepción TypeError lanzada por el error.
            except TypeError:
                print("La fecha fue proporcionada en un formato desconocido.")
                fechaHoraFinal_ISO = "Lo siento, no pude reconocer la fecha y hora de tu evento, repitemela de otra forma por favor."
                return fechaHoraFinal_ISO

    #Para definir un evento de Google Calendar el key start y end del diccionario body perteneciente al método 
    #events().create().insert() necesita recibir la fecha y hora en formato ISO, el cual es extraído a través de 
    #la librería datetime.
    def crearEvento(self, preguntaUsuario):
        respuestaEventoCalendario = ""
        try:
            tituloEvento = self.__tituloEvento(preguntaUsuario)
            time.sleep(0.5)
            descripcionEvento = self.__descripcionEvento(preguntaUsuario)
            time.sleep(0.5)
            horaFechaInicioEvento = self.__fechaHoraInicioEvento(preguntaUsuario)
            time.sleep(0.5)
            horaFechaFinalEvento = self.__fechaHoraFinalEvento(preguntaUsuario)
            time.sleep(0.5)
            #servicioAPIGoogleCalendar(): Función propia de la clase googleCalendar_auth que sirve para extablecer una 
            #conexión con la API de Google Calendar.
            calendar_service = self.servicioAPI
            #Con la variable que utilizó el método servicioAPIGoogleCalendar() se ejecuta el método events().insert() 
            #que recibe dos parámetros, el primero calendarId indica a qué calendario nos estamos refiriendo ya que 
            #pueden existir varios dentro de Google Calendar, aunque casi siempre se utiliza el principal, denotado por
            #el valor de primary, en el segundo parámetro llamado body se indican las características del evento como 
            #su título, descripción, fecha y hora de inicio, zona horaria y fecha y hora de finalización. 
            eventoGoogleCalendar = calendar_service.events().insert(
                calendarId = "primary",
                body = {
                    "summary": tituloEvento,
                    "description": descripcionEvento,
                    #timeZone: La zona horaria de cada locación se obtiene del siguiente enlace al buscar tz database 
                    #names: https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
                    "start": {"dateTime": horaFechaInicioEvento, "timeZone": "America/Mexico_City"},
                    "end": {"dateTime": horaFechaFinalEvento, "timeZone": "America/Mexico_City"},
                }
            ).execute()
            #Impresión en consola del resultado del evento agendado.
            print("Evento creado con éxito!!")
            print("Título:\t\t\t"           + str(eventoGoogleCalendar["summary"]))
            print("Descripción:\t\t"          + str(eventoGoogleCalendar["description"]))
            print("Fecha y Hora de Inicio:\t"   + str(eventoGoogleCalendar["start"]))
            print("Fecha y Hora de Fin:\t"      + str(eventoGoogleCalendar["end"]))
            locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
            horaFechaInicioEvento = datetime.datetime.fromisoformat(horaFechaInicioEvento)
            horaFechaFinalEvento = datetime.datetime.fromisoformat(horaFechaFinalEvento)
            fechaFormateadaInicio = horaFechaInicioEvento.strftime("%d de %B de %Y")
            fechaFormateadaFinal = horaFechaFinalEvento.strftime("%d de %B de %Y")
            respuestaEventoCalendario = f"""Evento creado con éxito!! con título de: {tituloEvento}, su descripción es: 
                                        {descripcionEvento}, su hora y fecha de inicio es el {fechaFormateadaInicio} y 
                                        finaliza el {fechaFormateadaFinal}."""
            respuestaEventoCalendario = re.sub(r'\s+', ' ', respuestaEventoCalendario).strip()
            #webbrowser.open(): Método que abre un navegador web en la dirección URL especificada.
            webbrowser.open("https://calendar.google.com/")
        except:
            respuestaEventoCalendario = """Lo siento, no entendí bien las características del evento que quieres agendar, 
                                        recuerda que para crear un evento en Google Calendar debes indicar su título, 
                                        descripción, fecha y hora de inicio y fecha y hora de finalización."""
            respuestaEventoCalendario = re.sub(r'\s+', ' ', respuestaEventoCalendario).strip()
        return respuestaEventoCalendario

#Creación de una excepción propia que sea lanzada cuando el formato de la fecha dada hacia el calendario se 
#proporcione en forma numérica.
class fechaFormatoDesconocido(Exception):
    def __init__(self, mensaje):
        super().__init__(mensaje)