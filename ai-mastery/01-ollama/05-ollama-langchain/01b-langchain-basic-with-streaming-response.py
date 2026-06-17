# ollama-langchain: Basic Langchain Example

# pip install langchain
# pip install langchain-core
# pip install langchain-Ollama
# pip install langchain_community

from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser

# system message defines the behavior of the assistant and to set the context for the conversation. 
# human message is the input from user. Can be used to set the variable for user input or to write the user query.
chat_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are an expert in AWS services and you provide short explanation and two use cases of AWS service mentioned by the user."),
        ("human", "{aws_service_name}"),
    ]
)

# format the messages using the chat template and provide the user input for the variable defined in human message.
messages = chat_template.format_messages(aws_service_name="EC2")
print("\n--- Messages ---")
print(messages)

# initialize the ChatOllama model with the desired model and temperature settings
# the model must be available in your local Ollama instance. You can check the available models by running `ollama list` in your terminal.
my_llm = ChatOllama(
    model="ministral-3:3b",
    temperature=0
)

# First we invoke without chain to see the full response with metadata and other information. Then we will create a chain with the chat template, the model and an output parser to extract the text response from the model's output.
print("\n\n--- AI Message ---")
# stream the model response chunk by chunk instead of waiting for the full response
for chunk in my_llm.stream(messages):
    print(chunk.content, end='', flush=True)
print()  # newline after streaming completes

#################################
# Now we will create a chain with the chat template, the model and an output parser to extract the text response from the model's output.

# StrOutputParser is used to extract the text response from the model's output without any additional information or metadata. There are many other output parsers available in langchain_core that can be used to extract structured data, JSON, or other formats from the model's output.
chain = chat_template | my_llm | StrOutputParser()

print("\n\n--- Now Generating Final Chain Response ---")
# stream() returns an iterator of chunks. With StrOutputParser in the chain, each chunk is already a plain string.
for chunk in chain.stream({"aws_service_name": "S3"}):
    print(chunk, end='', flush=True)
print()  # newline after streaming completes