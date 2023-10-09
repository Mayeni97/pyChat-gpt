import openai

openai.api_key ="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"

def chat_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "You are a chatbot."}, {"role": "user", "content": prompt}],
    )

    return response.choices[0].message.content.strip()
