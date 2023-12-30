import os
import openai
from dotenv import load_dotenv

load_dotenv()

myApiKey = os.getenv('API_KEY')
openai.api_key = myApiKey
messages = [
                { "role": "system",
                  "content":"You are a intelligent assistant act like a chat-gpt 3.5."
                 }
          ]
while True:
    message = input("User : ")
    if 'exit' in message or 'quit' in message:
            break
    if message:
        messages.append(
            {"role": "user", "content": message},
        )
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages,
            max_tokens=100,
            n=1,
            stop=None,
            temperature =0.5
        )
    reply = chat.choices[0].message.content
    print(f"NHKHAN_GPT: {reply}")
    messages.append({"role": "assistant", "content": reply})

