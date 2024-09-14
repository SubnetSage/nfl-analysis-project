import os
from langchain.document_loaders import TextLoader
from langchain.vectorstores import FAISS
from langchain_community.embeddings.ollama import OllamaEmbeddings
from langchain_community.document_loaders import UnstructuredHTMLLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.retrievers import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import FlashrankRerank
from langchain_community.llms import Ollama
from langchain.chains import RetrievalQA

# Define the source directory containing the HTML files
source_directory = "path/to/html/files"

# Load HTML files from the source directory
documents = []
for filename in os.listdir(source_directory):
    if filename.endswith(".html"):
        file_path = os.path.join(source_directory, filename)
        loader = UnstructuredHTMLLoader(file_path)
        documents.extend(loader.load())

# Split the documents into manageable chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
texts = text_splitter.split_documents(documents)
for idx, text in enumerate(texts):
    text.metadata["id"] = idx

# Define a function to pretty print documents (optional for debugging)
def pretty_print_docs(docs):
    print(
        f"\n{'-' * 100}\n".join(
            [f"Document {i+1}:\n\n" + d.page_content for i, d in enumerate(docs)]
        )
    )

# Create embeddings and retriever
embedding = OllamaEmbeddings(model="nomic-embed-text")
retriever = FAISS.from_documents(texts, embedding).as_retriever(search_kwargs={"k": 50})

# Ask a question about the player's position, stats, and safe bets
query = "Identify the player's position, analyze their statistics, and suggest safe bets with reasoning."

# Retrieve relevant documents (player's position, stats, etc.)
docs = retriever.invoke(query)

# Pretty print the retrieved documents (optional for debugging)
pretty_print_docs(docs)

# Set up the contextual compression retriever
llm = Ollama(model="llama3.1")
compressor = FlashrankRerank()
compression_retriever = ContextualCompressionRetriever(
    base_compressor=compressor, base_retriever=retriever
)

# Perform the compressed retrieval query
compressed_docs = compression_retriever.invoke(query)
print([doc.metadata["id"] for doc in compressed_docs])

# Create and execute the QA chain
chain = RetrievalQA.from_chain_type(llm=llm, retriever=compression_retriever)
response = chain({"query": query})

# Print the response from the chain
print("Player Position and Betting Recommendations with Reasoning:")
print(response['result'])
