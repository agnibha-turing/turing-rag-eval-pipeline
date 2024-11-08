import pytest
from giskard.rag import QATestset
from giskard.testing.tests.llm import test_llm_correctness
from evaluation_pipeline.answer_function import answer_fn
from evaluation_pipeline.data_loading import load_documents
from evaluation_pipeline.prompt_template import get_prompt_template
from evaluation_pipeline.retrieval_chain import create_chain
from evaluation_pipeline.test_suite import create_test_suite
from giskard import Model


@pytest.fixture
def dataset():
    test_suite = create_test_suite()
    return test_suite.df  # Access the dataset from the test suite


@pytest.fixture
def model():
    documents = load_documents()
    prompt = get_prompt_template()
    chain = create_chain(documents, prompt)

    def batch_prediction_fn(df):
        return [answer_fn(chain, question) for question in df["question"].values]

    return Model(
        model=batch_prediction_fn,
        model_type="text_generation",
        name="Your Model Name",
        description="Description of your model",
        feature_names=["question"],
    )


def test_chain_correctness(dataset, model):
    test_llm_correctness(model=model, dataset=dataset,
                         threshold=0.5).run().assert_()
