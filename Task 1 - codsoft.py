import re
from datetime import datetime

# Function to calculate basic arithmetic
def calculate(expression):
    try:
        return eval(expression)
    except:
        return "Sorry, I couldn't calculate that. Make sure the input is valid!"

# Chatbot function with specific rules
def chatbot_response(user_input):
    user_input = user_input.lower().strip()  # Normalize input

    # Greeting responses
    if re.search(r'\b(hi|hello|hey)\b', user_input):
        return "Hello! How can I help you today?"
    
    # Farewell responses
    elif re.search(r'\b(bye|goodbye|exit)\b', user_input):
        return "Goodbye! Have a nice day!"
    
    # Response to "How are you?"
    elif re.search(r'\b(how are you|how are you doing)\b', user_input):
        return "I'm just a chatbot, but I'm doing great! Thanks for asking. How can I assist you?"
    
    # Ask for chatbot's name
    elif "your name" in user_input:
        return "I'm a simple rule-based chatbot, here to assist you!"

    
    
    # Simple arithmetic calculation
    elif re.search(r'\b(\d+\s*[+\-*/]\s*\d+)\b', user_input):
        result = calculate(re.search(r'\d+\s*[+\-*/]\s*\d+', user_input).group())
        return f"The result is {result}."
    
    # Generic help response
    elif "help" in user_input:
        return "Sure! You can ask me about the time, perform simple calculations, or just chat with me!"
    
    # Fallback response
    else:
        return "I'm sorry, I don't understand that. Could you rephrase your question?"

# Simulate a conversation
def run_chatbot():
    print("Chatbot: Hello! Type 'bye' to exit.")
    while True:
        user_query = input("You: ")
        if user_query.lower() in ["bye", "exit"]:
            print("Chatbot: Goodbye! Have a nice day!")
            break
        print("Chatbot:", chatbot_response(user_query))

# Run the chatbot
run_chatbot()
