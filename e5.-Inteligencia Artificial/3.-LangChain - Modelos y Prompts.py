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
#compra el servicio de la API, se cobrará a través de Tokens, que representan pedazos de palabras. Como máximo se 
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
#A través de la instancia del objeto OpenAI se le puede mandar texto directamente al LLM convocado.
respuestaLLM = openaiLLM("Cuentame un chiste muy gracioso")
#print(): Método para imprimir un mensaje en consola y después dar un salto de línea (Enter).
print("Respuesta LLM: ", respuestaLLM + "\n\n")

#ChatOpenAI: Clase de la librería langchain que permite utilizar el modelo de chat (ChatGPT) de OpenAI con Python, este
#puede contestar preguntas adoptando un rol y guardar un historial durante la conversación.
from langchain.chat_models import ChatOpenAI    #ChatOpenAI: Modelo de Chat.
from langchain.schema import HumanMessage       #HumanMessage: Clase para mandar una pregunta del usuario al Chat.
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
#HumanMessage: A través de un objeto de la clase ChatOpenAI se le mandará al modelo una lista que indique el rol y 
#pregunta mandada al chat, de forma muy parecida a como se realiza con el método ChatCompletion.create() de la API 
#openai; esto dentro de la librería langchain se realiza a través del constructor de un objeto 
#HumanMessage(role = "", content = "") y el resultado de igual manera será una lista, por lo que se deberá transformar 
#a un string con el método str() para poder imprimirlo en consola.
respuestaChatGPT = openaiChatGPT([HumanMessage(role = "user", content="Hola como estás?")])
print("Respuesta Chat: " + str(respuestaChatGPT) + "\n\n")





#2.-PROMPTS: Es el texto que se le envía al modelo para generar una respuesta y en este es donde se utilizan las 
#técnicas de Prompt Engineering, para ello la librería LangChain cuenta con diferentes clases que permiten utilizar 
#dichas técnicas, dependiendo de si se está mandando el Prompt a un LLM o a un Chat.
print("\n\n-----------------------------------------------2.-PROMPTS-----------------------------------------------")
#PromptTemplate: Clase de la librería langchain que permite mandar instrucciones o preguntas personalizadas a un modelo 
#LLM (Large Language Model) previamente invocado con Python, que no guarda un historial.
from langchain import PromptTemplate            #PromptTemplate: Pregunta mandada a un modelo LLM.
#El template se declara como un String que se encuentre entre dos comillas triples """Instrucción Prompt""", el punto 
#de esto es declarar una instrucción que se puede aplicar a varias preguntas distintas y las variables de dicha 
#pregunta se declaran dentro de dos llaves {variablePrompt}.
templateTech = """Eres un asistente virtual de {rolAsistenteVirtual} que proporciona un camino de aprendizaje dando 
opciones cortas y concretas, pensando cada paso, paso a paso de los temas individuales que se deben aprender para 
convertirse en un conocedor de un tema en específico.
Pregunta: Cuales son los pasos para aprender sobre {aprenderTema}.
Respuesta:"""
#PromptTemplate(): En el constructor de la clase PromptTemplate perteneciente a la librería langchain se indica: 
# - template: Parámetro que indica la pregunta del prompt, esta se pudo haber guardado previamente en una variable.
# - input_variables: Indica a través de una lista todos los nombres de las variables incluidas en la plantilla del 
#   prompt, que se declararon dentro del template entre llaves {}.
plantillaPrompt = PromptTemplate(template = templateTech, input_variables = ["rolAsistenteVirtual", "aprenderTema"])
#PromptTemplate().format(): Método que rellena las variables del template con valores de entrada.
promptMandadoLLM = plantillaPrompt.format(rolAsistenteVirtual = "Tecnología", aprenderTema = "IoT")
print("Prompt LLM: " + promptMandadoLLM + "\n\n")
#OpenAI(PromptTemplate().format()): Prompt mandado al modelo LLM.
respuestaPromptLLM = openaiLLM(promptMandadoLLM)
print("Respuesta LLM con Prompt: ", respuestaPromptLLM + "\n\n")
#OpenAI().get_num_tokens(PromptTemplate().format()): El método get_num_tokens() se aplica al objeto del Modelo 
#utilizado y sirve para calcular el número de tokens enviados en un Prompt.
print("Número de Tokens del Promt =", openaiLLM.get_num_tokens(promptMandadoLLM), "del máximo que son 4096. \n\n")

#ChatPromptTemplate: Clase de la librería langchain que permite mandar instrucciones o preguntas personalizadas a un 
#modelo de Chat, este puede contestar preguntas adoptando un rol a través de las siguientes clases:
#   - SystemMessagePromptTemplate: Con esta clase se indica el rol que interpretará ChatGPT al responder las preguntas 
#     del usuario.
#   - HumanMessagePromptTemplate: Con esta clase se representa el rol del usuario que manda preguntas a ChatGPT.
#   - AIMessagePromptTemplate: Con esta clase se representa el rol que es adoptado por ChatGPT siempre que responda la 
#     pregunta de un usuario. Su mayor uso es el de permitir que el chat recuerde entradas y salidas anteriores.
from langchain.prompts import ChatPromptTemplate #ChatPromptTemplate: Instrucciones mandadas a un modelo de chat.
from langchain.prompts import  SystemMessagePromptTemplate, HumanMessagePromptTemplate, AIMessagePromptTemplate

