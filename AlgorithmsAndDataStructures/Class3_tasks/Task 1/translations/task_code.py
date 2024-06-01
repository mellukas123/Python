import os
import json

def read_files_in_directory(directory_path):
    translations = {}
    for file_name in os.listdir(directory_path):
        if file_name.endswith(".json"):
            file_path = os.path.join(directory_path, file_name)
            with open(file_path, "r") as file:
                data = json.load(file)
                extract_translations(data, translations, file_name)
    return translations

def extract_translations(data, translations, file_name):
    for key, value in data.items():
        if isinstance(value, dict):
            extract_translations(value, translations, file_name)
        elif isinstance(value, str) and value.startswith("TBT:"):
            translations.setdefault(file_name, {}).update({key: value})

def write_result_file(translations):
    with open("result.json", "w") as file:
        json.dump(translations, file, indent=4)

def main(directory_path):
    translations = read_files_in_directory(directory_path)
    write_result_file(translations)

if __name__ == "__main__":
    directory_path = "french"  # Adjust the folder path accordingly
    main(directory_path)
