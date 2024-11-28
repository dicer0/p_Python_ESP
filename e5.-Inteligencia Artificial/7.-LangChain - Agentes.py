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
#IMPORTACIÓN DE LLAVE: Cuando se quiera utilizar una API que utiliza un key, por seguridad es de buenas prácticas 
#declararla en un archivo externo, además cabe mencionar que el nombre de dicho archivo y constante no pueden empezar 
#con un número, sino cuando la quiera importar obtendré un error y se va accediendo a sus carpetas por medio de puntos:
# - Directorio normal:      carpeta1/carpeta2/carpeta3
# - Directorio paquetes:    carpeta1.carpeta2.carpeta3
#La parte del directorio se coloca después de la palabra reservada import y posteriormente se manda a llamar sus 
#variables o constantes de igual manera a través de un punto.
import API_Keys.Llaves_ChatGPT_Bard_etc
#ChatGPT API key
ApiKey = API_Keys.Llaves_ChatGPT_Bard_etc.LlaveChatGPT 





#1.-MODELOS (Models): El modelo se refiere a la red neuronal que se va a utilizar para procesar el texto de entrada y 
#generar una respuesta, los Large Language Model (LLM) responden preguntas sin guardar un historial, mientras que los 
#Chats si guardan las preguntas y respuestas realizadas para crear una conversación. Existen varios modelos dentro de 
#una misma compañía, por ejemplo, OpenAI cuenta con gpt3, gpt4, gpt3.5 turbo, etc.
print("\n\n-----------------------------------------------1.-MODELOS-----------------------------------------------")
#OpenAI: Clase de la librería langchain que permite utilizar el LLM (Large Language Model) de OpenAI con Python, este
#puede resolver tareas sencillas, pero no se le proporciona roles y no guarda un historial de conversación.
from langchain.llms import OpenAI               #OpenAI: Modelo LLM.
#Cabe mencionar que, al utilizar la API en su modo gratuito, solo se podrán realizar 100 llamadas a la API por día, 
#si se excede ese límite, se recibirá el error RateLimitError al intentar ejecutar el programa de Python, pero si se 
#compra el servicio de la API, se cobrará a través de Tokens, que representan pedazos de palabras; como máximo se 
#pueden recibir o mandar a la vez 4096 tokens, que aproximadamente son 3,072 palabras.
#OpenAI(): En el constructor de la clase OpenAI perteneciente al paquete llms de la librería langchain se indica: 
# - model_name: Parámetro que indica el modelo que se quiere utilizar, en este caso se utilizará text-davinci-003 que 
#   pertenece a GPT-3.5.
# - openai_api_key: Con este parámetro se proporciona la API key, que por buenas prácticas debe provenir de otro 
#   archivo.
# - prompt_length: La longitud del prompt.
# - max_tokens: El número máximo de tokens que se pueden generar.
# - stop_token: El token de parada.
# - temperature: La temperatura es un valor entre 0 y 1 que indica la creatividad con la que contesta el LLM, si es 
#   demasiado grande, puede responder con algo totalmente aleatorio y si es muy bajo responderá lo mismo siempre, 
#   función que podría ser deseada cuando por ejemplo se contestan problemas matemáticos.
#Todos los modelos disponibles para usarse con OpenAI estan enlistados en el siguiente enlace y cada uno es mejor 
#en ciertas funciones que el otro:
#https://platform.openai.com/docs/models
openaiLLM = OpenAI(model_name = "text-davinci-003", openai_api_key = ApiKey, temperature = 0)           #LLM.

#ChatOpenAI: Clase de la librería langchain que permite utilizar el modelo de chat (ChatGPT) de OpenAI con Python, este
#puede contestar preguntas adoptando un rol y guardar un historial durante la conversación.
from langchain.chat_models import ChatOpenAI    #ChatOpenAI: Modelo de Chat.
#ChatOpenAI(): En el constructor de la clase ChatOpenAI del paquete chat_models de la librería langchain se indica: 
# - model_name: Parámetro que indica el modelo que se quiere utilizar, en este caso se utilizará gpt-3.5-turbo que 
#   pertenece a GPT-3.5.
# - openai_api_key: Con este parámetro se proporciona la API key, que por buenas prácticas debe provenir de otro 
#   archivo.
# - prompt_length: Longitud del prompt.
# - max_tokens: Número máximo de tokens que se pueden generar.
# - stop_token: El token de parada.
# - temperature: La temperatura es un valor entre 0 y 1 que indica la creatividad con la que contesta el LLM, si es 
#   demasiado grande, puede responder con algo totalmente aleatorio y si es muy bajo responderá lo mismo siempre, 
#   función que podría ser deseada cuando por ejemplo se contestan problemas matemáticos.
#Todos los modelos disponibles para usarse con OpenAI estan enlistados en el siguiente enlace y cada uno es mejor 
#en ciertas funciones que el otro:
#https://platform.openai.com/docs/models
openaiChatGPT = ChatOpenAI(model_name = "gpt-3.5-turbo", openai_api_key = ApiKey, temperature = 0)    #Chat.