#SYSTEM - ROL DEL CHAT AL RESPONDER PREGUNTAS DEL USUARIO: Para ello se utiliza un objeto PromptTemplate.
#PromptTemplate(): En el constructor de la clase PromptTemplate perteneciente a la librería langchain se indica: 
# - template: Parámetro que indica la pregunta del prompt.
# - input_variables: Indica a través de una lista todos los nombres de las variables incluidas en la plantilla del 
#   prompt, que se declararon dentro del template entre llaves {}.
plantillaPromptSistema = PromptTemplate(
    template = "Eres un asistente virtual de viajes que me recomienda alternativas interesantes para viajar por {paisViaje}.",
    input_variables = ["paisViaje"]
)
#SystemMessagePromptTemplate(): Esta clase recibe como parámetro un objeto PromptTemplate, que previamente ya tiene 
#diseñado el template que se mandará en el Prompt, indicándole al Chat el rol que está interpretando al responder.
promptSistema = SystemMessagePromptTemplate(prompt = plantillaPromptSistema)

#HUMAN - PREGUNTAS QUE EL USUARIO LE HACE AL MODELO: Para ello se utiliza un objeto PromptTemplate.
plantillaPromptHumano = PromptTemplate(
    template = "Mi viaje empieza el {fechaInicio} y termina el {fechaFin}. El vuelo es redondo, llegando y saliendo de {ciudadVuelo}",
    input_variables = ["fechaInicio", "fechaFin", "ciudadVuelo"]
)
#HumanMessagePromptTemplate(): Esta clase recibe como parámetro un objeto PromptTemplate, que previamente ya tiene 
#diseñado el template de la pregunta que hace el usuario al chat.
promptHumano = HumanMessagePromptTemplate(prompt = plantillaPromptHumano)

#ChatPromptTemplate.from_messages(): Método que sirve para unificar los templates previamente creados para el sistema 
#(que le dice al modelo el rol que debe interpretar al responder mis preguntas), para el humano (que indica tal cual 
#la pregunta realizada por el usuario) y de la AI (que es un rol adoptado por el modelo para guardar las preguntas y 
#respuestas realizadas en un historial), creando así una conversación. El parámetro que recibe el método es una lista 
#que incluye todas las plantillas de Prompt mencionadas previamente.
plantillaChatPrompt = ChatPromptTemplate.from_messages([promptSistema, promptHumano])
#ChatPromptTemplate().format_prompt().to_messages(): Método que rellena las variables del template mandado al Chat con 
#valores de entrada para el prompt del sistema, del humano y de la AI, retornando una lista.
promptMandadoChat = plantillaChatPrompt.format_prompt(
                                            paisViaje = "Francia", 
                                            fechaInicio = "30/11/2023", 
                                            fechaFin = "30/11/2023",
                                            ciudadVuelo = "Madrid").to_messages()
#str(): Método que convierte un número, lista, diccionario, etc. en un string para que pueda ser impreso en consola.
print("Prompt Chat: " + str(promptMandadoChat) + "\n\n")
#ChatOpenAI(ChatPromptTemplate().format().to_messages()): Prompt mandado al modelo de Chat.
respuestaChat = openaiChatGPT(promptMandadoChat)
#Del diccionario retornado, el key de content es el que contiene la respuesta de la pregunta.
print("Respuesta de Chat con Prompt: ", respuestaChat.content + "\n\n")

