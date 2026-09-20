def chatbot():
    print("=" * 55)
    print("🤖 Welcome to Rule-Based AI Chatbot!")
    print("Type 'help' to see what I can do.")
    print("Type 'bye', 'exit', or 'quit' to end the chat.")
    print("=" * 55)
    while True:
        user_input = input("\nYou: ").strip().lower()
        if user_input in ["hello", "hi", "hey", "good morning", "good afternoon", "good evening"]:
            print("Bot: Hello! 👋 How can I help you today?")
        elif user_input in ["how are you", "how are you?"]:
            print("Bot: I'm doing great! Thanks for asking. 😊")
        elif user_input in ["what is your name", "what's your name", "your name"]:
            print("Bot: I'm DecodeBot, a simple rule-based AI chatbot.")
        elif user_input in ["who are you", "what are you"]:
            print("Bot: I am a rule-based chatbot created using Python if-else logic.")
        elif user_input in ["what can you do", "help", "menu"]:
            print("Bot: I can respond to greetings, answer simple predefined questions,")
            print("     tell you the time/date request format, and end the conversation.")
        elif user_input in ["thanks", "thank you", "thankyou"]:
            print("Bot: You're welcome! 😊")
        elif user_input in ["what is ai", "what is artificial intelligence", "define ai"]:
            print("Bot: Artificial Intelligence is the field of creating systems that")
            print("     can perform tasks that normally require human intelligence.")
        elif user_input in ["what is python", "define python"]:
            print("Bot: Python is a popular programming language known for its simple syntax.")
        elif user_input in ["bye", "goodbye", "exit", "quit"]:
            print("Bot: Goodbye! 👋 Keep learning and building!")
            break
        else:
            print("Bot: Sorry, I don't understand that yet.")
            print("Bot: Try a greeting, 'help', 'what is AI', or 'bye'.")
if __name__ == "__main__":
    chatbot()
