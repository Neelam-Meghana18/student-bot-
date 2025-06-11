import openai

# 💡 Use your actual OpenRouter API key here
openai.api_key = "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"
openai.api_base = "https://openrouter.ai/api/v1"

print("🤖 Welcome to Hope!")
print("I'm here to listen and support you with warmth and understanding. 🌸")
print("Type 'exit' anytime to end the chat.\n")

chat_history = [
    {
        "role": "system",
        "content": (
            "You are Hope, a soft-hearted, calm, and deeply empathetic mental health support friend. "
            "You talk like a loving human friend. Speak in short, gentle replies. Ask one heartfelt question at a time. "
            "Don't give full advice in one message. Let each reply feel like part of a warm, slow conversation. "
            "Always make the user feel heard, understood, and safe. Avoid robotic or generic responses."
        )
    }
]

while True:
    user_input = input("You: ")
    if user_input.lower() in ['exit', 'quit']:
        print("Hope: Take care of yourself, okay? I'm always here when you need me. 🌷")
        break

    chat_history.append({"role": "user", "content": user_input})

    try:
        response = openai.ChatCompletion.create(
            model="mistralai/mistral-7b-instruct",  # OpenRouter's Mistral model
            messages=chat_history,
            temperature=0.85,
            max_tokens=150,
        )

        reply = response["choices"][0]["message"]["content"].strip()
        print("Hope:", reply)

        chat_history.append({"role": "assistant", "content": reply})

    except Exception as e:
        print("⚠️ Something went wrong:", e)
        break
