# Chatbot responses
responses = {
    "greeting": ["Hello! How can I assist you today?", "Hi! How can I help you today?"],
    "help": ["You can ask me about our products, services, or get help with your account."],
    "products": ["We offer a wide range of products like electronics, furniture, and clothing."],
    "services": ["We provide home delivery, warranty services, and customer support."],
    "account": ["For account-related inquiries, you can visit our account page or contact support."],
    "bye": ["Goodbye! Have a great day!", "Thank you for visiting! See you soon!"]
}

def chatbot_response(user_input):
    """Returns a response based on the user's input."""
    user_input = user_input.lower()
    
    if "hi" in user_input or "hello" in user_input:
        return responses["greeting"]
    
    elif "help" in user_input:
        return responses["help"]
    
    elif "product" in user_input or "item" in user_input:
        return responses["products"]
    
    elif "service" in user_input:
        return responses["services"]
    
    elif "account" in user_input:
        return responses["account"]
    
    elif "bye" in user_input or "goodbye" in user_input:
        return responses["bye"]
    
    else:
        return ["Sorry, I didn't quite catch that. Can you ask something else?"]

def chatbot():
    """Main chatbot interaction loop."""
    print("Welcome to our customer support chatbot!")
    print("Type 'bye' or 'goodbye' to end the conversation.")
    
    while True:
        user_input = input("You: ")
        
        if "bye" in user_input.lower() or "goodbye" in user_input.lower():
            response = chatbot_response(user_input)
            print(f"Chatbot: {response[0]}")
            break
        
        response = chatbot_response(user_input)
        print(f"Chatbot: {response[0]}")

if __name__ == "__main__":
    chatbot()
