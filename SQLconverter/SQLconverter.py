from dotenv import load_dotenv, find_dotenv
from langchain import OpenAI
from langchain.agents import AgentType
from langchain.agents.agent_toolkits import create_python_agent
from langchain.chat_models import ChatOpenAI
from langchain.tools import PythonREPLTool
from langchain.python import PythonREPL

import openai
import os

from langchain.utilities import PythonREPL

# read local .env file
_ = load_dotenv(find_dotenv())
openai.api_key = os.environ['OPENAI_API_KEY']

#Definimos las rutas de carga y descarga.
sql_ruta = ('./scripts-sql/procedure1.sql')
py_ruta = ('./py-scripts/procedure1.py')

#Preparamos un buen prompt
prompt = f'''
Necesito un script en python el cual realice las mismas funciones que el script sql de esta ruta {sql_ruta}.\
Debes leer el script sql y traducirlo a lenguaje python para que ambos scripts realicen los mismos procesos sobre la base de datos.\
Despues debes escribir ese codigo python en el fichero de esta ruta {py_ruta}.
'''

#Creamos agente.
'''
agent_executor = create_python_agent(
    llm=ChatOpenAI(temperature=0, model="gpt-3.5-turbo-0613"),
    tool=PythonREPLTool(),
    verbose=True,
    agent_type=AgentType.OPENAI_FUNCTIONS,
    agent_executor_kwargs={"handle_parsing_errors": True},
)
'''
agent_executor = create_python_agent(
    llm=OpenAI(temperature=0, max_tokens=1000),
    tool=PythonREPLTool(),
    verbose=True,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
)



response = agent_executor.run(prompt)



print(response)