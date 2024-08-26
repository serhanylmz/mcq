# PDF Multiple Choice Question Extractor

This Python script extracts multiple-choice questions from PDF files using OpenAI's GPT-4o vision model. It's designed to process Swedish medical exam questions but can be adapted for other languages and subjects.

## Features

- Extracts multiple-choice questions from PDF files
- Maintains the original language (Swedish by default)
- Handles special cases such as invalid questions or multiple correct answers
- Saves extracted questions in JSON format

## Sample data row: 

{
  "language": "sv",
  "country": "Sweden",
  "file_name": "example_exam.pdf",
  "source": "https://www.umu.se/utbildning/sok/kunskapsprov/kunskapsprov-for-lakare/teoretiskt-delprov/",
  "license": "unknown",
  "level": "graduate",
  "category_en": "Medicine",
  "category_original_lang": "Medicin",
  "original_question_num": 1,
  "question": "En 45-årig kvinna söker på vårdcentralen för trötthet och viktuppgång. Hon har också noterat att hon fryser lätt. Vilken av följande laboratorieundersökningar är mest lämplig att beställa initialt?",
  "options": [
    "A. TSH",
    "B. T3",
    "C. T4",
    "D. TPO-antikroppar",
    "E. Kortisol"
  ],
  "answer": "A. TSH"
}

By automating the extraction process, it saves significant time and effort compared to manual transcription.

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/serhanylmz/mcq.git
   cd mcq
   ```

2. Create a virtual environment (optional but recommended):
    # using conda: 
    ```
    conda create -n mcq python=3.10
    ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Set up your OpenAI API key:
   - Create a `.env` file in the project root
   - Add your API key: `OPENAI_API_KEY=your_api_key_here`

## Usage

Run the script with the following command:
```
python pdf_parser.py -d /path/to/pdf/directory -l language
```

- `-d` or `--dir`: Directory containing the PDF files (default is "pdfs")
- `-l` or `--lang`: Language of the questions (default is "swedish")

or if you have specified the default language and directory: 
```
python pdf_parser.py
```
The script will process all PDF files in the specified directory and save the extracted questions as JSON files in the `pdfs/mcq` subdirectory.