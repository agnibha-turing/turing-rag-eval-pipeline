import os
from glob import glob
from langchain_community.document_loaders import PyPDFLoader, PDFMinerLoader, PyMuPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import logging

logging.basicConfig(level=logging.INFO)


def load_documents():
    # Initialize the text splitter
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000, chunk_overlap=20)

    # Initialize an empty list to hold all documents
    all_documents = []

    # Define the root data directory
    # Adjust the path if necessary
    data_dir = 'A:/github-profiles/turing/RAG/llm/financial-docs'

    # Use glob to recursively find all PDF files in subdirectories
    pdf_files = glob(os.path.join(data_dir, '**', '*.pdf'), recursive=True)

    logging.info(f"Found {len(pdf_files)} PDF files to process.")

    # Loop over each PDF file and load it
    for pdf_file in pdf_files:
        try:
            logging.info(f"Processing file: {pdf_file}")

            # Choose a PDF loader
            # You can try different loaders if one is not working
            loader = PyPDFLoader(pdf_file)
            # loader = PDFMinerLoader(pdf_file)
            # loader = PyMuPDFLoader(pdf_file)

            # Load and split the PDF document
            documents = loader.load_and_split(text_splitter)

            if documents:
                logging.info(
                    f"Loaded {len(documents)} documents from {pdf_file}")
                # Extend the all_documents list with documents from the current PDF
                all_documents.extend(documents)
            else:
                logging.warning(f"No documents loaded from {pdf_file}")

        except Exception as e:
            logging.error(f"Error processing {pdf_file}: {e}")

    logging.info(f"Total documents loaded: {len(all_documents)}")
    return all_documents


# import os
# from glob import glob
# from langchain_community.document_loaders import UnstructuredPDFLoader
# from langchain.text_splitter import RecursiveCharacterTextSplitter
# import logging

# logging.basicConfig(level=logging.INFO)

# def load_documents():
#     # Initialize the text splitter
#     text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=20)

#     # Initialize an empty list to hold all documents
#     all_documents = []

#     # Define the root data directory
#     data_dir = '../data'  # Adjust the path if necessary

#     # Use glob to recursively find all PDF files in subdirectories
#     pdf_files = glob(os.path.join(data_dir, '**', '*.pdf'), recursive=True)

#     logging.info(f"Found {len(pdf_files)} PDF files to process.")

#     # Loop over each PDF file and load it
#     for pdf_file in pdf_files:
#         try:
#             logging.info(f"Processing file: {pdf_file}")
#             # Use UnstructuredPDFLoader
#             loader = UnstructuredPDFLoader(pdf_file)

#             # Load and split the PDF document
#             documents = loader.load_and_split(text_splitter)

#             if documents:
#                 logging.info(f"Loaded {len(documents)} documents from {pdf_file}")
#                 # Extend the all_documents list with documents from the current PDF
#                 all_documents.extend(documents)
#             else:
#                 logging.warning(f"No documents loaded from {pdf_file}")

#         except Exception as e:
#             logging.error(f"Error processing {pdf_file}: {e}")

#     logging.info(f"Total documents loaded: {len(all_documents)}")
#     return all_documents
