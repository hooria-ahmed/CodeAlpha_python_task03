import nltk
import random
from nltk.chat.util import Chat, reflections

# List of jokes for more variety
joke_list = [
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "Why don't programmers like nature? Too many bugs!",
    "How do you comfort a JavaScript bug? You console it.",
    "Why was the math book sad? Because it had too many problems!"
]

# Define pairs of input and responses
pairs = [
    [
        r"my name is (.+)",
        ["Hello %1, nice to meet you! How can I assist?"]
    ],
    [
        r"hi|hello|hey",
        ["Hello!", "Hi there!", "Hey! How can I assist you today?"]
    ],
    [
        r"how are you?",
        ["I'm just a computer program, but thanks for asking!", "Doing well! What about you?"]
    ],
    [
        r"what is your name?",
        ["I'm your friendly chatbot, here to help!", "I go by many names, but you can call me ChatBot."]
    ],
    [
        r"tell me a joke",
        [random.choice(joke_list)]  # Selects a joke at random
    ],
    [
        r"quit",
        ["Bye! Take care!", "Goodbye! Have a great day!", "Catch you later!"]
    ],
    [
        r"(.*)",
        [
            "Whoa, that's deep. Can you simplify that for me?",
            "Hmm... I'm not sure about that. Can you say it differently?",
            "Did you really mean '{}' or was that a typo? 😆".format(random.choice(["something", "anything", "everything"])) if random.randint(1, 10) > 8 else "I spaced out for a second... What did you say?"
        ]
    ]
]

# Create the chatbot
chatbot = Chat(pairs, reflections)

# Start the conversation
print("Chatbot: Hi! I'm a chatbot. Type 'quit' to exit.")

# Introduce a slight random delay before starting
if random.randint(1, 5) == 3:
    print("... Sorry, I got distracted. What were we talking about?")

chatbot.converse()
