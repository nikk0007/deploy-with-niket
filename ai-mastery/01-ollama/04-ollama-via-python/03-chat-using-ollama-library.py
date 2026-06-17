# pip install ollama
# starting from v0.2.0, ollama library is available to interact with ollama server using python code. It also provides compatibility with OpenAI API and can be used as a drop in replacement for OpenAI library.

import ollama

# Download model
print('Pulling model from ollama server...')
ollama.pull('ministral-3:3b')
print('Model pulled successfully!')


print('\n\n--- CHAT ---')
# ollama.chat() is used to have a conversation with the model. It takes model name and a list of messages as input and returns the generated response. Each message is a dictionary with 'role' and 'content' keys. The 'role' can be 'system', 'user' or 'assistant'.
stream = ollama.chat(
    model='ministral-3:3b',
    messages=[
        {
            'role': 'system',
            'content': 'Rewrite message as email in a professional tone.'
        },
        {
            'role': 'user',
            'content': 'hey, the server is down again, fix it asap'
        }
    ],
    stream=True
)

for chunk in stream:
    print(chunk['message']['content'], end='', flush=True)
print()  # newline after streaming completes

print('\n\nChat completed!')