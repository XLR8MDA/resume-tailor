from langchain_community.document_loaders import UnstructuredPDFLoader
from pdfminer import extract_text

def pdf_loader(file_path):
    # loader = UnstructuredPDFLoader(file_path)
    # data = loader.load()
    # resume_content = data[0].page_content

    resume_content = extract_text(file_path)
    return resume_content
