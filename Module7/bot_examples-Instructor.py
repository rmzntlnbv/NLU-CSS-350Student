## ----------------- A simple Example ----------------------
import random

# This list contains the random responses (you can add your own or translate them into your own language too)
random_responses = ["That is quite interesting, please tell me more.",
                    "I see. Do go on.",
                    "Why do you say that?",
                    "Funny weather we've been having, isn't it?",
                    "Let's change the subject.",
                    "Did you catch the game last night?"]

print("Hello, I'm your friendly chatbot, the simple robot.")
print("You can end this conversation at any time by typing 'bye'")
print("After typing each answer, press 'enter'")
print("How are you today?")

while True:
    # wait for the user to enter some text
    user_input = input("> ")
    if user_input.lower() == "bye":
        # if they typed in 'bye' (or even BYE, ByE, byE etc.), break out of the loop
        break
    else:
        response = random.choices(random_responses)[0]
    print(response)

print("It was nice talking to you, goodbye!")

## ----------------- Another Example ----------------------
import random

# List of random therapist-like responses
responses = [
    "Can you tell me more about that?",
    "How does that make you feel?",
    "Why do you think that is?",
    "That's interesting. Go on.",
    "Can you elaborate on that?",
    "I see. What else can you share?",
    "Why do you feel that way?",
    "Let's explore that further.",
    "What do you think that means?",
    "How do you usually handle situations like this?"
]

def chatbot():
    print("Hi! I'm your friendly chatbot. Let's talk. Type 'quit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            print("Chatbot: It was nice talking to you. Goodbye!")
            break
        else:
            # Pick a random response
            response = random.choice(responses)
            print(f"Chatbot: {response}")

# Run the chatbot
if __name__ == "__main__":
    chatbot()
