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
import openai #openai: Librería que permite utilizar el LLM (Large Language Model) de ChatGPT con Python.
#Cabe mencionar que, al utilizar la API en su modo gratuito, solo se podrán realizar 100 llamadas a la API por día, 
#si se excede ese límite, se recibirá el error RateLimitError al intentar ejecutar el programa de Python.

#IMPORTACIÓN DE LLAVE: Cuando se quiera utilizar una API que utiliza un key, por seguridad es de buenas prácticas 
#declararla en un archivo externo, además cabe mencionar que el nombre de dicho archivo y constante no pueden empezar 
#con un número, sino cuando la quiera importar obtendré un error y se va accediendo a las carpetas por medio de puntos:
# - Directorio normal:      carpeta1/carpeta2/carpeta3
# - Directorio paquetes:    carpeta1.carpeta2.carpeta3
#La parte del directorio se coloca después de la palabra reservada from y la llave a importar después de import.
from API_Keys.Llaves_ChatGPT_Bard_etc import LlaveChatGPT

#openai.api_key: A través de este atributo perteneciente a la librería openai, se declara la API key, que previamente 
#debió ser creada y extraída de la página oficial de OpenAI, asociada a nuestro usuario: 
#https://platform.openai.com/account/api-keys 
openai.api_key = LlaveChatGPT

#pydantic: Librería que permite validar tipos de datos y opcionalmente aplicar transformaciones o lanzar errores si 
#los datos no coinciden con los tipos esperados. Por ejemplo, si se espera un número entero pero se recibe una cadena 
#como "42", Pydantic intentará convertirla a entero.
import pydantic

#SarcasmDetection: La clase hereda de la clase BaseModel, que a su vez pertenece a la librería pydantic y sirve para 
#crear modelos de tipos de datos. Estos modelos se utilizan para definir, validar, manejar y transformar datos.
#Utilice esta función cuando se detecte sarcasmo o cuando el usuario solicite que se detecte sarcasmo.
class SarcasmDetection(pydantic.BaseModel):
    #Anotación de tipo: Se utiliza principalmente para documentar y mejorar la legibilidad del código, pero cuando la 
    #clase herede de alguna herramienta de autocompletado o validación, las anotaciones de tipo sirven para especificar 
    #el tipo de dato que se espera para una variable, atributo o parámetro de función. Su sintaxis es la siguiente:
    # nombreAtributo: Tipo de dato
    #   - pydantic.Field(): Método de la librería Pydantic que se usa para configurar validaciones de datos, establecer 
    #     sus valores predeterminados, agregar descripciones y definir alias para los atributos en un modelo de datos. 
    #     Esto mejora la claridad del código al asegurar que los campos del modelo cumplan con las expectativas y se 
    #     cree su documentación. Para ello el método recibe los siguientes parámetros:
    #       - default: Establece un valor predeterminado para el atributo. Si no se proporciona un valor, se debe 
    #         usar ... para indicar que el campo es obligatorio.
    #       - default_factory: Permite proporcionar una función que genera el valor predeterminado para el campo. Esto 
    #         es útil para valores que necesitan ser calculados o generados dinámicamente.
    #       - title: Proporciona un título para el campo, que puede ser útil para la documentación.
    #       - description: Ofrece una descripción del campo, mejorando la claridad del propósito del atributo en la 
    #         documentación del modelo.
    #       - alias: Define un nombre alternativo para el campo, permitiendo que el campo sea referenciado con un 
    #         nombre diferente en la entrada y salida de datos.
    #       - const: Indica que el valor del campo debe ser constante y no puede cambiar una vez asignado.
    #       - gt (greater than >): Establece una restricción de valor mayor que a un número específico.
    #       - ge (greater than or equal >=): Establece una restricción de valor mayor o igual a un número específico.
    #       - lt (less than <): Establece una restricción de valor menor que a un número específico.
    #       - le (less than or equal <=): Establece una restricción de valor menor o igual a un número específico.
    #       - max_length: Define la longitud máxima permitida para cadenas de texto o listas.
    #       - min_length: Define la longitud mínima permitida para cadenas de texto o listas.
    #       - regex: Permite validar que el valor del campo coincide con una expresión regular específica.
    #       - example: Proporciona un ejemplo del valor que se espera para el campo, útil para la documentación y la 
    #         generación de esquemas.
    quote: str = pydantic.Field(..., description = "When sarcasm is detected, this is the quote of the sarcastic text.")
    score: int = pydantic.Field(..., description = "A score between 0 and 9, where 0 is not sarcastic and 9 is very sarcastic.")

#JokeExplanation: La clase hereda de la clase BaseModel, que a su vez pertenece a la librería pydantic y sirve para 
#crear modelos de tipos de datos. Estos modelos se utilizan para definir, validar, manejar y transformar datos.
#Utilice esta función cuando se detecte un chiste o el usuario solicite que se explique un chiste (donde se debe 
#proporcionar una explicación).
class JokeExplanation(pydantic.BaseModel):
    #Anotación de tipo: Se utiliza principalmente para documentar y mejorar la legibilidad del código, pero cuando la 
    #clase herede de alguna herramienta de autocompletado o validación, las anotaciones de tipo sirven para especificar 
    #el tipo de dato que se espera para una variable, atributo o parámetro de función. Su sintaxis es la siguiente:
    # nombreAtributo: Tipo de dato
    #   - pydantic.Field(): Método de la librería Pydantic que se usa para configurar validaciones de datos, establecer 
    #     sus valores predeterminados, agregar descripciones y definir alias para los atributos en un modelo de datos. 
    #     Esto mejora la claridad del código al asegurar que los campos del modelo cumplan con las expectativas y se 
    #     cree su documentación. Para ello el método recibe los siguientes parámetros:
    #       - default: Establece un valor predeterminado para el atributo. Si no se proporciona un valor, se debe 
    #         usar ... para indicar que el campo es obligatorio.
    #       - description: Ofrece una descripción del campo, mejorando la claridad del propósito del atributo en la 
    #         documentación del modelo.
    setup: str = pydantic.Field(..., description = "The initial part of the joke that sets the context. It includes "
                                        "background information necessary for understanding the joke.")
    premise: str = pydantic.Field(..., description = "The core idea or concept upon which the joke is built. It's the "
                                          "foundational situation or assumption that makes the joke work.")
    punchline: str = pydantic.Field(..., description = "The climax of the joke, usually delivering the humor. It typically "
                                            "comes with a twist or surprise that contrasts with the setup or premise, "
                                            "creating a humorous effect.")

