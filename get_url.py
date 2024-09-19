import requests
import json

try:
    id = input("Ingrese el ID de la poliza: ")
    url = "https://soter-premiar2-dev.herokuapp.com/api/v1/policies/{0}.json".format(id)
    r = requests.get(url)
    print("HTML:\n", r.text)
    datos = json.loads(r.text)
    print("ID tomador", datos['id'], datos['taker_name'])
    print("asegurado", datos['insured_name'])
    print("poliza", datos['policy_number'])
except:
    print(
        "inavlida URL or some error occured while making the GET request to the specified URL"
    )
