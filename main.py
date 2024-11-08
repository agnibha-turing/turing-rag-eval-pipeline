from evaluation_pipeline.data_loading import load_documents
from evaluation_pipeline.knowledge_base import create_knowledge_base
from evaluation_pipeline.test_set_generation import generate_test_set
from evaluation_pipeline.prompt_template import get_prompt_template
from evaluation_pipeline.retrieval_chain import create_chain
from evaluation_pipeline.answer_function import answer_fn
from evaluation_pipeline.evaluate_model import evaluate_model
from evaluation_pipeline.analyze_results import analyze_report
from langchain_community.chat_models import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import DocArrayInMemorySearch


def main():
    # Load and process documents
    documents = load_documents()

    # Create Knowledge Base
    knowledge_base = create_knowledge_base(documents)

    # Generate Test Set
    testset = generate_test_set(knowledge_base)

    # Prepare Prompt Template
    prompt = get_prompt_template()

    # Create Retrieval Chain
    chain = create_chain(documents, prompt)

    # Define Answer Function
    def answer_function(question, history=None):
        return answer_fn(chain, question, history)

    # Evaluate Model
    report = evaluate_model(answer_function, testset, knowledge_base)

    # Analyze Results
    analyze_report(report)


if __name__ == "__main__":
    main()
