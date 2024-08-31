import json
import re

def clean_options(data):
    for entry in data:
        options = entry.get('options', [])
        cleaned_options = []
        for option in options:
            # Remove letter prefix if it exists
            cleaned_option = re.sub(r'^[A-E]\.\s*', '', option)
            cleaned_options.append(cleaned_option)
        entry['options'] = cleaned_options
    return data

# Read the JSON file
with open('final_dataset.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Clean the options
cleaned_data = clean_options(data)

# Write the cleaned data back to a new JSON file
with open('cleaned_dataset.json', 'w', encoding='utf-8') as file:
    json.dump(cleaned_data, file, ensure_ascii=False, indent=2)

print("Processing complete. Cleaned data saved to 'cleaned_dataset.json'.")