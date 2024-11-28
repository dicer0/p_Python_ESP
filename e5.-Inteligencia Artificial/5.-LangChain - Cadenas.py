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
openaiLLM = OpenAI(model_name = "text-davinci-003", openai_api_key = ApiKey, temperature = 0.5)           #LLM.

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
openaiChatGPT = ChatOpenAI(model_name = "gpt-3.5-turbo", openai_api_key = ApiKey, temperature = 0.7)    #Chat.





#2.-PROMPTS: Es el texto que se le envía al modelo para generar una respuesta y en este es donde se utilizan las 
#técnicas de Prompt Engineering, para ello la librería LangChain cuenta con diferentes clases que permiten utilizar 
#dichas técnicas, dependiendo de si se está mandando el Prompt a un LLM o a un Chat.
print("\n-----------------------------------------------2.-PROMPTS-----------------------------------------------")
#PromptTemplate: Clase de la librería langchain que permite mandar instrucciones o preguntas personalizadas a un modelo 
#LLM (Large Language Model) previamente invocado con Python, que no guarda un historial.
from langchain import PromptTemplate            #PromptTemplate: Pregunta mandada a un modelo LLM.





#4.-CADENAS (Chains): Con esta herramienta se permite enlazar un modelo con un Prompt, también con ella se pueden 
#conectar varios modelos entre sí, hasta cuando son de distintos tipos, permitiéndonos así realizar varias iteraciones 
#entre modelos durante una consulta para obtener un mejor procesamiento final de los datos cuando este se busca aplicar 
#a tareas muy complejas.
print("\n-----------------------------------------------4.-CADENAS-----------------------------------------------")
#CADENA SIMPLE: Permite encadenar un prompt con un modelo.
#   - LLMChain: Con esta clase se conecta un prompt con un modelo de lenguaje, creando así una cadena individual.
from langchain import LLMChain      #LLMChain: Librería que crea una cadena, la cual incluye un prompt y un modelo.
#PromptTemplate(): En el constructor de la clase PromptTemplate perteneciente a la librería langchain se indica: 
# - template: Parámetro que indica la plantilla del prompt previamente creada y almacenada en una variable.
# - input_variables: Indica a través de una lista todos los nombres de las variables incluidas en la plantilla del 
#   prompt, que se declararon dentro de la variable template entre llaves {}.
plantillaPromptCadenaLLM = PromptTemplate(
    template = "Eres un asistente virtual experto en {tema} y respondes con una lista de 3 conceptos clave sobre el mismo.",
    input_variables = ["tema"]
)
#LLMChain(): Crea una cadena que unifica una plantilla de prompt con un modelo para que sea procesado.
# - llm: Indica el modelo de lenguaje o chat a utilizar.
# - prompt: Recibe un objeto tipo PromptTemplate que representa la plantilla del prompt mandada a la cadena LLM.
cadenaLLM = LLMChain(llm = openaiLLM, prompt = plantillaPromptCadenaLLM)
#LLMChain().predict(): El método predict lo que hace es rellenar las variables de la plantila del prompt con valores 
#de entrada. La cadena es una alternativa diferente a utilizar el objeto OpenAI(PromptTemplate().format()), pero 
#básicamente hacen lo mismo.
respuestaChainLLM = cadenaLLM.predict(tema = "inteligencia artificial")
print("Cadena LLM con plantilla de Prompt: ", str(cadenaLLM), "\n\n")
print("Respuesta de LLMChain con plantilla de Prompt: ", str(respuestaChainLLM), "\n\n")

