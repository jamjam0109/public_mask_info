import requests
import json
import csv
from utils import dict_to_csv

def storesByAddr(address, save_path):

    url = 'https://8oi9s0nnth.apigw.ntruss.com/corona19-masks/v1/storesByAddr/json'

    params = {'address': f'{address}'}

    output = requests.get(url, params=params)

    json_output = json.loads(output.text)

    stores = json_output['stores']

    dict_to_csv(stores, save_path)


def storesByGeo(lat, lng, m, save_path):

    url = 'https://8oi9s0nnth.apigw.ntruss.com/corona19-masks/v1/storesByGeo/json'

    params = {'lat': lat, 'lng': lng, 'm': m}

    output = requests.get(url, params=params)

    json_output = json.loads(output.text)

    stores = json_output['stores']

    dict_to_csv(stores, save_path)