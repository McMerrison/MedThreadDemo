import openai

# Set your API key
SECRET = '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'
openai.api_key = SECRET
messages = [ {"role": "system", "content": 
              "You are a intelligent assistant."} ]
while True:
    message = input("User : ")
    if message:
        messages.append(
            {"role": "user", "content": message},
        )
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
    reply = chat.choices[0].message.content
    print(f"ChatGPT: {reply}")
    messages.append({"role": "assistant", "content": reply})
