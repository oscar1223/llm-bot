# AGENT TO QUERY DATABASE BY CHATING.
import os
import openai
import sqlite3
from dotenv import load_dotenv, find_dotenv
from langchain.agents import load_tools, initialize_agent, AgentType, create_sql_agent
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.sql_database import SQLDatabase
from langchain.llms import OpenAI

# read local .env file
_ = load_dotenv(find_dotenv())
openai.api_key = os.environ['OPENAI_API_KEY']

# Langchain to Database connection
llm_db = SQLDatabase.from_uri('C:/Users/oarauz/musicdb.db')

toolkit = SQLDatabaseToolkit(db=llm_db, llm=OpenAI(temperature=0))

# Instanciamos agent
agent_executor = create_sql_agent(
    llm=OpenAI(temperature=0),
    toolkit=toolkit,
    verbose=True,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION
)

agent_executor.run('Muestrame todos los registros de la tabla Album')
