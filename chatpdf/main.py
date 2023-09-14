# Script para chatear por el terminal con el bot.
import os
import openai
from dotenv import load_dotenv, find_dotenv
from langchain import PromptTemplate, FAISS
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import PyPDFLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter

# read local .env file
_ = load_dotenv(find_dotenv())
openai.api_key = os.environ['OPENAI_API_KEY']

# Leemos el documento
template = '''
Use the following pieces of context to answer the question at the end. 
If you don't know the answer, just say that you don't know, don't try to make up an answer. 
Use 150 word maximum to answer.
Always include the number of the page from which you got the information.
When making a summary, always add the page number where it begins and the page number where it ends.
Always say "thanks for asking!" at the end of the answer.
Always response in Spanish.
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

    vectorstore = FAISS.from_documents(documents=docs,
                                       embedding=OpenAIEmbeddings()
                                       )

    datos = vectorstore.as_retriever(search_type='similarity', search_kwargs={'k': 4}, include_metadata=True)

    llm = ChatOpenAI(model_name='gpt-3.5-turbo', temperature=0)

    qa_chain = RetrievalQA.from_chain_type(llm=llm,
                                           retriever=datos,
                                           chain_type='stuff',
                                           chain_type_kwargs={'prompt': QA_CHAIN_PROMPT},
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
    '''
    memory = ConversationBufferMemory(memory_key="chat_history",
                                      return_messages=True,
                                      input_key='question',
                                      output_key='result'
                                      )
                                      '''
    while True:

        qa = load_db()
        try:
            question = input('¿Que quieres preguntar?\nHuman: ')
            respuesta = qa({'query': question})
            print(respuesta)
            answer = respuesta['result']
            print('IA: ' + answer)
        except KeyboardInterrupt:
            print('Algo ha fallado')

