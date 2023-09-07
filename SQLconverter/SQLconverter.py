from dotenv import load_dotenv, find_dotenv
from langchain.agents import initialize_agent, AgentType, load_tools, tool
from langchain.agents.agent_toolkits import create_python_agent
from langchain.chat_models import ChatOpenAI
from langchain.llms import OpenAI
import openai
import os
import datetime

from langchain.tools import PythonREPLTool

# read local .env file
_ = load_dotenv(find_dotenv())
openai.api_key = os.environ['OPENAI_API_KEY']

# Get the current date
current_date = datetime.datetime.now().date()

# Define the date after which the model should be set to "gpt-3.5-turbo"
target_date = datetime.date(2024, 6, 12)

# Set the model variable based on the current date
if current_date > target_date:
    llm_model = "gpt-3.5-turbo"
else:
    llm_model = "gpt-3.5-turbo-0301"

llm = ChatOpenAI(temperature=0, model=llm_model)
tools = load_tools(["PythonREPLTool"], llm=llm)

converter_agent = initialize_agent(
    llm=llm,
    tools=tools,
    agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION,
    handle_parsing_errors=True,
    verbose=True
)

#Definimos las rutas de carga y descarga.
sql_ruta = ('./scripts-sql/procedure1.sql')
py_ruta = ('./py-scripts/')

response = converter_agent.run(f"""
Tengo un script SQL en esta ruta {sql_ruta}. En ese script se realizan varias acciones sobre una base de datos. Necesito que entiendas las acciones que realiza el script sql, las transcribas a lenguaje python y crees un script en python con dichas acciones en esta ruta {py_ruta}. Llama al script final procedure1.py
""")

print(response)