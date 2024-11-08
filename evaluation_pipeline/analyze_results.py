def analyze_report(report):
    # Display correctness by question type
    correctness = report.correctness_by_question_type()
    print("Correctness by Question Type:")
    print(correctness)
    
    # Display failures
    failures = report.get_failures()
    print("\nFailures:")
    print(failures) 