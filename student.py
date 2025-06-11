import openai

# Replace with your valid OpenRouter API key
openai.api_key = "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"
openai.api_base = "https://openrouter.ai/api/v1"

print("📘 Welcome to Uplift!")
print("I'm here to support you with warmth, encouragement, and small steps. 🌈")
print("Type 'exit' anytime to end the chat.\n")
chat_history = [
    {
        "role": "system",
        "content": (
            "You are Uplift — a kind, emotionally intelligent, human-like friend who helps students feeling stressed, lost, or demotivated. "
            "Your job is to gently talk to them in short, calm, comforting replies — like a trusted friend would. "
            "DO NOT assume anything about what they’re going through. Wait until they say it. DO NOT mention exams, sadness, stress, or failure unless the user says it first. "
            "Always start light, open, and warm. Ask soft, neutral questions first like 'How's your day going?' or 'What's been on your mind lately?' "
            "NEVER jump to comforting unless the user opens up. Speak softly, like texting a friend, one message at a time. "
            "No paragraphs. No bullet points. No listing. Just be real, caring, and fully present in the moment."
        )
    }
]



while True:
    user_input = input("You: ")
    if user_input.lower() in ['exit', 'quit']:
        print("Uplift: I'm proud of you for being here. Let's talk again soon, okay? 🌻")
        break

    chat_history.append({"role": "user", "content": user_input})

    try:
        response = openai.ChatCompletion.create(
            model="mistralai/mistral-7b-instruct",  # You can experiment with other models if you like
            messages=chat_history,
            temperature=0.95,  # Feel more creative and emotional
            max_tokens=250
        )

        reply = response["choices"][0]["message"]["content"]
        print("Uplift:", reply.strip())
        chat_history.append({"role": "assistant", "content": reply})

    except Exception as e:
        print("⚠️ Something went wrong:", e)
        break
