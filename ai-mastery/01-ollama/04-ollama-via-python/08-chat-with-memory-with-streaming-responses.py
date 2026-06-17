# pip install ollama
# Multi-turn conversation with ollama - with user input, memory, AND streaming
# Streaming means tokens print to the screen as they are generated
# instead of waiting for the complete response.
# Type 'quit' or 'exit' to end the conversation.

import ollama

print('Pulling model from ollama server...')
ollama.pull('ministral-3:3b')
print('Model pulled successfully!')

print('\n--- MULTI-TURN CHAT (with memory + streaming) ---')
print('Type your message and press Enter to chat.')
print('Type "quit" or "exit" to end the conversation.\n')

messages = [
    {
        'role': 'system',
        'content': 'You are a Python tutor.'
    }
]

while True:

    user_input = input('You: ').strip()

    if not user_input:
        continue

    if user_input.lower() in ['quit', 'exit']:
        print('Ending conversation. Goodbye!')
        break

    messages.append({'role': 'user', 'content': user_input})

    print('Assistant: ', end='', flush=True)

    # stream=True tells ollama to return a generator instead of a complete response
    # each chunk contains a small piece of the response as it is generated
    full_reply = ''

    for chunk in ollama.chat(model='ministral-3:3b', messages=messages, stream=True):

        # each chunk has the same structure as a normal response
        # but content is a small piece of the full reply, not the entire thing
        token = chunk['message']['content']

        # print each token immediately without newline or space
        # flush=True forces the output to appear instantly without buffering
        print(token, end='', flush=True)

        # keep building the full reply so we can add it to history after streaming ends
        full_reply += token

    # streaming is done — move to next line
    print('\n')

    # add the complete assembled reply to conversation history
    # we cannot add chunks one by one — history needs the full message
    messages.append({'role': 'assistant', 'content': full_reply})

    # Optional: trim history to avoid hitting token limits on long conversations
    # messages = [messages[0]] + messages[-10:]