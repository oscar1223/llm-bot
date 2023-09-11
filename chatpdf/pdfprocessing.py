from PyPDF2 import PdfReader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import ElasticVectorSearch, Pinecone, Weaviate, FAISS
from dotenv import load_dotenv, find_dotenv
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
import openai
import os
from langchain.memory import ConversationBufferMemory


# read local .env file
_ = load_dotenv(find_dotenv())
openai.api_key = os.environ['OPENAI_API_KEY']

#Leemos el documento
reader = PdfReader('./pdfs/napoleon.pdf')

#Leemos el pdf y lo insertamos en una variable llamada raw_text
raw_text = ''
for i, page in enumerate(reader.pages):
    text = page.extract_text()
    if text:
        raw_text += text

#Separamos el texto en trozos(chunks) para cuando se procese no llegar al limite de caracteres permitido.
text_splitter =CharacterTextSplitter(
    separator='\n',
    chunk_size=1000,
    chunk_overlap=200,
    length_function=len,
)

texts = text_splitter.split_text(raw_text)

# Descargamos las incrustaciones(embeddings) desde OpenAI
embeddings = OpenAIEmbeddings()

docsearch = FAISS.from_texts(texts, embeddings)
chain = load_qa_chain(OpenAI(temperature=0),
                      chain_type='stuff'
                      )

query = '¿Donde nacio Napoleon?, dime las páginas de donde has sacado esa información'
docs = docsearch.similarity_search(query)
respuesta = chain.run(input_documents=docs, question=query)

print(respuesta)