#6.-AGENTES (Agents): Estos son modelos o cadenas a los cuales se les da acceso a una fuente o API para que puedan 
#realizar alguna acción o proporcionar una respuesta que solucione una tarea en específico.
print("\n-----------------------------------------------6.-AGENTES-----------------------------------------------")
#   - load_tools: Con este método perteneciente al paquete agents de la clase langchain se permite ingresar al 
#     programa la herramienta que se busca integrar al agente a través de su nombre, que puede servir para darle la 
#     habilidad de ejecutar comandos en consola, realizar búsquedas en internet, resolver o contestar preguntas acerca 
#     de operaciones matemáticas, obtener información meteorológica, de noticias, películas y/o crear una herramienta 
#     personalizada utilizando alguna otra API.
#      - Ejecutar comandos en consola:
#           - terminal: Herramienta que permite ejecutar comandos en consola.
#           - python_repl: Esta herramienta permite ejecutar solamente scripts (programas) de Python a través de la 
#             consola del sistema.
#      - Realizar búsquedas en internet:
#           - serpapi: Tool que permite extraer información de internet para responder una realizada por el usuario.
#           - google-search: Esta herramienta de langchain permite utilizar específicamente el buscador de Google para 
#             obtener la información que responde una pregunta realizada al agente.
#           - requests: Esta herramienta permite extraer información de la URL de un sitio web en específico para 
#             responder una pregunta.
#      - Resolver o contestar preguntas acerca de operaciones matemáticas: Cuando se usen estas tools es recomendable 
#        declarar que la temperatura del modelo sea de 0, para que siempre dé el mismo resultado. 
#           - wolfram-alpha: Esta herramienta permite resolver problemas o contestar preguntas que tengan que ver con 
#             matemáticas, ciencia, tecnología, etc.
#           - pal-math: Esta herramienta permite resolver problemas matemáticos a través de una instrucción, como 
#             crear ecuaciones a través de un problema de la vida real y cosas por el estilo.
#           - llm-math: Esta herramienta permite resolver problemas matemáticos.
#      - Obtener información meteorológica:
#           - open-meteo-api: Permite obtener información meteorológica a través de la herramienta OpenMeteo.
#      - Obtener información de noticias recientes o películas:
#           - news-api: Obtiene información acerca de noticias actuales.
#           - tmdb-api: Obtiene información acerca de películas.
#   - initialize_agent: Con esta función perteneciente al paquete agents de la clase langchain se indica el tipo de 
#     agente que se pretende crear. 
from langchain.agents import load_tools         #load_tools: Método que permite anexar una Tool a un agente.
#   - initialize_agent: Con este método perteneciente al paquete agents de la clase langchain se permite ingresar al 
#     programa el tipo de agente que se busca utilizar a través de su nombre. El mejor tipo de agente a elegir 
#     dependerá de las necesidades específicas del proyecto:
#       - Los agentes zero-shot-react-description y conversational-react-description son buenos al realizar tareas 
#         generales, el primero utilizando un modelo LLM y el segundo un modelo de Chat. 
#       - El agente react-docstore es mejor utilizarlo para interactuar con un almacén de documentos.
#       - El agente self-ask-with-search es una buena opción para realizar búsquedas en la web.
from langchain.agents import initialize_agent   #initialize_agent: Método que indica el tipo de agente que se creará.
#IMPORTACIÓN DE LIBRERÍAS:
#IMPORTACIÓN DE LLAVE: Cuando se quiera utilizar una API que utiliza un key, por seguridad es de buenas prácticas 
#declararla en un archivo externo, además cabe mencionar que el nombre de dicho archivo y constante no pueden empezar 
#con un número, sino cuando la quiera importar obtendré un error y se va accediendo a sus carpetas por medio de puntos:
# - Directorio normal:      carpeta1/carpeta2/carpeta3
# - Directorio paquetes:    carpeta1.carpeta2.carpeta3
#La parte del directorio se coloca después de la palabra reservada import y posteriormente se manda a llamar sus 
#variables o constantes de igual manera a través de un punto.
import os #os: Librería que permite acceder a funciones y métodos relacionados con el sistema operativo.
import API_Keys.Llaves_ChatGPT_Bard_etc
#SerpAPI API key
SerpApiKey = API_Keys.Llaves_ChatGPT_Bard_etc.LlaveSerpAPI
#os.environ: El método environ proveniente de la librería os permite acceder a las variables de entorno del sistema 
#operativo, estas están organizadas en una forma de key:value, por lo que serán datos tipo diccionario o JSON, y su 
#objetivo es proveer cierta información de configuración que afecte a múltiples programas o aplicaciones, evitando 
#así que cada uno deba ser configurado por separado, pudiendo adaptarse automáticamente a diferentes entornos al leer 
#las variables de entorno relevantes, que usualmente almacenan información sensible, como contraseñas o API keys.
#Para crear una nueva variable de entorno se utiliza la siguiente sintaxis, indicando su nombre en mayúsculas:
#   os.environ['NOMBRE_VARIABLE'] = 'valorVariableDeEntorno'
os.environ["SERPAPI_API_KEY"] = SerpApiKey
#load_tools(): Método que sirve para cargar al programa las herramientas que se quiera integrar a un agente. El 
#resultado se entrega en forma de diccionario y será recibido como parámetro del método initialize_agent(), además se 
#debe indicar que modelo está utilizando, ya sea LLM o de Chat, dependiendo del tipo de agente al que se integre.
# - tool_names: A través de una lista se declaran los nombres de las tools que se quiera integrar al agente.
# - llm: Indica el modelo de lenguaje o chat a utilizar.
nombreHerramientas = ["serpapi", "llm-math", "wikipedia", "terminal"]
herramientasAgente = load_tools(tool_names = nombreHerramientas, llm = openaiLLM)
print("Las herramientas que se utilizaron son:\n", str(herramientasAgente), "\n")
print("Sus nombres y lo que hacen respectivamente es:\n",   str(herramientasAgente[0].name), ":\t", 
                                                            str(herramientasAgente[0].description), "\n\n",
                                                            str(herramientasAgente[1].name), ":\t",
                                                            str(herramientasAgente[1].description), "\n\n",
                                                            str(herramientasAgente[2].name), ":\t",
                                                            str(herramientasAgente[2].description), "\n\n", 
                                                            str(herramientasAgente[3].name), ":\t",
                                                            str(herramientasAgente[3].description), "\n")
