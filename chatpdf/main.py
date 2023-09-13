# Script para chatear por el terminal con el bot.
import os
import param

from chatpdf.pdfprocessing import load_db

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
        qa = load_db('./pdfs/napoleon.pdf', 'stuff', 4)
        try:
            question = input('¿Que quieres preguntar?\nHuman: ')
            respuesta = qa({'question': question, 'chat_history': chat_history})
            print(respuesta)
            answer = respuesta['answer']
            print('IA: '+answer)
            chat_history.append({'query': question, 'answer': answer})
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