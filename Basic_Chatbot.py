import nltk
from nltk.chat.util import Chat, reflections

# Ensure that you have downloaded necessary NLTK data
nltk.download('punkt')
# Define the patterns and responses for the chatbot
patterns_responses = [
    (r'hi|hello|hey', ['Hello! How can I assist you today?', 'Hi there! How can I help you?']),
    (r'how are you?', ['I am doing great, thanks for asking!', 'I am just a chatbot, but I am doing fine!']),
    (r'what is your name?', ['I am a simple chatbot created to help you.', 'You can call me Chatbot.']),
    (r'bye|goodbye', ['Goodbye! It was nice talking to you.', 'See you later!']),
    (r'(.*)', ['Sorry, I didn’t quite catch that. Could you please rephrase?'])
]

# Create a chatbot with the defined patterns and responses
chatbot = Chat(patterns_responses, reflections)
# Function to start the chatbot
def start_chat():
    print("Chatbot: Hello! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['bye', 'goodbye']:
            print("Chatbot: Goodbye!")
            break
        response = chatbot.respond(user_input)
        print("Chatbot:", response)

# Start the chat
if __name__ == "__main__":
    start_chat()
