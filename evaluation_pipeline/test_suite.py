from giskard.rag import QATestset


def create_test_suite():
    # Load test set from the evaluation_pipeline folder
    testset = QATestset.load(
        "./evaluation_pipeline/test-set-alphabet-gm.jsonl")
    # Create test suite
    test_suite = testset.to_test_suite("Your System Test Suite")
    return test_suite
