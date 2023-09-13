# Script para chatear por el terminal con el bot.
import os

import openai
import param
from dotenv import load_dotenv, find_dotenv
from langchain import PromptTemplate
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import PyPDFLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.vectorstores.base import VectorStoreRetriever

from chatpdf.pdfprocessing import load_db


# read local .env file
_ = load_dotenv(find_dotenv())
openai.api_key = os.environ['OPENAI_API_KEY']

#Leemos el documento
template = '''
Use the following pieces of context to answer the question at the end. 
If you don't know the answer, just say that you don't know, don't try to make up an answer. 
Use 150 word maximum to answer.
Always include the page where the answer is.
Always say "thanks for asking!" at the end of the answer.
Context is delimited by triple dollar signs.

$$${context}$$$

Question: {question}
Helpful Answer:
'''




def load_db():
    QA_CHAIN_PROMPT = PromptTemplate.from_template(template)
    # Cargamos documento
    loader = PyPDFLoader('./pdfs/napoleon.pdf')
    data = loader.load()

    pdf_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1500,
        chunk_overlap=150,
        separators=["\n\n", "\n", "(?<=\. )", " ", ""]
    )

    docs = pdf_splitter.split_documents(data)

    persist_directory = './pdfs/chroma/'

    vectorstore = Chroma.from_documents(documents=docs,
                                        embedding=OpenAIEmbeddings(),
                                        persist_directory=persist_directory)

    retriever = VectorStoreRetriever(vectorstore=vectorstore)

    #memory = ConversationBufferWindowMemory(memory_key="chat_history", return_messages=True)

    llm = ChatOpenAI(model_name='gpt-3.5-turbo', temperature=0)

    '''
    #Chain to form
    qa = ConversationalRetrievalChain.from_llm(
        llm,
        retriever=retriever,
        chain_type=chain_type,
        memory=memory,
        input_documents=docs,
        return_source_documents=True,
        condense_question_prompt=QA_CHAIN_PROMPT,
        verbose=True
    )
    '''
    qa_chain = RetrievalQA.from_chain_type(llm,
                                           retriever=retriever,
                                           chain_type='stuff',
                                           chain_type_kwargs={'prompt': QA_CHAIN_PROMPT},
                                           chain_kwargs={'input_documents': docs},
                                           verbose=True
                                           )

    return qa_chain

if __name__ == '__main__':
    print(
        '''
                    #######################################################################\n
                    \b Bienvenido a CHATPDF BOT desarrollado por Óscar.\b\n
                    Podras hacerme todas las preguntas que quieras acerca del\n
                    pdf de Napoleón Bonaparte donde explica su vida.\n
                    #######################################################################
        '''
    )
    chat_history = []
    while True:
        qa = load_db()
        try:
            question = input('¿Que quieres preguntar?\nHuman: ')
            respuesta = qa({'query': question})
            print(respuesta)
            answer = respuesta['result']
            print('IA: '+answer)
            chat_history = [(question, answer)]
        except KeyboardInterrupt:
            print('Algo ha fallado')

'''
def convchain(self, query):
    if not query:
        return pn.WidgetBox(pn.Row('User:', pn.pane.Markdown("", width=600)), scroll=True)
    result = self.qa({"question": query, "chat_history": self.chat_history})
    self.chat_history.extend([(query, result["answer"])])
    self.db_query = result["generated_question"]
    self.db_response = result["source_documents"]
    self.answer = result['answer'] 
    self.panels.extend([
        pn.Row('User:', pn.pane.Markdown(query, width=600)),
        pn.Row('ChatBot:', pn.pane.Markdown(self.answer, width=600, style={'background-color': '#F6F6F6'}))
    ])
    inp.value = ''  #clears loading indicator when cleared
    return pn.WidgetBox(*self.panels,scroll=True)

'''