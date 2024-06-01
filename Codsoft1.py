rules = {

    "hello": "Hi there! How can I help you today?",

    "how are you": "I'm just a bot, but I'm here to help you!",

    "what is your name": "I'm a simple rule-based chatbot.",

    "bye": "Goodbye! Have a great day!",

    "help": "Sure, I can help you. Please tell me what you need assistance with."

} 
import string

def normalize_input(user_input):

    return user_input.lower().translate(str.maketrans("", "", string.punctuation))

def get_response(user_input):

    normalized_input = normalize_input(user_input)

    for pattern, response in rules.items():

        if pattern in normalized_input:

            return response

    return "I'm sorry, I don't understand that. Can you please rephrase?"

def chatbot():

    print("Hello! I'm your chatbot. Type 'bye' to end the conversation.")

    while True:

        user_input = input("You: ")

        if "bye" in normalize_input(user_input):

            print("Chatbot: Goodbye! Have a great day!")
            break

        response = get_response (user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":

    chatbot()

import string

# Step 1: Define the rules and responses

rules = {

    "hello": "Hi there! How can I help you today?",

    "how are you": "I'm just a bot, but I'm here to help you!",

    "what is your name": "I'm a simple rule-based chatbot.",

    "bye": "Goodbye! Have a great day!",

    "help": "Sure, I can help you. Please tell me what you need assistance with."

}

# Step 2: Normalize the user input 
def normalize_input(user_input):

    return user_input.lower().translate(str.maketrans("", "", string.punctuation))

#Step 3: Match user input to rules

def get_response(user_input):

    normalized_input = normalize_input(user_input)

    for pattern, response in rules.items():

        if pattern in normalized_input:

            return response

    return "I'm sorry, I don't understand that. Can you please rephrase?"

#Step 4: Create the chatbot loop

def chatbot():

    print("Hellol I'm your chatbot. Type 'bye' to end the conversation.")

    while True:

        user_input=input("You: ")

        if "bye" in normalize_input(user_input):
            print("Chatbot: Goodbye! Have a great day!")
            break

        response = get_response(user_input)

        print(f"Chatbot: {response}")
# Step 5: Run the chatbot
if __name__ == "__main__": 
    chatbot()