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

print("\n\n--- AI Message ---")
# invoke the model with the formatted messages and get the response
ai_msg = my_llm.invoke(messages)

# ai_msg will contain message, metadata and other information. To get the actual response from the model, you can access the content attribute of the message.
print(ai_msg.content)

#################################

# StrOutputParser is used to extract the text response from the model's output without any additional information or metadata. There are many other output parsers available in langchain_core that can be used to extract structured data, JSON, or other formats from the model's output.
chain = chat_template | my_llm | StrOutputParser()
response = chain.invoke({"aws_service_name": "S3"})

print("\n\n--- Final Chain Response ---")
print(response)