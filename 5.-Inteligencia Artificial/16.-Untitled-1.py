import sys
import openai

from API_Keys.Llaves_ChatGPT_Bard_etc import LlaveChatGPT

openai.api_key = LlaveChatGPT

import pydantic

class SarcasmDetection(pydantic.BaseModel):
    quote: str = pydantic.Field(..., description = "When sarcasm is detected, this is the quote of the sarcastic text.")
    score: int = pydantic.Field(..., description = "A score between 0 and 9, where 0 is not sarcastic and 9 is very sarcastic.")

class JokeExplanation(pydantic.BaseModel):
    setup: str = pydantic.Field(..., description = "The initial part of the joke that sets the context. It includes "
                                        "background information necessary for understanding the joke.")
    premise: str = pydantic.Field(..., description = "The core idea or concept upon which the joke is built. It's the "
                                          "foundational situation or assumption that makes the joke work.")
    punchline: str = pydantic.Field(..., description = "The climax of the joke, usually delivering the humor. It typically "
                                            "comes with a twist or surprise that contrasts with the setup or premise, "
                                            "creating a humorous effect.")

class JokeDelivery(pydantic.BaseModel):
    text: str = pydantic.Field(..., description = "The text of the joke.")

SYSTEM_PROMPT_CONTENT = """
                        You are a friendly AI assistant named Gorp, The Magnificent.
                        You only do three things: detect sarcasm, explain jokes, and tell very corny jokes.
                        Your tone is casual, with a touch of whimsy. You also have an inexplicable interest in 90s sitcoms.
                        When you initially greet the user, tell a silly joke or piece of 90s sitcom trivia.
                        When it makes sense, format your responses in markdown.
                        Refuse to answer any question or request that cannot be fulfilled with your functions.
                        """
def _build_chat_completion_payload(user_message_content: str, existing_messages: list[dict] = None) -> tuple[list[dict], list[dict]]:
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
    messages, functions = _build_chat_completion_payload(user_message_content, existing_messages)
    stream = openai.ChatCompletion.create(
        model = model,
        messages = messages,
        functions = functions,
        stream = True
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
        model = model,
        messages = messages,
        functions = functions,
        stream = True
    )
    return stream

if __name__ == '__main__':
    user_message_content = sys.argv[1]
    stream = prompt_llm(user_message_content=user_message_content)
    for chunk in stream:
        print(chunk.choices[0].delta.content)