#initialize_agent(): Método que sirve para anexar a un agente las herramientas previamente cargadas al programa con el 
#método load_tools(), además en este se indica el LLM que se quiere utilizar y el tipo de agente que se pretende crear.
# - tools: Indica el diccionario que contiene el nombre de las herramientas que se quiere enlazar al agente.
# - llm: Indica el modelo de lenguaje o chat a utilizar.
# - agent: En este parámetro se indica el nombre del tipo de agente.
# - max_iterations: Este parámetro indica el máximo número de pensamientos (thoughts) que puede realizar el agente al 
#   responder una pregunta, esto es bueno declararlo porque así se evita que el agente se quede atorado en un bucle 
#   infinito buscando entre sus herramientas para contestar una pregunta que no puede responder.
# - verbose: Variable booleana que controla la información impresa en consola. Cuando verbose es True, el objeto 
#   agente imprimirá información sobre el proceso de generación de la conversación, incluyendo el prompt, la 
#   herramienta que está utilizando para resolver cada parte del prompt, la respuesta dada por cada herramienta y 
#   la respuesta final del agente.
Agente = initialize_agent(tools = herramientasAgente, llm = openaiLLM,
                          agent = "zero-shot-react-description",
                          max_iterations = 3,
                          verbose = True)
#initialize_agent().run(): El método run() proporciona el valor de entrada del agente y luego lo ejecuta para que 
#podamos ver su resultado.
resultadoAgente = Agente.run("Quien es más viejo, el presidente actual de USA o Robert Downey Jr? Toma la edad más grande y saca su raíz cuadrada.")
print("Respuesta de Agente de tipo Zero Shot enlazado con la herramienta serpapi: ", str(resultadoAgente), "\n\n\n")
resultadoAgente = Agente.run("En cual carpeta de mi ordenador se encuentra el archivo 17.-Vibracion en Estructuras.mph?")
print("Respuesta de Agente de tipo Zero Shot enlazado con la herramienta serpapi: ", str(resultadoAgente), "\n\n\n")

