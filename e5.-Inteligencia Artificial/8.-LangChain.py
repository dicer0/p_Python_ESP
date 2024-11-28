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
# - openai_api_key: Con este parámetro se roporciona la API key, que por buenas prácticas debe provenir de otro 
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
#A través de un objeto de la clase ChatOpenAI se le mandará al modelo una lista que indique el rol y pregunta mandada 
#al chat, de forma muy parecida a como se realiza con el método ChatCompletion.create() de la API openai; esto dentro 
#de la librería langchain se realiza a través del constructor de un objeto HumanMessage(role = "", content = "") y el
#resultado de igual manera será una lista, por lo que se deberá transformar a un string con el método str() para poder
#imprimirlo en consola.
respuestaChatGPT = openaiChatGPT([HumanMessage(role = "user", content="Hola como estás?")])
print("Respuesta Chat: " + str(respuestaChatGPT) + "\n\n")





#2.-PROMPTS: Es el texto que se le envía al modelo para generar una respuesta y en este es donde se utilizan las 
#técnicas de Prompt Engineering, para ello la librería LangChain cuenta con diferentes clases que permiten utilizar 
#dichas técnicas, dependiendo de si se está mandando el Prompt a un LLM o a un Chat.
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





#3.-MEMORIA (Memory): Esta clase permite almacenar las preguntas y respuestas hechas entre el LLM y el usuario, 
#permitiendo así que se simule una conversación entre ambos.
print("\n\n-----------------------------------------------3.-MEMORIA-----------------------------------------------")
#MEMORIA DE HISTORIAL COMPLETO: Guarda todos los mensajes enviados y recibidos del chat.
#   - ConversationBufferMemory: Con esta clase se crea una de las memorias más básicas para guardar todo el historial 
#     de preguntas y respuestas mandadas y recibidas de un modelo de chat creado con la clase ChatOpenAI.
#   - ConversationChain: Clase para generar conversaciones entre dos o más participantes, indicando el rol de cada 
#     uno, ya sea el usuario (Human) o el modelo (AI). Esta clase se apoya de alguna otra que almacene el historial 
#     de la conversación y puede ser configurada para conectar diferentes modelos de lenguaje entre sí, resolviendo 
#     así tareas más complejas.
from langchain.memory import ConversationBufferMemory #ConversationBufferMemory: Memoria de historial de chat.
from langchain.chains import ConversationChain        #ConversationChain: Cadena de memoria del chat.
#ConversationBufferMemory(): Esta clase nos ayuda a gestionar todo el histórico de la conversación en un modelo de 
#chat, no recibe nada como parámetro, solamente se utiliza para crear una instancia de la clase.
memoriaHistorial = ConversationBufferMemory()                    #Instancia de la clase ConversationBufferMemory.
#ConversationChain(): La clase ConversationChain se utiliza para generar conversaciones de texto entre dos o más 
#participantes y puede ser configurada para conectar diferentes modelos de lenguaje (LLM) o modelos de chat entre sí.
#Además, cabe mencionar que durante la conversación se estará indicando quién es el que está realizando cada 
#interacción, ya sea el usuario (Human) o el modelo (AI).
# - llm: Indica el modelo de lenguaje o chat a utilizar.
# - memory: Recibe un objeto de memoria que gestione el historial de la conversación.
# - verbose: Variable booleana que controla la información impresa en consola. Cuando verbose es True, el objeto 
#   ConversationChain imprimirá información sobre el proceso de generación de la conversación, incluyendo el prompt
#   y el rol del usuario que está contestando cada cosa, pero cuando es False, no se imprimirá ninguna información.
chatbotHistorial = ConversationChain(llm = openaiChatGPT, memory = memoriaHistorial, verbose = True)
#ConversationChain.predict(): El método predict() genera una conversación de texto utilizando el objeto 
#ConversationChain y a través de su parámetro input se introduce el Prompt mandado al chat.
chatbotHistorial.predict(input = "Hola como estás? Me llamo di_cer0 y soy la mente maestra detrás de la máquina.")
#Si se imprime en consola el resultado del objeto ConversationChain podremos observar que lo que retorna es lo que 
#está almacenado en la instancia de la clase ConversationBufferMemory, ya que esta representa el historial guardado 
#del chat.
print("Respuesta de Chat con Memoria:\n" + str(chatbotHistorial) + "\n\n")
#ConversationBufferMemory.chat_memory.messages: Dentro de la variable de memoria del chat se encuentra el valor 
#chat_memory, este almacena todos los roles del chat, ya sea el del usuario (Human) o el del modelo (AI), todo el 
#historial es guardado dentro de una lista interna llamada messages. 
print("Historial del chat guardado en el objeto ConversationBufferMemory:\n" + str(memoriaHistorial.chat_memory.messages) + "\n\n")
#Debido al historial creado, esta nueva instrucción la contestará en función de lo que previamente le dije. 
chatbotHistorial.predict(input = "Como me llamo?")
print("Historial del chat:\n" + str(memoriaHistorial.chat_memory.messages) + "\n\n")

