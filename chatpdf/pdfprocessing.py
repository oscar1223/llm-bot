from langchain.chains import RetrievalQA
from langchain.chains.question_answering import load_qa_chain
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import PyPDFLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS, Chroma, Pinecone
from dotenv import load_dotenv, find_dotenv
from langchain.prompts import PromptTemplate
import streamlit as st, pinecone
import openai
import os
import pinecone
from langchain.vectorstores.base import VectorStoreRetriever

# read local .env file
_ = load_dotenv(find_dotenv())
openai.api_key = os.environ['OPENAI_API_KEY']
pinecone_api_key = pinecone.api_key = os.environ['PINECONE_API_KEY']

#Leemos el documento
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
#index = pinecone.Index('https://qaindex-92149fa.svc.gcp-starter.pinecone.io')

pdf_splitter = RecursiveCharacterTextSplitter()
all_splits = pdf_splitter.split_documents(data)




#vectorstore = Chroma.from_documents(documents=data, embedding=OpenAIEmbeddings())
#retriever = VectorStoreRetriever(vectorstore=vectorstore)
faiss_index = FAISS.from_documents(data, OpenAIEmbeddings())

#pinecone.init(api_key='55b25d59-23c8-466a-968e-a4d2d690f09a', enviroment='gcp-starter')

embedding = OpenAIEmbeddings()
#vectordb = Pinecone.from_documents(data, embedding, index_name=index)


question = '¿Donde nacio Napoleon?'

llm = ChatOpenAI(model_name='gpt-3.5-turbo', temperature=0, verbose=True)

qa_chain = load_qa_chain(llm=llm,
                         chain_type='stuff',
                         prompt=QA_CHAIN_PROMPT,
                         verbose=True
                         )
docs = faiss_index.similarity_search(question, include_metadata=True)
result = qa_chain.run(input_documents=docs, question=question, return_only_outputs=True, verbose=True)
print(result)











