# 🩺 Medical Reports Analyzer

This project is a Streamlit application that analyzes medical reports in PDF or image format to provide insights. It uses the Google Gemini language model for natural language processing.

## AIM
System that takes your Medical Report as input and provides insights based on the content.

## Features

- 📄 Upload a medical report in PDF or image format.
- 🔍 Analyze the report content and provide insights.

## Technologies Used

- [Streamlit](https://streamlit.io/) for the user interface.
- [Google Gemini](https://ai.google/) as the language model for analyzing the report.
- [PyPDF2](https://pypi.org/project/PyPDF2/) for reading PDF files AND [pillow](https://pypi.org/project/pillow/) for reading images.

## Requirements

- Python 3.7 or higher
- Google API key for accessing the Google Gemini language model

## Installation

1. **Clone the repository:**

    ```bash
    https://github.com/mayurd8862/Medical-Reports-Analyzer.git
    cd Medical-Reports-Analyzer
    ```

2. **Create and activate a virtual environment (optional but recommended):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up your Google API key:**

    - Create a file named `secrets.toml` in the `.streamlit` directory (create the directory if it doesn't exist).
    - Add your Google API key to `secrets.toml`:

    ```toml
    [general]
    GOOGLE_API_KEY = "your_google_api_key"
    ```

## Usage

1. **Run the Streamlit app:**

    ```bash
    streamlit run app.py
    ```

2. **Upload a medical report in PDF or image format.**

3. **View the insights and analysis provided by the application.**

---
[Click here](https://medical-reports-analyzer.streamlit.app/) to use the web application.