#MEMORIA DE VENTANA: Guarda solo los últimos mensajes enviados y recibidos del chat.
#   - ConversationBufferWindowMemory: Con esta clase se crea un tipo de memoria que en vez de guardar todo el historial 
#     de preguntas y respuestas mandadas y recibidas de un modelo de chat creado con la clase ChatOpenAI, solo guarda 
#     los últimos mensajes mandados, a esto se le llama ventana de mensajes.
from langchain.memory import ConversationBufferWindowMemory #ConversationBufferWindowMemory: Memoria de mensajes.
#ConversationBufferMemory(): Esta clase nos ayuda a gestionar la ventana de mensajes que guarda parte de la conversación 
#realizada sobre un modelo de chat. Por medio del parámetro k se indica el número de los últimos mensajes a guardar.
memoriaMensajes = ConversationBufferWindowMemory(k = 2)         #Instancia de la clase ConversationBufferWindowMemory.
#ConversationChain(): La clase ConversationChain se utiliza para generar conversaciones de texto entre dos o más 
#participantes y puede ser configurada para conectar diferentes modelos de lenguaje (LLM) o modelos de chat entre sí. 
#Además, cabe mencionar que durante la conversación se estará indicando quién es el que está realizando cada 
#interacción, ya sea el usuario (Human) o el modelo (AI).
# - llm: Indica el modelo de lenguaje o chat a utilizar.
# - memory: Recibe un objeto de memoria que gestione el historial de la conversación.
# - verbose: Variable booleana que controla la información impresa en consola. Cuando verbose es True, el objeto 
#   ConversationChain imprimirá información sobre el proceso de generación de la conversación, incluyendo el prompt
#   y el rol del usuario que está contestando cada cosa, pero cuando es False, no se imprimirá ninguna información.
chatbotMensajes = ConversationChain(llm = openaiChatGPT, memory = memoriaMensajes, verbose = True)
#ConversationChain.predict(): El método predict() genera una conversación de texto utilizando el objeto 
#ConversationChain y a través de su parámetro input se introduce el Prompt mandado al chat.
chatbotMensajes.predict(input = "Hello... I like trains, chu chu.")
#Si se imprime en consola el resultado del objeto ConversationChain podremos observar que lo que retorna es lo que 
#está almacenado en la instancia de la clase ConversationBufferMemory, ya que esta representa el historial guardado 
#del chat.
print("Respuesta de Chat con Memoria:\n" + str(chatbotMensajes) + "\n\n")
#ConversationBufferWindowMemory.chat_memory.messages: Dentro de la variable de memoria del chat se encuentra el valor 
#chat_memory, este almacena todos los roles del chat, ya sea el del usuario (Human) o el del modelo (AI) y también las 
#partes del historial de la conversación incluidas en la ventana de memoria en una lista interna llamada messages. 
print("Historial del chat guardado en el objeto ConversationBufferWindowMemory:\n" 
      + str(memoriaMensajes.chat_memory.messages) + "\n\n")
chatbotMensajes.predict(input = "What do I like?")
print("Historial del chat:\n" + str(memoriaMensajes.chat_memory.messages) + "\n\n")
#Debido al historial creado, esta nueva instrucción la contestará en función de lo que previamente le dije, pero 
#ya con esto último se borrará el primer mensaje en el historial, porque solo indicamos que guarde k = 2, por lo 
#que almacenará solo los últimos 2 mensajes, incluyendo la respuesta del modelo, debido a esta situación no sabrá 
#como responder la última pregunta que le hice, entonces hay que tener cuidado porque al utilizar esta memoria, 
#el chat empezará a olvidar información.
chatbotMensajes.predict(input = "What do I like?")
#Aunque la variable de la memoria si guarda todo el historial de la conversación, solamente manda los últimos dos
#mensajes de este al modelo, por eso es que olvida cosas.
print("Historial del chat:\n" + str(memoriaMensajes.chat_memory.messages) + "\n\n")

#RESUMEN DE CONVERSACIÓN: Utiliza un segundo modelo para crear un resumen en inglés de la conversación entre el 
#usuario y el modelo, reduciendo así el número de tokens utilizados y bajando el costo de la API.
#   - ConversationSummaryMemory: Con esta clase se crea una cadena de modelos, donde en vez de guardar todo el 
#     historial de la conversación de forma literal, cada vez que responda un prompt el chat, el historial será 
#     mandado a otro modelo que realice un resumen de la conversación, con el peligro de que se borren algunos 
#     datos importantes o que se haga un mal resumen, pero de esta forma se optimiza el uso de recursos y además
#     el costo de la API baja porque se reduce el número de tokens en uso.
from langchain.memory import ConversationSummaryMemory #ConversationSummaryMemory: Memoria de resumen de historial.
#ConversationSummaryMemory(): Esta clase crea un resumen en inglés de todo el historial de la conversación a través 
#de un segundo modelo para seguir teniendo un contexto del tema tratado en el chat, reduciendo así el número de tokens 
#utilizados para bajar el costo de uso de la API, para ello se le debe pasar el modelo auxiliar de chat que utiliza
#en su parámetro llm, que puede ser tanto de tipo Chat (ChatOpenAI) como de tipo LLM (OpenAI).
#ChatOpenAI(): En el constructor de la clase OpenAI perteneciente al paquete llms de la librería langchain se indica: 
# - model_name: Parámetro que indica el modelo que se quiere utilizar, en este caso se utilizará gpt-3.5-turbo que 
#   pertenece a GPT-3.5.
# - openai_api_key: Con este parámetro se proporciona la API key, que por buenas prácticas debe provenir de otro 
#   archivo.
# - temperature: La temperatura es un valor entre 0 y 1 que indica la creatividad con la que contesta el LLM, si es 
#   demasiado grande, puede responder con algo totalmente aleatorio.
#Todos los modelos disponibles para usarse con OpenAI estan enlistados en el siguiente enlace y cada uno es mejor 
#en ciertas funciones que el otro:
#https://platform.openai.com/docs/models
modeloResumen = ChatOpenAI(model_name = "gpt-3.5-turbo", openai_api_key = ApiKey, temperature = 0.7)    #Chat.
memoriaResumen = ConversationSummaryMemory(llm = modeloResumen) #Instancia de la clase ConversationSummaryMemory.
#participantes y puede ser configurada para conectar diferentes modelos de lenguaje (LLM) o modelos de chat entre sí. 
#Además, cabe mencionar que durante la conversación se estará indicando quién es el que está realizando cada 
#interacción, ya sea el usuario (Human) o el modelo (AI).
# - llm: Indica el modelo de lenguaje o chat a utilizar.
# - memory: Recibe un objeto de memoria que gestione el historial de la conversación.
# - verbose: Variable booleana que controla la información impresa en consola. Cuando verbose es True, el objeto 
#   ConversationChain imprimirá información sobre el proceso de generación de la conversación, incluyendo el prompt
#   y el rol del usuario que está contestando cada cosa, pero cuando es False, no se imprimirá ninguna información.
chatbotResumen = ConversationChain(llm = openaiChatGPT, memory = memoriaResumen, verbose = True)
#ConversationChain.predict(): El método predict() genera una conversación de texto utilizando el objeto 
#ConversationChain y a través de su parámetro input se introduce el Prompt mandado al chat.
chatbotResumen.predict(input = "Oye ChatGpt si quiero crear un asistente virtual como Jarvis de Ironman como le hago?")
#Si se imprime en consola el resultado del objeto ConversationChain podremos observar que lo que retorna es lo que 
#está almacenado en la instancia de la clase ConversationBufferMemory, ya que esta representa el historial guardado 
#del chat.
print("Respuesta de Chat con Memoria:\n" + str(chatbotResumen) + "\n\n")
#ConversationSummaryMemory.chat_memory.messages: Dentro de la variable de memoria del chat se encuentra el valor 
#chat_memory, este almacena todos los roles del chat, ya sea el del usuario (Human) o el del modelo (AI), y un resumen 
#de todo el historial, que se encuentra guardado dentro de una lista interna llamada messages.
chatbotResumen.predict(input = "Pero cuales son las mejores herramientas que puedo utilizar?")
print("Historial del chat:\n" + str(memoriaResumen.chat_memory.messages) + "\n\n")
chatbotResumen.predict(input = "De donde puedo obtener un sintetizador de voz para que me pueda responder?")
print("Historial del chat:\n" + str(memoriaResumen.chat_memory.messages) + "\n\n")