#UTILIZAR HERRAMIENTAS PERSONALIZADAS:
#   - BaseTool: A través de una clase propia que herede de la clase Tool que pertenece al paquete tools de la librería 
#     langchain se permite crear herramientas personalizadas, que pueden servir para darle al agente la habilidad de 
#     ejecutar alguna acción en específico.
from langchain.tools import BaseTool            #BaseTool: Clase que permite crear herramientas personalizadas.
import math                                     #math: Librería que permite usar constantes o funciones matemáticas.
import random                                   #random: Librería que permite crear números aleatorios.
#BaseTool: La clase que herede de la clase BaseTool debe declarar los atributos name y description, además de indicar
#a través de su método _run() la acción específica que se realiza cuando el agente utilice la clase: 
# - name: En este atributo se declara el nombre de la herramienta personalizada.
# - description: Este atribito es muy importante, ya que a través de él se le indicará al agente cuando es que debe 
#   utilizar esta herramienta.
# - _run(): Este método es el que se va a ejecutar cuando el agente utilice esta herramienta. 
#HERRAMIENTA PERSONALIZADA QUE CREA UN NÚMERO ALEATORIO ENTRE 0 Y 100:
class NumeroAleatorio(BaseTool):
    #name =         Nombre de la herramienta.
    name = "Numero aleatorio"
    #description =  Instrucción que le indica al agente en qué situaciones deberá utilizar esta herramienta.
    description = "Usa esta herramienta cuando necesites un número aleatorio"
    #_run()      =  Método que describe la acción que ejecuta esta herramienta en específico para contestar una 
    #pregunta hecha al agente, ya sea acerca de matemáticas, búsquedas a internet, uso de APIs específicas, etc.
    #self: La instrucción self se utiliza para hacer referencia al objeto que se está manipulando cuando se instancíe
    #la clase. Por eso es que a través de la misma nomenclatura que incluye un punto se accede a los distintos 
    #atributos y/o métodos con un objeto desde fuera de la clase.
    def _run(self, operacion: str):
        return "Numero aleatorio = " + str(random.randint(0, 100))
    #_arun(): Este método se utiliza cuando se quiera que esta función se corra de forma asíncrona.
    async def _arun(self):
        raise NotImplementedError("Esta herramienta no tiene una ejecución asíncrona.")

#HERRAMIENTA PERSONALIZADA QUE CALCULA EL PERÍMETRO DE UN CÍRCULO A TRAVÉS DE UN SOLO PARÁMETRO QUE INDICA SU RADIO:
import re       #re: Librería que permite utilizar expresiones regulares para detectar patrones.
#Es de mucha utilidad utilizar la librería re, ya que esta permite identificar patrones en un string, y que lo que 
#siempre recibirán este tipo de funciones es una instrucción en forma de string, y de esta se deben extraer los números 
#que necesitamos para ejecutar la acción deseada y luego transformar eso a un formato de número entero o decimal.  
class CircunferenciaCirculo(BaseTool):
    #name =         Nombre de la herramienta.
    name = "Calculadora de circunferencia"
    #description =  Instrucción que le indica al agente en qué situaciones deberá utilizar esta herramienta.
    description = "Usa esta herramienta cuando necesites calcular la circunferencia de un círculo con su radio"
    #_run()      =  Método que describe la acción que ejecuta esta herramienta en específico para contestar una 
    #pregunta hecha al agente, ya sea acerca de matemáticas, búsquedas a internet, uso de APIs específicas, etc.
    def _run(self, radio: float):
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
        # - string: Palabra en la que se desea buscar patrones a través de la expresión regular especificada.
        # - flags: Modificadores opcionales que personalizan el comportamiento de la búsqueda.
        #   - re.IGNORECASE: Realiza la búsqueda sin distinción entre mayúsculas y minúsculas.
        #   - re.MULTILINE: Permite que el patrón coincida con múltiples líneas en la cadena.
        #   - re.DOTALL: Hace que el carácter . en el patrón coincida también con el carácter de nueva línea \n.
        #Esta expresión regular busca en el string un número, un espacio opcional seguido de más números, otro 
        #espacio opcional y finalmente la palabra mm, cm o m, para así identificar el valor del radio y su unidad,
        #regresando como resultado una lista de tuplas que contiene cada elemento encontrado.
        unidades = re.findall(pattern = r"(\d+(\s?\d*)?)\s?(mm|cm|m)", string = radio, flags = re.IGNORECASE)
        #Luego para extraer solamente la unidad se recorre solo la tercera tupla en la lista y se guarda en la 
        #variable unidades.
        unidades = [unidad for _, _, unidad in unidades]
        #Si existe un punto en la instrucción se jutará el resultado para que se considere como un número decimal.
        if "." in radio:    
            radio_operacion = re.findall(r"\d+", radio)
            #join(): Este método toma una lista de strings como argumento y los concatena, juntando cada string con el 
            #carácter especificado.
            radio_operacion = ".".join(radio_operacion)
        else:
            radio_operacion = re.findall(r"\d+", radio)
            radio_operacion = radio_operacion[0]
        #float(): Método utilizado para convertir cualquier tipo de dato a un decimal de tipo float.
        #math.pi: El atributo pi de la librería math representa la constante π.
        return str(float(radio_operacion)*2.0*math.pi) + " " + unidades[0]
    #_arun(): Este método se utiliza cuando se quiera que esta función se corra de forma asíncrona.
    async def _arun(self):
        #raise: Palabra reservada que se utiliza para lanzar una excepción que interrumpa la ejecución de un programa.
        #NotImplementedError(): Tipo de excepción que se lanza cuando una función o método no implementa una 
        #funcionalidad específica. 
        raise NotImplementedError("Esta herramienta no tiene una ejecución asíncrona.")
    
