
# RAG using Ollama and Langchain
import ollama
from langchain_community.document_loaders import TextLoader

# pip install pypdf
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings

# pip install langchain-chroma
from langchain_chroma import Chroma

# we have other types of loaders also like PDFLoader, UnstructuredFileLoader, WebBaseLoader etc. that can be used to load different types of data.
my_document = TextLoader("lambda.txt").load() # for loading text files

# for loading PDF files, we can use PyPDFLoader which is a simple and efficient loader for PDF documents.
# loader = PyPDFLoader("lambda.pdf")
# my_document = loader.load()

# to split the loaded documents into smaller chunks, we can use RecursiveCharacterTextSplitter which is a text splitter that splits the text based on character count. It takes two parameters, chunk_size which is the maximum number of characters in each chunk and chunk_overlap which is the number of characters to overlap between chunks. This helps in maintaining the context between chunks when they are processed by the model.
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
chunks = text_splitter.split_documents(my_document)
print("Number of chunks: " + str(len(chunks)))
print('\n\n -- Chunk 0 -- \n\n')
print(chunks[0])

print('\n\n -- Chunk 1 -- \n\n')
print(chunks[1])

print('\n\n -- Chunk 2 -- \n\n')
print(chunks[2])

# to convert chunks of text into vector embeddings, we can use OllamaEmbeddings which is compatible with any model in Ollama that can generate embeddings. In this example, we are using nomic-embed-text model which is a small and efficient model for generating text embeddings.

# You can choose any other model that is available in your local Ollama instance and is suitable for generating embeddings. You can check the available models by running `ollama list` in your terminal.
# Ensure model exists
ollama.pull("nomic-embed-text")

embedder  = OllamaEmbeddings(
    model="nomic-embed-text"
)

# Chroma is a simple and efficient vector database that can be used to store and retrieve vector embeddings. We can create a Chroma database from the documents and their corresponding embeddings.
my_db = Chroma.from_documents(chunks, embedding=embedder)

# now embeddings are stored in the Chroma database and we can query it to find similar documents based on a query. We can use the similarity_search method of the Chroma database to find similar documents. It takes a query string as input and returns a list of similar documents based on the cosine similarity of their embeddings.

query = "What is Lamda ?"
similar_docs = my_db.similarity_search(query)
print("\n\nNumber of similar documents: " + str(len(similar_docs)))
print("\n\n-- Similar document 1 --\n")
print(similar_docs[0].page_content)
