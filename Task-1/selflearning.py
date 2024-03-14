def conversation_chatbot(user_input):
    
    user_input = user_input.lower()

    
    if "how are you" in user_input:
        return "I'm pretty gud  , thanks for asking..,what's about you!"

    elif "what's your name" in user_input:
        return "I'm a chatbot, no specific name. How can I assist you today?"

    elif "tell me a joke" in user_input:
        return "Why don't scientists trust atoms? Because they make up everything!"

    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! If you have more questions, feel free to return."

    else:
        return "I'm here to chat! Ask me anything or share your thoughts."


while True:
    user_message = input("You: ")
    
    if user_message.lower() == "exit":
        print("Bot: Goodbye!")
        break

    response = conversation_chatbot(user_message)
    print("Bot:", response)