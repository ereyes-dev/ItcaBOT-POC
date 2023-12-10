import openai
from PyPDF2 import PdfReader

# Set your OpenAI API key
openai.api_key = 'XXX'

def read_pdf(file_path):
    # Read the content of the PDF document
    with open(file_path, 'rb') as file:
        pdf_reader = PdfReader(file)
        text = ''
        for page_num in range(len(pdf_reader.pages)):
            text += pdf_reader.pages[page_num].extract_text()
    return text

def ask_question(question, context):
    # Use OpenAI API to generate an answer based on the question and the context
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Pregunta: {question}\nContexto: {context}",  # Use Spanish prompts
        temperature=0.7,
        max_tokens=150,
        n=1,
    )
    return response.choices[0].text.strip()

if __name__ == "__main__":
    # Replace 'your_pdf_path_here' with the path to your PDF file
    pdf_path = 'C:\\Users\\erick\\OneDrive\\Escritorio\\Erick Desktop\\Tesis\\App\\Backend\\POC-CustomChatbot\\docs\\cuentos-cortos-el-gato-con-botas.pdf'

    # Read the content of the PDF document
    pdf_text = read_pdf(pdf_path)

    # Mensaje de bienvenida
    print("Bienvenido al asistente inteligente de ITCA. Dime cómo puedo ayudarte.")

    while True:
        # Get user input for a question
        user_question = input("Hazme una pregunta (o escribe 'salir' para terminar): ")

        # Check if the user wants to exit
        if user_question.lower() == 'salir':
            break

        # Get the answer from the chatbot
        answer = ask_question(user_question, pdf_text)

        # Display the answer
        print("Respuesta:", answer)
