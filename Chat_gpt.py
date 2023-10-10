import openai
import cred

def chat_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "You are a chatbot."}, {"role": "user", "content": prompt}],
    )

    return response.choices[0].message.content.strip()
