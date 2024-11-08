# Evaluation Pipeline for Your System

This repository contains an evaluation pipeline designed to systematically test, benchmark, and improve the various components of your system, particularly focusing on document processing, embedding, and querying flows. The pipeline utilizes tools like LangChain, Giskard, and OpenAI's GPT models to create a robust automated testing environment.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Usage](#usage)
  - [1. Set Up Environment Variables](#1-set-up-environment-variables)
  - [2. Prepare Data](#2-prepare-data)
  - [3. Run the Evaluation Pipeline](#3-run-the-evaluation-pipeline)
  - [4. View the Evaluation Report](#4-view-the-evaluation-report)
- [Tests](#tests)
- [Customization](#customization)
- [Troubleshooting](#troubleshooting)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

The evaluation pipeline enables:

- **Automated Testing**: Regular tests on key functionalities like query retrieval accuracy and document embedding efficacy.
- **Benchmarking**: Establish performance benchmarks to measure system efficiency and response times.
- **Quality Metrics**: Assess the relevance and accuracy of responses to user queries.
- **Continuous Improvement**: Track and compare metrics over time to support iterative improvement.

---

## Features

- Recursive loading and processing of PDF documents from nested directories.
- Creation of a knowledge base using the processed documents.
- Automated test set generation based on the knowledge base.
- Evaluation of the retrieval chain using the generated test set.
- Detailed evaluation reports highlighting performance metrics.
- Integration with Pytest for automated testing and continuous integration.

---

## Prerequisites

- **Python 3.8 or higher**
- **OpenAI API Key**: Required for using OpenAI's GPT models.

---

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/agnibha-turing/turing-rag-eval-pipeline.git
   cd turing-rag-eval-pipeline
   ```
2. **Create a Virtual Environment**

   ```bash
   python -m venv venv
   ```
3. **Activate the Virtual Environment**

   - On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```
   - On Windows:

     ```bash
     venv\Scripts\activate
     ```
4. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

---

## Project Structure

```
yourproject/
│
├── evaluation_pipeline/
│   ├── __init__.py
│   ├── answer_function.py
│   ├── analyze_results.py
│   ├── data_loading.py
│   ├── evaluate_model.py
│   ├── knowledge_base.py
│   ├── prompt_template.py
│   ├── retrieval_chain.py
│   ├── test_set_generation.py
│   └── test_suite.py
│
├── tests/
│   └── test_pipeline.py
│
├── data/
│   └── (Place your PDF files and subfolders here)
│
├── main.py
├── requirements.txt
└── README.md
```

---

## Usage

### 1. Set Up Environment Variables

Set your OpenAI API key as an environment variable.

- **On macOS/Linux:**

  ```bash
  export OPENAI_API_KEY='your-api-key-here'
  ```
- **On Windows:**

  ```bash
  set OPENAI_API_KEY='your-api-key-here'
  ```

### 2. Prepare Data

Place all your PDF files and subfolders by creating a  `data/` directory.

**Example Directory Structure:**

```
data/
├── folder1/
│   ├── document1.pdf
│   ├── document2.pdf
├── folder2/
│   ├── document3.pdf
└── document4.pdf
```

### 3. Run the Evaluation Pipeline

Execute the main script:

```bash
python main.py
```

This script performs the following steps:

- **Loads and processes** all PDFs from the `data/` directory and subdirectories.
- **Creates a knowledge base** from the processed documents.
- **Generates a test set** of questions and reference answers.
- **Prepares a prompt template**.
- **Creates a retrieval chain** using the documents and prompt.
- **Defines an answer function** using the chain.
- **Evaluates the model** against the test set.
- **Generates an evaluation report**.

### 4. View the Evaluation Report

After running the script, an HTML report will be generated:

```
evaluation_pipeline/report.html
```

Open this file in your web browser to view detailed evaluation metrics and results.

---

## Tests

Pytest is used for the automated test suite.

1. **Ensure that `pytest` is installed:**

   ```bash
   pip install pytest
   ```
2. **Run Tests:**

   ```bash
   pytest tests/
   ```

This will execute the test suite defined in `tests/test_pipeline.py`.

---

## Customization

- **Adjust Chunk Size and Overlap:**

  In `data_loading.py`, you can modify the chunk size and overlap for the text splitter:

  ```python
  text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=20)
  ```
- **Modify the Prompt Template:**

  In `prompt_template.py`, you can customize the prompt used for the retrieval chain:

  ```python
  template = """
  Answer the question based on the context below. If you can't
  answer the question, reply "I don't know".

  Context: {context}

  Question: {question}
  """
  ```
- **Change the Number of Test Questions:**

  In `test_set_generation.py`, adjust the `num_questions` parameter:

  ```python
  testset = generate_testset(
      knowledge_base,
      num_questions=60,  # Adjust the number as needed
      agent_description="A chatbot answering questions about your system",
  )
  ```

---

## Troubleshooting

- **No Documents Loaded:**

  If you encounter a `ValueError` indicating that no documents were loaded:

  - Ensure that the `data_dir` in `data_loading.py` correctly points to your data directory.
  - Verify that there are PDF files in the `data/` directory and its subfolders.
  - Check the console logs for any errors during PDF processing.
- **Dependencies Issues:**

  - Make sure all dependencies are installed using the provided `requirements.txt`.
  - For `UnstructuredPDFLoader`, additional system dependencies like Tesseract OCR and Poppler may be required.

    - **On Ubuntu:**

      ```bash
      sudo apt-get install tesseract-ocr poppler-utils
      ```
    - **On macOS (using Homebrew):**

      ```bash
      brew install tesseract poppler
      ```
- **OpenAI API Errors:**

  - Ensure your OpenAI API key is set correctly.
  - Check your API usage and rate limits.

---

## Dependencies

- **Python Packages:**

  - langchain
  - langchain-community
  - giskard[llm]
  - openai
  - pandas
  - unstructured[pdf]
  - pdfminer.six
  - PyMuPDF
  - pytest
- **System-Level Dependencies (for `unstructured`):**

  - **Tesseract OCR**
  - **Poppler Utils**

---

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes or additions you would like to make.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

Feel free to reach out if you have any questions or need further assistance with the setup and usage of this evaluation pipeline.
