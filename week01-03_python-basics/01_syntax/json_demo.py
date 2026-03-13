# JSON handing module
from pathlib import Path
import json

# read json
def read_json(json_file_path):
    with open(json_file_path) as file:
        return json.load(file);


# Extract data from JSON
def extract_json_from_key(json_file_path, key):
    json_tmp = read_json(json_file_path)
    return json_tmp.get(key)


# save a new json file
def save_new_json_file(json_file_path, new_path):
    json_tmp = read_json(json_file_path)
    with open(new_path, "w") as file:
        json.dump(json_tmp, file, indent=4)

if __name__ == "__main__":
    json_path = Path(__file__).parent / "free_code_camp.json"
    new_json_path = Path(__file__).parent / "free_code_camp2.json"
    print(extract_json_from_key(json_path, "organization"))
    save_new_json_file(json_path, new_json_path)
