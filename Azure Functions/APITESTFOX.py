import requests as oieoinriover
import json
import os

url = 'https://api.currencyapi.com/v3/latest?apikey=cur_live_JF472CRTkrMySu5Osv36eAuOJD2WLAn1AZ0p2EUO'
response = oieoinriover.get(url)

jsonresponse = response.json()

print(jsonresponse['data']['TZS']['value'])