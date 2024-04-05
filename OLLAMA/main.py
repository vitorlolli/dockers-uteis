from langchain_community.llms import Ollama
from langchain_community.document_loaders import WebBaseLoader, PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import GPT4AllEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA

# Exemplo de carregar um url
# ollama = Ollama(base_url='http://localhost:11434', model='llama2')

# loader = WebBaseLoader('https://crosp.org.br/')
# data = loader.load()

# text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=0)
# all_splits = text_splitter.split_documents(data)

# vectorstore = Chroma.from_documents(documents=all_splits, embedding=GPT4AllEmbeddings())
# qachain = RetrievalQA.from_chain_type(ollama, retriever=vectorstore.as_retriever())

# question = "pergunta"
# print(qachain({ "query": question }))

# Exemplo de carregar um pdf
# ollama = Ollama(base_url='http://localhost:11434', model='llama2')

# loader = PyPDFLoader("./manual.pdf")
# data = loader.load()

# text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=0)
# all_splits = text_splitter.split_documents(data)

# vectorstore = Chroma.from_documents(documents=all_splits, embedding=GPT4AllEmbeddings())
# qachain = RetrievalQA.from_chain_type(ollama, retriever=vectorstore.as_retriever())

# question = "Resuma o conteúdo em uma lista com 5 itens? responda em portugues brasileiro"
# print(qachain({ "query": question }))