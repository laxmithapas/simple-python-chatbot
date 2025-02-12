from advanced_chatbot import AdvancedChatBot

# Create an instance of the advanced chatbot
chatbot = AdvancedChatBot()

# Run chatbot
print("Advanced ChatBot: Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() in ["bye", "goodbye"]:
        print("ChatBot: Goodbye!")
        break
    response = chatbot.get_response(user_input)
    print("ChatBot:", response)
