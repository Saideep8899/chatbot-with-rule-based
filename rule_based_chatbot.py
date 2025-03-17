import re

def chatbot():
    print("Hello! I'm your simple chatbot. Type 'exit' to end the conversation.")
    
    while True:
        user_input = input("You: ").lower()
        
        # Exit condition
        if user_input == "exit":
            print("Goodbye! Have a great day!")
            break
        
        # Rule-based responses
        if re.search(r"\b(hi|hello|hey)\b", user_input):
            print("Bot: Hello! How can I assist you today?")
        
        elif re.search(r"\b(bye|goodbye)\b", user_input):
            print("Bot: Goodbye! Take care!")
        
        elif re.search(r"\b(how are you|how are you doing)\b", user_input):
            print("Bot: I'm doing well, thank you for asking!")
        
        elif re.search(r"\b(name|your name)\b", user_input):
            print("Bot: My name is Chatbot. What's yours?")
        
        elif re.search(r"\b(help)\b", user_input):
            print("Bot: How can I help you? You can ask me anything.")
        
        elif re.search(r"\b(weather)\b", user_input):
            print("Bot: I can't check the weather, but you can use a weather app or website to get the latest updates!")
        
        else:
            print("Bot: I'm sorry, I didn't understand that. Could you please rephrase?")

# Run the chatbot
chatbot()
