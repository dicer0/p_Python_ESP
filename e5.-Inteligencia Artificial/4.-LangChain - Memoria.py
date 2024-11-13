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





#3.-MEMORIA (Memory): Esta clase permite almacenar las preguntas y respuestas hechas entre el LLM y el usuario, 
#permitiendo así que se simule una conversación entre ambos.
print("\n-----------------------------------------------3.-MEMORIA-----------------------------------------------")
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
print("1.-Respuesta de Chat con Memoria Buffer:\n" + str(chatbotHistorial) + "\n\n")
#ConversationBufferMemory.chat_memory.messages: Dentro de la variable de memoria del chat se encuentra el valor 
#chat_memory, este almacena todos los roles del chat, ya sea el del usuario (Human) o el del modelo (AI), todo el 
#historial es guardado dentro de una lista interna llamada messages. 
print("\tHistorial del chat guardado en el objeto ConversationBufferMemory:\n" + str(memoriaHistorial.chat_memory.messages) + "\n\n")
#Debido al historial creado, esta nueva instrucción la contestará en función de lo que previamente le dije. 
chatbotHistorial.predict(input = "Como me llamo?")
print("\tHistorial del chat con memoria Buffer:\n" + str(memoriaHistorial.chat_memory.messages) + "\n\n")

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
print("2.-Respuesta de Chat con Memoria de Ventana:\n" + str(chatbotMensajes) + "\n\n")
#ConversationBufferWindowMemory.chat_memory.messages: Dentro de la variable de memoria del chat se encuentra el valor 
#chat_memory, este almacena todos los roles del chat, ya sea el del usuario (Human) o el del modelo (AI) y también las 
#partes del historial de la conversación incluidas en la ventana de memoria en una lista interna llamada messages. 
print("\tHistorial del chat guardado en el objeto ConversationBufferWindowMemory:\n" 
      + str(memoriaMensajes.chat_memory.messages) + "\n\n")
chatbotMensajes.predict(input = "What do I like?")
print("\tHistorial del chat con memoria de ventana:\n" + str(memoriaMensajes.chat_memory.messages) + "\n\n")
#Debido al historial creado, esta nueva instrucción la contestará en función de lo que previamente le dije, pero 
#ya con esto último se borrará el primer mensaje en el historial, porque solo indicamos que guarde k = 2, por lo 
#que almacenará solo los últimos 2 mensajes, incluyendo la respuesta del modelo, debido a esta situación no sabrá 
#como responder la última pregunta que le hice, entonces hay que tener cuidado porque al utilizar esta memoria, 
#el chat empezará a olvidar información.
chatbotMensajes.predict(input = "What do I like?")
#Aunque la variable de la memoria si guarda todo el historial de la conversación, solamente manda los últimos dos
#mensajes de este al modelo, por eso es que olvida cosas.
print("\tHistorial del chat con memoria de ventana ya cuando olvidó información:\n" + str(memoriaMensajes.chat_memory.messages) + "\n\n")

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
print("3.-Respuesta de Chat con Memoria de Resumen:\n" + str(chatbotResumen) + "\n\n")
#ConversationSummaryMemory.chat_memory.messages: Dentro de la variable de memoria del chat se encuentra el valor 
#chat_memory, este almacena todos los roles del chat, ya sea el del usuario (Human) o el del modelo (AI), y un resumen 
#de todo el historial, que se encuentra guardado dentro de una lista interna llamada messages.
chatbotResumen.predict(input = "Pero cuales son las mejores herramientas que puedo utilizar?")
print("\tHistorial del chat con memoria de resumen:\n" + str(memoriaResumen.chat_memory.messages) + "\n\n")
chatbotResumen.predict(input = "De donde puedo obtener un sintetizador de voz para que me pueda responder?")
print("\tHistorial del chat con memoria de resumen:\n" + str(memoriaResumen.chat_memory.messages) + "\n\n")

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
print("4.-Respuesta de Chat con Palabras Clave de Knowledge Graph:\n" + str(chatbotPalabrasClave) + "\n\n")
#ConversationKGMemory.memory.kg.get_triples(): Para obtener el Knowledge Graph que representa las palabras clave de 
#la conversación se debe acceder a su valor memory.kg dentro del objeto ConversationChain, para ahí aplicar el 
#método get_triples() y así obtener la lista de palabras clave que le dan contexto a la memoria de la conversación.
#Pero hay que tener muy en cuenta que esto puede tener errores cuando se utiliza un lenguaje que no sea el inglés.
chatbotPalabrasClave.predict(input = "Mi película favorita es Ironman, mis series favoritas son Daredevil y How I met your mother")
print("\tKnowledge Graph del chat:\n" + str(chatbotPalabrasClave.memory.kg.get_triples()) + "\n\n")
chatbotPalabrasClave.predict(input = "Mis habilidades técnicas son de desarrollador web, móvil, sistemas embebidos, robótica, etc.")
print("\tKnowledge Graph del chat:\n" + str(chatbotPalabrasClave.memory.kg.get_triples()) + "\n\n")
#ConversationKGMemory.chat_memory.messages: Dentro de la variable de memoria del chat se encuentra el valor 
#chat_memory, este almacena todos los roles del chat, ya sea el del usuario (Human) o el del modelo (AI) y también la  
#respuesta del chat en función del Knowledge Graph de la conversación guardada en la lista interna llamada messages. 
chatbotPalabrasClave.predict(input = "Cuál es mi nombre, a que me dedico y cual es mi serie favorita?")
print("\tHistorial del chat con memoria de Knowledge Graph:\n" + str(memoriaGraph.chat_memory.messages) + "\n\n")