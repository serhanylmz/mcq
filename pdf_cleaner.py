import json
from typing import List, Dict

# Input and output file paths
INPUT_FILE = "pdfs/mcq/delprov-preklinisk-och-klinisk-del-2020-09-10---med-svar.json"
OUTPUT_FILE = "pdfs/mcq/cleaned_delprov-preklinisk-och-klinisk-del-2020-09-10---med-svar.json"

# Question numbers to exclude (leave empty if none)
EXCLUDE_NUMBERS = [90, 91, 94, 118, 125, 128]

def read_json_file(file_path: str) -> List[Dict]:
    """Read and return data from a JSON file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def write_json_file(file_path: str, data: List[Dict]):
    """Write data to a JSON file."""
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def clean_mcq_data(data: List[Dict], exclude_numbers: List[int]) -> List[Dict]:
    """
    Clean MCQ data by removing invalid questions and specified question numbers.
    
    :param data: List of dictionaries containing MCQ data
    :param exclude_numbers: List of question numbers to exclude
    :return: Cleaned list of MCQ data
    """
    return [
        question for question in data
        if question['answer'].lower() != 'invalid' and
        question['original_question_num'] not in exclude_numbers
    ]

def main():
    # Read input JSON file
    data = read_json_file(INPUT_FILE)

    # Clean the data
    cleaned_data = clean_mcq_data(data, EXCLUDE_NUMBERS)

    # Write cleaned data to output JSON file
    write_json_file(OUTPUT_FILE, cleaned_data)

    print(f"Cleaned data saved to {OUTPUT_FILE}")
    print(f"Removed {len(data) - len(cleaned_data)} questions")

if __name__ == "__main__":
    main()