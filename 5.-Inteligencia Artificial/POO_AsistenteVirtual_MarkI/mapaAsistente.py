import requests #requests: Biblioteca que sirve para realizar solicitudes HTTP de manera sencilla y eficiente.
import urllib   #urllib: Librería que proporciona herramientas para trabajar con URLs y realizar solicitudes HTTP.
from PIL import Image   #PIL: La librería Pillow sirve para mostrar una imagen con python extraída de una URL.
import io       #io: Librería que permite la manipulación de los archivos y carpetas de nuestro ordenador.
import re       #re: Librería que permite utilizar expresiones regulares para detectar patrones.

class widgetDireccionesMapa:
    #CONSTRUCTOR O INICIALIZADOR DE LA CLASE: En él se declaran los parámetros que recibe la clase, que además se 
    #utilizarán en los demás métodos, estos a fuerza deben tener un valor.
    #self: La instrucción self se utiliza para hacer referencia al objeto que se está manipulando cuando se instancía 
    #la clase. Por eso es que a través de la misma nomenclatura de un punto se accede a los distintos atributos y/o 
    #métodos con un objeto desde fuera de la clase.
    def __init__(self, parametro_de_la_clase):
        #ChatGPT API key
        self.MapQuestApiKey = parametro_de_la_clase

    def direccionesMapa(self, peticionDireccion):
        respuestaMapa = ""
        punto_inicial = ""
        punto_final = ""
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
        patronDirecciones = re.findall(r"\b(desde|entre|para|inicio|a|de|ir)\b\s+(.*?)\s+\b(a|y|hasta|final)\b\s+(.*?)$", peticionDireccion, re.IGNORECASE|re.UNICODE)
        
        #Al utilizar el método re.findall() se retorna una lista de tuplas de todas las ocurrencias que encuentre, 
        #para recorrer estos y filtrarlos se usa el método propio filtroTexto(), que será declarado posteriormente 
        #y se encargará de eliminar palabras clave que estorben al obtener el punto de inicio y final al buscar 
        #los puntos iniciales y finales de la ruta.
        if patronDirecciones:
            for coincidencia in patronDirecciones:
                #strip(): Método utilizado para eliminar los caracteres especificados en una cadena, como espacios 
                #saltos de línea (\n), tabuladores (\t), etc. Si no se le pasa ningún parámetro, eliminará los 
                #espacios del string.
                punto_inicial = self.__filtroTexto(coincidencia[1].strip())
                punto_final = self.__filtroTexto(coincidencia[3].strip())
        else:
            print("No se encontró un patrón de inicio y destino en la solicitud.")
        
        print("Punto Inicial: " + punto_inicial)
        print("Punto Final: " + punto_final + "\n")

        #El endpoint de una API se refiere a una URL específica a través de la cual se pueden realizar peticiones, en 
        #el caso de la API MapQuest, esta se obtiene al ingresar a la opción de Documentation -> APIs -> Directions 
        #API -> Route -> GET -> Route -> Resource URL y al final de esa URL agregar un signo de interrogación. Este 
        #endpoint sirve para obtener la distancia entre dos puntos, el tiempo del recorrido en auto, consumo de 
        #combustible, las indicaciones para llegar desde un punto al otro, etc.
        MapQuestEndpoint = "https://www.mapquestapi.com/directions/v2/route?"
        #urllib.parse.urlencode(): Método que convierte un objeto de diccionario o una secuencia de tuplas de dos 
        #elementos en una cadena de consulta URL, para ello anteriormente se tuvo que haber declarado la URL a la que 
        #se realizará la consulta y al final haber puesto un signo de interrogación.
        peticionAPI = MapQuestEndpoint + urllib.parse.urlencode({
            "key": self.MapQuestApiKey,
            "from": punto_inicial,
            "to": punto_final
        })
        print("La consulta realizada a la herramienta MapQuest Developer para obtener los datos de la ruta fue:\n" + peticionAPI)
        #requests.get(endpoint).json(): A través de la librería request se puede usar cualquier método HTTP, en este 
        #caso se utiliza el método get que devuelve la respuesta retornada por una API en una endpoint específica, 
        #una vez que se recibe la respuesta del servidor, se utiliza el método .json() para interpretar la respuesta 
        #como dato tipo JSON o en forma de diccionario, que es su equivalente pero en Python. 
        respuestaAPI = requests.get(peticionAPI).json()
        #En el JSON de la respuesta de la API si su key statuscode tiene un value de 0, esto significa que se han 
        #recibido correctamente sus datos.
        if (respuestaAPI["info"]["statuscode"] == 0):
            print("Respuesta recibida correctamente de la API de MapQuest.")
            respuestaMapa += " la información de la ruta que va desde " + punto_inicial + " hasta " + punto_final + " es la siguiente... "
            duracionRuta = respuestaAPI["route"]["formattedTime"]       #Tiempo del recorrido.
            respuestaMapa += "La duración del viaje es de " + duracionRuta + " aproximadamente y "
            distanciaRuta = respuestaAPI["route"]["distance"] * 1.60934 #La distancia en millas se convierte a km.
            #"{:.2f}".format(): Con esta instrucción se indica que un número decimal solo muestre dos decimales.
            respuestaMapa += "La distancia recorrida en auto durante el viaje es de " + str("{:.2f}".format(distanciaRuta)) + " kilometros. "
        else:
            print("Respuesta recibida erróneamente de la API de MapQuest.")
            respuestaMapa += "Lo siento di0, no pude procesar bien la ruta, podrías repetirmela por favor? "
        
        #El endpoint de una API se refiere a una URL específica a través de la cual se pueden realizar distintas 
        #peticiones, en este caso se utiliza para obtener el mapa que muestra la ruta entre dos puntos, para ello 
        #ingresaremos a la opción de Documentation -> APIs -> Static Map API -> GET -> Map -> Resource URL -> Adding 
        #a Route to the Map y al final de esa URL agregar de nuevo un signo de interrogación.
        MapQuestMapEndpoint = "https://www.mapquestapi.com/staticmap/v5/map?"
        #urllib.parse.urlencode(): Método que convierte un objeto de diccionario o una secuencia de tuplas de dos 
        #elementos en una cadena de consulta URL, para ello anteriormente se tuvo que haber declarado la URL a la que 
        #se realizará la consulta y al final haber puesto un signo de interrogación.
        peticionMapaAPI = MapQuestMapEndpoint + urllib.parse.urlencode({
            "key": self.MapQuestApiKey,
            "start": punto_inicial,
            "end": punto_final,
            "size": "700,700"
        })
        print("La consulta realizada a la herramienta MapQuest Developer para obtener el mapa de la ruta fue:\n" + peticionMapaAPI + "\n")
        respuestaMapa += "He desplegado una imagen con el mapa de la ruta, en esta el círculo verde marca el punto de inicio y el rojo el final."
        print("Hola di_cer0." + respuestaMapa + "\n")
        #requests.get(endpoint): A través de la librería request se puede usar cualquier método HTTP, en este caso se 
        #utiliza el método get, que devuelve la respuesta retornada por una API en una endpoint específica.
        imagenMapaAPI = requests.get(peticionMapaAPI)
        #io.BytesIO(): Método que sirve para crear un flujo de bytes en memoria que puede utilizarse para almacenar 
        #datos binarios, como imágenes, audio y video. Este se almacena en un archivo temporal perteneciente a la 
        #carpeta %temp% = C:\Users\diego\AppData\Local\Temp.
        imagen_bytes = io.BytesIO(imagenMapaAPI.content)
        #PIL.Image.open(): Método que se utiliza para abrir una imagen desde un archivo local o desde una fuente de 
        #datos en memoria, como bytes. Después se aplica el método show() para abrir dicha imagen.
        Image.open(imagen_bytes).show()
        return respuestaMapa
    
    
    def __filtroTexto(self, texto):
        #re.sub(r): El método sub() se utiliza para realizar sustituciones en una cadena de texto (string) utilizando 
        #expresiones regulares. Este recibe 4 parámetros, la expresión regular que se quiere encontrar, la cadena o 
        #caracter que las sustituirá, el texto original donde se buscará el patrón y modificadores opcionales que se 
        #pueden utilizar para personalizar el comportamiento de la búsqueda. 
        #En este caso se buscan palabras clave que estorben al encontrar las direcciones de inicio y final dadas al 
        #asistente virtual.
        texto_limpio = re.sub(r'\b(desde|entre|llegar|muestrame|distancia|muéstrame|mismo|para|inicio|ruta|rapida|rápida|lenta|cual|cuál|mas|más|una|de|ir|es|la|a)\b', '', texto, flags=re.IGNORECASE|re.UNICODE)
        #Posteriormente se eliminan todos los caracteres especiales que no sean letras, números o espacios.
        texto_limpio = re.sub(r'[^\w\s]', '', texto_limpio)
        return texto_limpio