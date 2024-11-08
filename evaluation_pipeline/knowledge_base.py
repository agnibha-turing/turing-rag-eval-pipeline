import pandas as pd
from giskard.rag import KnowledgeBase


def create_knowledge_base(documents):
    # Convert documents to DataFrame
    df = pd.DataFrame([d.page_content for d in documents], columns=["text"])

    # Create Knowledge Base
    knowledge_base = KnowledgeBase(df)
    return knowledge_base
