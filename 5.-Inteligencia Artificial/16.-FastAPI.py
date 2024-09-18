#API 
#IMPORTACIÓN DE CLASES: Cuando se quiera importar una clase, el nombre de esta no puede empezar con un número, 
#sino cuando la quiera importar obtendré un error y se va accediendo a las carpetas o también llamados paquetes 
#en la programación orientada a objetos (POO), por medio de puntos:
# - Directorio normal:      carpeta1/carpeta2/carpeta3
# - Directorio paquetes:    carpeta1.carpeta2.carpeta3
#La parte del directorio se coloca después de la palabra reservada from y la clase a importar después de import.
from POO_API_AsistenteVirtual import ChatGPT_TypeNotation

#IMPORTACIÓN DE LLAVE: Cuando se quiera utilizar una API que utiliza un key, por seguridad es de buenas prácticas 
#declararla en un archivo externo, además cabe mencionar que el nombre de dicho archivo y constante no pueden empezar 
#con un número, sino cuando la quiera importar obtendré un error y se va accediendo a las carpetas por medio de puntos:
# - Directorio normal:      carpeta1/carpeta2/carpeta3
# - Directorio paquetes:    carpeta1.carpeta2.carpeta3
#La parte del directorio se coloca después de la palabra reservada from y la llave a importar después de import.
from API_Keys.Llaves_ChatGPT_Bard_etc import LlaveChatGPT

#AsyncIO: Librería que permite escribir código concurrente (asíncrono) que puede realizar múltiples tareas al mismo 
#tiempo sin la necesidad de usar hilos (threads) o procesos múltiples. En lugar de bloquear el programa mientras se 
#espera una operación de I/O (entradas/salidas como leer de una base de datos, recibir datos de una API o interactuar 
#con un archivo), asyncio permite que otras tareas continúen ejecutándose.
import asyncio
#random: Librería para generar números aleatorios y realizar operaciones relacionadas con la aleatoriedad.
import random

#FastAPI: Es una bilbioteca para crear APIs web rápidas y eficientes. Está basada en la librería Starlette para la 
#gestión de solicitudes HTTP y la librería Pydantic para la validación de datos, lo que la convierte en una opción 
#ideal para construir APIs modernas y robustas. Sus mayores ventajas son:
# - Documentación Automática: Mientras se construyen los endpoints de la API (las carpetas o rutas de la URL) usando 
#   los 4 métodos HTTP que conforman el CRUD (Create, Read, Update y Delete): GET, POST, PUT y DELETE. Se estará 
#   creando automáticamente una documentación de su uso al acceder al endpoint URL/docs.
#       - Create -> POST: Método HTTP que permite mandar datos al endpoint de una API.
#       - Read ->   GET: Método HTTP que permite obtener los datos almacenados en algún endpoint de una API.
#       - Update -> PUT: Método HTTP que permite actualizar los datos previamente almacenados en un endpoint.
#       - Delete -> DELETE: Método HTTP que permite borrar los datos previamente almacenados en un endpoint.
# - Validación de Datos: Estos se realizan a través de la librería Pydantic, la cual realiza operaciones de anotación 
#   de datos con la siguiente sintaxis: nombreAtributo: Tipo de dato = "Valor por default".
import fastapi
#sse_starlette: Esta librería se utiliza en aplicaciones web que usen la bilbioteca FastAPI para habilitar el soporte 
#de Server-Sent Events (SSE); tecnología que permite al servidor enviar actualizaciones automáticas al cliente a través 
#de una conexión HTTP persistente, lo que facilita la transmisión continua de datos en tiempo real.
import sse_starlette


app = fastapi.FastAPI()

@app.get("/stream-example")
async def stream_example():
    """
    Example route for streaming text to the client, one word/token at a time.
    """
    async def stream_tokens():
        """
        Placeholder implementation for token streaming. Try running this route as-is to better understand how to
        stream data using Server-Sent Events (SSEs) in FastAPI.
        See this tutorial for more information: https://devdojo.com/bobbyiliev/how-to-use-server-sent-events-sse-with-fastapi
        """
        for token in ['hello', ', ', 'this ', 'is ', 'a ', 'streamed ', 'response.']:
            # fake delay:
            await asyncio.sleep(random.randint(0, 3))

            print(f"Yielding token: {token}")
            yield token

    return sse_starlette.sse.EventSourceResponse(stream_tokens())
# Your code/routes here (you may also keep code in separate files and import/it them here):