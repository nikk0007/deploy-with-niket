# pip install ollama
# starting from v0.2.0, ollama library is available to interact with ollama server using python code. It also provides compatibility with OpenAI API and can be used as a drop in replacement for OpenAI library.

import ollama

# Download model
print('Pulling model from ollama server...')
ollama.pull('ministral-3:3b')
print('Model pulled successfully!')

# to list all the available models on the server
models_list = ollama.list()
model_names = [m.model for m in models_list.models]
print('Available models:')
print(model_names)

# ollama.generate() is used to generate response from the model. It takes model name and prompt as input and returns the generated response.
print('Generating response from the model...')
result = ollama.generate(model='ministral-3:3b', prompt='Explain AWS Sagemaker in simple terms')
print('Generated response:')
print(result['response'])

print('\n\nResponse generation completed!')
