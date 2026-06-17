# pip install ollama
# Multi-turn conversation with ollama - with user input and memory
# User can type messages in the terminal and chat interactively.
# Type 'quit' or 'exit' to end the conversation.

import ollama

print('Pulling model from ollama server...')
ollama.pull('ministral-3:3b')
print('Model pulled successfully!')

print('\n--- MULTI-TURN CHAT (with memory) ---')
print('Type your message and press Enter to chat.')
print('Type "quit" or "exit" to end the conversation.\n')

# System prompt sets the assistant's persona for the entire conversation
messages = [
    {
        'role': 'system',
        'content': 'You are a Python tutor.'
    }
]

# Keep chatting until the user decides to quit
while True:

    # Take input from the user
    # The .strip() removes any leading/trailing whitespace, so if the user just presses Enter, it will be an empty string.
    user_input = input('You: ').strip()

    # Skip empty inputs — if user just pressed Enter
    if not user_input:
        continue

    # Exit condition
    if user_input.lower() in ['quit', 'exit']:
        print('Ending conversation. Goodbye!')
        break

    # Add user message to conversation history
    messages.append({'role': 'user', 'content': user_input})

    # Send full conversation history so the model has memory of previous turns
    response = ollama.chat(model='ministral-3:3b', messages=messages)
    reply = response['message']['content']

    print(f'Assistant: {reply}\n')

    # Add assistant reply to history so next turn has full context
    messages.append({'role': 'assistant', 'content': reply})

    # Optional: prevent hitting token limits on long conversations
    # Keeps system prompt + last 10 messages only
    # messages = [messages[0]] + messages[-10:]