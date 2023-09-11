from PyPDF2 import PdfReader
from langchain import text_splitter
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import PyPDFLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter, RecursiveCharacterTextSplitter
from langchain.vectorstores import ElasticVectorSearch, Pinecone, Weaviate, FAISS, Chroma
from dotenv import load_dotenv, find_dotenv
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

import openai
import os
from langchain.memory import ConversationBufferMemory


# read local .env file
_ = load_dotenv(find_dotenv())
openai.api_key = os.environ['OPENAI_API_KEY']

#Leemos el documento
#reader = PdfReader('./pdfs/napoleon.pdf')
'''
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
'''

template='''
Use the following pieces of context to answer the question at the end. 
If you don't know the answer, just say that you don't know, don't try to make up an answer. 
Use 150 word maximun to answer.
Always include the page where the answer is.
Always say "thanks for asking!" at the end of the answer.
Context is delimited by triple dollar signs.

$$${context}$$$
Question: {question}
Helpful Answer:
'''

QA_CHAIN_PROMPT = PromptTemplate.from_template(template)

loader = PyPDFLoader('./pdfs/napoleon.pdf')
data = loader.load()

pdf_splitter = RecursiveCharacterTextSplitter()
all_splits = pdf_splitter.split_documents(data)

vectorstore = Chroma.from_documents(documents=all_splits, embedding=OpenAIEmbeddings())

question = 'Haz un resumen del ascenso de Napoleon al poder'

llm = ChatOpenAI(model_name='gpt-3.5-turbo', temperature=0)

qa_chain = RetrievalQA.from_chain_type(
    llm,
    retriever=vectorstore.as_retriever(),
    chain_type_kwargs={'prompt': QA_CHAIN_PROMPT})

result = qa_chain({'query':question})
print(result)









#faiss_index = FAISS.from_documents(pages, OpenAIEmbeddings)
#docs = faiss_index.similarity_search()
#for doc in docs:
#    print(str(doc.metadata['page'])+':', doc.page_content[:300])
# Descargamos las incrustaciones(embeddings) desde OpenAI
#embeddings = OpenAIEmbeddings()
#docsearch = FAISS.from_texts(texts, embeddings)
#chain = load_qa_chain(OpenAI(temperature=0),
#                             chain_type='stuff'
#                      )
#query = '¿Donde nacio Napoleon?, dime las páginas de donde has sacado esa información'
#docs = docsearch.similarity_search(query)
#respuesta = chain.run(input_documents=docs, question=query)
#print(respuesta)