#PALABRAS CLAVE DEL HISTORIAL: Utiliza un segundo modelo para crear listas con las palabras clave de la conversación.
#   - ConversationKGMemory: Con esta clase se crea una cadena de modelos, donde en vez de guardar todo el historial 
#     de la conversación de forma literal, cada vez que responda un prompt el chat, el historial será mandado a otro 
#     modelo que extraiga palabras clave de la conversación, creando así un gráfico de conocimiento en forma de lista
#     llamado Knowledge Graph para después poder contestar con ese contexto.
#Esta clase a veces llega a tener problemas al acceder los elementos en memoria ya que tiene problema con la traducción
#de las instrucciones del prompt, que por default están en inglés.
from langchain.memory import ConversationKGMemory #ConversationKGMemory: Memoria de palabras clave del historial.
#ConversationKGMemory(): Esta clase crea una lista con palabras clave de todo el historial de la conversación a través 
#de un segundo modelo para seguir teniendo un contexto del tema tratado en el chat, reduciendo así el número de tokens 
#utilizados para bajar el costo de uso de la API, para ello se le debe pasar el modelo auxiliar de chat que utiliza
#en su parámetro llm, que puede ser tanto de tipo Chat (ChatOpenAI) como de tipo LLM (OpenAI).
#ChatOpenAI(): En el constructor de la clase OpenAI perteneciente al paquete llms de la librería langchain se indica: 
# - model_name: Parámetro que indica el modelo que se quiere utilizar, en este caso se utilizará gpt-3.5-turbo que 
#   pertenece a GPT-3.5.
# - openai_api_key: Con este parámetro se proporciona la API key, que por buenas prácticas debe provenir de otro 
#   archivo.
# - temperature: La temperatura es un valor entre 0 y 1 que indica la creatividad con la que contesta el LLM, si es 
#   demasiado grande, puede responder con algo totalmente aleatorio y si es muy bajo responderá lo mismo siempre, 
#   función que podría ser deseada cuando por ejemplo se contestan problemas matemáticos.
#Todos los modelos disponibles para usarse con OpenAI estan enlistados en el siguiente enlace y cada uno es mejor 
#en ciertas funciones que el otro:
#https://platform.openai.com/docs/models
modeloPalabrasClave = ChatOpenAI(model_name = "gpt-3.5-turbo", openai_api_key = ApiKey, temperature = 1)    #Chat.
memoriaGraph = ConversationKGMemory(llm = modeloPalabrasClave) #Instancia de la clase ConversationKGMemory.
#ConversationChain(): La clase ConversationChain se utiliza para generar conversaciones de texto entre dos o más 
#participantes y puede ser configurada para conectar diferentes modelos de lenguaje (LLM) o modelos de chat entre sí. 
#Además, cabe mencionar que durante la conversación se estará indicando quién es el que está realizando cada 
#interacción, ya sea el usuario (Human) o el modelo (AI).
# - llm: Indica el modelo de lenguaje o chat a utilizar.
# - memory: Recibe un objeto de memoria que gestione el historial de la conversación.
# - verbose: Variable booleana que controla la información impresa en consola. Cuando verbose es True, el objeto 
#   ConversationChain imprimirá información sobre el proceso de generación de la conversación, incluyendo el prompt
#   y el rol del usuario que está contestando cada cosa, pero cuando es False, no se imprimirá ninguna información.
chatbotPalabrasClave = ConversationChain(llm = openaiChatGPT, memory = memoriaGraph, verbose = True)
#ConversationChain.predict(): El método predict() genera una conversación de texto utilizando el objeto 
#ConversationChain y a través de su parámetro input se introduce el Prompt mandado al chat.
chatbotPalabrasClave.predict(input = "Holis ChatGpt mi nombre es Diego Cervantes y soy mecatrónico.")
#Si se imprime en consola el resultado del objeto ConversationChain podremos observar que lo que retorna es lo que 
#está almacenado en la instancia de la clase ConversationBufferMemory, ya que esta representa el historial guardado 
#del chat.
print("Respuesta de Chat con Palabras Clave de Knowledge Graph:\n" + str(chatbotPalabrasClave) + "\n\n")
#ConversationKGMemory.memory.kg.get_triples(): Para obtener el Knowledge Graph que representa las palabras clave de 
#la conversación se debe acceder a su valor memory.kg dentro del objeto ConversationChain, para ahí aplicar el 
#método get_triples() y así obtener la lista de palabras clave que le dan contexto a la memoria de la conversación.
#Pero hay que tener muy en cuenta que esto puede tener errores cuando se utiliza un lenguaje que no sea el inglés.
chatbotPalabrasClave.predict(input = "Mi película favorita es Ironman, mis series favoritas son Daredevil y How I met your mother")
print("Knowledge Graph del chat:\n" + str(chatbotPalabrasClave.memory.kg.get_triples()) + "\n\n")
chatbotPalabrasClave.predict(input = "Mis habilidades técnicas son de desarrollador web, móvil, sistemas embebidos, robótica, etc.")
print("Knowledge Graph del chat:\n" + str(chatbotPalabrasClave.memory.kg.get_triples()) + "\n\n")
#ConversationKGMemory.chat_memory.messages: Dentro de la variable de memoria del chat se encuentra el valor 
#chat_memory, este almacena todos los roles del chat, ya sea el del usuario (Human) o el del modelo (AI) y también la  
#respuesta del chat en función del Knowledge Graph de la conversación guardada en la lista interna llamada messages. 
chatbotPalabrasClave.predict(input = "Cuál es mi nombre, a que me dedico y cual es mi serie favorita?")
print("Knowledge Graph del chat:\n" + str(memoriaGraph.chat_memory.messages) + "\n\n")





