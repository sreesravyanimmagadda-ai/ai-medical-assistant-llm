import openai

openai.api_key = "YOUR_API_KEY"

def ask_ai(question):
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful medical assistant."},
            {"role": "user", "content": question}
        ]
    )
    return response['choices'][0]['message']['content']


if __name__ == "__main__":
    while True:
        user_input = input("Enter symptoms: ")
        answer = ask_ai(user_input)
        print("\nAI Response:", answer)
