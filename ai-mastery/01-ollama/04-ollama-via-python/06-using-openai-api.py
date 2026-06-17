# the code used to interact with openai API can be used to interact with ollama server by just changing the base_url to point to ollama server and using any string as api_key. This is because ollama server provides compatibility with OpenAI API and can be used as a drop in replacement for OpenAI library.

# Usage: OpenAI API is paid and requires internet connection, but using OpenAI API compatibility with ollama server allows you to use the same code to interact with the model running on your local machine without any cost and without internet connection. This is useful for development and testing purposes.

import ollama

# Download model
ollama.pull('ministral-3:3b')

# pip install openai
from openai import OpenAI

# you can also set other parameters like timeout, proxies etc. if needed
# api_key is required by the OpenAI library but it is not used by the ollama server, so you can set it to any string.
my_llm = OpenAI(
    base_url = 'http://localhost:11434/v1',
    api_key='blank', # required, but unused
    )

stream = my_llm.chat.completions.create(
  model="ministral-3:3b",
  messages=[
    {"role": "system", "content": "You are an AWS interview coach and the user is a candidate preparing for AWS interview. Respond in a concise and clear manner."},
    {"role": "user", "content": "Hi"},
    {"role": "assistant", "content": "Hello there. How can I assist you with your AWS interview preparation?"},
    {"role": "user", "content": "Can you explain what is AWS S3 and its use cases?"}
  ],
  stream=True
)

for chunk in stream:
    print(chunk.choices[0].delta.content or '', end='', flush=True)
print()  # newline after streaming completes