
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

import asyncio
import random
import fastapi
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