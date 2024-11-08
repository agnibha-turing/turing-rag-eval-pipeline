from giskard.rag import generate_testset


def generate_test_set(knowledge_base):
    testset = generate_testset(
        knowledge_base,
        num_questions=60,
        agent_description="A chatbot answering questions about your system",
    )
    # Save test set in the evaluation_pipeline folder
    testset.save("./evaluation_pipeline/test-set.jsonl")
    return testset