#FewShotPromptSelector: Clase de la librería langchain que permite mandar ejemplos con el formato de respuesta que se 
#espera obtener al mandar un Prompt, utilizando así la técnica Few-Shot Prompting, también llamada Example Selector.
from langchain import FewShotPromptTemplate     #FewShotPromptTemplate: Ejemplos de respuesta mandados al modelo.
#Primero se declara una lista con diccionarios anidados de preguntas y respuestas con el formato que se busca obtener.
ejemplos = [
    {"pregunta": "¿Cuales son los lugares más interesantes de la ciudad de México?", "respuesta": "El paseo en globo aerostático sobre las pirámides de Teotihuacán"},
    {"pregunta": "¿Cuales son los lugares más interesantes de Puerto Vallarta?", "respuesta": "La cascada El Salto"},
    {"pregunta": "¿Cuales son los lugares más interesantes de Toluca?", "respuesta": "El nevado de Toluca"}
]
#PromptTemplate(): En el constructor de la clase PromptTemplate perteneciente a la librería langchain se indica: 
# - template: Parámetro que indica la pregunta del prompt.
# - input_variables: Indica a través de una lista todos los nombres de las variables incluidas en la plantilla del 
#   prompt, que se declararon dentro del template entre llaves {}.
#Cuando esto se utiliza después de haber declarado una lista de ejemplos, se debe indicar el mismo nombre de las keys 
#de sus diccionarios en la lista del parámetro input_variables.
plantillaPromptEjemplos = PromptTemplate(
    input_variables = ["pregunta", "respuesta"],
    template = "La Pregunta es: {pregunta} y su Respuesta es: {respuesta}"
)
#FewShotPromptTemplate(): Esta clase recibe como parámetro un objeto PromptTemplate, que ya tiene diseñado un template 
#que incluye los ejemplos de preguntas y respuestas que se espera recibir al hacer una pregunta al Chat:
# - example_prompt: Parámetro que recibe un objeto PromptTemplate, que previamente haya declarado una plantilla de 
#   Prompt que incluya ejemplos de la respuesta que se espera obtener.
# - examples: Recibe una lista de prompts de ejemplo, que ayuda a obtener una respuesta con un formato específico.
# - prefix: Indica la instrucción inicial que se dá al Prompt, la cual puede estar asignando un rol de comportamiento 
#   al modelo.
# - suffix: Indica la instrucción final que se dá al Prompt, que usualmente es la pregunta realizada al modelo.
# - input_variables: Indica a través de una lista todos los nombres de las variables incluidas en la plantilla del 
#   prompt, que se declararon dentro del parámetro suffix de este mismo objeto FewShotPromptTemplate entre llaves {}.
promptEjemplos = FewShotPromptTemplate(
    example_prompt = plantillaPromptEjemplos,
    examples = ejemplos,
    prefix = "Eres un asistente virtual inútil y burlón que hace bromas de lo que sea que el usuario pregunte",
    suffix = "La Pregunta es: {Preguuuuntame} y su Respuesta es:",
    input_variables = ["Preguuuuntame"]
)
#FewShotPromptTemplate().format(): Método que rellena las variables del template con valores de entrada.
promptEjemlosLLM = promptEjemplos.format(Preguuuuntame = "¿Cuál es el lugar más interesante de 5 ciudades diferentes en Francia?")
print("Prompt Ejemplos LLM: " + promptEjemlosLLM + "\n\n")
#OpenAI(FewShotPromptTemplate().format()): Prompt mandado al modelo LLM.
respuestaEjemplosLLM = openaiLLM(promptEjemlosLLM)
print("Respuesta LLM con Prompt de Ejemplos: ", respuestaEjemplosLLM + "\n\n")

#output_parsers: Paquete de la librería langchain que permite transformar la respuesta obtenida de un modelo LLM en un 
#JSON, diccionario, lista, tupla o cualquier otro tipo de dato estructurado que se pueda analizar dentro de un código.
#CommaSeparatedListOutputParser: Clase del paquete output_parsers perteneciente a la librería langchain que permite 
#separar la respuesta obtenida de un modelo en una lista de elementos separados por comas.
from langchain.output_parsers import CommaSeparatedListOutputParser
outputParser = CommaSeparatedListOutputParser()         #Instancia de la clase CommaSeparatedListOutputParser.
#CommaSeparatedListOutputParser.get_format_instructions(): Método que crea una variable que incluye el formato de 
#respuesta que se busca obtener al mandar un Prompt para que sea procesado por un modelo.
formatoSalida = outputParser.get_format_instructions()
#PromptTemplate(): En el constructor de la clase PromptTemplate perteneciente a la librería langchain se indica: 
# - template: Parámetro que indica la pregunta del prompt.
# - input_variables: Indica a través de una lista todos los nombres de las variables incluidas en la plantilla del 
#   prompt, que se declararon dentro del template entre llaves {}.
# - partial_variables: Parámetro que recibe un diccionario para indicar el formato de salida del prompt, el cual 
#   en este caso será en forma de lista, para ello se declara una key que indique el nombre del formato declarado 
#   como variable {} en el parámetro template del prompt y como su value se utiliza la variable que utilizó el método 
#   CommaSeparatedListOutputParser.get_format_instructions().
plantillaPromptFormato = PromptTemplate(
    template = "Cuales son los ingredientes para preparar {platillo}\n{variableFormato}",
    input_variables = ["platillo"],
    partial_variables = {"variableFormato" : formatoSalida}
)
#PromptTemplate().format(): Método que rellena las variables del template con valores de entrada.
promptFormatoLLM = plantillaPromptFormato.format(platillo = "un brownie Keto")
print("Prompt Formato Lista LLM: " + promptFormatoLLM + "\n\n")
#OpenAI(PromptTemplate().format()): Prompt mandado al modelo LLM.
respuestaFormatoLLM = openaiLLM(promptFormatoLLM)
print("Respuesta de LLM con Formato de Prompt: ", respuestaFormatoLLM + "\n\n")
#CommaSeparatedListOutputParser().parse(PromptTemplate().format()): El método .parse() permite utilizar el formato que 
#instancía la clase CommaSeparatedListOutputParser aplicado a la plantilla creada con el objeto PromptTemplate después 
#de haber sido mandada al modelo de lenguaje.
respuestaFormateada = outputParser.parse(respuestaFormatoLLM)
print("Respuesta en forma de lista de un Prompt: ", str(respuestaFormateada) + "\n\n")