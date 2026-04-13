from pathlib import Path
import json
import json

def read_data(file_name, field):


    with open(file_name, "r") as file:
        data = json.load(file)


    if field not in data.keys():
        return None
    else:
        return data[field]

    cwd_path = Path.cwd()
    
    file_path = cwd_path / file_name




#nejlepsi = nejhorsi scenar, protoze musime stejne projit cely seznam
#On (pokud by jsme pouzili metody napr find, zvysi slozitost)
#append pri aktualizaci indexu predchozim prvkum nezmeni
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






def binary_search(prohledavany_seznam, hledane_cislo):
    pocet_prvku = len(prohledavany_seznam)
    prostredni_index = pocet_prvku // 2
    prostredni_prvek = prohledavany_seznam[prostredni_index]
    left = 0
    right = len(prohledavany_seznam) - 1

    if hledane_cislo not in prohledavany_seznam:
        return None

    while left <= right:

        prostredni_index = (left + right) // 2


        if prohledavany_seznam[prostredni_index] == hledane_cislo:
            return prostredni_index

        elif prohledavany_seznam[prostredni_index] < hledane_cislo:
            left = prostredni_index + 1

        else:
            right = prostredni_index - 1
    return None







def main():
    sequential_data = read_data("sequential.json", "unordered_numbers")
    serazene_data = read_data("sequential.json", "ordered_numbers")
    print(serazene_data)
    print(sequential_data)
    print(linear_search([0, 2, 2, 22, 5, 55, 12, 10], 2))
    print(binary_search(serazene_data, 21))



if __name__ == "__main__":
    main()






