from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file

import warnings
warnings.filterwarnings('ignore')

from langchain.chat_models import ChatOpenAI

#Example of ConversationBufferMemory

from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory


llm = ChatOpenAI(temperature=0.0)
memory = ConversationBufferMemory()
conversation = ConversationChain(
    llm=llm,
    memory=memory,
    verbose=True
)

respuesta = conversation.predict(input="What was my name?")

print(respuesta)

# Example of ConversationTokenBufferMemory
from langchain.memory import ConversationTokenBufferMemory

llm = ChatOpenAI(temperature=0.0)

memory = ConversationTokenBufferMemory(llm=llm, max_token_limit=30)
memory.save_context({"input": "AI is what?!"},
                    {"output": "Amazing!"})
memory.save_context({"input": "Backpropagation is what?"},
                    {"output": "Beautiful!"})
memory.save_context({"input": "Chatbots are what?"},
                    {"output": "Charming!"})

respuesta2 = memory.load_memory_variables({})
print(respuesta2)

# Example of ConversationSummaryBufferMemory
from langchain.memory import ConversationSummaryBufferMemory

# create a long string
schedule = "There is a meeting at 8am with your product team. \
You will need your powerpoint presentation prepared. \
9am-12pm have time to work on your LangChain \
project which will go quickly because Langchain is such a powerful tool. \
At Noon, lunch at the italian resturant with a customer who is driving \
from over an hour away to meet you to understand the latest in AI. \
Be sure to bring your laptop to show the latest LLM demo."

memory = ConversationSummaryBufferMemory(llm=llm, max_token_limit=100)
memory.save_context({"input": "Hello"}, {"output": "What's up"})
memory.save_context({"input": "Not much, just hanging"},
                    {"output": "Cool"})
memory.save_context({"input": "What is on the schedule today?"},
                    {"output": f"{schedule}"})

summary = memory.load_memory_variables({})
print(summary)

conversation = ConversationChain(
    llm=llm,
    memory=memory,
    verbose=True
)

respuesta3 = conversation.predict(input="What would be a good demo to show?")
print(respuesta3)