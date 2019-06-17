#!/usr/bin/env python
import requests

url = "https://api.weather.gov/products/types/afd/locations/mpx"

headers = {
    'User-Agent': "Python"
    }

response = requests.request("GET", url, headers=headers)

latest_afd = response.json()['@graph'][0]['@id']

afd_txt = requests.request("GET", latest_afd, headers=headers)

afd_json = afd_txt.json()

print(afd_json['issuanceTime'])
print(afd_json['productText'])
