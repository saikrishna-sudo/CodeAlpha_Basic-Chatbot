import random
import spacy

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

# Sample responses
responses = {
    "greeting": ["Hi there!", "Hello!", "Hey! How can I help you?"],
    "how_are_you": ["I'm good, how about you?", "Doing well, thank you!", "I'm fine, thank you! How are you?"],
    "goodbye": ["Goodbye!", "See you later!", "Take care!"],
    "default": ["I'm sorry, I don't understand that.", "Could you please rephrase?", "I'm not sure I follow."]
}

# Intent keywords
intent_keywords = {
    "greeting": ["hello", "hi", "hey"],
    "how_are_you": ["how are you", "how's it going", "how do you do"],
    "goodbye": ["bye", "goodbye", "see you", "take care"]
}

def get_intent(user_input):
    doc = nlp(user_input.lower())
    for intent, keywords in intent_keywords.items():
        for keyword in keywords:
            if keyword in doc.text:
                return intent
    return "default"

def generate_response(intent):
    return random.choice(responses[intent])

def chatbot():
    print("Chatbot: Hello! How can I help you today? (type 'bye' to exit)")
    while True:
        user_input = input("You: ")
        if "bye" in user_input.lower():
            print("Chatbot: Goodbye!")
            break
        intent = get_intent(user_input)
        response = generate_response(intent)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    chatbot()
