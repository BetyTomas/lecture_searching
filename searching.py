from pathlib import Path
import json
import json

def read_data(file_name, field):


    with open(file_name, "r") as file:
        data = json.load(file)

    for key in data:
        if key != field:
            return None
        else:
            return data[field]

    cwd_path = Path.cwd()
    
    file_path = cwd_path / file_name


def main():
    sequential_data = read_data("sequential.json", "unordered_numbers")
    print(sequential_data)


if __name__ == "__main__":
    main()

