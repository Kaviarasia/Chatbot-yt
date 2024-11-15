from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.shortcuts import render

@csrf_exempt
def chatbot_response(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user_message = data.get('message', '')

        # Simple response logic
        response_message = generate_response(user_message)
        return JsonResponse({'response': response_message})
    
    return JsonResponse({'error': 'Invalid request'}, status=400)
def generate_response(user_message):
    """
    Generate a natural, conversational response based on user input.
    """
    user_message = user_message.lower()  # Normalize input for consistent matching
    
    if "hi" in user_message or "hello" in user_message:
        return "Hi there! It's great to chat with you. How can I assist you today?"
    elif "i am" in user_message:
        # Extract name if user says "I am <name>"
        name_start = user_message.find("i am") + len("i am")
        name = user_message[name_start:].strip().split()[0].capitalize()
        return f"Nice to meet you, {name}! How's your day going?"
    elif "what's your name" in user_message or "what is your name" in user_message:
        return "I’m Newbot, your friendly assistant. What's on your mind?"
    elif "how are you" in user_message:
        return "I'm just a bot, but I'm doing fantastic! Thanks for asking. How about you?"
    elif "time" in user_message:
        from datetime import datetime
        current_time = datetime.now().strftime("%I:%M %p")
        return f"It's currently {current_time}. What else can I help you with?"
    elif "date" in user_message:
        from datetime import datetime
        current_date = datetime.now().strftime("%A, %B %d, %Y")
        return f"Today is {current_date}. Anything else you'd like to know?"
    elif "help" in user_message:
        return "I'm here to chat, share the time and date, tell jokes, or help with simple tasks. Let me know what you need!"
    elif "joke" in user_message:
        return "Why did the computer cross the road? To get to the other byte!"
    elif "bye" in user_message:
        return "Goodbye! It was lovely talking to you. Have a great day!"
    elif "thank you" in user_message or "thanks" in user_message:
        return "You're welcome! I'm always here if you need help."
    elif "what can you do" in user_message:
        return ("I can provide the current time and date, tell jokes, "
                "and chat about various topics. Let me know how I can assist!")
    else:
        return "Hmm, that's interesting. Could you elaborate or ask me something else?"


def chat(request):
    return render(request, 'newbot/chat.html')