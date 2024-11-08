from giskard.rag import evaluate


def evaluate_model(answer_fn, testset, knowledge_base):
    report = evaluate(answer_fn, testset=testset,
                      knowledge_base=knowledge_base)
    # Save the report in evaluation_pipeline folder
    report.to_html("./evaluation_pipeline/report.html")
    return report
