def chatbot():
    print("Chatbot: Hello! How can I help you?")

    while True:
        user_input = input("You: ").lower().strip()

        if user_input == "hello" or user_input == "hi":
            print("Chatbot: Hello! Nice to meet you.")

        elif user_input == "how are you":
            print("Chatbot: I'm doing great! Thanks for asking.")

        elif user_input == "bye" or user_input == "goodbye":
            print("Chatbot: Goodbye! Have a great day!")
            break

        elif user_input == "what is your name":
            print("Chatbot: My name is Python Chatbot.")

        elif user_input == "what can you do":
            print("Chatbot: I can respond to simple messages and have a basic conversation with you.")

        elif user_input == "thank you" or user_input == "thanks":
            print("Chatbot: You're welcome!")

        elif user_input == "help":
            print("Chatbot: You can say hello, ask how I am, ask my name, or say goodbye.")

        else:
            print("Chatbot: Sorry, I don't understand that.")

chatbot()