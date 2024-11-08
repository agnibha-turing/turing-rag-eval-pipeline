def answer_fn(chain, question, history=None):
    return chain.invoke({"question": question})
