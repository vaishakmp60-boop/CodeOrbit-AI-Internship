import re

def simple_chatbot(user_input):
    # Convert input to lowercase for easier matching
    user_input = user_input.lower()
    
    # Rule 1: Greetings
    if re.search(r'\b(hi|hello|hey|namaskara)\b', user_input):
        return "Hello! I am your CodeOrbit AI assistant. How can I help you today?"
    
    # Rule 2: Basic Check-in
    elif re.search(r'\bhow are you\b', user_input):
        return "I'm just a simple bot, but I'm functioning perfectly! Thanks for asking."
    
    # Rule 3: Internship questions
    elif re.search(r'\b(internship|task|deadline)\b', user_input):
        return "Your AI Internship tasks are due by October 22. We are going to crush it!"
        
    # Rule 4: Identity/Name
    elif re.search(r'\b(who are you|your name)\b', user_input):
        return "I am a basic rule-based chatbot built for the CodeOrbit AI internship."
    
    # Rule 5: Goodbye
    elif re.search(r'\b(bye|goodbye|exit)\b', user_input):
        return "Goodbye! Good luck with the rest of your internship!"
    
    # Fallback response for unknown input (Requirement for Task 1)
    else:
        return "I'm sorry, I didn't quite understand that. Could you try rephrasing?"

# Main loop to interact with the user in the terminal
print("Chatbot initialized. Type 'bye' to exit.")
while True:
    user_message = input("You: ")
    
    # Check if the user wants to end the chat
    if user_message.lower() in ['bye', 'goodbye', 'exit', 'quit']:
        print("Bot:", simple_chatbot(user_message))
        break
    
    # Get the bot's response based on the rules above
    response = simple_chatbot(user_message)
    print("Bot:", response)