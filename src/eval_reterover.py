import os
os.environ['GOOGLE_API'] = "AIzaSyDPLK5D2NL82CIoEd2Suzia2jRy8iPo-20"

import google.generativeai as genai
genai.configure(api_key=os.environ['GOOGLE_API'])

class MockRetriver:
    
    def generate(self,query,retrived_context):
    
        model = genai.GenerativeModel('gemini-2.5-flash')

        response = model.generate_content(f"""

        you are an a retrevied answer evalivator you are porvided with the user question
        and a retrived information from the vector database with the score your task is to check the 
        retrived answer the correct answer and if wrong say where is the mistake is and give correct answer

        Question:{query}

        Retrived_context:{retrived_context}

        """)

        return response.text