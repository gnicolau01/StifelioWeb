import http.client
#import render
import json


def importar_sabates():
    conn = http.client.HTTPSConnection("the-sneaker-database.p.rapidapi.com")

    headers = {
        'x-rapidapi-key': "1f694f120fmsha0cd23a556b6420p16bc69jsn241d2b68b7d9",
        'x-rapidapi-host': "the-sneaker-database.p.rapidapi.com"
    }

    conn.request("GET", "/brands", headers=headers)

    res = conn.getresponse()
    data = res.read()

    dades = json.loads(data.decode("utf-8"))
    return dades