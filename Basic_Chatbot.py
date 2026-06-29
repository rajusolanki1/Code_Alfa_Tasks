def chatbot():
    print("=== Welcome to Simple Chatbot ===")
    print("Type 'bye' to exit.\n")

    while True:
        user = input("You: ").lower()

        if user == "hello":
            print("Bot: Hi!")
        elif user == "how are you":
            print("Bot: I'm fine, thanks!")
        elif user == "what is your name":
            print("Bot: I am a simple Python chatbot.")
        elif user == "who created you":
            print("Bot: I was created using Python.")
        elif user == "bye":
            print("Bot: Goodbye! Have a nice day.")
            break
        else:
            print("Bot: Sorry, I don't understand that.")

chatbot()
