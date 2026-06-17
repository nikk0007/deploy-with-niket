
# RAG using Ollama and Langchain
import ollama
from langchain_community.document_loaders import TextLoader

# pip install pypdf
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings

# pip install langchain-chroma
from langchain_chroma import Chroma
from langchain_ollama import ChatOllama
import sys

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

# we have other types of loaders also like PDFLoader, UnstructuredFileLoader, WebBaseLoader etc. that can be used to load different types of data.
my_document = TextLoader("lambda.txt").load() # for loading text files

# for loading PDF files, we can use PyPDFLoader which is a simple and efficient loader for PDF documents.
# loader = PyPDFLoader("lambda.pdf")
# my_document = loader.load()

# to split the loaded documents into smaller chunks, we can use RecursiveCharacterTextSplitter which is a text splitter that splits the text based on character count. It takes two parameters, chunk_size which is the maximum number of characters in each chunk and chunk_overlap which is the number of characters to overlap between chunks. This helps in maintaining the context between chunks when they are processed by the model.
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
chunks = text_splitter.split_documents(my_document)
print("Number of chunks: " + str(len(chunks)))

# to convert chunks of text into vector embeddings, we can use OllamaEmbeddings which is compatible with any model in Ollama that can generate embeddings. In this example, we are using nomic-embed-text model which is a small and efficient model for generating text embeddings. We need to provide the base_url of the Ollama server and the model name to initialize the OllamaEmbeddings.
# Ensure model exists
ollama.pull("nomic-embed-text")

print('\n\n Now initializing embeddings \n\n')
embedder  = OllamaEmbeddings(
    model="nomic-embed-text"
)


# Chroma is a simple and efficient vector database that can be used to store and retrieve vector embeddings. We can create a Chroma database from the documents and their corresponding embeddings.
print('\n\n Now creating Chroma database from documents and embeddings \n\n')
my_db = Chroma.from_documents(chunks, embedding=embedder)

# now embeddings are stored in the Chroma database and we can query it to find similar documents based on a query. We can use the similarity_search method of the Chroma database to find similar documents. It takes a query string as input and returns a list of similar documents based on the cosine similarity of their embeddings.
# Prompt
template = """You are a helpful cloud assistant.

Use ONLY the context below to answer the question.
If the answer is not present, say "I don't know".

Context:
{context}

Question:
{question}

Answer:"""

prompt = ChatPromptTemplate.from_template(template)

# Model
my_llm = ChatOllama(
    model="ministral-3:3b",
    temperature=0
)

# Retriever - we can use the as_retriever method of the Chroma database to create a retriever that can be used to retrieve similar documents based on a query. We can also specify the number of similar documents to retrieve using the search_kwargs parameter.
# we are using it instead of similarity_search because it returns a retriever object that can be used in the chain instead of directly returning the similar documents. This allows us to integrate the retriever into the chain and use it to retrieve relevant documents based on the query.
print('\n\n Now creating retriever from Chroma database \n\n')
retriever = my_db.as_retriever(search_kwargs={"k": 3})

# now context has been retrieved using the retriever and we can format it to be used in the prompt. We can create a function format_docs that takes a list of documents and formats them into a single string that can be used in the prompt. In this example, we are joining the page_content of each document with two newlines in between to create a formatted context string.
def format_docs(documemts):
    return "\n\n".join([d.page_content for d in documemts])

# Chain
# output of retriever is passed to format_docs function to format the retrieved documents and then the formatted context along with the question is passed to the prompt which generates the final answer using the model. The StrOutputParser is used to parse the output of the model into a string format.
# RunnablePassthrough passes whatever we give as input using the invoke() method to the prompt without any changes.
chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | prompt
    | my_llm
    | StrOutputParser()
)

print("\n\n--- Now Generating Response for the query: What is AWS Lambda? ---\n\n")

# For NON-STRAMING RESPONSE
# response = chain.invoke("What is AWS Lambda?")
# print("\n\nResponse: " + response)


# for streaming response:
print("\n\nResponse: ")
for chunk in chain.stream("What is AWS Lambda?"):
    print(chunk, end='', flush=True)
print()  # newline after streaming completes