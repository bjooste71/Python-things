import requests as req
import json


api_url = "http://localhost:7071/api/httptestfunction"

response = req.post(api_url, json={"name": "Test"})

print(response.text)