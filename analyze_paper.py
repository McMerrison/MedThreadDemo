import openai

# Set your API key
openai.api_key = 'KEY'


messages = [ {"role": "system", "content": 
              "You are an intelligent paralegal tasked with reading scientific papers to find a correlation between a commerical substance and a life-threatening disease. Read the excerpts provided and draw correlations between use of the substance and the disease."} ]

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
