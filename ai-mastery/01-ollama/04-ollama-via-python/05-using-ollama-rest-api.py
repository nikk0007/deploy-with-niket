import ollama

# Download model
ollama.pull('ministral-3:3b')

## Ollama REST API
from ollama import Client

# using REST API to interact with ollama server. This is useful when you want to interact with ollama server from a different programming language or from a different machine. You can also use REST API to interact with ollama server from command line using curl or httpie.

# host is the URL where ollama server is running. By default it is http://localhost:11434
client = Client(host='http://localhost:11434')

print('response from REST API:')
stream = client.chat(model='ministral-3:3b', messages=[
  {
    'role': 'user',
    'content': 'Explain Kubernetes crashLoopBackOff error in short?',
  },
], stream=True)

for chunk in stream:
    print(chunk['message']['content'], end='', flush=True)
print()  # newline after streaming completes

# similarly we can have a history of messages to have a conversation with the model.