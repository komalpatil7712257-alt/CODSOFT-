import datetime

print("🤖 ChatBot: Hello! I am your assistant.")
print("Type 'menu' to see options or 'exit' to quit.\n")

while True:
    user = input("You: ").lower()

    if user == "exit":
        print("ChatBot: Goodbye! Have a great day 👋")
        break

    elif "menu" in user:
        print("\n📋 I can help you with:")
        print("1. Greetings (hi, hello)")
        print("2. Time")
        print("3. Date")
        print("4. Basic questions")
        print("5. Simple math (like 2 + 2)")
        print("Type anything!\n")

    elif "hi" in user or "hello" in user:
        print("ChatBot: Hello! 😊 How can I help you?")

    
    elif "how are you" in user:
        print("ChatBot: I'm doing great! 😄 What about you?")

    
    elif "your name" in user:
        print("ChatBot: I am a Rule-Based Chatbot created in Python.")

    
    elif "time" in user:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print("ChatBot: Current time is", current_time)

    elif "date" in user:
        current_date = datetime.datetime.now().strftime("%d-%m-%Y")
        print("ChatBot: Today's date is", current_date)


    elif "+" in user:
        try:
            parts = user.split("+")
            result = int(parts[0]) + int(parts[1])
            print("ChatBot: Answer =", result)
        except:
            print("ChatBot: Please enter numbers like 2 + 2")

    elif "-" in user:
        try:
            parts = user.split("-")
            result = int(parts[0]) - int(parts[1])
            print("ChatBot: Answer =", result)
        except:
            print("ChatBot: Please enter numbers like 5 - 2")

    elif "*" in user:
        try:
            parts = user.split("*")
            result = int(parts[0]) * int(parts[1])
            print("ChatBot: Answer =", result)
        except:
            print("ChatBot: Please enter numbers like 3 * 2")

    elif "/" in user:
        try:
            parts = user.split("/")
            result = int(parts[0]) / int(parts[1])
            print("ChatBot: Answer =", result)
        except:
            print("ChatBot: Please enter numbers like 10 / 2")


    elif "help" in user:
        print("ChatBot: Try asking about time, date, math or greetings!")

    elif "thank" in user:
        print("ChatBot: You're welcome! 😊")

    elif "bye" in user:
        print("ChatBot: Bye! Take care 👋")

    else:
        print("ChatBot: Sorry, I didn't understand that 😅")