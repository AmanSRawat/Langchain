from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader  = PyPDFLoader("sample.pdf")

docs = loader.load()

text_splitter  = CharacterTextSplitter(
    chunk_size = 100,
    chunk_overlap = 0,
    separator= ''
)

result = text_splitter.split_documents(docs)

print(result[0])