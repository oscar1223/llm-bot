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


#Database stuff
