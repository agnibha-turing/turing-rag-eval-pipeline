from langchain_community.chat_models import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import DocArrayInMemorySearch
from operator import itemgetter


def create_chain(documents, prompt):
    # Create a vector store
    vectorstore = DocArrayInMemorySearch.from_documents(
        documents, embedding=OpenAIEmbeddings()
    )
    retriever = vectorstore.as_retriever()

    # Initialize the language model
    model = ChatOpenAI(model="gpt-4o")

    # Create the retrieval chain
    chain = (
        {
            "context": itemgetter("question") | retriever,
            "question": itemgetter("question"),
        }
        | prompt
        | model
        | StrOutputParser()
    )
    return chain
