
from POO_API_AsistenteVirtual import ChatGPT_TypeNotation

from API_Keys.Llaves_ChatGPT_Bard_etc import LlaveChatGPT

import asyncio
import random
import fastapi
import sse_starlette

app = fastapi.FastAPI()

@app.get("/stream-example")
async def stream_example():
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