#4.-CADENAS (Chains): Con esta herramienta se permite enlazar un modelo con un Prompt, también con ella se pueden 
#conectar varios modelos entre sí, hasta cuando son de distintos tipos, permitiéndonos así realizar varias iteraciones 
#entre modelos durante una consulta para obtener un mejor procesamiento final de los datos cuando este se busca aplicar 
#a tareas muy complejas.
print("\n\n-----------------------------------------------4.-CADENAS-----------------------------------------------")
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
                 viajar por {paisViaje}."""
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





#5.0.-EMBEDDINGS: Los LLM convierten y asocian palabras a través de un vector llamado Embedding, el cual es un simple 
#array de varias dimensiones que se encuentra en un espacio vectorial, cuya función es asociar de forma gráfica una 
#palabra con otras parecidas y/o alejarla de otras que sean muy distintas, de esta manera es como el modelo entiende 
#el lenguaje humano para realizar búsquedas, agrupaciones, clasificaciones, recomendaciones, etc.
print("\n\n-----------------------------------------------5.-ÍNDICES-----------------------------------------------")
#   - OpenAIEmbeddings: Clase que convierte cualquier texto que se le mande en un vector numérico.
from langchain.embeddings import OpenAIEmbeddings
#OpenAIEmbeddings(): El constructor de la clase OpenAIEmbeddings recibe los siguientes parámetros de OpenAI:
# - openai_api_key: Con este parámetro se roporciona la API key, que por buenas prácticas debe provenir de otro 
#   archivo.
# - model: Parámetro que indica el modelo que se quiere utilizar, en este caso se utilizará el más recomendado, que es 
#   el text-embedding-ada-002, que puede recibir como máximo 8191 y da como salida un vector con tamaño de 1536.
#https://platform.openai.com/docs/guides/embeddings/what-are-embeddings
modeloEmbedding = OpenAIEmbeddings(openai_api_key = ApiKey, model = "text-embedding-ada-002")
promptEmbedding = "Soy di_cer0!!!"
#OpenAIEmbeddings().embed_query(): El método .embed_query() toma una cadena de texto como entrada y devuelve un vector 
#(osea una lista) de números que representa su embedding. 
respuestaEmbedding = modeloEmbedding.embed_query(promptEmbedding)
#len(lista): Devuelve el tamaño de la lista a la que se le aplique, en este caso devuelve el tamaño del embedding.
print("Embedding obtenido del Prompt: ", promptEmbedding, "=", str(respuestaEmbedding), "con tamaño de",  
      str(len(respuestaEmbedding)), "\n\n")

#5.1.-ÍNDICES (Retrieval o Data connection): La forma en la que más se aprovechan los modelos de lenguaje es cuando se 
#les da acceso a distintas fuentes de información, como lo puede ser un archivo PDF, Word, Excel, PowerPoint, etc. 
#Los índices en LangChain son los que nos van a permitir enlazar un gran número de documentos para que sean procesados 
#por el modelo, para ello la librería cuenta con diferentes clases que permiten realizar el enlace.

#CARGAR VARIOS DOCUMENTOS .TXT, .DOCX O .PDF A LA VEZ DE UNA CARPETA CON LA CLASE DirectoryLoader: La gran 
#funcionalidad de esto radica cuando se quiere crear una base de datos de nuestros propios archivos, para hacerle 
#preguntas sobre ellos. 
#   - DirectoryLoader: Clase perteneciente al paquete document_loaders que permite cargar en el programa el contenido 
#     de todos los archivos incluidos en una carpeta, para ello se debe proporcionar el path completo del directorio e 
#     indicar el tipo de documento que se quiere importar. 
#     Cabe mencionar que esta Clase se apoya en la librería unstructured al ejecutarse, por lo que para cada tipo de 
#     documento que sea distinto a archivos con extensión .txt se deberá hacer una instalación adicional.
#       LEER DIRECTORIO CON ARCHIVOS .TXT:             Instalar con comando: pip install unstructured
#       LEER DIRECTORIO CON ARCHIVOS .PDF:             Instalar con comando: pip install unstructured[pdf]
#       LEER DIRECTORIO CON ARCHIVOS DE WORD .DOCX:    Instalar con comando: pip install unstructured[docx]
#   - CharacterTextSplitter: Esta clase perteneciente al paquete text_splitter de la librería langchain permite 
#     dividir un texto muy grande en cachos limitados por cierto número de caracteres, ya que recordemos que el máximo 
#     de tokens que admiten los modelos de OpenAI son de 4096 tokens, que aproximadamente son 3,072 palabras.
from langchain.document_loaders import DirectoryLoader             #DirectoryLoader: Carga varios archivos a la vez.
from langchain.text_splitter import CharacterTextSplitter          #CharacterTextSplitter: División por caracteres.
#DirectoryLoader(): El constructor recibe dos parámetros, el path global del directorio al que se quiere acceder y 
#el parámetro glob indica el tipo de archivos que se recibirá de la carpeta indicada: glob = "**/*.extensiónArchivo".
cargarDirectorio = DirectoryLoader("C:/Users/diego/OneDrive/Documents/Aprendiendo/Python/5.-Inteligencia Artificial/0.-Archivos_Ejercicios_Python/", glob = "**/*.txt")
#DirectoryLoader().load(): El método .load() carga en una variable todos los archivos contenidos en la carpeta 
#indicada dentro del constructor del objeto DirectoryLoader.
documentosTxt = cargarDirectorio.load() #Carga todos los archivos txt de una carpeta.
print("Documentos txt originales extraídos de un directorio:\n", documentosTxt, "\n")
#DirectoryLoader().load()[0].page_content: El método page_content devuelve el contenido del documento.
#len(lista): Devuelve el tamaño de la lista a la que se le aplique, en este caso devuelve el número de palabras del 
#documento.
print("El número de palabras del documento es de:\n", len(documentosTxt[0].page_content), "\n")
#CharacterTextSplitter(): El constructor del objeto lo que hace es indicar las características con las que se dividirá 
#un texto grande que se quiere procesar a través de algún modelo de lenguaje, ya que estos están limitados en el 
#número de tokens que pueden recibir, por ejemplo OpenAI solo admite 4096 tokens, que son aproximadamente 3,072 
#palabras. Esta clase se utiliza cuando se busca que los trozos sean grandes.
# - chunk_size: Con este parámetro se indica el número de caracteres de cada cacho de texto, llamado chunk, este 
#   número usualmente se encuentra entre 400 y 1000 caracteres. Pero es importante mencionar que, si el modelo 
#   considera que al cortar cierta parte del texto con el chunk_size indicado hace que se pierda contexto, este número 
#   será cambiado automáticamente por el método .split_documents().
# - chunk_overlap: Con este parámetro se indica los caracteres que se entrelazan con el cacho que tiene alado, para 
#   que de esta forma no se pierda ninguna palabra.
dividirTexto = CharacterTextSplitter(chunk_size = 40, chunk_overlap = 0)    #División de texto por caracteres.
#CharacterTextSplitter().split_documents(): Método que divide el texto grande que recibe como parámetro en cachos 
#cuyas características fueron descritas en el constructor de la clase CharacterTextSplitter.
documentosDivididos = dividirTexto.split_documents(documentosTxt)
print("Documentos txt divididos con la clase CharacterTextSplitter:\n", documentosDivididos, "\n")
print("Cacho de documento txt dividido:\n", documentosDivididos[5], "\n\n\n")

#CARGAR UN DOCUMENTO PDF A LA VEZ Y DIVIDIRLO POR PÁGINAS CON LA CLASE PyPDFLoader DE LANGCHAIN:
#   - PyPDFLoader: Clase del paquete document_loaders que permite leer documentos PDF con la librería langchain. Su 
#     mayor ventaja es que de forma muy sencilla permite separar su contenido por página. 
#   - OnlinePDFLoader: Clase del paquete document_loaders que permite leer documentos PDF a través de un enlace. Se 
#     carga su contenido con el método .load() como se hace con el objeto DirectoryLoader.
from langchain.document_loaders import PyPDFLoader                 #PyPDFLoader: Carga 1 documento PDF a la vez.
#PyPDFLoader(): El constructor recibe como único parámetro el path global del archivo PDF al que se quiere acceder.
cargarDocumentoPDF = PyPDFLoader("C:/Users/diego/OneDrive/Documents/Aprendiendo/Python/5.-Inteligencia Artificial/0.-Archivos_Ejercicios_Python/0.-Python - Conceptos Básicos.pdf")
#PyPDFLoader().load_and_split(): Método que divide el texto grande del archivo PDF recibido en el constructor de la 
#clase PyPDFLoader por páginas, dentro un objeto document que incluye todo el contenido del PDF, esto después no 
#podrá ser dividido de nuevo con alguna clase del paquete text_splitter perteneciente a la librería langchain, por 
#lo que directamente con ella se creará el embedding de cada página.
paginasPDF = cargarDocumentoPDF.load_and_split()                   #División del texto de un PDF por página.
print("Documento PDF dividido por páginas con la clase PyPDFLoader de langchain:\n", paginasPDF[2], "\n")
print("Número total de páginas en el documento:\n", len(paginasPDF), "\n")
print("Contenido de la segunda página del documento PyPDFLoader:\n", paginasPDF[2].page_content, "\n")
print("Número de caracteres de la segunda página del documento PyPDFLoader:\n", len(paginasPDF[2].page_content), "\n")
print("Tipo de dato del resultado obtenido con la clase PyPDFLoader:\n", type(paginasPDF), "\n\n\n")

#CARGAR UN DOCUMENTO PDF, DIVIDIRLO POR PÁGINAS Y LUEGO ESAS PÁGINAS PARTIRLAS EN CACHOS CON LA LIBRERÍA PyPDF2:
#   - PdfReader: Esta clase de la librería open source PyPDF2 permite leer escribir y manipular archivos PDF con 
#     python.
#   - RecursiveCharacterTextSplitter: Esta clase permite dividir un texto grande en cachos para que pueda ser 
#     procesado por un modelo de lenguaje, pero limita los cachos en los que se divide el texto en forma de tokens, 
#     no de caracteres.
from PyPDF2 import PdfReader                                       #PdfReader: Carga 1 documento PDF a la vez.
from langchain.text_splitter import RecursiveCharacterTextSplitter #RecursiveCharacterTextSplitter: Cachos de tokens.
documentoPDF = PdfReader("C:/Users/diego/OneDrive/Documents/Aprendiendo/Python/5.-Inteligencia Artificial/0.-Archivos_Ejercicios_Python/2.-Op-Amp Inversor con Filtro Pasa Altas.pdf")
#PdfReader().pages: Con el atributo .pages se accede al número de páginas del documento pdf leído con el constructor 
#del objeto PdfReader.
#PdfReader().pages[i].extract_text(): Con el método .extract_text() se extrae todo el texto perteneciente a una 
#página en específico del documento pdf ingresado a través del constructor del objeto PdfReader.
#len(): Método que devuelve el tamaño de la lista a la que se le aplique, en este caso devuelve el número de páginas 
#del documento pdf.
textoPDF = ""                               #Variable textoPDF que después guardará todo el texto del pdf.
for i in range(len(documentoPDF.pages)):    #Bucle for que lee todas las páginas del documento.
    pagina = documentoPDF.pages[i]          #En la variable página se guarda el número de página.
    textoPagina = pagina.extract_text()     #En la variable textoPagina se guarda el texto contenido en cada página.
    textoPDF += textoPagina                 #Concatenación del texto extraído de cada página.
print("Texto extraído de un documento PDF completo con la clase PdfReader de PyPDF2:\n", textoPDF, "\n\n")
print("Documento PDF dividido por páginas con la clase PdfReader de PyPDF2:\n", documentoPDF.pages[2].extract_text(), "\n")
print("Número total de páginas en el documento:\n", len(documentoPDF.pages), "\n")
print("Tipo de dato del resultado obtenido con la clase PyPDF2:\n", type(documentoPDF), "\n\n\n")
#RecursiveCharacterTextSplitter(): El constructor del objeto lo que hace es indicar las características con las que se 
#separará en cachos un texto grande para que se pueda procesar con algún modelo de lenguaje, pero esto se hace eun 
#función de un número de tokens, no de caracteres. Esta clase se utiliza cuando se busca que los trozos sean pequeños.
# - chunk_size: Con este parámetro se indica el número de tokens de cada cacho de texto, llamado chunk, este número 
#   usualmente se encuentra entre 512 y 1000 tokens. Pero es importante mencionar que si el modelo considera que al 
#   cortar cierta parte del texto con el chunk_size indicado hace que pierda contexto, este número será cambiado 
#   automáticamente por el método .create_documents().
# - chunk_size: Con este parámetro se indica los caracteres que se entrelazan con el cacho que tiene alado, para que 
#   de esta forma no se pierda ninguna palabra.
# - length_function: Indica qué función se utilizará para contar el número de tokens de cada cacho, puede ser la 
#   función predefinida len(lista) o una función propia.
dividirPaginasPDF = RecursiveCharacterTextSplitter(chunk_size = 160, chunk_overlap = 10, length_function = len)
#CharacterTextSplitter().split_documents(): Método que divide el texto grande que recibe como parámetro en cachos 
#cuyas características fueron descritas en el constructor de la clase RecursiveCharacterTextSplitter.
chunksPaginasPDF = dividirPaginasPDF.create_documents([textoPDF])
print("Documento pdf dividido con la clase RecursiveCharacterTextSplitter:\n", chunksPaginasPDF, "\n")
print("Cacho de documento pdf dividido:\n", chunksPaginasPDF[10], "\n\n\n")
print("Cacho de documento pdf dividido:\n", chunksPaginasPDF[11].page_content, "\n\n\n")

#5.2.-VECTOR STORES: Los LLM convierten y asocian palabras a través de un vector llamado Embedding, la clase Vector 
#Stores ayuda a integrar bases de datos optimizadas para almacenar los vectores obtenidos después de procesar los 
#Chunks de información.
#Embeddings: Es la herramienta que convierte los pedazos de palabras obtenidos de un documento (chunks) en vectores
#numéricos.
from langchain.embeddings import OpenAIEmbeddings
#OpenAIEmbeddings(): El constructor de la clase OpenAIEmbeddings recibe los siguientes parámetros de OpenAI:
# - openai_api_key: Con este parámetro se roporciona la API key, que por buenas prácticas debe provenir de otro 
#   archivo.
# - model: Parámetro que indica el modelo que se quiere utilizar, en este caso se utilizará el más recomendado, que es 
#   el text-embedding-ada-002, que puede recibir como máximo 8191 y da como salida un vector con tamaño de 1536.
#https://platform.openai.com/docs/guides/embeddings/what-are-embeddings
modeloEmbedding = OpenAIEmbeddings(openai_api_key = ApiKey, model = "text-embedding-ada-002")
#Vectorstores: Representa una base de datos donde se asocian los chunks de palabras con sus embeddings 
#correspondientes para que así se alimente a cualquier modelo de lenguaje con nuestra información, pudiendo así 
#realizarle consultas sobre ella.
from langchain.vectorstores import FAISS    #FAISS: Vector store rápida, poco flexible y difícil de usar.
from langchain.vectorstores import Chroma   #Chroma: Vector store no tan rápida, flexible y fácil de usar.
#FAISS.from_documents(): Método que crea la base de datos de vectores tipo FAISS, esta recibe los chunks del texto 
#y el modelo de embeddings declarado para su conversión.
baseDeDatosFAISS_PyPDFLoader = Chroma.from_documents(paginasPDF, modeloEmbedding) #PyPDFLoader (langchain).
baseDeDatosFAISS_PdfReader = FAISS.from_documents(chunksPaginasPDF, modeloEmbedding) #PdfReader (PyPDF2).
baseDeDatosFAISS_DirectoryLoader = Chroma.from_documents(documentosDivididos, modeloEmbedding) #Dir..Load (langchain).

#5.3.-RETRIEVER: Este tipo de clases permiten extraer información de alguna fuente en específico que suelen ser VECTOR 
#STORES, sabiendo a dónde tiene que ir a buscar para obtener la respuesta solicitada a través de cadenas de búsqueda o 
#algoritmos de búsqueda de proximidad.
#El concepto de cadena de búsqueda se refiere a un modelo de lenguaje que se ha entrenado con un conjunto de datos de 
#preguntas y respuestas. Puede utilizarse para responder a preguntas sobre un documento personal ingresado a un VECTOR 
#STORE. Para ello se puede utilizar alguna de las siguientes herramientas:
from langchain.chains.question_answering import load_qa_chain
from langchain.chains import RetrievalQA
from langchain.chains import ConversationalRetrievalChain
# - load_qa_chain(): Objeto que carga una cadena de búsqueda de preguntas y respuestas preentrenada.
#   - llm: Indica el modelo de lenguaje o chat a utilizar.
#   - chain_type: Indica el tipo de cadena de búsqueda a utilizar:
#       - "stuff": Cadena de búsqueda predeterminada (LLM factual de Google AI) que es capaz de generar texto, 
#         traducir idiomas, escribir diferentes tipos de contenido creativo y responder a sus preguntas de manera 
#         informativa.
# - RetrievalQA.from_chain_type(): Método que crea una cadena de búsqueda de preguntas y respuestas de un tipo 
#   específico. Los tipos de cadenas de búsqueda disponibles son: "map_reduce", "refine" y "map_rerank".
#   - llm: Indica el modelo de lenguaje o chat a utilizar.
#   - chain_type: Indica el tipo de cadena de búsqueda a utilizar:
#       - "stuff": Cadena de búsqueda predeterminada (LLM factual de Google AI) que es capaz de generar texto, 
#         traducir idiomas, escribir diferentes tipos de contenido creativo y responder a sus preguntas de manera 
#         informativa.
#       - "map_reduce": Cadena de búsqueda que primero utiliza un retriever para recuperar documentos relevantes.
#       - "refine": Cadena de búsqueda que primero utiliza un retriever para recuperar documentos relevantes y 
#         luego utiliza el LLM para refinar las respuestas.
#       - "map_rerank": Cadena de búsqueda que primero utiliza un retriever para recuperar documentos relevantes y 
#         luego utiliza el LLM para reordenar las respuestas.
#   - retriever: Tipo de retriever que se utilizará para recuperar los documentos relevantes para contestar la 
#     pregunta.
#       - "faiss": Retriever predeterminado que utiliza el algoritmo de búsqueda vectorial faiss para recuperar los 
#         documentos relevantes.
#       - "multi_query_retriever": Este retriever genera variantes de la pregunta de entrada y luego utiliza un 
#         algoritmo de búsqueda vectorial para recuperar los documentos relevantes para cada variante.
#       - vectorStore.as_retriever(): El método as_retriever() convierte cualquier base de datos vectorial en un 
#         retriever para que de ahí se extraiga la información para responder la pregunta del usuario.
# - ConversationalRetrievalChain.from_llm(): Método que crea una cadena de búsqueda de preguntas y respuestas a través 
#   de un modelo de lenguaje probabilístico. El modelo de lenguaje se puede utilizar para generar respuestas más 
#   naturales y conversacionales a través de la memoria de un historial de chat.
#   - llm: Indica el modelo de lenguaje o chat a utilizar.
#   - chain_type: Indica el tipo de cadena de búsqueda a utilizar:
#       - "stuff": Cadena de búsqueda predeterminada (LLM factual de Google AI) que es capaz de generar texto, 
#         traducir idiomas, escribir diferentes tipos de contenido creativo y responder a sus preguntas de manera 
#         informativa.
#   - retriever: Tipo de retriever que se utilizará para recuperar los documentos relevantes para contestar la 
#     pregunta.
#       - "faiss": Retriever predeterminado que utiliza el algoritmo de búsqueda vectorial faiss para recuperar los 
#         documentos relevantes.
#       - "multi_query_retriever": Este retriever genera variantes de la pregunta de entrada y luego utiliza un 
#         algoritmo de búsqueda vectorial para recuperar los documentos relevantes para cada variante.
#       - vectorStore.as_retriever(): El método as_retriever() convierte cualquier base de datos vectorial en un 
#         retriever para que de ahí se extraiga la información para responder la pregunta del usuario.
#   - memory: Recibe un objeto de memoria que se utilizará para almacenar el historial de la cadena de búsqueda.
#   - prompt: Plantilla de pregunta variable que se utilizará para generar respuestas.
#   - verbose: Variable booleana que controla la información impresa en consola. Cuando verbose es True, el objeto 
#     ConversationChain imprimirá información sobre el proceso de generación de la conversación, incluyendo el prompt, 
#     los tokens generados, y las puntuaciones de los tokens, pero cuando es False, no se imprimirá ninguna 
#     información.
#   - return_source_documents: Variable booleana que por default se encuentra con valor de False, pero cuando vale 
#     True retorna la página de mis documentos en la cual se basó para contestar la pregunta.
cadenaBusquedaPreentrenada = load_qa_chain(llm = openaiLLM, chain_type = "stuff")
cadenaBusquedaPersonalizada = RetrievalQA.from_chain_type(llm = openaiLLM, chain_type = "map_reduce", 
                                                          retriever = baseDeDatosFAISS_PdfReader.as_retriever())
cadenaBusquedaHistorialChat = ConversationalRetrievalChain.from_llm(llm = openaiLLM, chain_type = "map_reduce", 
                                                                    retriever = baseDeDatosFAISS_DirectoryLoader.as_retriever(),
                                                                    return_source_documents = True)
#El concepto de búsqueda de proximidad se refiere a un algoritmo de filtrado que se puede utilizar para encontrar los 
#documentos más similares a una consulta realizada. Para ello se puede utiliza la siguiente herramienta:
# - FAISS_o_Chroma.from_documents().similarity_search(): El método similarity_search() utiliza el VECTOR STORE FAISS o 
#   Chroma para realizar una búsqueda de proximidad.
#Pregunta hecha al documento ingresado al programa a través de la librería PyPDFLoader de langchain.
preguntaDocumento_PyPDFLoader = "Dime algunos usos del lenguaje de programación Python" 
busqueda_PyPDFLoader = baseDeDatosFAISS_PyPDFLoader.similarity_search(preguntaDocumento_PyPDFLoader)
#Pregunta hecha al documento ingresado al programa a través de la librería PdfReader de PyPDF2.
preguntaDocumento_PdfReader = "Cómo decae la amplitud al modificar la frecuencia en un filtro pasa bajas?"
busqueda_PdfReader = baseDeDatosFAISS_PdfReader.similarity_search(preguntaDocumento_PdfReader)
#Pregunta hecha a los documentos ingresados al programa a través de la librería DirectoryLoader de langchain.
historialChat = []
preguntaDocumento_DirectoryLoader = "Cuales son las variables utilizadas para calcular la matriz de rigidez de un elemento?"
busquedaDirectoryLoader = baseDeDatosFAISS_DirectoryLoader.similarity_search(preguntaDocumento_DirectoryLoader)
#load_qa_chain().run(): El método run() se aplica a la cadena de búsqueda load_qa_chain, recibiendo como parámetros 
#el resultado del método similarity_search() y la pregunta realizada para que así se busque en la VECTOR STORE y se
#obtenga el resultado de la pregunta realizada en base a la información del documento txt, word, pdf, etc.
resultado_PyPDFLoader = cadenaBusquedaPreentrenada.run(
                                                    input_documents = busqueda_PyPDFLoader, 
                                                    question = preguntaDocumento_PyPDFLoader)
print("Cadena de Búsqueda load_qa_chain con base de datos vectorial FAISS al documento cargado con PyPDFLoader (langchain):\n", 
      str(resultado_PyPDFLoader), "\n\n")
#RetrievalQA.from_chain_type()({"query": pregunta}): A través de un diccionario con la key "query" se realiza una 
#pregunta a una cadena de búsqueda RetrievalQA.
resultado_PdfReader = cadenaBusquedaPersonalizada({"query" : preguntaDocumento_PdfReader})
print("Cadena de Búsqueda RetrievalQA con base de datos vectorial Chroma al documento cargado con PdfReader (PyPDF2):\n", 
      str(resultado_PdfReader), "\n\n")
#ConversationalRetrievalChain.from_llm()({"query": pregunta, "chat_history": listaHistorial}): A través de un 
#diccionario con la key "question" y "chat_history" se realiza una pregunta a una cadena de búsqueda de chat 
#ConversationalRetrievalChain y luego se almacena en una lista el historial de preguntas y respuestas.
resultado_DirectoryLoader = cadenaBusquedaHistorialChat({"question" : preguntaDocumento_DirectoryLoader, "chat_history" : historialChat})
print("Cadena de Búsqueda ConversationalRetrievalChain con base de datos vectorial FAISS al documento cargado con DirectoryLoader (langchain):\n", 
      str(resultado_DirectoryLoader), "\n\n")
print("Fuente de donde le cadena de búsqueda extrajo la respuesta de la pregunta hecha a los documentos DirectoryLoader:\n", 
      str(resultado_DirectoryLoader['source_documents']), "\n\n", 
      str(resultado_DirectoryLoader['source_documents'][0]), "\n\n", 
      str(resultado_DirectoryLoader['source_documents'][0].page_content), "\n\n\n")





#6.-AGENTES (Agents): Estos son modelos o cadenas a los cuales se les da acceso a una fuente o API para que puedan 
#tomar acción o proporcionar una respuesta que solucione una tarea en específico.
print("\n\n-----------------------------------------------6.-AGENTES-----------------------------------------------")
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
#resultado se entrega en forma de diccionario y será recibido como parámetro del método initialize_agent() y se debe 
#indicar también que modelo se está utilizando.
# - tool_names: A través de una lista se declaran los nombres de las tools que se quiera integrar al agente.
# - llm: Indica el modelo de lenguaje o chat a utilizar.
nombreHerramientas = ["serpapi", "llm-math", "wikipedia", "terminal"]
herramientasAgente = load_tools(nombreHerramientas, llm = openaiLLM)
print("Las herramientas que se utilizaron son:\n", str(herramientasAgente), "\n")
print("Sus nombres individuales son: ", str(herramientasAgente[0].name), ",",
                                        str(herramientasAgente[1].name), ",",
                                        str(herramientasAgente[2].name), "y", 
                                        str(herramientasAgente[3].name), "\n")
print("Lo que hacen respectivamente es:\n", str(herramientasAgente[0].description), ",\n",
                                            str(herramientasAgente[1].description), ",\n", 
                                            str(herramientasAgente[2].description), "y\n", 
                                            str(herramientasAgente[3].description), "\n\n")
#initialize_agent(): Método que sirve para anexar al agente las herramientas previamente cargadas al programa con el 
#método load_tools(), además en este se indica el LLM que se quiere utilizar y el tipo de agente.
# - llm: Indica el modelo de lenguaje o chat a utilizar.
# - tools: Indica el diccionario que contiene el nombre de las herramientas que se quiere enlazar al agente.
# - agent: En este parámetro se indica el nombre del tipo de agente. 
# - verbose: Variable booleana que controla la información impresa en consola. Cuando verbose es True, el objeto 
#   agente imprimirá información sobre el proceso de generación de la conversación, incluyendo el prompt, la 
#   herramienta que está utilizando para resolver cada parte del prompt, la respuesta dada por cada herramienta y 
#   la respuesta final del agente.
Agente = initialize_agent(tools = herramientasAgente, llm = openaiLLM,
                          agent = "zero-shot-react-description",
                          verbose = True)
#initialize_agent().run(): El método run() proporciona el valor de entrada del agente y luego lo ejecuta para que 
#podamos ver su resultado.
resultadoAgente = Agente.run("Quien es más viejo, el presidente actual de USA o Robert Downey Jr? Toma la edad más grande y saca su raíz cuadrada.")
print("Respuesta de Agente de tipo Zero Shot enlazado con la herramienta serpapi: ", str(resultadoAgente), "\n\n\n")
resultadoAgente = Agente.run("En cual carpeta de mi ordenador se encuentra el archivo 17.-Vibracion en Estructuras.mph?")
print("Respuesta de Agente de tipo Zero Shot enlazado con la herramienta serpapi: ", str(resultadoAgente), "\n\n\n")
resultadoAgente = Agente.run("What files are located in my current directory?")
print("Respuesta de Agente de tipo Zero Shot enlazado con la herramienta serpapi: ", str(resultadoAgente), "\n\n\n")