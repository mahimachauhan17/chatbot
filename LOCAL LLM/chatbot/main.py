from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = """
Answer the question below.

Here is the conversation history: {contex}

Question: {question}

Answer:
"""


model = OllamaLLM(model="llama3")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

def handel_conversation():
    context = ""
    print("Welcome to the AI Chatbot! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break


            result = chain.invoke({"context": "", "question": "hey how are you"})
            print("Bot: ", result)
            context += f"\nUser: {user_input}\nAI: {result}"


if __name__ == "__main__":
    handel_conversation()