#HERRAMIENTA PERSONALIZADA QUE CALCULA LA SUMA DE 2 NÚMEROS A TRAVÉS DE DOS PARÁMETROS:
class Suma(BaseTool):
    name = "Suma"
    description = "Usa esta herramienta para sumar dos números"
    def _run(self, operacion: str):
        #Esta expresión regular busca en el string un número y un punto decimal opcional seguido de más números 
        #dentro de una misma palabra.
        numeros = re.findall(r'\b\d+(?:\.\d+)?\b', operacion)
        num1 = numeros[0]
        num2 = numeros[1]
        return float(num1) + float(num2)
    async def _arun(self):
        raise NotImplementedError("Esta herramienta no tiene una ejecución asíncrona.")
    
#HERRAMIENTA PERSONALIZADA QUE CALCULA LA HIPOTENUSA DE UN TRIÁNGULO A TRAVÉS DE DOS POSIBLES VALORES RECIBIDOS A 
#TRAVÉS DE TRES PARÁMETROS:
class HipotenusaTriangulo(BaseTool):
    name = "Hipotenusa de un triángulo"
    description = """Usa esta herramienta para calcular la longitud de una hipotenusa 
                  usando dos o más lados de un triángulo, y/o uno de sus ángulos en grados.
                  Para usar esta herramienta se debe recibir al menos dos de los siguientes 
                  parametros = ['cateto adyacente', 'cateto opuesto', 'angulo']"""
    def _run(self, operacion: str):
        cateto_adyacente = None                     #Iniciación de la variable del cateto_adyacente.
        cateto_opuesto = None                       #Iniciación de la variable del cateto_opuesto.
        angulo = None                               #Iniciación de la variable del angulo.
        hipotenusa = None                           #Iniciación de la variable de la hipotenusa.
        #Esta expresión regular busca en el string las palabras cateto adyacente, cateto opuesto, angulo o ángulo, 
        #luego un espacio opcional, un signo de igual = y otro espacio opcional, eso lo mete en la primera tupla,
        #después busca en el string un número y un punto decimal opcional seguido de más números y eso lo mete en una 
        #segunda tupla.
        triangulo = re.findall(r'(cateto adyacente|cateto opuesto|angulo|ángulo)\s*=\s*(\d+(?:\.\d+)?)', operacion.lower(), re.IGNORECASE)
        #Bucle for que extrae el valor de las dos tuplas contenidas en la lista retornada por la expresión regular, 
        #la cual contiene alguna de las palabras cateto adyacente, cateto opuesto, angulo o ángulo y en la otra tupla
        #su valor.
        for lados_angulo, valor in triangulo:
            if lados_angulo == "cateto adyacente":  
                cateto_adyacente = float(valor)     #Asignación de valor a la variable cateto_adyacente.
            if lados_angulo == "cateto opuesto":
                cateto_opuesto = float(valor)       #Asignación de valor a la variable cateto_opuesto.
            if lados_angulo == "angulo":
                #math.radians(): Método que convierte ángulos a radianes.
                angulo = math.radians(float(valor)) #Asignación de valor a la variable angulo.
            if ((cateto_adyacente != None) and (cateto_opuesto != None)):
                #math.sqrt(): Método que saca la raíz cuadrada de un número.
                #**: Por medio de dos símbolos de multiplicación se obtiene el exponente de un número (^). 
                hipotenusa = math.sqrt(cateto_adyacente**2 + cateto_adyacente**2)
            elif ((cateto_adyacente != None) and (angulo != None)):
                #math.cos(): Con este método se obtiene el coseno de un ángulo, que debe estar en radianes.
                hipotenusa = cateto_adyacente / math.cos(angulo)
            elif ((cateto_opuesto != None) and (angulo != None)):
                #math.sin(): Con este método se obtiene el seno de un ángulo, que debe estar en radianes.
                hipotenusa = cateto_opuesto / math.sin(angulo)
            else:
                hipotenusa = "No se han dado los datos necesarios para calcular la hipotenusa del triángulo."
        return hipotenusa
    async def _arun(self):
        raise NotImplementedError("Esta herramienta no tiene una ejecución asíncrona.")

