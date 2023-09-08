from dotenv import load_dotenv, find_dotenv
import openai
import os

import langchain
import re
from langchain.schema import AgentAction, AgentFinish
from typing import List, Union

from langchain import OpenAI, LLMChain
from langchain.tools import DuckDuckGoSearchRun

from langchain.agents import Tool, AgentExecutor, LLMSingleActionAgent, AgentOutputParser
from langchain.prompts import StringPromptTemplate


# read local .env file
_ = load_dotenv(find_dotenv())
openai.api_key = os.environ['OPENAI_API_KEY']

#
# Bot Medico para resolver dudas sobre pacientes y sintomas.
# Ejercicio para saber como crear un agente con memoria usando langchain.
#


# Definimos las herramientas que el agente usará.
search = DuckDuckGoSearchRun()

tools = [
    Tool(
        name='Search',
        func=search.run,
        description='Herramienta muy util cuando tienes que responder preguntas sobre temas varios'
    )
]

obj = search.run('¿Cuales son los principales efectos de un ataque epileptico?')

print(obj)
