from langchain.prompts import PromptTemplate


def get_prompt_template():
    template = """
    Answer the question based on the context below. If you can't 
    answer the question, reply "I don't know".

    Context: {context}

    Question: {question}
    """
    prompt = PromptTemplate.from_template(template)
    return prompt
