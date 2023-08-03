'''from langchain.llms import OpenAI
from langchain.schema import HumanMessage

llm = OpenAI(openai_api_key='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')

text = 'Cual es la distancia que existe entre el sol y el ultimo planeta del sistema solar, y cual es el nombre de este?'

message = [HumanMessage(contex=text)]

response = llm.predict_messages(message)
print(response)

'''
import openai
import os

from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())# read local .env file
openai.api_key = os.environ['OPENAI_API_KEY']

def get_completion(prompt, model='gpt-3.5-turbo'):
    messages = [{'role': 'user', 'content': prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0
    )
    return response.choices[0].message['content']

respuesta = get_completion('¿Cual es la distacia entre el Sol y Jupiter?')

print(respuesta)