#Para declarar las herramientas personalizadas de un agente no se debe utilizar el método load_tools(), para ello 
#simplemente se declara una lista que contenga una inicialización de las clases que hereden de la clase BaseTool.
nombreHerramientaPersonalizada = [NumeroAleatorio(), CircunferenciaCirculo(), Suma(), HipotenusaTriangulo()]

#initialize_agent(): Método que sirve para anexar a un agente las herramientas previamente cargadas al programa con el 
#método load_tools() o de forma directa cuando se trata de herramientas personalizadas que heredan de la clase 
#BaseTool, además en este se indica el LLM que se quiere utilizar y el tipo de agente que se pretende crear.
# - tools: Indica el diccionario que contiene el nombre de las herramientas que se quiere enlazar al agente.
# - llm: Indica el modelo de lenguaje o chat a utilizar.
# - agent: En este parámetro se indica el nombre del tipo de agente.
# - max_iterations: Este parámetro indica el máximo número de pensamientos (thoughts) que puede realizar el agente al 
#   responder una pregunta, esto es bueno declararlo porque así se evita que el agente se quede atorado en un bucle 
#   infinito buscando entre sus herramientas para contestar una pregunta que no puede responder.
# - verbose: Variable booleana que controla la información impresa en consola. Cuando verbose es True, el objeto 
#   agente imprimirá información sobre el proceso de generación de la conversación, incluyendo el prompt, la 
#   herramienta que está utilizando para resolver cada parte del prompt, la respuesta dada por cada herramienta y 
#   la respuesta final del agente.
AgentePersonalizado = initialize_agent(
    agent = "zero-shot-react-description",
    tools = nombreHerramientaPersonalizada,
    llm = openaiLLM,
    verbose = True,
    max_iterations = 3
)
#initialize_agent().run(): El método run() proporciona el valor de entrada del agente y luego lo ejecuta para que 
#podamos ver su resultado.
resultadoAgentePersonalizado = AgentePersonalizado.run("Calcula la circunferencia de un círculo con radio de 0.5m.")
print("Respuesta de Agente Personalizado: ", str(resultadoAgentePersonalizado), "\n\n")
resultadoAgentePersonalizado = AgentePersonalizado.run("Dame un número aleatorio.")
print("Respuesta de Agente Personalizado: ", str(resultadoAgentePersonalizado), "\n\n")
resultadoAgentePersonalizado = AgentePersonalizado.run("Suma los números 12.5 y 0.6")
print("Respuesta de Agente Personalizado: ", str(resultadoAgentePersonalizado), "\n\n")
resultadoAgentePersonalizado = AgentePersonalizado.run("Si tengo un triángulo con dos lados de longitud de 51cm y 34cm, cual es el valor de su hipotenusa")
print("Respuesta de Agente Personalizado: ", str(resultadoAgentePersonalizado), "\n\n")
resultadoAgentePersonalizado = AgentePersonalizado.run("Si en un triángulo tengo un cateto opuesto de 51cm y un ángulo de 60 grados, cual es el valor de su hipotenusa?")
print("Respuesta de Agente Personalizado: ", str(resultadoAgentePersonalizado), "\n\n")