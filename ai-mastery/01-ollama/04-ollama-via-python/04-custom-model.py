import sys
import ollama

# Download model
ollama.pull('ministral-3:3b')

# Create custom model by inheriting from the base model and adding system instructions. This is useful to create a specialized version of the base model for specific use cases. Here we are creating a custom model called 'coach' which is based on 'ministral-3:3b' and has system instructions to act as a DevOps Interview Coach.
print('Creating custom model...')

# we are using "from_" and not from because "from" is a reserved keyword in python.
ollama.create(
    model='coach',
    from_='ministral-3:3b',
    system='You are a DevOps Interview Coach. Ask interview questions and give feedback on answers.'
)
print('Custom model created successfully!')

print('\nAvailable models:')
print([m.model for m in ollama.list().models])

# now you can use this model like any other model to generate response or have a chat in terminal or using REST API or using ollama library in python code. Here is an example of having a chat using ollama library in python code.
print('\n\n--- CHAT WITH CUSTOM MODEL ---')
stream = ollama.chat(model='coach', messages=[
    {'role': 'user', 'content': 'Hi, I have an interview for a DevOps role tomorrow, can you help me prepare by providing 2 potential questions which the interviewer can ask?'},
], stream=True)

for chunk in stream:
    print(chunk['message']['content'], end='', flush=True)
print()  # newline after streaming completes

print('\n\nChat with custom model completed!')
#sys.exit(0)

ollama.delete('coach')
print('Custom model deleted successfully!')

print('\nAvailable models after deletion:')
print([m.model for m in ollama.list().models])
