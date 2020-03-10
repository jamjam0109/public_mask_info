import requests
import json
import csv

def storesByAddr(address, save_path):

    url = 'https://8oi9s0nnth.apigw.ntruss.com/corona19-masks/v1/storesByAddr/json'

    params = {'address': f'{address}'}

    output = requests.get(url, params=params)

    json_output = json.loads(output.text)

    stores = json_output['stores']

    keys = stores[0].keys()

    with open(f'{save_path}', 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(stores)


def storesByGeo(lat, lng, m, save_path):

    url = 'https://8oi9s0nnth.apigw.ntruss.com/corona19-masks/v1/storesByGeo/json'

    params = {'lat': lat, 'lng': lng, 'm': m}

    output = requests.get(url, params=params)

    json_output = json.loads(output.text)

    stores = json_output['stores']
    keys = stores[0].keys()

    with open(f'{save_path}', 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(stores)
