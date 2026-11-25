print("WELCOME TO AI CHATBOT")
print("Type 'bye' to exit")

while True:
    user = input("You: ").lower().strip()

    if user in ["hello", "hi"]:
        print("Bot: Hello! Welcome!")
    elif user == "how are you":
        print("Bot: I am fine. How are you?")
    elif user == "what is your name":
        print("Bot: I am your Simple AI Chatbot!")
    elif user == "who created you":
        print("Bot: I was created using Python.")
    elif user == "what is python":
        print("Bot: Python is a programming language.")
    elif user == "bye":
        print("Bot: Goodbye!")
        break
    else:
        print("Bot: Sorry, I don't understand.")
