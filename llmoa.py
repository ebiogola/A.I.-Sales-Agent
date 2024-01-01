# Libraries and Modules
from langchain.llms import OpenAI
import os
from langchain.chains import RetrievalQA
from langchain.document_loaders import UnstructuredFileLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma


# OpenAI key
os.environ['OPENAI_API_KEY'] = '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'

# OpenAI LLM 
llm = OpenAI(temperature=0.9, verbose=True)



#Document Loader and Splitter
loader = UnstructuredFileLoader("C:/Users/ebiog/OneDrive/Documents/Master projects/A.I. Sales Agent/stockprice_text.txt")
documents = loader.load()
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
texts = text_splitter.split_documents(documents)

# Embeddings and vectorstores
embeddings = OpenAIEmbeddings()
docsearch = Chroma.from_documents(texts, embeddings)

#Chain 
qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=docsearch.as_retriever())

# Prompt
query = "What is the price of MULTIVERS"
response = qa.run(query)
print(response)