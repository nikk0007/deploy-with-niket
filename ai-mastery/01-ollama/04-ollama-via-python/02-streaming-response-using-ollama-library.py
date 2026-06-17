# pip install ollama
# starting from v0.2.0, ollama library is available to interact with ollama server using python code. It also provides compatibility with OpenAI API and can be used as a drop in replacement for OpenAI library.

import ollama

# Download model
print('Pulling model from ollama server...')
ollama.pull('ministral-3:3b')
print('Model pulled successfully!')

print('\n\n--- STREAMING RESPONSE ---')
# streaming response from the model can be done by setting stream=True in the generate() method. It returns a generator that yields chunks of response as they are generated. This is useful for long responses or when you want to display the response in real-time.
print('Generating response from the model...')
stream = ollama.generate(model='ministral-3:3b', prompt='Explain AWS Sagemaker in simple terms', stream=True)
for chunk in stream:
    print(chunk['response'], end='', flush=True)

print('\n\nResponse generation completed!')

