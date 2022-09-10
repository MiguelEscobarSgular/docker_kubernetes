#!/bin/python3
import requests

API_URL = 'http://localhost:3000/saludo/MiguelEscobar'

# Test GET request
response = requests.request("GET", API_URL)

print(response.status_code)
print(response.text)

if response.status_code != 200:
    print('Se activo fail')
    exit(1)