#JokeExplanation: La clase hereda de la clase BaseModel, que a su vez pertenece a la librería pydantic y sirve para 
#crear modelos de tipos de datos. Estos modelos se utilizan para definir, validar, manejar y transformar datos.
#Utilice esta función cuando quiera contar un chiste. Use un poco de capricho y cuente chistes aparentemente al azar. 
#Pero también cuente chistes cuando el usuario se lo pida. Cuente sólo chistes con comedia limpia.
class JokeDelivery(pydantic.BaseModel):
    #Anotación de tipo: Se utiliza principalmente para documentar y mejorar la legibilidad del código, pero cuando la 
    #clase herede de alguna herramienta de autocompletado o validación, las anotaciones de tipo sirven para especificar 
    #el tipo de dato que se espera para una variable, atributo o parámetro de función. Su sintaxis es la siguiente:
    # nombreAtributo: Tipo de dato
    #   - pydantic.Field(): Método de la librería Pydantic que se usa para configurar validaciones de datos, establecer 
    #     sus valores predeterminados, agregar descripciones y definir alias para los atributos en un modelo de datos. 
    #     Esto mejora la claridad del código al asegurar que los campos del modelo cumplan con las expectativas y se 
    #     cree su documentación. Para ello el método recibe los siguientes parámetros:
    #       - default: Establece un valor predeterminado para el atributo. Si no se proporciona un valor, se debe 
    #         usar ... para indicar que el campo es obligatorio.
    #       - description: Ofrece una descripción del campo, mejorando la claridad del propósito del atributo en la 
    #         documentación del modelo.
    text: str = pydantic.Field(..., description = "The text of the joke.")

#Constantes: En Python no existen las constantes, pero se puede denotar la existencia simbolica de una a través de 
#indicar el nombre de una variable en mayúsculas: NOMBRE_CONSTANTE = VALOR
SYSTEM_PROMPT_CONTENT: str = (
    f"You are a friendly AI assistant named Gorp, The Magnificent. "
    f"You only do three things: detect sarcasm, explain jokes, and tell very corny jokes. "
    f"Your tone is casual, with a touch of whimsy. You also have an inexplicable interest in 90s sitcoms. "
    f"When you initially greet the user, tell a silly joke or piece of 90s sitcom trivia. "
    f"When it makes sense, format your responses in markdown. "
    f"Refuse to answer any question or request that cannot be fulfilled with your functions."
)

def _build_chat_completion_payload(
        user_message_content: str,
        existing_messages: list[dict] = None
) -> tuple[list[dict], list[dict]]:
    """
    Convenience function to build the messages and functions lists needed to call the chat completions service.

    :param user_message_content: the string of the user message
    :param existing_messages: an optional list of existing messages
    :return: tuple of list[dict] (messages) and list[dict] (functions)
    """
    if not existing_messages:
        existing_messages = []

    system_message = {"role": "system", "content": SYSTEM_PROMPT_CONTENT}
    user_message = {"role": "user", "content": user_message_content}
    all_messages = [system_message] + existing_messages + [user_message]

    sarcasm_function = {
        "name": "SarcasmDetection",
        "parameters": SarcasmDetection.schema()
    }

    joke_explanation_function = {
        "name": "JokeExplanation",
        "parameters": JokeExplanation.schema()
    }

    joke_delivery = {
        "name": "JokeDelivery",
        "parameters": JokeDelivery.schema()
    }

    all_functions = [sarcasm_function, joke_explanation_function, joke_delivery]

    return all_messages, all_functions

DEFAULT_MODEL = "gpt-3.5-turbo"

def prompt_llm(user_message_content: str, existing_messages: list[dict] = None, model: str = DEFAULT_MODEL):
    """
    Send a new user message string to the LLM and get back a response.

    :param user_message_content: the string of the user message
    :param existing_messages: an optional list of existing messages
    :param model: the OpenAI model
    :return: a Stream of ChatCompletionChunk instances
    """
    messages, functions = _build_chat_completion_payload(user_message_content, existing_messages)
    stream = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        functions=functions,
        stream=True
    )
    return stream

async def prompt_llm_async(user_message_content: str, existing_messages: list[dict] = None, model: str = DEFAULT_MODEL):
    """
    Asynchronously send a new user message string to the LLM and get back a response.

    :param user_message_content: the string of the user message
    :param existing_messages: an optional list of existing messages
    :param model: the OpenAI model
    :return: a Stream of ChatCompletionChunk instances
    """
    messages, functions = _build_chat_completion_payload(user_message_content, existing_messages)
    stream = await openai.ChatCompletion.acreate(
        model=model,
        messages=messages,
        functions=functions,
        stream=True
    )
    return stream

if __name__ == '__main__':
    import sys
    user_message_content = sys.argv[1]
    stream = prompt_llm(user_message_content=user_message_content)
    for chunk in stream:
        print(chunk.choices[0].delta.content)