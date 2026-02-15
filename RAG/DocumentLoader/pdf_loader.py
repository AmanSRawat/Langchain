from langchain_community.document_loaders import PyPDFLoader
 
loader = PyPDFLoader('IsThisAnythingPDF.pdf')

docs = loader.load()

print(len(docs))