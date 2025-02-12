import nltk
from nltk.chat.util import Chat, reflections
import logging

# Define advanced chatbot responses
pairs = [
    # ...existing pairs...
    ["hi|hello|hey", ["Hello!", "Hi there!", "Hey!"]],
    ["how are you?", ["I'm just a bot, but I'm doing fine!", "I'm good, thanks for asking!"]],
    ["what is your name?", ["I'm a simple chatbot!", "Call me ChatBot!"]],
    ["bye|goodbye", ["Goodbye!", "See you later!", "Bye! Have a great day!"]],
    ["what can you do?", ["I can chat with you!", "I can answer your questions!"]],
    ["who created you?", ["I was created by a developer!", "A developer built me!"]],
    ["what is your favorite color?", ["I like blue!", "Red is my favorite color!"]],
    ["where are you from?", ["I'm from the internet!", "I live in the cloud!"]],
    ["tell me a joke", ["Why don't scientists trust atoms? Because they make up everything!", "Why did the scarecrow win an award? Because he was outstanding in his field!"]],
    ["what is the meaning of life?", ["42", "To find happiness and share it with others."]],
    # Add more complex patterns
    ["(.*) your name?", ["My name is ChatBot.", "You can call me ChatBot."]],
    ["(.*) created you?", ["I was created by a developer.", "A developer built me."]],
    ["(.*) (location|city)?", ["I'm from the internet.", "I live in the cloud."]],
    ["(.*) weather (.*)", ["I'm not sure about the weather.", "I can't check the weather right now."]],
]

class AdvancedChatBot:
    def __init__(self):
        self.chatbot = Chat(pairs, reflections)
        logging.basicConfig(filename='chatbot.log', level=logging.INFO)

    def get_response(self, user_input):
        response = self.chatbot.respond(user_input)
        if not response:
            response = "I'm sorry, I don't understand that."
        self.log_interaction(user_input, response)
        return response

    def log_interaction(self, user_input, response):
        logging.info(f"User: {user_input} | ChatBot: {response}")