#CADENA SECUENCIAL: Permite encadenar un prompt con varios modelos de forma secuencial, uniendo así varias cadenas.
#   - SequentialChain: Con esta clase se pueden conectar dos o más cadenas, osea modelos de lenguaje que se encuentran 
#     enlazados con un prompt, pudiendo recibir así múltiples entradas y generar múltiples salidas, ya que la salida de
#     una cadena puede ser la entrada de otra cadena de forma secuencial. Además existe la clase SimpleSequentialChain 
#     que hace lo mismo pero con la condición de que solo puede recibir 1 entrada y proporcionar 1 salida.
#Para que una cadena SequentialChain funcione, se deben declarar varias cadenas individuales LLMChain, cada una con su 
#propio PromptTemplate.
from langchain.chains import SequentialChain        #SequentialChain: Cadena de cadenas con muchas entradas y salidas.
from langchain.chains import SimpleSequentialChain  #SimpleSequentialChain: Cadena de cadenas con 1 entrada y 1 salida.
#PromptTemplate.from_template(): Método que crea un objeto PromptTemplate a partir de una plantilla de texto, la gran
#diferencia de usar este método en vez del constructor de la clase PromptTemplate() es que no se indica de forma 
#explícita las variables del prompt, solo se crea el objeto. La asignación de valor de las variables será realizada a 
#través de su nombre con el método LLMChain().predict() después de haber creado la cadena individual.  
promptTemplate_1 = """Eres un asistente virtual de viajes que enumera 3 recomiendaciones de ciudades interesantes para 
                 viajar por {paisViaje}. Si el país es Francia, no se debe incluir la ciudad de París."""
plantillaPromptCadenaLLM_1 = PromptTemplate.from_template(promptTemplate_1)
#LLMChain(): Crea una cadena que unifica una plantilla de prompt con un modelo para que sea procesado.
# - llm: Indica el modelo de lenguaje o chat a utilizar.
# - prompt: Recibe un objeto tipo PromptTemplate que representa la plantilla del prompt mandada a la cadena LLM.
# - output_key: Este parámetro representa el nombre que se le asigna a la salida de esta cadena individualmente, para 
#   que así cuando se unifiquen varias a través del objeto SequentialChain, se pueda elegir cuales salidas se reciben 
#   como entrada de otras cadenas o cuales hasta se consideran como la salida del mismo objeto SequentialChain.
cadenaLLM_1 = LLMChain(llm = openaiLLM, prompt = plantillaPromptCadenaLLM_1, output_key = "listaCiudades", verbose = True)
#PromptTemplate.from_template(): Método que crea un objeto PromptTemplate a partir de una plantilla de texto.
promptTemplate_2 = """Eres un asistente virtual de viajes que recibe una lista de 3 ciudades interesantes para 
                   viajar por un país y debe devolver 5 lugares interesantes para visitar en cada ciudad.
                   La lista de ciudades es {listaCiudades}"""
plantillaPromptCadenaLLM_2 = PromptTemplate.from_template(promptTemplate_2)
#LLMChain(): Crea una cadena individual que unifica una plantilla de prompt con un modelo para que sea procesado.
cadenaLLM_2 = LLMChain(llm = openaiLLM, prompt = plantillaPromptCadenaLLM_2, output_key = "atraccionesCiudad", verbose = True)
#SequentialChain(): Objeto que crea una cadena de cadenas LLMChain, pudiendo recibir múltiples entradas y generar 
#múltiples salidas, ya que la salida de una cadena puede ser la entrada de otra cadena de forma secuencial.
# - chains: Parámetro que recibe una lista con todas las cadenas individuales LLMChain que se conectarán, declarándolas
#   en el órden en el que se ejecutarán de forma secuencial.
# - input_variables: Indica a través de una lista todos los nombres de las variables de entrada incluidas en las 
#   plantillas de los prompts pertenecientes a cada cadena, que se declararon entre llaves {}.
# - output_variables: Indica a través de una lista los nombres de las output_key que se quieren considerar como salida 
#   de la cadena.
# - verbose: Variable booleana que controla la información impresa en consola. Cuando verbose es True, el objeto 
#   ConversationChain imprimirá información sobre el proceso de generación de la conversación, incluyendo el prompt
#   y el rol del usuario que está contestando cada cosa, pero cuando es False, no se imprimirá ninguna información.
cadenaSecuencial = SequentialChain(chains = [cadenaLLM_1, cadenaLLM_2],
                                   input_variables = ["paisViaje"],
                                   output_variables = ["listaCiudades", "atraccionesCiudad"],
                                   verbose = True)
