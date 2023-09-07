from dotenv import load_dotenv, find_dotenv
from langchain.llms import OpenAI
import openai
import os

# read local .env file
_ = load_dotenv(find_dotenv())
openai.api_key = os.environ['OPENAI_API_KEY']


