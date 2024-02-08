import requests
import json

def get_all_bank_id():
    url = "https://api.vietqr.io/v2/banks"
    response = requests.get(url)
    data = response.json()
    # parse data
    bank_list = {}
    for bank in data['data']:
        bank_list[bank['shortName']] = bank['bin']
    return bank_list

def get_bank_name_by_id(bank_id):
    bank_list = get_all_bank_id()
    for bank_name, id in bank_list.items():
        if id == bank_id:
            return bank_name 

if __name__ == "__main__":
    print(get_all_bank_id()) 