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





def linear_search(prohledavana_sekvence, hledane_cislo):
    slovnik_klice = {"positions": "", "count": 0}

    seznam_pozic = []
    count = 0

    for i in range(len(prohledavana_sekvence)):
        if prohledavana_sekvence[i] == hledane_cislo:
            seznam_pozic.append(i)
            count += 1

    slovnik_klice["positions"] = seznam_pozic
    slovnik_klice["count"] = count

    return slovnik_klice


def main():
    sequential_data = read_data("sequential.json", "unordered_numbers")
    print(sequential_data)
    print(linear_search([0, 2, 2, 22, 5, 55, 12, 10], 2))




if __name__ == "__main__":
    print(linear_search([0, 2, 2, 22, 5, 55, 12, 10], 2))