#Para asignar valores a las entradas de una cadena se debe utilizar un diccionario, donde la key representa el nombre 
#de la variable y el value su valor: {key: value} = {"nombreVariable": "Valor"}
respuestaSequentialChain = cadenaSecuencial({"paisViaje" : "Alemania"})
print("Cadena Secuencial LLM con plantilla de Prompt: ", str(cadenaSecuencial), "\n\n")
print("Respuesta de SequentialChain con plantillas de Prompt: ", str(respuestaSequentialChain), "\n\n")
print("Respuesta 1 de SequentialChain con plantillas de Prompt: ", str(respuestaSequentialChain["listaCiudades"]), "\n\n")
print("Respuesta 2 de SequentialChain con plantillas de Prompt: ", str(respuestaSequentialChain["atraccionesCiudad"]), "\n\n")

#SimpleSequentialChain(): Objeto que crea una cadena de cadenas LLMChain, pudiendo recibir una entrada y generar 
#una salida.
# - chains: Parámetro que recibe una lista con todas las cadenas individuales LLMChain que se conectarán, declarándolas
#   en el órden en el que se ejecutarán de forma secuencial.
# - verbose: Variable booleana que controla la información impresa en consola. Cuando verbose es True, el objeto 
#   ConversationChain imprimirá información sobre el proceso de generación de la conversación, incluyendo el prompt
#   y el rol del usuario que está contestando cada cosa, pero cuando es False, no se imprimirá ninguna información.
cadenaSecuencialSimple = SimpleSequentialChain(chains = [cadenaLLM_1, cadenaLLM_2],
                                               verbose = True)
#SimpleSequentialChain().run(): El método run() proporciona el valor de la única entrada que puede tener la cadena de 
#tipo SimpleSequentialChain y luego la ejecuta para que podamos ver su resultado.
respuestaSimpleSequentialChain = cadenaSecuencialSimple.run("Francia")
print("Cadena Secuencial Simple de LLM con plantilla de Prompt: ", str(cadenaSecuencialSimple), "\n\n")
print("Respuesta de SimpleSequentialChain con plantillas de Prompt: ", str(respuestaSimpleSequentialChain), "\n\n")

#PROCESAMIENTO DE LLM: Permite encadenar un prompt con varios modelos de forma secuencial, uniendo así varias cadenas.
#   - TransformChain: Con esta clase se implementa una cadena de transformación, que se aplica a una entrada para 
#     producir una salida con un formato personalizado. Las transformaciones pueden ser representadas por cualquier 
#     función que tome una secuencia como entrada y devuelva una secuencia como salida.
#Por lo tanto, para que una cadena TransformChain funcione, se debe declarar una función propia que cambie el formato 
#de la salida de otra cadena.
from langchain.chains import TransformChain    #TransformChain: Librería que crea una cadena de cadenas.
#Función propia que cambia el formato de cualquier salida proporcionada por un modelo de Chat o LLM.
def eliminarSaltosDeLinea(entrada):
    #Función que intercambia los saltos de línea por espacios.
    texto = entrada["texto"]    #Recibe una lista con un diccionario interno de key = texto.
    #lista.replace(): Método que reemplaza dentro de una lista un string por otro.
    return {"texto_limpio" : texto.replace("\n", "")}
#TransformChain(): Objeto que recibe un prompt, cambia su formato de una forma personalizada y lo retorna en una 
#variable nueva.
# - input_variables: Indica a través de una lista los prompts de entrada.
# - output_variables: Indica a través de una lista el nombre de la variable de salida ya con el formato deseado.
# - transform: Recibe el nombre de la función propia que transforma el formato de la variable de entrada.
cadenaTransformarFormato = TransformChain(input_variables = ["texto"],
                                          output_variables = ["texto_limpio"],
                                          transform = eliminarSaltosDeLinea)
prompt_transform = """\n Este es un texto \ncon brincos \nde linea innecesarios\n."""
#TransformChain().run(): El método run() proporciona el valor de entrada del prompt y luego la ejecuta para que 
#podamos ver su resultado.
respuestaTransformChain = cadenaTransformarFormato.run(prompt_transform)
print("Cadena TransformChain de LLM con plantilla de Prompt: ", str(cadenaTransformarFormato), "\n\n")
print("Respuesta de TransformChain con plantillas de Prompt: ", str(respuestaTransformChain), "\n\n")