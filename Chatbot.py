# import the regular expression module to handle pattern matching
import re
# A dictionary that maps keywords to predefined responses
responses = {
    "hello": "Hello! How can I assist you today?",
    "help": "Sure! What do you need help with?",
    "bye": "Goodbye! Have a great day!",
    "thanks": "You're welcome! If you have any more questions, feel free to ask.",
    "default": "I'm sorry, I don't understand. Can you please rephrase?"
    
}
# Function to get a response based on user input
def chatbot_response(user_input):
    # Convert the input to lowercase for case-insensitive matching
    user_input = user_input.lower()
    
    # Check for keywords in the user input and return the corresponding response
    for keyword in responses:
        if re.search(r'\b' + re.escape(keyword) + r'\b', user_input):
            return responses[keyword]
    
    # Return a default response if no keywords are found
    return responses["default"]

# main function to run the chatbo
def chatbot():
    print("Welcome to the Chatbot! Type 'exit or bye' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")

# Run the chatbot
if __name__ == "__main__":
    chatbot()
